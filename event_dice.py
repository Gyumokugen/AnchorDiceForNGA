# event_dice.py
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QFileDialog, QDialog, QMessageBox, QWidget, QSizePolicy, QLineEdit
)
import sys
import Methods
import random
import time

_rng = random.Random()


def _prepare_weight_data(weight_list, text_list):
    valid = []

    i = 0
    for w, t in zip(weight_list, text_list):
        if t is None:
            continue

        t = str(t).strip()
        if t == "":
            continue

        try:
            w = float(w)
        except:
            continue

        if w <= 0:
            continue

        valid.append((w, t, i))
        i = i + 1

    return valid


def weighted_roll(valid):
    total = sum(int(v[0]) for v in valid)

    r = _rng.randint(1, total)
    cur = 0

    for w, t, idx in valid:
        cur += int(w)
        if r <= cur:
            return r, total, idx

    return r, total, valid[-1][2]


def build_weight_table(valid):
    _range = []
    _text = []
    cur = 1

    for w, t, i in valid:
        w = int(w)

        start = cur
        end = cur + w - 1

        if start == end:
            r = f"{start} "
        else:
            r = f"{start}-{end} "
        _range.append(r)
        _text.append(f"{t}")
        cur = end + 1

    return _range, _text
    # return "\n".join(result_lines)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Methods.import_ui_event()()
        self.ui.setupUi(self)

        self.weight_le = []
        self.choice_le = []
        self.initialize_choice_line_edit()

        self.addition_sign = [self.ui.comboBox_sign0, self.ui.comboBox_sign1]
        self.addition_text = [self.ui.le_text0, self.ui.le_text1]
        self.addition_value = [self.ui.le_number0, self.ui.le_number1]
        self.tendency_text = [self.ui.le_0, self.ui.le_1]
        self.initialize_addition_sign()

        self.ui.pb_copy.clicked.connect(self.copy_output)

    def copy_output(self):
        text = self.ui.pte_output.toPlainText()
        QApplication.clipboard().setText(text)

    def initialize_addition_sign(self):
        for cb in self.addition_sign:
            cb.addItems(["+", "-"])
            cb.setCurrentIndex(0)
        return

    def initialize_choice_line_edit(self):
        for i in range(10):
            le0 = QLineEdit()
            le1 = QLineEdit()
            self.ui.gl_choices.addWidget(le0, i + 1, 0)
            self.ui.gl_choices.addWidget(le1, i + 1, 1)
            self.weight_le.append(le0)
            self.choice_le.append(le1)

        self.weight_le[-1].setEnabled(False)
        self.choice_le[-1].setEnabled(False)
        self.choice_le[-1].setText("大成失！")

        self.ui.pb_roll.clicked.connect(self.pb_roll_clicked)
        self.ui.cb_last.clicked.connect(self.cb_last_clicked)

    def cb_last_clicked(self):
        if self.ui.cb_last.isChecked():
            self.weight_le[-1].setText("1")
        else:
            self.weight_le[-1].setText("")
        return

    def pb_roll_clicked(self):
        text = "[quote]"
        if self.ui.rb_0.isChecked():
            text += f"0<--{self.tendency_text[0].text()} -- {self.tendency_text[1].text()}-->100 ||"
            for i in range(2):
                if Methods.try_int(self.addition_value[i].text()):
                    text += (f"{self.addition_sign[i].currentText()}{self.addition_value[i].text()} "
                             f"{self.addition_text[i].text()}")
            text += "\n"

            r = _rng.randint(1, 100)
            result = r
            text += f"1d100 = {r}"

            addition = False
            for i in range(2):
                value = Methods.try_int(self.addition_value[i].text())
                if value:
                    text += f" {self.addition_sign[i].currentText()} {self.addition_value[i].text()}"
                    sign = 1 if self.addition_sign[i].currentIndex() == 0 else -1
                    result += sign * value
                    addition = True
            if addition:
                text += f" = {result} ==> {max(0, min(100, result))} "
            if r <= 5:
                text += " 大失败！\n"
            if r >= 96:
                text += " 大成功！\n"

        elif self.ui.rb_1.isChecked():
            weights = [tb.text() for tb in self.weight_le]
            texts = [tb.text() for tb in self.choice_le]
            valid = _prepare_weight_data(weights, texts)
            dice, total, idx = weighted_roll(valid)
            _range, choice = build_weight_table(valid)
            for i in range(len(choice)):
                if i != idx:
                    text += _range[i] + choice[i] + "\n"
                else:
                    text += "[b]" + _range[i] + choice[i] + "[/b]\n"

            text += f"d{total} = {dice} " + f"{choice[idx]}" + "\n"

            if choice[idx] == f"大成失！":
                r = _rng.randint(1, 2)
                text += f"d2 = {r} "
                if r == 1:
                    text += "大成功！"
                else:
                    text += "大失败！"

        elif self.ui.rb_2.isChecked():
            text = ""
            try:
                number = int(self.ui.le_dice_count.text().strip())
            except ValueError:
                number = 1
            try:
                dice = int(self.ui.le_dice_size.text().strip())
            except ValueError:
                dice = 1
            try:
                base = int(self.ui.le_dice_base.text().strip())
            except ValueError:
                base = 0
            if base != 0:
                text = f"{base} "

            sum_r = base

            for i in range(number):
                r = _rng.randint(1, dice)
                text += f"+{r}(d{dice}) "
                sum_r += r
            text += f"= {sum_r}"

            if number == 1:
                r = _rng.randint(1, dice)
                text += f"\nd{dice} = {r}"

        text += "\n[/quote]"
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.ui.pte_output.setPlainText(text)
        self.ui.lb_update_time.setText(f"Updated In: {time_str}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    event = MyWindow()
    event.show()

    sys.exit(app.exec())
