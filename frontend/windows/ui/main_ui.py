
import sys
from customtkinter import *

sys.path.insert(1, 'D:\PYTHON\Projects\PdfEditor')
from backend.pdf_editor import Pdf_Editor


class Gui():
    def __init__(self) -> None:
        self.root = CTk()
        self.pdf = Pdf_Editor()
        set_appearance_mode("dark")
        set_default_color_theme("blue")

        self.window()
        self.buttons()

        self.root.mainloop()

    def window(self):
        self.root.title("Pdf Editor")
        self.root.iconbitmap()   # Icon location not specified
        self.root.geometry("360x640")
        self.root.minsize(width=360, height=640)
        self.root.maxsize(width=360, height=640)

    def buttons(self):
        button1 = CTkButton(self.root, 
                            text="PDF to docx", 
                            command=self.pdf_to_word,
                            height=75,
                            width=150, 
                            # fg_color="blue", 
                            ).place(x=20,y=20)
        
        button2 = CTkButton(self.root, 
                            text="Extract Pages", 
                            command=self.extract_pages, 
                            height=75,
                            width=150, 
                            ).place(x=190,y=20)
        
        button3 = CTkButton(self.root, 
                            text="Combine Files", 
                            command=self.combine, 
                            height=75,
                            width=150, 
                            ).place(x=20,y=115)
        
        button4 = CTkButton(self.root, 
                            text="Encrypt File", 
                            command=self.protect, 
                            height=75,
                            width=150, 
                            ).place(x=190,y=115)
        
        button5 = CTkButton(self.root, 
                            text="Rotate Pdf", 
                            command=self.rotate, 
                            height=75,
                            width=150, 
                            ).place(x=20,y=210)
        
        button6 = CTkButton(self.root, 
                            text="Delete Pages", 
                            command=self.delete, 
                            height=75,
                            width=150, 
                            ).place(x=190,y=210)
        
        button7 = CTkButton(self.root, 
                            text="Pdf to Image", 
                            command=self.pdf_to_image, 
                            height=75,
                            width=150, 
                            ).place(x=20,y=315)
        
        button8 = CTkButton(self.root, 
                            text="Compress File", 
                            command=self.compress, 
                            height=75,
                            width=150, 
                            ).place(x=190,y=315)

    def pdf_to_word(self):
        self.root1 = CTk()
        self.root1.title("PDF to docx")
        self.root1.iconbitmap()   # Icon location not specified
        self.root1.minsize(height=360,width=450)
        self.root1.maxsize(height=360,width=450)

        # self.pdf.pdf_to_word()

        self.root1.mainloop()
        return

    def extract_pages(self):
        self.root2 = CTk()
        self.root2.title("Extract Pages")
        self.root2.iconbitmap()   # Icon location not specified
        self.root2.minsize(height=360,width=450)
        self.root2.maxsize(height=360,width=450)

        # backend function call

        self.root2.mainloop()
        return

    def combine(self):
        self.root3 = CTk()
        self.root3.title("Combine Files")
        self.root3.iconbitmap()   # Icon location not specified
        self.root3.minsize(height=360,width=450)
        self.root3.maxsize(height=360,width=450)
        
        # backend function call
        
        self.root3.mainloop()
        return

    def protect(self):
        self.root4 = CTk()
        self.root4.title("Encrypt File")
        self.root4.iconbitmap()   # Icon location not specified
        self.root4.minsize(height=360,width=450)
        self.root4.maxsize(height=360,width=450)

        # backend function call

        self.root4.mainloop()
        return

    def rotate(self):
        self.root5 = CTk()
        self.root5.title("Rotate Pdf")
        self.root5.iconbitmap()   # Icon location not specified
        self.root5.minsize(height=360,width=450)
        self.root5.maxsize(height=360,width=450)

        # backend function call

        self.root5.mainloop()
        return

    def delete(self):
        self.root6 = CTk()
        self.root6.title("Delete Pages")
        self.root6.iconbitmap()   # Icon location not specified
        self.root6.minsize(height=360,width=450)
        self.root6.maxsize(height=360,width=450)

        # backend function call

        self.root6.mainloop()
        return

    def pdf_to_image(self):
        self.root7 = CTk()
        self.root7.title("Pdf to Image")
        self.root7.iconbitmap()   # Icon location not specified
        self.root7.minsize(height=360,width=450)
        self.root7.maxsize(height=360,width=450)

        # backend function call

        self.root7.mainloop()
        return

    def compress(self):
        self.root8 = CTk()
        self.root8.title("Compress File")
        self.root8.iconbitmap()   # Icon location not specified
        self.root8.minsize(height=360,width=450)
        self.root8.maxsize(height=360,width=450)

        # backend function call

        self.root8.mainloop()
        return


if __name__ == "__main__":
    app = Gui()
