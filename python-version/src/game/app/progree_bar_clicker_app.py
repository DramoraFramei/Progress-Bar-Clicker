# pylint: disable=line-too-long, unused-import, dangerous-default-value
"""
Progress Bar Clicker App
"""
import os
import tkinter as tk
from tkinter import ttk

IMPORTS = getattr(
    __import__(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).replace(
        "\\", "/").split("/")[-1]), "imports.py")
FILE_CHECK_FILE = IMPORTS["FILE_CHECK_FILE"]
MENUS_FILES = IMPORTS["MENUS_FILES"]
SCREENS_FILES = IMPORTS["SCREENS_FILES"]
SLOTS_FILES_NAME = IMPORTS["SLOTS_FILES_NAME"]
SLOTS_FOLDERS = IMPORTS["SLOTS_FOLDERS"]
APP_FILE = IMPORTS["APP_FILE"]


class ProgressBarClickerApp(tk.Tk):
    """
    Progress Bar Clicker App
    """

    def __init__(self, title: str = "Progress Bar Clicker"):
        """
        Initialize the Progress Bar Clicker App
        """
        super().__init__()
        self.title(title)
        self.geometry("1920x1080")
        self.resizable(True, True)
        self.main_game_screen = SCREENS_FILES["main_game_screen"](
            tk.Frame(self))
        self.quit_game_screen = SCREENS_FILES["quit_game_screen"](
            tk.Frame(self))
        self.upgrades_screen = SCREENS_FILES["upgrades_screen"](tk.Frame(self))
        self.rebirth_screen = SCREENS_FILES["rebirth_screen"](tk.Frame(self))
        self.prestige_screen = SCREENS_FILES["prestige_screen"](tk.Frame(self))
        self.reincarnation_screen = SCREENS_FILES["reincarnation_screen"](
            tk.Frame(self))
        self.main_menu = MENUS_FILES["main_menu"](tk.Frame(self))
        self.save_menu = MENUS_FILES["save_menu"](tk.Frame(self))
        self.load_menu = MENUS_FILES["load_menu"](tk.Frame(self))
        self.options_menu = MENUS_FILES["options_menu"](tk.Frame(self))
        self.credits_menu = MENUS_FILES["credits_menu"](tk.Frame(self))
        self.pause_menu = MENUS_FILES["pause_menu"](tk.Frame(self))
        self.main_game_screen.pack(fill="both", expand=True)

    def switch_screen(self, screen_name: str):
        """
        Switch to the specified screen
        """
        for screen_name, screen_widget in SCREENS_FILES.items():
            screen_widget.grid_forget()
            if screen_name == "main_game_screen":
                screen_widget.grid(row=0, column=0, sticky="nsew")
            elif screen_name == "quit_game_screen":
                self.quit()
                self.destroy()
            elif screen_name == "upgrades_screen":
                screen_widget.grid(row=0, column=0, sticky="nsew")
            elif screen_name == "rebirth_screen":
                screen_widget.grid(row=0, column=0, sticky="nsew")
            elif screen_name == "prestige_screen":
                screen_widget.grid(row=0, column=0, sticky="nsew")
            elif screen_name == "reincarnation_screen":
                screen_widget.grid(row=0, column=0, sticky="nsew")
            else:
                print(f"Unknown screen: {screen_name}")
                raise ValueError(f"Unknown screen: {screen_name}")

    def switch_menu(self, menu_name: str):
        """
        Switch to the specified menu
        """
        for menu_name, menu_widget in MENUS_FILES.items():
            menu_widget.grid_forget()
            if menu_name == "main_menu":
                menu_widget.grid(row=0, column=0, sticky="nsew")
            elif menu_name == "save_menu":
                menu_widget.grid(row=0, column=0, sticky="nsew")
            elif menu_name == "load_menu":
                menu_widget.grid(row=0, column=0, sticky="nsew")
            elif menu_name == "options_menu":
                menu_widget.grid(row=0, column=0, sticky="nsew")
            elif menu_name == "credits_menu":
                menu_widget.grid(row=0, column=0, sticky="nsew")
            elif menu_name == "pause_menu":
                menu_widget.grid(row=0, column=0, sticky="nsew")
            else:
                print(f"Unknown menu: {menu_name}")
                raise ValueError(f"Unknown menu: {menu_name}")

    def check_save_file(self, slots_exists: dict[list[str], bool] = {}, result: bool = False):
        """
        Check if a save file exists
        """
        # Run the file check file with the slots folders and return the result
        # of the file check file as a boolean
        file_check_result = FILE_CHECK_FILE(
            list(SLOTS_FOLDERS.values()), list(slots_exists.keys()))
        # If the file check finds a file in any slot folder, set the result to
        # True and return the result along with the slot folders with a file in
        # them as a list that includes the file name and timestamp
        if file_check_result.bool():
            result = True
            slot_folders = [os.path.join(slot_folder, SLOTS_FILES_NAME) for slot_folder in list(
                SLOTS_FOLDERS.values()) for slot_name in list(slots_exists.keys()) if slots_exists[slot_name] is True]
            return result, slot_folders
        else:
            result = False
        return result

    def run(self):
        """
        Run the Progress Bar Clicker App
        """
        self.mainloop()

    def quit_game(self):
        """
        Quit the Progress Bar Clicker App
        """
        self.switch_screen("quit_game_screen")


def main():
    """
    Main function to run the Progress Bar Clicker App
    """
    app = ProgressBarClickerApp()
    app.run()


if __name__ == "__main__":
    main()
