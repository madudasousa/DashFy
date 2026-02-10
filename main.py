from PySide6.QtWidgets import QApplication, QFileDialog, QWidget, QMainWindow, QMessageBox, QTreeWidgetItem
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from ui_login import Ui_Form
from ui_main import Ui_MainWindow
from xml_files import Read_xml
from database import Database
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from datetime import date
import resources_rc
import re
import sqlite3
import pandas as pd
import sys
import os


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
        
        self.user = user
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
        
        #FILTRO DE PESQUISA
        self.txt_filtro.textChanged.connect(self.update_filter)
        
        #GERAR SAIDA E ESTORNO
        self.btn_gerar.clicked.connect(self.gerar_saida)
        self.btn_estorno.clicked.connect(self.gerar_estorno)
        
        self.reset_table()
        
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
        path = self.txt_file.text().strip()
        if not path:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Diretório vazio")
            msg.setText("Selecione a pasta com os arquivos XML.")
            msg.exec()
            return

        if not os.path.isdir(path):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Diretório inválido")
            msg.setText("O caminho informado não é uma pasta válida.")
            msg.exec()
            return

        xml = Read_xml(path)
        all = xml.all_files()
        if not all:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Nenhum XML encontrado")
            msg.setText("Não há arquivos .xml na pasta selecionada.")
            msg.exec()
            return
        self.progressBar.setMaximum(len(all))
        
        db = Database()
        db.conecta()
        db.create_table_notas()
        cont = 1
        inserted = 0
        failed = 0
        
        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            ok, bad = db.insert_data(fullDataSet)
            inserted += ok
            failed += bad
            cont += 1
        #ATUALIZAR A TABELA
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information if inserted > 0 else QMessageBox.Warning)
        msg.setWindowTitle("Importação concluída")
        msg.setText(f"Itens importados: {inserted}\nItens com erro: {failed}")
        msg.exec()
        self.progressBar.setValue(0)
        self.reset_table()
        db.close_connection()
        
    def table_estoque(self):
        self.tw_estoque.setStyleSheet("color:#000; font-size: 15px;")
        self.tw_estoque.setStyleSheet(u" QHeaderView{color:black}")
        
        conec = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM notas WHERE data_saida = ''", conec)
        result = result.values.tolist()
        
        self.x = ""
        for i in result:
            #faz o check para identificar a mesma nota e adicionar apenas um
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, Qt.CheckState.Unchecked)   
                
                self.x = i[0]
        self.tw_estoque.setSortingEnabled(True)
        
        for i in range (1, 17):
            self.tw_estoque.resizeColumnToContents(i)        
        
    def table_saida(self):
        self.tw_saida.setStyleSheet("color:#000; font-size: 15px;")
        self.tw_saida.setStyleSheet(u" QHeaderView{color:black}")
        
        conec = sqlite3.connect('system.db')
        result = pd.read_sql_query("""SELECT NFe, serie, data_importacao, data_saida, usuario FROM notas WHERE data_saida != ''""", conec)
        result = result.values.tolist()
        
        self.x = ""
        for i in result:
            #faz o check para identificar a mesma nota e adicionar apenas um
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida, i)
                self.campo.setCheckState(0, Qt.CheckState.Unchecked)   
                
                self.x = i[0]
        self.tw_saida.setSortingEnabled(True)
        
        for i in range (1, 17):
            self.tw_saida.resizeColumnToContents(i) 
    
    def table_geral(self):
        self.tb_geral.setStyleSheet("color:#000; font-size: 15px;")
        self.tb_geral.setStyleSheet(u" QHeaderView{color:black}")
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()
        
        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("notas")
        self.model.select()
        
    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()
         
        self.table_saida()
        self.table_estoque()
        self.table_geral()
    
    def update_filter(self, s):
        s = re.sub("[\\W_]+", "", s)
        filter_str = 'NFe LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)     
    
    def gerar_saida(self):
        self.checked_items_out = []
        
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i) 
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == Qt.Checked:
                    self.checked_items_out.append(child.text(0))
        recurse(self.tw_estoque.invisibleRootItem())      
        
        #Pergunta se o usuario tem certeza que deseja gerar a saída   
        self.question('saida') 
        
    def gerar_estorno(self):
        self.checked_items = []
        
        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i) 
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == Qt.Checked:
                    self.checked_items.append(child.text(0))
        recurse(self.tw_saida.invisibleRootItem())  
        
        #Pergunta se o usuario tem certeza que deseja estornar as notas selecionadas
        self.question('estorno')  
        
    def question(self, table):
        msg = QMessageBox()
        if table == 'estorno':
            msg.setText("Tem certeza que deseja estornar as notas selecionadas?")
            msg.setInformativeText("As notas selecionadas voltarão para o estoque \n clique em Yes para confirmar ou No para cancelar.") 
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDetailedText(f"Notas: {self.checked_items}")
            
        else:
            msg.setText("Tem certeza que deseja gerar a saída das notas selecionadas?")
            msg.setInformativeText("As notas abaixo será baixada no estoque \n clique em Yes para confirmar ou No para cancelar.") 
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDetailedText(f"Notas: {self.checked_items_out}")
            
        msg.setIcon(QMessageBox.Question)   
        ret = msg.exec()
        
        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = Database() 
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()
            else:
                data_saida = date.today() 
                data_saida = data_saida.strftime("%d/%m/%Y")  
                self.db = Database()  
                self.db.conecta()
                self.db.update_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()
                       
              
     
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())

    