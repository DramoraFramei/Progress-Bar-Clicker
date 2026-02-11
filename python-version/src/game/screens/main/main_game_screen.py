# pylint: disable=line-too-long, unused-import, global-statement
#
"""
Main game screen
"""

import tkinter as tk
from tkinter import ttk


try:
    from ...app.progree_bar_clicker_app import ProgressBarClickerApp
except ImportError:
    print("Could not import ProgressBarClickerApp")

MAX_VALUE = 100
FILL_SPEED = 0.01
CLICKS = 0


class MainGameScreen(tk.Frame):
    """
    Main game screen
    """

    def __init__(self, parent: "ProgressBarClickerApp"):
        """
        Initialize the main game screen
        """
        super().__init__(parent)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title = tk.Label(
            self, text="Progress Bar Clicker Game - Main Game Screen", font=("Arial", 20))
        self.title.grid(row=0, column=2, columnspan=3,
                        sticky="nsew", pady=(0, 10))
        self.progress_label = tk.Label(
            self, text=f"Progress: {CLICKS / MAX_VALUE * 100}%", font=("Arial", 16))
        self.progress_label.grid(
            row=1, column=2, columnspan=3, sticky="nsew", pady=(0, 10))
        self.progress_bar = ttk.Progressbar(
            self, orient="horizontal", length=300, mode="determinate", maximum=MAX_VALUE, value=CLICKS * FILL_SPEED)
        self.progress_bar.grid(
            row=1, column=2, columnspan=3, sticky="nsew", pady=(0, 10))
        self.clicks_label = tk.Label(
            self, text=f"Clicks: {CLICKS}", font=("Arial", 16))
        self.clicks_label.grid(
            row=2, column=2, columnspan=3, sticky="nsew", pady=(0, 10))
        self.click_button = tk.Button(
            self, text="Click me", command=self.click_button_command, font=("Arial", 16))
        self.click_button.grid(
            row=2, column=2, columnspan=3, sticky="nsew", pady=(0, 10))
        self.upgrades_screen_button = tk.Button(
            self, text="Upgrades Screen", command=lambda: self.parent.switch_menu("upgrades_screen"), font=("Arial", 16))
        self.upgrades_screen_button.grid(
            row=2, column=2, columnspan=3, sticky="nsew", pady=(0, 10))

    def click_button_command(self):
        """
        Command to be executed when the click button is clicked
        """
        global CLICKS
        CLICKS += 1
        self.progress_bar.config(value=CLICKS * FILL_SPEED)
        self.progress_label.config(
            text=f"Progress: {CLICKS / MAX_VALUE * 100}%")
        self.clicks_label.config(text=f"Clicks: {CLICKS}")
