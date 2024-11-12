import PyPDF2

merger = PyPDF2.PdfMerger()

# All the pdf files in list format
pdfiles = ["1.pdf", "2.pdf"]

# Iterating through the pdfiles list
for filename in pdfiles:
    # Opening the pdf and storing the result in "pdFile" variable.
    pdFile = open(filename, 'rb')
    # Reading the pdf and storing the result in "pdfReader" variable.
    pdfReader = PyPDF2.PdfReader(pdFile)
    # Finally merging the pdf's
    merger.append(pdfReader)

pdFile.close()
merger.write("Merged.pdf")