import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import CTkImage
from PIL import Image
from datetime import datetime
from docxtpl import DocxTemplate
import jinja2
from customtkinter import filedialog  
from CustomTkinterMessagebox import CTkMessagebox
import re
from dotenv import load_dotenv
import os
from logging import Handler, error, log
import logging
import logging.handlers
from docx2pdf import convert

load_dotenv()

tpl = DocxTemplate(r'C:\Users\ArturSzczotarski\psyche\RODO_template.DOCX')
logging.basicConfig(filename=f"{os.getcwd()}/logs.log",format='%(asctime)s %(message)s', datefmt ="%d-%m-%Y %H:%M:%S",level=logging.INFO)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("rose.json")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Psyche Forms")
        self.geometry(f"{900}x{580}")

        logo_image = CTkImage(light_image=Image.open(r"C:\Users\ArturSzczotarski\psyche\logo.png"), size=(150 ,150))
        dominka_iamge = CTkImage(light_image=Image.open(r"C:\Users\ArturSzczotarski\psyche\Dominika.jpg"), size=(150 ,150))
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, image=logo_image , text="")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text = "Zmień ścieżkę zapisu", command=self.selectOutputDirectory, font=(10,15))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.selectfile)
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #Photo 
        # self.photo = customtkinter.CTkLabel(self, image=my_image, text = "", font=customtkinter.CTkFont(size=20, weight="bold"))
        # self.photo.grid(row=1, column=1, padx=0, pady=0)

        # create tabview
        self.tabview = customtkinter.Form1(self)
        self.tabview.grid(row=0, column=1, padx=10, pady=(20, 0), sticky="ew")
        self.tabview.add("Rodo")
        self.tabview.add("Upoważnienie")
        
        # Rodo inside
        self.tabview.tab("Rodo").grid_columnconfigure((0,1,2,3), weight=1)  # configure grid of individual tabs
        self.tabview.tab("Rodo").grid_rowconfigure((0,1,2,3,4,5,6,7), weight=0)

        #Name
        self.nameLabel = customtkinter.CTkLabel(self.tabview.tab("Rodo"),
									text="Imię", font=(10,15, "bold"))
        self.nameLabel.grid(row=0, column=0,
							padx=10, pady=10,
							sticky="ew"
                              )
        self.nameEntry = customtkinter.CTkEntry(self.tabview.tab("Rodo"),
						placeholder_text="Jan")
        self.nameEntry.grid(row=0, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")      
        #Last name
        self.lastnameLabel = customtkinter.CTkLabel(self.tabview.tab("Rodo"),
									text="Nazwisko", font=(10,15, "bold")) 
        self.lastnameLabel.grid(row=1, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.lasNameEntry = customtkinter.CTkEntry(self.tabview.tab("Rodo"),
						placeholder_text="Kowalski")
        self.lasNameEntry.grid(row=1, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")       
        #PESEL
        self.peselLabel = customtkinter.CTkLabel(self.tabview.tab("Rodo"),
									text="PESEL", font=(10,15, "bold"))
        self.peselLabel.grid(row=2, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.peselEntry = customtkinter.CTkEntry(self.tabview.tab("Rodo"),
						placeholder_text="000000")
        self.peselEntry.grid(row=2, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")
        #Tele
        self.phoneLabel = customtkinter.CTkLabel(self.tabview.tab("Rodo"),
									text="Telefon", font=(10,15, "bold"))
        self.phoneLabel.grid(row=4, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.phoneEntry = customtkinter.CTkEntry(self.tabview.tab("Rodo"),
						placeholder_text="00000")
        self.phoneEntry.grid(row=4, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")
        #Email
        self.emailLabel = customtkinter.CTkLabel(self.tabview.tab("Rodo"),
									text="e-mail", font=(10,15, "bold"))
        self.emailLabel.grid(row=5, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.emailEntry = customtkinter.CTkEntry(self.tabview.tab("Rodo"),
						placeholder_text="jan.kowalski@gmai.com")
        self.emailEntry.grid(row=5, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")
        #output type

        self.outputLabel = customtkinter.CTkLabel(self.tabview.tab("Rodo"), text = "Format zapisu", font=(10,15, "bold"))
        self.outputLabel.grid(row=6, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.docx_type = customtkinter.CTkCheckBox(self.tabview.tab("Rodo"), text = "docx",)
        self.pdf_type = customtkinter.CTkCheckBox(self.tabview.tab("Rodo"), text = "pdf")
        self.docx_type.grid(row=6, column=1, padx=0, pady=20)
        self.pdf_type.grid(row=6, column=2, padx=0, pady=20)
        self.docx_type.select(True)

        #generate button
        self.generate_button1 = customtkinter.CTkButton(self.tabview.tab("Rodo"), text="Generuj plik" , command=self.generate_template_rodo, font=(10,15, "bold"))
        self.generate_button1.grid(row=8, column=0, padx=20, pady=50)

        
        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Rodo"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=10, pady=(20, 10))

        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Rodo"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=10, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Rodo"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=10, pady=(10, 10))


        # Form 2 inside
        self.tabview.tab("Upoważnienie").grid_columnconfigure(0, weight=1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Upoważnienie"), text="Select Gender")
        self.gander_checkbox1 = customtkinter.CTkCheckBox(self.tabview.tab("Upoważnienie"), text = "male")
        self.gander_checkbox2 = customtkinter.CTkCheckBox(self.tabview.tab("Upoważnienie"), text = "female")

        self.gander_checkbox1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.gander_checkbox2.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.tabview.tab("Upoważnienie").grid_columnconfigure((0,1,2,3), weight=1)  # configure grid of individual tabs
        self.tabview.tab("Upoważnienie").grid_rowconfigure((0,1,2,3,4,5,6,7), weight=0)
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.nameLabel = customtkinter.CTkLabel(self.tabview.tab("Upoważnienie"),
									text="Imię", font=(10,15, "bold"))
        self.nameLabel.grid(row=0, column=0,
							padx=10, pady=10,
							sticky="ew"
                              )
        self.nameEntry = customtkinter.CTkEntry(self.tabview.tab("Upoważnienie"),
						placeholder_text="Jan")
        self.nameEntry.grid(row=0, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")      
        #Last name
        self.lastnameLabel = customtkinter.CTkLabel(self.tabview.tab("Upoważnienie"),
									text="Nazwisko", font=(10,15, "bold")) 
        self.lastnameLabel.grid(row=1, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.lasNameEntry = customtkinter.CTkEntry(self.tabview.tab("Upoważnienie"),
						placeholder_text="Kowalski")
        self.lasNameEntry.grid(row=1, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")       
        #PESEL
        self.peselLabel = customtkinter.CTkLabel(self.tabview.tab("Upoważnienie"),
									text="PESEL", font=(10,15, "bold"))
        self.peselLabel.grid(row=2, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.peselEntry = customtkinter.CTkEntry(self.tabview.tab("Upoważnienie"),
						placeholder_text="000000")
        self.peselEntry.grid(row=2, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    
    # def explorer_window(self):

    #     self.new_window = customtkinter.CTkToplevel(self)
    #     self.new_window.title("new window")
    #     self.new_window.geometry("400x200")
    #     self.new_window.grid_columnconfigure((0,1,2), weight=0)
    #     self.new_window.grid_rowconfigure((0,1,3), weight=0)

    #     self.pathLabel = customtkinter.CTkLabel(self.new_window, text= "Zapisz: ")

    #     self.pathLabel.grid(row = 0, column = 0, padx= 50)

    #     self.FormPath = customtkinter.CTkEntry(self.new_window,
    #                     placeholder_text="path")
                        
    #     self.FormPath.grid(row=0, column=1,
    #                         columnspan=3, padx=0,
    #                         pady=50, sticky="ew") 
        
    #     self.selecPathButton =  customtkinter.CTkButton(self.new_window, text="Wybierz")
    #     self.selecPathButton.grid(row=1, column=2, padx=20, pady=0)

    #     self.OkButton =  customtkinter.CTkButton(self.new_window, text="OK")
    #     self.OkButton.grid(row=2, column=2, padx=20, pady=10)


    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def generate_template_rodo(self,):
        
        #validation pesel 
        if len(self.peselEntry.get()) == 11:
            pass
        else:
            CTkMessagebox.messagebox(title="Błędny pesel", text = "Pesel powinien składać się z 11 cyfr.")
            raise TypeError("Only 11 didgits are allowed")
        
        if re.match(r'^([0-9]+_?)+$', self.peselEntry.get()):
            pass  
        else:
            CTkMessagebox.messagebox(title="Błędny pesel", text = "Pesel powinien składać się jedynie z cyfr.")
            raise TypeError("Only didgits are allowed")

        #validation empty fields
        if len(self.peselEntry.get()) != 0 and  len(self.nameEntry.get()) != 0 and len(self.lasNameEntry.get()) != 0 and len(self.phoneEntry.get()) != 0 and len(self.emailEntry.get()) != 0:
            pass
        else:
            CTkMessagebox.messagebox(title="Brak danych", text = "Uzupełnij wszystkie pola.")
            raise TypeError("not all fields are filled in")
        
        #validate file format
        if self.docx_type.get() == False and self.pdf_type.get() == False:
            CTkMessagebox.messagebox(title="Brak danych", text = "Wybierz format zapisu.")
            raise TypeError("File format was not selected")
        else:
            pass
        try:

        #data provided
            name = self.nameEntry.get()
            lastName =  self.lasNameEntry.get()
            pesel = self.peselEntry.get()
            phone = self.phoneEntry.get()
            email = self.emailEntry.get()

            context = {
                "pesel" : pesel,
                "name" : name,
                "last_name" : lastName,
                "date" : str(datetime.strftime(datetime.today(),'%d-%m-%Y')),
                "email" : email,
                "tel" :phone
                }

            jinja_env = jinja2.Environment(autoescape=True)
            tpl.render(context, jinja_env)

            file_path = f"{os.environ['output_path']}/Rodo_{name}_{lastName}"
            tpl.save(f"{file_path}.docx")

            #Output format options
            if self.pdf_type.get() == True:
                convert(f"{file_path}.docx", f"{file_path}.pdf")
                CTkMessagebox.messagebox(title="Plik pdf został wygenerowany", text = f"Plik został utworzony i zapisany jako\n: {f"{file_path}.pdf"}", size = "700x200")
            if self.docx_type.get() == False:
                os.remove(f"{file_path}.docx")
            else:
                CTkMessagebox.messagebox(title="Plik docx został wygenerowany", text = f"Plik został utworzony i zapisany jako\n: {f"{file_path}.docx"}", size = "700x200")

        except PermissionError as error:
            CTkMessagebox.messagebox(title="Błąd", text = f"Wybierz siężkę zapisu pliku", size = "700x200")
            
        except BaseException as error:
            logging.error(datetime.today().strftime("%d-%m-%Y %H:%M:%S") + str(error))
            CTkMessagebox.messagebox(title="Błąd", text = f"Nie można wygenerować pliku: \n {error}", size = "700x200")
          
            
            
    def selectOutputDirectory(self):       
        new_directory = filedialog.askdirectory()
        if new_directory != os.environ['output_path'] and len(new_directory) > 0:
            os.environ['output_path'] = new_directory
            with open(".env", "w") as file:
                file.write(f"output_path ={new_directory}")

        print(new_directory) 


if __name__ == "__main__":
    app = App()
    app.mainloop()