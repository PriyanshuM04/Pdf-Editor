from random import randint
import pikepdf as pp
import PyPDF2
from pdf2docx import Converter
from pdf2image import convert_from_path


class Pdf_Editor:
    def __init__(self) -> None:
        pass

    def pdf_to_word(self, file):
        old_pdf = file
        new_doc = file.replace('.pdf', '.docx')

        obj = Converter(old_pdf)
        obj.convert(new_doc)
        obj.close()

    def extract_pages(self, file, start=0, end=0):
        pages = list(range(start-1, end))
        name = file.replace('.pdf', "")

        with open(file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            writer = PyPDF2.PdfWriter()
            rest_writer = PyPDF2.PdfWriter()
            for page in range(len(reader.pages)):
                if page in pages:
                    writer.add_page(reader.pages[page])
                else:
                    rest_writer.add_page(reader.pages[page])

            with open(name + '_selected.pdf', 'wb') as f2:
                writer.write(f2)

            with open(name + "_rest.pdf", 'wb') as f2:
                rest_writer.write(f2)

    def combine(self, files):
        out_path = r"C:\Users\priya\OneDrive\Documents\1st SEM ADMIT CARD.pdf".replace('1st SEM ADMIT CARD', "New_Document")
        merger = PyPDF2.PdfMerger()
        for pdf in files:
            merger.append(pdf)
        merger.write(out_path)
        merger.close()

    def protect(self, file):
        password = input("Enter Password: ")
        name = file.replace('.pdf', "")

        old_pdf = pp.Pdf.open(file)
        no_extract = pp.Permissions(extract=False)
        old_pdf.save(name + "_protected.pdf",
                    encryption=pp.Encryption(user=password, owner="priyanshu", allow=no_extract))
        print("Encryption Successful")

    def rotate(self, file):
        name = file.replace('.pdf', "")
        old_pdf = pp.Pdf.open(file)
        for i in old_pdf.pages:
            i.Rotate = 90
            old_pdf.save(name + "_rotate90.pdf")    # NOT WORKING
        print("Execution Successful")

    def delete(self, file, start, end):
       name = file.replace('.pdf', "")
       old_pdf = pp.Pdf.open(file)
       del old_pdf.pages[start-1:end]
       old_pdf.save(name +"_deleted.pdf")
       

    def pdf_to_image(self, file, start, end):
        old_pdf = convert_from_path(file, poppler_path=r"D:\PYTHON\Projects\Pdf Editor\poppler-24.02.0\Library\bin")
        for i in range(start-1, end):
            old_pdf[i].save(r"C:\Users\priya\OneDrive\Documents\new"+str(i+1)+".png", "PNG")

    def compress(self, file):
        name = file.replace('.pdf', "")
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)

        with open(name + "_Compressed.pdf", 'wb') as f:
            writer.write(f)

        print("Successfully Compressed!")


if __name__ == "__main__":
    pdf_editor = Pdf_Editor()

    print("1. Pdf to Word", end="    ")
    print("2. Extract Pages")
    print("3. Combine Files", end="    ")
    print("4. Encrypt File")
    print("5. Rotate Pdf", end="    ")
    print("6. Delete Pages")
    print("7. Pdf to Image", end="    ")
    print("8. Compress File")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        file = input("Enter Path: ").replace('"', '')
        pdf_editor.pdf_to_word(file)
    elif ch == 2:
        file = input("Enter Path: ").replace('"', '')
        start_page = int(input("From: "))
        end_page = int(input("To: "))
        pdf_editor.extract_pages(file, start_page, end_page)
    elif ch == 3:
        file_count = int(input("No. of files to Merge: "))
        files = []
        for i in range(file_count):
            file = (input("Enter File Path: ")).replace('"', '')
            files.append(file)
        pdf_editor.combine(files)
    elif ch == 4:
        file = input("Enter Path: ").replace('"', '')
        pdf_editor.protect(file)
    elif ch == 5:
        file = (input("Enter File Path: ")).replace('"', '')
        pdf_editor.rotate(file)
    elif ch == 6:
        file = (input("Enter File Path: ")).replace('"', '')
        start_page = int(input("From: "))
        end_page = int(input("To: "))
        pdf_editor.delete(file, start_page, end_page)
    elif ch == 7:
        file = (input("Enter File Path: ")).replace('"', '')
        start_page = int(input("From: "))
        end_page = int(input("To: "))
        pdf_editor.pdf_to_image(file, start_page, end_page)
    elif ch == 8:
        file = (input("Enter File Path: ")).replace('"', '')
        pdf_editor.compress(file)
    else:
        print("Invalid Choice!!")
