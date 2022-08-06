#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF

import PyPDF2, os 
# get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
# we alphabetize the filenames
pdfFiles.sort(key=str.lower)
print(pdfFiles)
pdfWriter = PyPDF2.PdfFileWriter()

# loop through all the PDF files

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted == True : pdfReader.decrypt('rosebud')
    # loop through all the pages (except the first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

