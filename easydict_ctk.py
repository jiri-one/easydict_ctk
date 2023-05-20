import customtkinter as ctk
from customtkinter.windows.widgets.core_widget_classes import DropdownMenu
from easydict_ctk_widgets import OptionMenuWithImages
from tkinter import Menu
from PIL import Image
from pathlib import Path
import sys
import hupper

FLAG_CZE = Path(__file__).parent / "images/flag_cze.png"
FLAG_ENG = Path(__file__).parent / "images/flag_eng.png"
assert FLAG_CZE.exists()
assert FLAG_CZE.exists()


class EasyDict(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EasyDict-CTk")
        self.grid_columnconfigure(0, weight=1)
        self.geometry(f"{580}x{1100}")

        # and then create widgets
        self.create_widgets()

    def create_widgets(self):
        # add flag images
        self.flag_cze = ctk.CTkImage(Image.open(FLAG_CZE))
        self.flag_eng = ctk.CTkImage(Image.open(FLAG_ENG))
        # add search entry
        self.entry_search = ctk.CTkEntry(self)
        self.entry_search.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        # add search button
        self.button_search = ctk.CTkButton(
            self,
            text="Search",
            image=self.flag_cze,
            command=self.search_callback,
            compound="right",
        )
        self.button_search.grid(row=0, column=1, padx=20, pady=20)
        self.button_search.bind("<Button-3>", self.do_popup)
        self.lang_menu = DropdownMenu(
            master=self, values=["Czech", "English2"], command=self.test
        )
        self.lang_chooser = OptionMenuWithImages(
            self, values=["option 1", "option 2"], command=self.test
        )
        self.lang_chooser.set("")
        self.lang_chooser.grid(row=0, column=2, padx=20, pady=20)

        # add segmented button for switch between Fulltext and Whole word
        self.seg_button = ctk.CTkSegmentedButton(self)
        self.seg_button.grid(
            row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew", columnspan=2
        )
        self.seg_button.configure(values=["Whole word", "Fulltext"])
        self.seg_button.set("Whole word")

        # self.optionmenu = ctk.CTkOptionMenu(
        #     self, values=[self.flag_cze, self.flag_eng], command=self.test
        # )
        # self.optionmenu.set(self.flag_cze)
        # self.optionmenu.grid(
        #     row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew", columnspan=2
        # )

    def test(nevim, event):
        print("event", nevim, event)

    def search_callback(test):
        print(test)

    def do_popup(self, event):
        self.lang_menu.open(
            self.button_search.winfo_rootx(),
            self.button_search.winfo_rooty() + self.button_search._current_height + 0,
        )


def main(args=sys.argv[1:]):
    if "--reload" in args:
        # start_reloader will only return in a monitored subprocess
        reloader = hupper.start_reloader("easydict_ctk.main")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        ctk.set_widget_scaling(1.2)
        app = EasyDict()
        app.mainloop()


if __name__ == "__main__":
    main()
