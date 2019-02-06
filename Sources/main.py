import sys

from PySide2.QtWidgets import QApplication

from main_form import MainForm
from logic import Logic


def __main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    main_form = MainForm(Logic())
    main_form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    __main()
