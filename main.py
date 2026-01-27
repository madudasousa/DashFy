from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from ui_login import Ui_Form
from ui_main import Ui_MainWindow
import sys

class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        
        self.QPushButton.clicked.connect(self.open_system)
##botao de login com o nome QPushButton (definido no ui_login.py) por enquanto nao esta mudando o nome do botao
        
    def open_system(self):
        
        if self.txt_password.text()=="789":
             self.w = MainWindow()
             self.w.show()
             self.close()
             
        else:
            print("Senha incorreta!")        
           
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        
        ##PAGINAS DO SISTEMA
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_table.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_sobre))
        self.btn_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())