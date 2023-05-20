# CTk widget created only for EasyDict-CTk

import customtkinter as ctk
import tkinter


class OptionMenuWithImages(ctk.CTkOptionMenu):
    def _create_grid(self):
        self._canvas.grid(row=0, column=0, sticky="nsew")

        left_section_width = self._current_width - self._current_height
        self._text_label.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(
                max(
                    self._apply_widget_scaling(self._corner_radius),
                    self._apply_widget_scaling(3),
                ),
                max(
                    self._apply_widget_scaling(
                        self._current_width - left_section_width + 3
                    ),
                    self._apply_widget_scaling(3),
                ),
            ),
        )

    def _draw(self, no_color_updates=False):
        super()._draw(no_color_updates)

        left_section_width = self._current_width - self._current_height
        requires_recoloring = (
            self._draw_engine.draw_rounded_rect_with_border_vertical_split(
                self._apply_widget_scaling(self._current_width),
                self._apply_widget_scaling(self._current_height),
                self._apply_widget_scaling(self._corner_radius),
                0,
                self._apply_widget_scaling(left_section_width),
            )
        )

        requires_recoloring_2 = self._draw_engine.draw_dropdown_arrow(
            self._apply_widget_scaling(
                self._current_width - (self._current_height / 2)
            ),
            self._apply_widget_scaling(self._current_height / 2),
            self._apply_widget_scaling(self._current_height / 3),
        )

        if no_color_updates is False or requires_recoloring or requires_recoloring_2:
            self._canvas.configure(bg=self._apply_appearance_mode(self._bg_color))

            # self._canvas.itemconfig(
            #     "inner_parts_left",
            #     outline=self._apply_appearance_mode(self._fg_color),
            #     fill=self._apply_appearance_mode(self._fg_color),
            # )
            # self._canvas.itemconfig(
            #     "inner_parts_right",
            #     outline=self._apply_appearance_mode(self._button_color),
            #     fill=self._apply_appearance_mode(self._button_color),
            # )

            # self._text_label.configure(fg=self._apply_appearance_mode(self._text_color))

            if self._state == tkinter.DISABLED:
                # self._text_label.configure(
                #     fg=(self._apply_appearance_mode(self._text_color_disabled))
                # )
                self._canvas.itemconfig(
                    "dropdown_arrow",
                    fill=self._apply_appearance_mode(self._text_color_disabled),
                )
            else:
                # self._text_label.configure(
                #     fg=self._apply_appearance_mode(self._text_color)
                # )
                self._canvas.itemconfig(
                    "dropdown_arrow", fill=self._apply_appearance_mode(self._text_color)
                )

            # self._text_label.configure(bg=self._apply_appearance_mode(self._fg_color))

        self._canvas.update_idletasks()
