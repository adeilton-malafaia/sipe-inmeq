import datetime
import os

import camelot.io as cm
import pandas as pd


class PDFhandler:
    def __init__(self, filename):
        self.filename = filename
        self.url = "/home/" + str(os.environ.get('USERNAME')) + "/Documentos/"
        self.data = ''
    
    def readFile(self):
        # Extraindo todas as tabelas existentes do PDF para um objeto Camelot.
        # O objeto é uma espeçie de array de tabelas (se houver mais de uma página)
        tbl = cm.read_pdf(self.url + self.filename + ".pdf",'all')
        
        # Criando listas vazias, uma para cada coluna da planilha que será gerada...
        data = list()
        tc = list()
        tipo_saida = list()
        produto = list()
        marca = list()
        qn = list()
        qt = list()

        # Navegando em cada tabela para coletar os dados das colunas
        for i in range(0, len(tbl)):
            # Tabela (dataset) atual
            tab = tbl[i].df

            # Navegando em cada linha da tabela atual para adicionar dados nas listas
            for k in (range(1, len(tab[i]))):
                try:
                    dt = str(tab[0][k])
                    d = int(dt[0:2])
                    m = int(dt[3:5])
                    y = int(dt[6:10])
                    dat = datetime.datetime(y, m, d)
                    data.append(dat)
                except Exception:
                    data.append('')

                tc.append(int(tab[5][k]))
                tipo_saida.append('')
                produto.append(tab[3][k])
                marca.append(tab[6][k])
                qn.append(tab[7][k])
                try:
                    qt.append(int(tab[8][k]))
                except Exception:
                    qt.append(5)
                
        # Criando um dicionário com as listas...
        self.data = {
            'data' : data,
            'tc' : tc,
            'tipo_saida' : tipo_saida,
            'produto' : produto,
            'marca' : marca,
            'qn' : qn,
            'qt' : qt
        }

    def exportData(self):
        plan = pd.DataFrame(self.data)
        plan.to_excel(self.url + 'crono.xlsx')