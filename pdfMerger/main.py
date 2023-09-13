import PyPDF2

merger = PyPDF2.PdfMerger()  # extracting class
files = ["1.pdf", "2.pdf"]

for filename in files:
    pdf_file = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdf_file)
    merger.append(pdfReader)
    pdf_file.close()

merger.write('merged.pdf')


