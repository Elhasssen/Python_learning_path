# import PyPDF2

# pdfFileObj = open('learningpy/working with pdf/meetingminutes.pdf','rb')

# pdfreader = PyPDF2.PdfFileReader(pdfFileObj)

# print(pdfreader.numPages) # get the numbers of the pages
# #output : 19

# pageObj = pdfreader.getPage(0) # get the first page 

# print(pageObj.extractText()) # extract the text from the pdf 

# pdfFileObj.close() # clsoe the opened pdf file 

############################################
# import PyPDF2

# pdfReader = PyPDF2.PdfFileReader(open('learningpy/working with pdf/encrypted.pdf','rb'))

# # now we test if the pdf is encrypted 
# print(pdfReader.isEncrypted)
# # output : True
# # now we try to get the first page of the pdf 
# # bla = pdfReader.getPage(0)
# #output : the file has not been decrypted
# # now we try decrypt the file
# pdfReader = PyPDF2.PdfFileReader(open('learningpy/working with pdf/encrypted.pdf','rb'))

# pdfReader.decrypt('rosebud')

# pageObj = pdfReader.getPage(0)

# print(pageObj.extractText())
###########################
# # copying PDF Pages
# import os
# import PyPDF2


# os.chdir('learningpy/working with pdf')
# pdf1File = open('meetingminutes.pdf', 'rb')

# pdf2File = open('meetingminutes2.pdf', 'rb')
# # we read both files in binary mode and store them in two variables
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# pdfWriter = PyPDF2.PdfFileWriter()

# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)

# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# # we use wb when we write a file
# pdfOutputFile = open('combinedminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close().
###################################
# # operations on PDFs
# # rotation 
# # wwe read the pdf then : 
# page = pdfReader.getpage(0)
# page.rotateClockwise(90)

#####################################
# Overlaying Pages 
# adding watermarks

import PyPDF2
import os
os.chdir('learningpy/working with pdf')
minutesFile = open('meetingminutes.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(minutesFile)

minutesFirstPage = pdfReader.getPage(0)
# we read the watermark.pdf
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
# we add the watermark to the first page
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()

pdfWriter.addPage(minutesFirstPage)

# then we add the watermark to the rest of the pages

for pagenum in range(1,pdfReader.numPages):
    pageObj = pdfReader.getPage(pagenum)
    pdfWriter.addPage(pageObj)

resultedPdfFile = open('watermarkdCover.pdf','wb')

pdfWriter.write(resultedPdfFile)

minutesFile.close()

resultedPdfFile.close()

######################################
# Encypting PDFs
#  
import PyPDF2
import os
os.chdir('/home/elhassen/Desktop/Python/learningpy/working with pdf')

pdfFile = open('meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

pdfWriter = PyPDF2.PdfFileWriter()

for pagenum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pagenum))

pdfWriter.encrypt('swordfish')
resultPdf = open('encyptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()













