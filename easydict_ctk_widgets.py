import customtkinter as ctk
from pathlib import Path
from PIL import Image

ED_ICON = Path(__file__).parent / "images/ed_icon.png"
assert ED_ICON.exists()


class ResultsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.font = ctk.CTkFont(family="Arial", size=22, weight="normal")
        self.label_list = []

        # create "front page"
        welcome_label = ctk.CTkLabel(
            self,
            text="Welcome to EasyDict\n",
            padx=5,
            font=ctk.CTkFont(family="Arial", size=24, weight="bold"),
        )
        self.label_list.append(welcome_label)
        welcome_label.grid(row=len(self.label_list), column=0, sticky="nsew")

        ed_icon = ctk.CTkImage(Image.open(ED_ICON), size=(284, 285))
        icon_label = ctk.CTkLabel(
            self, text="", compound="bottom", padx=5, image=ed_icon
        )
        self.label_list.append(icon_label)
        icon_label.grid(row=len(self.label_list), column=0, sticky="nsew")
        
        open_label = ctk.CTkLabel(
            self,
            text="\nThe first open source translator which is completely open with dictionary data too.",
            padx=5,
            font=self.font,
        )
        open_label.configure(wraplength=open_label.winfo_width() - 500)
        open_label.bind(
            "<Configure>",
            lambda e: open_label.configure(wraplength=open_label.winfo_width() - 500),
        )
        self.label_list.append(open_label)
        open_label.grid(row=len(self.label_list), column=0, sticky="nsew")

    def add_count(self, count):
        first_label_with_count_info = ctk.CTkLabel(
            self,
            text=f"The number of results found is: {count}",
            compound="left",
            padx=5,
            anchor="w",
        )

        first_label_with_count_info.grid(
            row=len(self.label_list), column=0, pady=(0, 10), sticky="w"
        )
        self.label_list.append(first_label_with_count_info)

    def add_result(self, item):
        label = ctk.CTkLabel(self, text=item, compound="left", padx=5, anchor="w")

        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        self.label_list.append(label)

    def remove_results(self):
        while self.label_list:
            label = self.label_list.pop()
            label.destroy()
        return
