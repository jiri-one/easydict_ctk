import customtkinter as ctk
import tkinter.font as tkFont
import sys
import hupper


class EasyDict(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EasyDict-CTk")
        #self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.geometry(f"{580}x{1100}")
        # add search entry
        self.entry_search = ctk.CTkEntry(self)
        self.entry_search.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        # add search button
        self.button_search = ctk.CTkButton(self, text="Search", command=self.search_callback)
        self.button_search.grid(row=0, column=1, padx=20, pady=20)
        self.button_search.bind("<Button-3>", self.test)
        # add segmented button for switch between Fulltext and Whole word
        self.seg_button = ctk.CTkSegmentedButton(self)
        self.seg_button.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew", columnspan=2)
        self.seg_button.configure(values=["Whole word", "Fulltext"])
        self.seg_button.set("Whole word")
    
    def test(nevim, event):
        print("event", nevim, event)


    def search_callback(test):
        print(test)


def main(args=sys.argv[1:]):
    if '--reload' in args:
        # start_reloader will only return in a monitored subprocess
        reloader = hupper.start_reloader('easydict_ctk.main')
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        app = EasyDict()
        app.mainloop()
        

if __name__ == "__main__":
    main()
