from typing import Union, Iterable, List

from PySide2.QtWidgets import QWidget, QMessageBox

from ui_MainForm import Ui_MainForm
from logic import Logic


class MainForm(QWidget, Ui_MainForm):

    def __init__(self, logic_obj: Logic, parent=None):

        super().__init__(parent)
        self.setupUi(self)

        self.logic_obj = logic_obj

        self.solve_button.clicked.connect(self.solve)

    @staticmethod
    def str_to_vec(s: str) -> Union[List[float], None]:

        if not s:
            return None

        str_values = s.split()

        try:
            return [float(s) for s in str_values]
        except:
            return None

    @staticmethod
    def vec_to_str(vec: Iterable, sep: str = ' ') -> str:
        return sep.join([str(v) for v in vec])

    def solve(self):

        self.result_line.clear()

        v1 = self.str_to_vec(self.input1_line.text())
        if v1 is None:
            QMessageBox(text='Неверный формат в первом поле',
                        parent=self).show()
            return

        v2 = self.str_to_vec(self.input2_line.text())
        if v2 is None:
            QMessageBox(text='Неверный формат во втором поле',
                        parent=self).show()
            return

        if self.radio_elementwise.isChecked():
            res = self.logic_obj.vectors_mult(v1, v2)
        else:
            res = self.logic_obj.vectors_dot_mult(v1, v2)

        if res is None:
            QMessageBox(text='Вычислительная ошибка',
                        parent=self).show()
            return

        if isinstance(res, Iterable):
            self.result_line.setText(self.vec_to_str(res))
        else:
            self.result_line.setText(str(res))
