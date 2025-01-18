import sys

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

from auth_design import (
    Ui_Auth,
)


class AuthWindow(QDialog):
    def __init__(self):
        super(AuthWindow, self).__init__()

        self.ui = Ui_Auth()
        self.ui.setupUi(self)

        self.is_wrong = True

        self.ui.pb.clicked.connect(
            self.login,
        )
    
    def login(self):
        self.u, self.l = (
            self.ui.le_lgn.text(),
            self.ui.le_pwd.text(),
        )
        if self.u == '1':
            self.is_wrong = False
            self.close()
            return None
        else:
            self.is_wrong = True
            self.ui.label_error.setText(
                'Неправильное имя'
                'пользователя или пароль'
            )
            return None


if __name__ == "__main__":
    app = QApplication(
        sys.argv
    )
    
    window = AuthWindow()
    window.show()
    
    sys.exit(
        app.exec()
    )