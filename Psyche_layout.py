import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
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

        # create tabview
        self.tabview = customtkinter.Form1(self)
        self.tabview.grid(row=0, column=1, padx=10, pady=(20, 0), sticky="nsew")
        self.tabview.add("Form1")
        self.tabview.add("Form2")
        
        # Form1 inside
        self.tabview.tab("Form1").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.nameLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="Name")
        
        self.nameLabel.grid(row=0, column=0,
							padx=100, pady=20,
							sticky="nsew")
        
        self.nameEntry = customtkinter.CTkEntry(self.tabview.tab("Form1"),
						placeholder_text="Teja")
        self.nameEntry.grid(row=0, column=1,
							columnspan=3, padx=100,

							pady=20, sticky="ew")
        
        self.lastnameLabel = customtkinter.CTkLabel(self.tabview.tab("Form1"),
									text="LastName")
        
        self.lastnameLabel.grid(row=1, column=0,
							padx=0, pady=20,
							sticky="nsew")
        
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


if __name__ == "__main__":
    app = App()
    app.mainloop()