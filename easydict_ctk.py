import customtkinter as ctk
from customtkinter.windows.widgets.core_widget_classes import DropdownMenu
from PIL import Image
from pathlib import Path
import sys
import hupper

# internal imports
from easydict_ctk_widgets import ResultsFrame
from backends import sqlite_backend

FLAG_CZE = Path(__file__).parent / "images/flag_cze.png"
FLAG_ENG = Path(__file__).parent / "images/flag_eng.png"
assert FLAG_CZE.exists()
assert FLAG_CZE.exists()


class EasyDict(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EasyDict-CTk")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.geometry(f"{580}x{1100}")
        self.db = sqlite_backend.SQLiteBackend()
        self.lang = "eng"
        self.font = ctk.CTkFont(family="Arial", size=22, weight="normal")

        # and then create widgets
        self.create_widgets()

    def create_widgets(self):
        # add flag images
        self.flag_cze = ctk.CTkImage(Image.open(FLAG_CZE))
        self.flag_eng = ctk.CTkImage(Image.open(FLAG_ENG))
        # add search entry
        self.search_text = ctk.StringVar(value="Enter your search text here.")
        self.entry_search = ctk.CTkEntry(
            self,
            textvariable=self.search_text,
            corner_radius=0,
            border_width=3,
            font=self.font,
        )
        self.entry_search.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        # add search button
        self.button_search = ctk.CTkButton(
            self,
            text="Search",
            image=self.flag_cze if self.lang == "cze" else self.flag_eng,
            command=self.search_callback,
            compound="right",
            font=self.font,
            width=5,  # it will be bigger then 5, it will fit to text and image
        )
        self.button_search.grid(row=0, column=1, pady=10)
        self.button_search.bind("<Button-3>", self.do_popup)
        self.lang_menu = DropdownMenu(
            master=self,
            values=["CZE", "ENG"],
            command=self.lang_selector,
            font=self.font,
        )
        # add language chooser
        self.lang_chooser = ctk.CTkOptionMenu(
            self,
            values=["CZE", "ENG"],
            command=self.lang_selector,
            width=5,  # it will be bigger then 5, it will fit to text and image
            font=self.font,
        )
        # set lang_chooser to same height like button_search
        self.lang_chooser.configure(height=self.button_search._current_height)
        self.lang_chooser.set("ENG" if self.lang == "eng" else "CZE")
        self.lang_chooser.grid(row=0, column=2, padx=10)
        # add segmented button for switch between Fulltext and Whole word
        self.fulltext = ctk.StringVar(value="Whole word")
        self.seg_button = ctk.CTkSegmentedButton(
            self,
            values=["Whole word", "Fulltext"],
            variable=self.fulltext,
            font=self.font,
        )
        self.seg_button.grid(row=1, column=0, sticky="ew", padx=10, columnspan=3)
        # add results frame
        self.results_frame = ResultsFrame(self)
        self.results_frame.grid(
            row=2, column=0, padx=10, pady=10, columnspan=3, sticky="nsew"
        )
        # for i in range(20):  # add items with images
        #     self.results_frame.add_result(f"image and item {i}")

    def lang_selector(self, lang):
        self.lang = lang.lower()
        self.button_search.configure(
            image=self.flag_cze if self.lang == "cze" else self.flag_eng
        )
        self.lang_chooser.set("ENG" if self.lang == "eng" else "CZE")

    def search_callback(self):
        word = self.search_text.get()
        fulltext = False
        if self.fulltext.get() == "Fulltext":
            fulltext = True
        results = self.db.search_sorted(word=word, lang=self.lang, fulltext=fulltext)
        count = len(results)
        # remove old results
        self.results_frame.remove_results()
        # add first label with total number of results
        self.results_frame.add_count(count)
        # and add labels with results (one by one)
        for result in results:
            self.results_frame.add_result(result)

    def do_popup(self, event):
        self.lang_menu.open(
            self.button_search.winfo_rootx(),
            self.button_search.winfo_rooty() + self.button_search.winfo_height() + 0,
        )


def main(args=sys.argv[1:]):
    if "--reload" in args:
        # start_reloader will only return in a monitored subprocess
        reloader = hupper.start_reloader("easydict_ctk.main")
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        ctk.set_widget_scaling(1.2)
        app = EasyDict()
        app.mainloop()


if __name__ == "__main__":
    main()
