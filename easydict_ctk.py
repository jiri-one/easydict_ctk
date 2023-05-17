import customtkinter as ctk
import tkinter.font as tkFont
from PIL import Image
from pathlib import Path
import sys
import hupper

FLAG_CZE = Path(__file__).parent / "images/flag_cze.svg"
FLAG_ENG = Path(__file__).parent / "images/flag_eng.svg"
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
        # add search entry
        self.entry_search = ctk.CTkEntry(self)
        self.entry_search.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        # add search button
        self.button_search = ctk.CTkButton(
            self, text="Search", command=self.search_callback
        )
        self.button_search.grid(row=0, column=1, padx=20, pady=20)
        self.button_search.bind("<Button-3>", self.test)
        # add flag images
        self.flag_cze = ctk.CTkImage(Image.open(FLAG_CZE, "CZE FLAG"), size=(26, 26))
        self.flag_eng = ctk.CTkImage(Image.open(FLAG_ENG, "ENG FLAG"), size=(26, 26))
        self.navigation_frame_label = ctk.CTkLabel(
            self, text="Image Example", image=self.flag_cze, compound="right"
        )

        # add segmented button for switch between Fulltext and Whole word
        self.seg_button = ctk.CTkSegmentedButton(self)
        self.seg_button.grid(
            row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew", columnspan=2
        )
        self.seg_button.configure(values=["Whole word", "Fulltext"])
        self.seg_button.set("Whole word")

    def test(nevim, event):
        print("event", nevim, event)

    def search_callback(test):
        print(test)


def main(args=sys.argv[1:]):
    if "--reload" in args:
        # start_reloader will only return in a monitored subprocess
        reloader = hupper.start_reloader("easydict_ctk.main")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        app = EasyDict()
        app.mainloop()


if __name__ == "__main__":
    main()
