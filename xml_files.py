import os
import xml.etree.ElementTree as ET
from datetime import date

class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory
        
    def all_files(self):
        return [ os.path.join(self.directory, arq) for arq in os.listdir(self.directory)
            if arq.lower().endswith(".xml")]
        
    def nfe_data(self, xml):
        root = ET.parse(xml).getroot()    
        nsNfe = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
        
        #DADOS DA NOTA FISCAL
        nfe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNfe))
        serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNfe))
        data_emissao = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhEmi", nsNfe))
        data_emissao = F'{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[0:4]}'
        
        #DADOS EMITENTE
        chave = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:chNFe", nsNfe))
        cnpj_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNfe))
        nome_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNfe))
        
        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        valorNfe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNfe))
        data_importacao = date.today()
        data_importacao = data_importacao.strftime("%d/%m/%Y")
        data_saida = ""
        usuario = ''
        
        itemNota = 1
        notas = []
        
        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNfe):
            #DADOS DOS ITENS DA NOTA FISCAL
            codigo = self.check_none(item.find("./ns:prod/ns:cProd", nsNfe))
            descricao = self.check_none(item.find("./ns:prod/ns:xProd", nsNfe))
            ncm = self.check_none(item.find("./ns:prod/ns:NCM", nsNfe))
            quantidade = self.check_none(item.find("./ns:prod/ns:qCom", nsNfe))
            valor_unitario = self.check_none(item.find("./ns:prod/ns:vUnCom", nsNfe))
            valor_total = self.check_none(item.find("./ns:prod/ns:vProd", nsNfe))
            
            notas.append({
                "itemNota": itemNota,
                "codigo": codigo,
                "descricao": descricao,
                "ncm": ncm,
                "quantidade": quantidade,
                "valor_unitario": valor_unitario,
                "valor_total": valor_total,
                "nfe": nfe,
                "serie": serie,
                "data_emissao": data_emissao,
                "chave": chave,
                "cnpj_emitente": cnpj_emitente,
                "nome_emitente": nome_emitente,
                "valorNfe": valorNfe,
                "data_importacao": data_importacao,
                "data_saida": data_saida,
                "usuario": usuario
            })
            itemNota += 1
        return notas
        
             
    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace('.', ',')
            except:
                return var.text
    
    def format_cnpj(self,cnpj):
        try:
            cnpj = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
            return cnpj
             
        except:
             return ""
         
if __name__ == "__main__":
    xml = Read_xml()
    all = xml.all_files()
    for i in all:
        result = xml.nfe_data(i)
        print(result)