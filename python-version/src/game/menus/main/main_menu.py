# pylint: disable=line-too-long, unused-import, global-statement
# type: ignore[arg-type]
"""
Main menu
"""

import tkinter as tk
from tkinter import ttk


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
            "Arial", 16), default="disabled")
        self.load_button.grid(row=3, column=0, sticky="nsew")
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

    def load_button_command(self):
        """
        Command to be executed when the load button is clicked
        """
        # TODO: Implement save file checking to determine if a save file exists
        # and in turn enable the load button
        self.parent.check_save_file()
        # if self.save_file_exists:
        #     self.load_button.config(state="normal")
        # else:
        #     self.load_button.config(state="disabled")
        pass

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
