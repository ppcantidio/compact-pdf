from PyPDF2 import PdfWriter, PdfReader
from PIL import Image
import os

class MergeFiles:
    def converter_imagem_para_pdf(self, imagem, nome_pdf):
        imagem = imagem.convert("RGB")
        imagem.save(nome_pdf, "PDF", resolution=100.0)
        
    def juntar_arquivos_em_pdf(self, files, save_file_name):
        pdf_writer = PdfWriter()

        for arquivo in files:
            if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
                imagem = Image.open(arquivo)
                self.converter_imagem_para_pdf(imagem, "temp.pdf")
                pdf_reader = PdfReader("temp.pdf")
                for pagina in range(len(pdf_reader.pages)):
                    pagina_pdf = pdf_reader.pages[pagina]
                    pdf_writer.add_page(pagina_pdf)
                os.remove("temp.pdf")
            elif arquivo.lower().endswith(".pdf"):
                pdf_reader = PdfReader(arquivo)
                for pagina in range(len(pdf_reader.pages)):
                    pagina_pdf = pdf_reader.pages[pagina]
                    pdf_writer.add_page(pagina_pdf)

        with open(f'{save_file_name}', "wb") as output_pdf:
            pdf_writer.write(output_pdf)
