import customtkinter


class ResultsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.label_list = []

    def add_count(self, count):
        first_label_with_count_info = customtkinter.CTkLabel(
            self, text=f"The number of results found is: {count}", compound="left", padx=5, anchor="w"
        )

        first_label_with_count_info.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        self.label_list.append(first_label_with_count_info)

    def add_result(self, item):
        label = customtkinter.CTkLabel(
            self, text=item, compound="left", padx=5, anchor="w"
        )

        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        self.label_list.append(label)

    def remove_results(self):
        while self.label_list:
            label = self.label_list.pop()
            label.destroy()
        return
