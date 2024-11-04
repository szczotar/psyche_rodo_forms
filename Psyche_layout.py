import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import CTkImage
from PIL import Image
from datetime import datetime
from docxtpl import DocxTemplate
import jinja2

tpl = DocxTemplate(r'C:\Users\ArturSzczotarski\psyche\RODO_template.DOCX')


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Psyche Forms")
        self.geometry(f"{900}x{580}")

        my_image = CTkImage(light_image=Image.open(r"C:\Users\ArturSzczotarski\psyche\Dominika.jpg"), size=(200,250))
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Psyche", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
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
        self.tabview.add("Form1")
        self.tabview.add("Form2")
        
        # Form1 inside
        self.tabview.tab("Form1").grid_columnconfigure((0,1,2,3), weight=1)  # configure grid of individual tabs
        self.tabview.tab("Form1").grid_rowconfigure((0,1,2,3,4,5,6,7), weight=0)


        #Name
        self.nameLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="Imię")
        self.nameLabel.grid(row=0, column=0,
							padx=10, pady=10,
							sticky="ew",
                              )
        self.nameEntry = customtkinter.CTkEntry(self.tabview.tab("Form1"),
						placeholder_text="Jan")
        self.nameEntry.grid(row=0, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")      
        #Last name
        self.lastnameLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="Nazwisko") 
        self.lastnameLabel.grid(row=1, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.lasNameEntry = customtkinter.CTkEntry(self.tabview.tab("Form1"),
						placeholder_text="Kowalski")
        self.lasNameEntry.grid(row=1, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")       
        #PESEL
        self.peselLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="PESEL")
        self.peselLabel.grid(row=2, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.peselEntry = customtkinter.CTkEntry(self.tabview.tab("Form1"),
						placeholder_text="000000")
        self.peselEntry.grid(row=2, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")
        #Tele
        self.phoneLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="Telefon")
        self.phoneLabel.grid(row=4, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.phoneEntry = customtkinter.CTkEntry(self.tabview.tab("Form1"),
						placeholder_text="00000")
        self.phoneEntry.grid(row=4, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")
        #Email
        self.emailLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="e-mail")
        self.emailLabel.grid(row=5, column=0,
							padx=10, pady=10,
							sticky="ew")
        self.emailEntry = customtkinter.CTkEntry(self.tabview.tab("Form1"),
						placeholder_text="jan.kowalski@gmai.com")
        self.emailEntry.grid(row=5, column=1,
							columnspan=2, padx=10,
							pady=10, sticky="ew")
        
        #generate button
        self.generate_button1 = customtkinter.CTkButton(self.tabview.tab("Form1"), text="Generuj" , command=self.generate_template_rodo)
        self.generate_button1.grid(row=6, column=0, padx=20, pady=50)

        
        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Form1"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=10, pady=(20, 10))

        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Form1"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=10, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Form1"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=10, pady=(10, 10))


        # Form 2 inside
        self.tabview.tab("Form2").grid_columnconfigure(0, weight=1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Form2"), text="Select Gender")
        self.gander_checkbox1 = customtkinter.CTkCheckBox(self.tabview.tab("Form2"), text = "male")
        self.gander_checkbox2 = customtkinter.CTkCheckBox(self.tabview.tab("Form2"), text = "female")

        self.gander_checkbox1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.gander_checkbox2.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def generate_template_rodo(self):

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
        tpl.save(fr"C:\Users\ArturSzczotarski\psyche\Rodo_{name}.DOCX")

        


if __name__ == "__main__":
    app = App()
    app.mainloop()