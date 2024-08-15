import os

from utils.destinations.pdfhandler import PDFhandler

pd = PDFhandler()
os.remove(pd.getURL() + 'crono.pdf')

# pd.readFile()
# pd.exportData()
