from fpdf import FPDF
from docx import Document

# PDF erstellen
def pdfcreator(txt,zsm_txt,kltxt,senttxt):
    pdf = FPDF()
    
    pdf.add_page()
    
    # set style and size of font
    pdf.set_font("Arial", "B", size = 18)
    # create a cell
    pdf.cell(200, 10, txt = "Projektrealisierung Download-Bericht",
            ln = 1, align = 'C')

    
    pdf.set_font("Arial", "U", size = 14)
    pdf.cell(200, 10, txt = "Text Zusammenfassung",
            ln = 1, align = 'L')
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(200, 5, txt = zsm_txt, align = 'L')

    pdf.set_font("Arial","U", size = 14)
    pdf.cell(200, 15, txt = "Text Klassifizierung",
            ln = 1, align = 'L')
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(200, 5, txt = kltxt, align = 'L')


    pdf.set_font("Arial","U", size = 14)
    pdf.cell(200, 15, txt = "Text Sentiment",
            ln = 1, align = 'L')
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(200, 5, txt = senttxt, align = 'L')
    
    pdf.add_page()
    pdf.set_font("Arial", "U",size = 14)
    pdf.cell(200, 10, txt = "Original Text",
            ln = 1, align = 'L')
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(200, 5, txt = txt, align = 'L')
    
    # save the pdf with name .pdf
    pdf.output("download.pdf")
    
# docx erstellen
def docxcreator(txt,zsm_txt,kltxt,senttxt):
        #doc erstellen
        document = Document()
        document.add_heading('Projektrealisierung Download-Bericht', 0)


        document.add_heading('Text Zusammenfassung', level=1)
        document.add_paragraph(zsm_txt)
        document.add_heading('Text Klassifizierung', level=1)
        document.add_paragraph(kltxt)
        document.add_heading('Text Sentiment', level=1)
        document.add_paragraph(senttxt)

        document.add_page_break()
        document.add_heading('Original Text', level=1)
        document.add_paragraph(txt)
        #doc runterladen
        document.save('download.docx')

        return document

