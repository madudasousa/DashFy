import sqlite3


class Database():
    def __init__(self, name = "system.db") -> None:
        self.name = name
        
    def conecta(self):
        self.connection = sqlite3.connect(self.name)
        
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
        
    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                 CREATE TABLE IF NOT EXISTS users(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                );     
            """)
        except AttributeError:
            print ("Faça a conexão")     
            
    def insert_user(self, name, user, password, access):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                    INSERT INTO users (name, user, password, access) VALUES (?,?,?,?)      
                """, (name, user, password, access))       
            self.connection.commit()
        except AttributeError:
            print ("Faça a conexão")
            
            
    def check_user(self, user, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                     SELECT * FROM users    
            """)  
             
            for linha in cursor.fetchall(): 
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4].lower() == "administrador":
                    return "Administrador" 
                        
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4].lower() in ["usuario", "usuário", "user"]:
                    return "Usuário Comum"
                        
                else:
                    continue
            return "Inexistente"
        except:    
            pass
        
    def insert_data(self, full_dataset):
        cursor = self.connection.cursor()
        campos_tabela = ( 
                'NFe', 'serie', 'data_emissao', 'chave', 'cnpj_emitente',
                'nome_emitente', 'valorNfe', 'data_importacao',
                'itemNota', 'codigo', 'descricao', 'ncm', 'quantidade',
                'valor_unitario', 'valor_total', 'usuario', 'data_saida')
        qntd = ','.join(map(str, ['?'] * len(campos_tabela)))
        query = f"""INSERT INTO notas ({', '.join(campos_tabela)}) VALUES ({qntd})"""
        
        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Erro ao inserir dados: {e}")   
            
    def create_table_notas(self):
       cursor = self.connection.cursor()
       cursor.execute("""
            CREATE TABLE IF NOT EXISTS notas(
                NFe TEXT,
                serie TEXT,
                data_emissao TEXT,
                chave TEXT,
                cnpj_emitente TEXT,
                nome_emitente TEXT,
                valorNfe TEXT,
                data_importacao TEXT,
                itemNota INTEGER,
                codigo TEXT,
                descricao TEXT,
                ncm TEXT,
                quantidade TEXT,
                valor_unitario TEXT,
                valor_total TEXT,
                usuario TEXT,
                data_saida TEXT,
                
                PRIMARY KEY (chave, NFe, itemNota)
            );     
        """)              
        
            
if __name__ == "__main__":
    db = Database()
    db.conecta()
    db.create_table_users()
    db.create_table_notas()
    db.close_connection()
    