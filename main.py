from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QMessageBox
from ui_login import Ui_Form
from ui_main import Ui_MainWindow
import sys
from database import Database
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import resources_rc
from xml_files import Read_xml


class Login(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        
        self.QPushButton.clicked.connect(self.checkLogin)
##botao de login com o nome QPushButton (definido no ui_login.py) por enquanto nao esta mudando o nome do botao
 
    def checkLogin(self):
        ###autenticação do usuario no banco de dados
        self.users = Database()
        self.users.conecta()
        authenticated = self.users.check_user(self.txt_user.text().upper(), self.txt_password.text())
        
        if authenticated and authenticated.lower() in ["administrador", "usuário comum"]:
            self.w = MainWindow(authenticated.lower())
            self.w.show()
            self.close()
        else: 
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Login inválido")
                msg.setText(f'Login ou senha incorretos. \n \n Tentativa: {self.tentativas +1} de 3')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                #BLOQUEAR O USUARIO APOS 3 TENTATIVAS
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        
        self.logo_path = "img/logo.png"
        pixmap = QPixmap(self.logo_path)
        
        ##Controle de acesso por usuário, a tela de cadastro
        if user.lower() == "usuário comum":
            self.btn_cadastro.setVisible(False)
        
        ####PAGINAS DO SISTEMA ####
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_table.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_import.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_import))
        self.btn_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        
        self.btn_cadastrar.clicked.connect(self.subscribe_user)
        
        ####CONEXOES DE IMPORTACAO####
        self.btn_open.clicked.connect(self.open_path)
        self.btn_importar.clicked.connect(self.import_xml_files)
        
        #ARQUIVOS XML
        self.btn_open.clicked.connect(self.open_path)
        self.btn_importar.clicked.connect(self.import_xml_files)
        
    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_senha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("As senhas não coincidem!")
            msg.setText("A senha digitada no campo de confirmação é diferente da senha principal.")
            msg.exec()
            return None
        
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()
        
        db = Database()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Usuário cadastrado.")
        msg.setText("O usuário foi cadastrado no sistema com sucesso!")
        msg.exec()
        
        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha2.setText("")
        self.cb_perfil.setCurrentIndex(0)

    def resizeEvent(self, event):
        pixmap = QPixmap(self.logo_path)
        pixmap = pixmap.scaled(
            self.lbl_logo.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.lbl_logo.setPixmap(pixmap)
        super().resizeEvent(event)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str("Open Directory"),
                                                    "/home", QFileDialog.ShowDirsOnly
                                                    | QFileDialog.DontResolveSymlinks)
        self.txt_file.setText(self.path)
    def import_xml_files(self):
        xml = Read_xml(self.txt_file.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))
        
        db = Database()
        db.conecta()
        cont = 1
        
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont += 1
         #ATUALIZAR A TABELA   
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação concluída")
        msg.setText("Os arquivos XML foram importados com sucesso!")
        msg.exec()
        self.progressBar.setValue(0)
        db.close_connection()

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())
