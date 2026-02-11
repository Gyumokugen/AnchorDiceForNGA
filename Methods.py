# Methods
import sys
import os
import subprocess




def generate_ui_py(ui_file):
   base = os.path.splitext(os.path.basename(ui_file))[0]
   py_file = f"ui_{base}.py"


   subprocess.run(
       ["pyside6-uic", ui_file, "-o", py_file],
       check=True
   )




def import_ui_event():
   if getattr(sys, "frozen", False):
       from ui_qt import Ui_MainWindow
       return Ui_MainWindow
   else:
       ui_file = "qt.ui"


       if not os.path.exists(ui_file):
           raise FileNotFoundError(f"{ui_file} 不存在")


       generate_ui_py(ui_file)


       if "ui_qt" in sys.modules:
           del sys.modules["ui_qt"]
       from ui_qt import Ui_MainWindow
       return Ui_MainWindow




# def import_ui_fight():
#    if getattr(sys, "frozen", False):
#        from ui_fight import Ui_MainWindow
#        return Ui_MainWindow
#    else:
#        ui_file = "fight.ui"
#
#
#        if not os.path.exists(ui_file):
#            raise FileNotFoundError(f"{ui_file} 不存在")
#
#
#        generate_ui_py(ui_file)
#
#
#        if "ui_fight" in sys.modules:
#            del sys.modules["ui_fight"]
#        from ui_fight import Ui_MainWindow
#        return Ui_MainWindow




def try_int(v):
   try:
       return int(v)
   except ValueError:
       return 0
