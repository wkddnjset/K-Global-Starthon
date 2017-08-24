from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
import io

# Open a PDF file.
fp = open("../../resources/ICML2011.pdf", "rb")
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser, 1234)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
# Create a PDF interpreter object.


# Process each page contained in the document.
retstr = io.StringIO()
codec = 'utf-8'
password = ""
maxpages = 0
caching = True
pagenos=set()
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

text = retstr.getvalue()
# 띄어쓰기
result = text.replace('\xa0'," ")
# 예외처리
for i in ['\u2013','\xe9','\xa9','\u2014','\uf0b6','\u018a','\ufb00','\ufb02','\ufb03','\uf065','\u2212','\u0374','\ufb01','\xf6','\xe0','\xe8','\xfc']:
  if i in result:
    result=result.replace(i,'')

#print(result)
contents = result.split(". ")
