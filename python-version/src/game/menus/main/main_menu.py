# pylint: disable=line-too-long, unused-import, global-statement, too-many-instance-attributes
# type: ignore[arg-type]
"""
Main menu
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...app.imports import APP_FILE as ProgressBarClickerApp


class MainMenu(tk.Frame):
    """
    Main menu
    """

    def __init__(self, parent: "ProgressBarClickerApp"):
        """
        Initialize the main menu
        """
        super().__init__(parent)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title = tk.Label(self, text="Main Menu", font=("Arial", 20))
        self.title.grid(row=0, column=0, sticky="nsew")
        self.play_button = tk.Button(
            self, text="Play", command=self.play_button_command, font=("Arial", 16))
        self.play_button.grid(row=1, column=0, sticky="nsew")
        self.save_button = tk.Button(
            self, text="Save", command=self.save_button_command, font=("Arial", 16))
        self.save_button.grid(row=2, column=0, sticky="nsew")
        self.load_button = tk.Button(self, text="Load", command=self.load_button_command, font=(
            "Arial", 16), state="disabled")
        self.load_button.grid(row=3, column=0, sticky="nsew")
        self.load_button_command_enabled()
        self.options_button = tk.Button(
            self, text="Options", command=self.options_button_command, font=("Arial", 16))
        self.options_button.grid(row=4, column=0, sticky="nsew")
        self.credits_button = tk.Button(
            self, text="Credits", command=self.credits_button_command, font=("Arial", 16))
        self.credits_button.grid(row=5, column=0, sticky="nsew")
        self.quit_button = tk.Button(
            self, text="Quit", command=self.quit_button_command, font=("Arial", 16))
        self.quit_button.grid(row=6, column=0, sticky="nsew")

    def play_button_command(self):
        """
        Command to be executed when the play button is clicked
        """
        self.parent.switch_screen("main_game_screen")

    def save_button_command(self):
        """
        Command to be executed when the save button is clicked
        """
        self.parent.switch_menu("save_menu")

    def load_button_command_enabled(self):
        """
        Command to be executed when the main menu is loaded and the load button is enabled
        """
        slots_exists = getattr(self.parent, "slots_exists", {})
        result = self.parent.check_save_file(slots_exists=slots_exists, result=False)
        if isinstance(result, tuple):
            result = result[0]
        if hasattr(result, "bool") and result.bool():
            self.load_button.config(state="normal")
        elif result:
            self.load_button.config(state="normal")
        else:
            self.load_button.config(state="disabled")

    def load_button_command(self):
        """
        Command to be executed when the load button is clicked
        """
        self.parent.switch_menu("load_menu")

    def options_button_command(self):
        """
        Command to be executed when the options button is clicked
        """
        self.parent.switch_menu("options_menu")

    def credits_button_command(self):
        """
        Command to be executed when the credits button is clicked
        """
        self.parent.switch_menu("credits_menu")

    def quit_button_command(self):
        """
        Command to be executed when the quit button is clicked
        """
        self.parent.switch_menu("quit_menu")


def main():
    """
    Main function to run the Main Menu
    """
    from ...app.imports import APP_FILE as ProgressBarClickerApp

    parent = ProgressBarClickerApp(title="Main Menu")
    main_menu = MainMenu(parent)
    main_menu.pack(fill="both", expand=True)
    parent.run()


if __name__ == "__main__":
    main()
