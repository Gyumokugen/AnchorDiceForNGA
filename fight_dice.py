# fight_dice
import copy
from PySide6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QFileDialog, QDialog, QMessageBox, QWidget, QSizePolicy, QLineEdit, QLabel
)
import PySide6.QtCore as Qt
import Methods
import random
import sys

# 基本规则
# 拼敏捷+1d20决定攻击，同点格攻击一次。
# 力量+1d10对拼，结果+2， 差值=>10最终倍率x1.5，差值=<-10被对方命中，最终倍率*1，除此之外，>=0最终倍率*1，<0倍率*0
# 最后受攻方造成 生命值 - （攻击 - 防御）* 最终倍率
extra_Strength = 2
critical_threshold = 10
critical_ratio = 1.5
counter_threshold = -10
hit_threshold = 0
world_parameter = 20

BATTLE_P1_WIN = 1
BATTLE_P2_WIN = 2
BATTLE_DRAW = 3
BATTLE_CONTINUE = 4

_rng = random.Random()

columns = ["Name", "Agility", "Strength", "Intelligence", "Attack", "Defense", "HealthPoint"]
_index = {Name: i for i, Name in enumerate(columns)}


def process_attack(attacker, defender):
    # 力量拼点
    roll1 = _rng.randint(1, 10)
    roll2 = _rng.randint(1, 10)

    r1 = attacker[_index["Strength"]] + roll1
    r2 = defender[_index["Strength"]] + roll2

    text = (f"{attacker[_index["Name"]]}攻击：{attacker[_index["Strength"]]} + 1d10({roll1}) = {r1}"
            f"<==> {defender[_index["Name"]]}防守：{defender[_index["Strength"]]} + 1d10({roll2}) = {r2}" + "\n")

    diff = r1 - r2 + 2
    text += f"差值：{diff} "
    if diff >= critical_threshold:
        mult = critical_ratio
        text += f"[color=red]Critical! x{critical_ratio}[/color] "
    elif diff <= counter_threshold:
        mult = -1  # 被反击
    elif diff >= hit_threshold:
        mult = 1
        text += "Hit! "
    else:
        mult = 0
        text += "Miss! "

    if mult == -1:
        # 反击
        dmg = max(defender[_index["Attack"]] - attacker[_index["Defense"]], 0)
        attacker[_index["HealthPoint"]] -= dmg
        text += f"[color=chocolate]Counter![/color] {attacker[_index["Name"]]}受到反击 {dmg}\n"
        return text

    dmg = max(attacker[_index["Attack"]] - defender[_index["Defense"]], 0) * mult
    defender[_index["HealthPoint"]] -= int(dmg)
    text += f"{defender[_index["Name"]]}受到伤害 {dmg}\n"
    return text


def round_over_check(player1, player2):
    health_point1 = player1[_index["HealthPoint"]]
    health_point2 = player2[_index["HealthPoint"]]
    text = f"{player1[_index["Name"]]}剩余生命值：{health_point1}<==>{player2[_index["Name"]]}剩余生命值：{health_point2}\n"
    p1_alive = health_point1 > 0
    p2_alive = health_point2 > 0

    if p1_alive and not p2_alive:
        status = BATTLE_P1_WIN
    elif p2_alive and not p1_alive:
        status = BATTLE_P2_WIN
    elif not p1_alive and not p2_alive:
        status = BATTLE_DRAW
    else:
        status = BATTLE_CONTINUE

    return status, text


def one_round(player1, player2):
    # 拼攻击权，敏捷[1] + 1d世界参数
    roll1 = _rng.randint(1, world_parameter)
    roll2 = _rng.randint(1, world_parameter)

    r1 = player1[_index["Agility"]] + roll1
    r2 = player2[_index["Agility"]] + roll2

    text = (f"[i]<<<攻击权争夺>>>[/i]\n"
            f"{player1[_index["Name"]]}： {player1[_index["Agility"]]} + 1d{world_parameter}({roll1}) = {r1}"
            f"<==>"
            f"{player2[_index["Name"]]}： {player2[_index["Agility"]]} + 1d{world_parameter}({roll2}) = {r2}" + "\n")

    if r1 > r2:
        attack_order = [(player1, player2)]
        text += f"{player1[_index["Name"]]}攻击！"
    elif r2 > r1:
        attack_order = [(player2, player1)]
        text += f"{player2[_index["Name"]]}攻击！"
    else:
        attack_order = [
            (player1, player2),
            (player2, player1)
        ]
        text += f"[color=red]双向攻击！[/color]"
    text += "\n[i]<<<攻击阶段>>>[/i]\n"
    # ==== 攻击阶段 ====
    for attacker, defender in attack_order:
        text += process_attack(attacker, defender)

    return text


def one_round_gwent(player1, player2):
    wins = {player1[0]: 0, player2[0]: 0}
    text = ""
    status = BATTLE_DRAW
    for i in range(1, 4):
        text += f"====Round{i}====\n"
        r1, r2 = _rng.randint(1, player1[2]), _rng.randint(1, player2[2])
        p1, p2 = player1[1] + player1[2] + r1, player2[1] + player2[2] + r2

        text += (f"{player1[0]}： {player1[1]} + {player1[2]} + 1d{player1[2]}({r1}) = {p1}"
                 f"<==>"
                 f"{player2[0]}： {player2[1]} + {player2[2]} + 1d{player2[2]}({r2}) = {p2}" + "    ")

        # 1. 确定本轮赢家（平局默认 P1）
        round_winner = player1[0] if p1 >= p2 else player2[0]

        # 2. 累加分数并记录
        wins[round_winner] += 1
        text += f"[b]{round_winner} 得分！[/b]\n"

        # 3. 统一检查胜出条件
        if wins[round_winner] >= 2:
            text += f"[b]{round_winner} 最终胜利！[/b]"
            status = BATTLE_P1_WIN if round_winner == player1[0] else BATTLE_P2_WIN
            break

    return text, status


def start_battle(player1, player2, if_gwent=False):
    text = ""
    if if_gwent:
        text, status = one_round_gwent(player1, player2)
        text = "[collapse=紧张刺激的昆特牌大战]\n" + text
    else:
        round_count = 1
        text = ""
        while True:
            text += f"===Round{round_count}===\n"
            text += one_round(player1, player2)
            status, t_result = round_over_check(player1, player2)
            text += t_result
            if status != BATTLE_CONTINUE:
                break
            round_count += 1

        text += "[b][size=150%]"
        if status == BATTLE_P1_WIN:
            text += f"{player1[_index["Name"]]}胜利！"
        if status == BATTLE_P2_WIN:
            text += f"{player2[_index["Name"]]}胜利！"
        if status == BATTLE_DRAW:
            text += "[color=red]同归于尽！[/color]"
        text = f"[collapse=战斗共计{round_count}轮]\n" + text + "[/size][/b]"
    text += "\n[/collapse]\n"

    return text, status


def build_enemy_from_scale(player2, scale):
    new_enemy = [player2[_index["Name"]]]
    for i in range(6):
        new_enemy.append(int(player2[i + 1] * scale[1 + 1].text()))
    return new_enemy


def win_rate_calculate(player1, player2, if_gwent=False, count=3000):
    draw = 0
    player1_win = 0
    player2_win = 0
    for i in range(count):
        a = copy.deepcopy(player1)
        b = copy.deepcopy(player2)
        _, result = start_battle(a, b, if_gwent)
        if result == BATTLE_P1_WIN:
            player1_win += 1
        if result == BATTLE_P2_WIN:
            player2_win += 1
        if result == BATTLE_DRAW:
            draw += 1
    return player1_win, player2_win, draw, player1_win / count


class FightSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Methods.import_ui_fight()()
        self.ui.setupUi(self)
        self.ui.pb_roll.clicked.connect(self.pb_roll_clicked)
        self.ui.pb_test.clicked.connect(self.pb_test_clicked)
        self.player_data_le = [[], []]
        self.status_label = []
        self.initialize_status_line_edit()
        self.change_label_status(False)
        self.settings = Qt.QSettings("FightSimulator", "status")
        self.load_settings()

        self.ui.pb_copy.clicked.connect(self.copy_output)
        self.ui.pb_create_enemy.clicked.connect(self.create_enemy)
        self.ui.cb_gwent.clicked.connect(self.gwent_changed)
        self.ui.pb_character_card.clicked.connect(
            lambda: self.out_put_character_card(0))

    def copy_output(self):
        text = self.ui.pte_output.toPlainText()
        QApplication.clipboard().setText(text)

    def closeEvent(self, event):
        self.save_settings()
        # key = "rate"
        # self.settings.setValue(key, self.ui.le_target_winrate().text())

    def load_settings(self):
        for i, row in enumerate(self.player_data_le):
            for j, le in enumerate(row):
                key = f"player_{i}_{j}"
                value = self.settings.value(key, "")
                le.setText(value)
        # key = "rate"
        # value = self.settings.value(key, "")
        # self.ui.le_target_winrate.setText(value)

    def save_settings(self):
        for i, row in enumerate(self.player_data_le):
            for j, le in enumerate(row):
                key = f"player_{i}_{j}"
                self.settings.setValue(key, le.text())

    def initialize_status_line_edit(self):
        for i in range(7):
            le0 = QLineEdit()
            le1 = QLineEdit()
            lb = QLabel()
            lb.setAlignment(Qt.Qt.AlignCenter)
            self.ui.gl_status.addWidget(lb, i, 0)
            self.ui.gl_status.addWidget(le0, i, 1)
            self.ui.gl_status.addWidget(le1, i, 2)
            self.status_label.append(lb)
            self.player_data_le[0].append(le0)
            self.player_data_le[1].append(le1)

    def change_label_status(self, if_gwent):
        if if_gwent:
            gwent_tittle = ["Name", "Skill", "Deck"]
            for i in range(7):
                if i < 3:
                    self.status_label[i].setText(gwent_tittle[i])
                else:
                    self.status_label[i].setText("")
        else:
            for i in range(7):
                self.status_label[i].setText(columns[i])

    def pb_roll_clicked(self):
        if_gwent = self.ui.cb_gwent.isChecked()
        player1, player2 = self.read_player_data()
        text, _ = start_battle(player1, player2, if_gwent)
        self.ui.pte_output.setPlainText(text)

    def pb_test_clicked(self):
        if_gwent = self.ui.cb_gwent.isChecked()
        player1, player2 = self.read_player_data()
        player1_win, player2_win, draw, rate = win_rate_calculate(player1, player2, if_gwent)
        self.ui.pte_output.setPlainText(f"P1胜：{player1_win} P2胜：{player2_win} 平：{draw} 胜率{rate}")

    def gwent_changed(self):
        if self.ui.cb_gwent.isChecked():
            self.save_settings()
            self.change_label_status(True)
        else:
            self.load_settings()
            self.change_label_status(False)

    def create_enemy(self):
        try:
            target = float(self.ui.le_target_winrate.text())
        except:
            self.ui.pte_output.setPlainText("Win Rate Error!")
            return
        player1, player2 = self.read_player_data()
        best_b = copy.deepcopy(player2)

        _, _, _, rate = win_rate_calculate(player1, best_b)
        best_diff = abs(rate - target)

        for _ in range(300):
            new_b = best_b.copy()
            idx = _rng.randint(1, len(new_b) - 1)

            change = _rng.randint(1, 5)

            if rate > target:
                new_b[idx] += abs(change)
            else:
                new_b[idx] -= abs(change)

            if new_b[idx] < 1:
                new_b[idx] = 1

            _, _, _, new_rate = win_rate_calculate(player1, new_b)
            diff = abs(new_rate - target)

            if diff < best_diff:
                best_diff = diff
                best_b = new_b
                rate = new_rate

            else:
                # 5%概率接受更差解（防止卡死）
                if _rng.random() < 0.05:
                    best_b = new_b
                    rate = new_rate
                    best_diff = diff

            if best_diff < 0.02:
                break

        for i in range(len(best_b)):
            self.player_data_le[1][i].setText(f"{best_b[i]}")

        self.out_put_character_card(1)

    # [table]
    # [tr][td]一[/td][td]二[/td][/tr]
    # [tr][td]三[/td][td]四[/td][/tr]
    # [tr][td]五[/td][td]六[/td][/tr]
    # [/table]

    def out_put_character_card(self, character):
        text2 = ""
        text1 = "[table]"
        tittle = ["角色卡", "敏捷", "力量", "智力", "攻击", "防御", "生命值"]
        for i in range(7):
            text1 += ("[tr][td width=10]" + tittle[i] + "[/td][td][b]" + self.player_data_le[0][
                i].text() + "[/b][/td][td][b]" +
                      self.player_data_le[1][i].text() + "[/b][/td][td width=10][/td][/tr]")

        for j in range(7):
            text2 += tittle[j] + ": " + self.player_data_le[character][j].text() + "\n"
        text1 += "[/table]"
        QApplication.clipboard().setText(text1)

    def read_player_data(self):
        player_data = [[], []]
        # Name
        player_data[0].append(self.player_data_le[0][0].text())
        player_data[1].append(self.player_data_le[1][0].text())
        # status
        for i in range(2):
            for j in range(6):
                value = Methods.try_int(self.player_data_le[i][j + 1].text())
                player_data[i].append(value)
        return player_data[0], player_data[1]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fight = FightSimulator()
    fight.show()

    sys.exit(app.exec())
