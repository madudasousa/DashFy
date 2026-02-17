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
        has_ns = root.tag.startswith("{")
        
        # Detecta se root é NFeList ou similar (múltiplas NFes)
        root_tag = root.tag.split('}')[-1] if '}' in root.tag else root.tag
        if root_tag in ['NFeList', 'nfeProc', 'NFes']:
            # Processa cada NFe separadamente
            all_notas = []
            nfes = root.findall('.//NFe') if not has_ns else root.findall('.//{http://www.portalfiscal.inf.br/nfe}NFe')
            for nfe_node in nfes:
                all_notas.extend(self._process_single_nfe(nfe_node, has_ns, nsNfe))
            return all_notas
        else:
            # Processa como NFe única
            return self._process_single_nfe(root, has_ns, nsNfe)
    
    def _process_single_nfe(self, root, has_ns, nsNfe):
        def find_text(path_ns, path_plain):
            node = root.find(path_ns, nsNfe) if has_ns else root.find(path_plain)
            return self.check_none(node)

        def findall_nodes(path_ns, path_plain):
            return root.findall(path_ns, nsNfe) if has_ns else root.findall(path_plain)
        
        #DADOS DA NOTA FISCAL
        nfe = find_text("./ns:infNFe/ns:ide/ns:nNF", "./infNFe/ide/nNF")
        serie = find_text("./ns:infNFe/ns:ide/ns:serie", "./infNFe/ide/serie")
        data_emissao = find_text("./ns:infNFe/ns:ide/ns:dhEmi", "./infNFe/ide/dhEmi")
        data_emissao = F'{data_emissao[8:10]}/{data_emissao[5:7]}/{data_emissao[0:4]}'
        
        #DADOS EMITENTE
        chave = find_text("./ns:infNFe/ns:ide/ns:chNFe", "./infNFe/ide/chNFe")
        if not chave:
            chave = find_text("./ns:infNFe/ns:infAdic/ns:chNFe", "./infNFe/infAdic/chNFe")

        cnpj_emitente = find_text("./ns:infNFe/ns:emit/ns:CNPJ", "./infNFe/emit/CNPJ")
        nome_emitente = find_text("./ns:infNFe/ns:emit/ns:xNome", "./infNFe/emit/xNome")
        
        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        valorNfe = find_text("./ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", "./infNFe/total/ICMSTot/vNF")
        data_importacao = date.today()
        data_importacao = data_importacao.strftime("%d/%m/%Y")
        data_saida = ""
        usuario = ''
        
        itemNota = 1
        notas = []
        
        for item in findall_nodes("./ns:infNFe/ns:det", "./infNFe/det"):
            #DADOS DOS ITENS DA NOTA FISCAL
            codigo = self.check_none(item.find("./ns:prod/ns:cProd", nsNfe) if has_ns else item.find("./prod/cProd"))
            descricao = self.check_none(item.find("./ns:prod/ns:xProd", nsNfe) if has_ns else item.find("./prod/xProd"))
            ncm = self.check_none(item.find("./ns:prod/ns:NCM", nsNfe) if has_ns else item.find("./prod/NCM"))
            quantidade = self.check_none(item.find("./ns:prod/ns:qCom", nsNfe) if has_ns else item.find("./prod/qCom"))
            valor_unitario = self.check_none(item.find("./ns:prod/ns:vUnCom", nsNfe) if has_ns else item.find("./prod/vUnCom"))
            valor_total = self.check_none(item.find("./ns:prod/ns:vProd", nsNfe) if has_ns else item.find("./prod/vProd"))
            
            # Ordem deve bater com a lista de colunas usada no banco.
            notas.append((
                nfe,
                serie,
                data_emissao,
                chave,
                cnpj_emitente,
                nome_emitente,
                valorNfe,
                data_importacao,
                itemNota,
                codigo,
                descricao,
                ncm,
                quantidade,
                valor_unitario,
                valor_total,
                usuario,
                data_saida,
            ))
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