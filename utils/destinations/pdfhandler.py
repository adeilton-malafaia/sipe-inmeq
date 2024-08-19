import datetime
import os

import camelot.io as cm  # type: ignore
import pandas as pd  # type: ignore


class PDFhandler:
    def __init__(self, file, filename='crono.pdf'):
        self.filename = filename
        self.url = os.getcwd() + "/"
        with open(self.url + self.filename, "wb+") as crono:
            for chunk in file.chunks():
                crono.write(chunk)

        self.data = ''

    def readFile(self):
        # Extraindo todas as tabelas existentes do PDF para um objeto Camelot.
        # O objeto é uma espeçie de array de tabelas (se houver mais de uma
        # página)
        # tbl = cm.read_pdf(self.url + self.filename + ".pdf", 'all')

        tbl = cm.read_pdf(self.filename, 'all')

        # Criando listas vazias, uma para cada coluna da planilha que será
        # gerada...
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

            # Navegando em cada linha da tabela atual para adicionar dados nas
            # listas
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
            'data': data,
            'tc': tc,
            'tipo_saida': tipo_saida,
            'produto': produto,
            'marca': marca,
            'qn': qn,
            'qt': qt
        }

    def readFile2(self):
        # Extraindo todas as tabelas existentes do PDF para um objeto Camelot.
        # O objeto é uma espeçie de array de tabelas (se houver mais de uma
        # página)
        # tbl = cm.read_pdf(self.url + self.filename + ".pdf", 'all')

        tbl = cm.read_pdf(self.filename, 'all')

        # Criando listas vazias, uma para cada coluna da planilha que será
        # gerada...
        data = list()
        # dt = dict()

        # Navegando em cada tabela para coletar os dados das colunas
        for i in range(0, len(tbl)):
            # Tabela (dataset) atual
            tab = tbl[i].df

            # Navegando em cada linha da tabela atual para adicionar dados nas
            # listas
            for k in (range(1, len(tab[i]))):
                dt = dict()
                try:
                    date = str(tab[0][k])
                    d = str(date[0:2])
                    m = str(date[3:5])
                    y = str(date[6:10])
                    dat = d + "/" + m + "/" + y  # datetime.datetime(y, m, d)
                    dt['data'] = dat
                except Exception:
                    dt['data'] = ''

                dt['tc'] = int(tab[5][k])
                dt['tipo_saida'] = ''
                dt['produto'] = tab[3][k]
                dt['marca'] = tab[6][k]
                dt['qn'] = tab[7][k]
                try:
                    dt['qt'] = int(tab[8][k])
                except Exception:
                    dt['qt'] = 5
                data.insert(len(data), dt)

        # Criando um dicionário com as listas...
        self.data = data
        ...

    def getURL(self):
        return self.url

    def getSizeData(self):
        return len(self.data)

    def getData(self):
        return self.data

    def exportData(self):
        plan = pd.DataFrame(self.data)
        plan.to_excel(self.url + 'crono.xlsx')
