import sys
from typing import Union, Iterable, List

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox
import numpy as np

from ui_MainForm import Ui_MainForm


class MainForm(QWidget, Ui_MainForm):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
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

        res_vec = vectors_mult(v1, v2)
        if res_vec is None:
            QMessageBox(text='Вычислительная ошибка',
                        parent=self).show()
            return

        self.result_line.setText(self.vec_to_str(res_vec))


def vectors_mult(v1: List[float], v2: List[float]) \
        -> Union[Iterable, None]:

    try:
        return (np.array(v1, dtype=np.float64) *
                np.array(v2, dtype=np.float64)).tolist()
    except:
        return None


def vectors_dot_mult(v1: List[float], v2: List[float]) \
        -> Union[Iterable, None]:

    try:
        return np.dot(np.array(v1, dtype=np.float64),
                      np.array(v2, dtype=np.float64)
                      ).tolist()
    except:
        return None


def __main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    __main()
