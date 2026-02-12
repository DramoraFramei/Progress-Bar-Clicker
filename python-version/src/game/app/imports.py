# pylint: disable=line-too-long
"""
Imports for the Progress Bar Clicker App
This file is used to import all the necessary modules for the Progress Bar
Clicker App in order to avoid circular imports.
"""

import datetime
import os

# Package base for src.game layout (when run from project root)
_PKG = "src.game"

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
ROOT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))).replace("\\", "/")
SRC_DIR = os.path.join(ROOT_DIR, "src").replace("\\", "/")
GAME_DIR = os.path.join(SRC_DIR, "game").replace("\\", "/")
APP_DIR = os.path.join(GAME_DIR, "app").replace("\\", "/")

SCREENS_DIR = os.path.join(GAME_DIR, "screens").replace("\\", "/")
_screens_main = __import__(f"{_PKG}.screens.main", fromlist=["main"])
_screens_quit = __import__(f"{_PKG}.screens.quit", fromlist=["quit"])
SCREENS_FILES = {
    "main_game_screen": getattr(_screens_main, "MainGameScreen"),
    "quit_game_screen": getattr(_screens_quit, "QuitGameScreen"),
    "upgrades_screen": getattr(_screens_main, "UpgradesScreen"),
    "rebirth_screen": getattr(_screens_main, "RebirthScreen"),
    "prestige_screen": getattr(_screens_main, "PrestigeScreen"),
    "reincarnation_screen": getattr(_screens_main, "ReincarnationScreen"),
}

SAVE_DIR = os.path.join(GAME_DIR, "saves").replace("\\", "/")
SLOTS_DIR = os.path.join(SAVE_DIR, "slots").replace("\\", "/")
SLOTS_FOLDERS = {
    "slot1": os.path.join(SLOTS_DIR, "slot1").replace("\\", "/"),
    "slot2": os.path.join(SLOTS_DIR, "slot2").replace("\\", "/"),
    "slot3": os.path.join(SLOTS_DIR, "slot3").replace("\\", "/"),
    "slot4": os.path.join(SLOTS_DIR, "slot4").replace("\\", "/"),
    "slot5": os.path.join(SLOTS_DIR, "slot5").replace("\\", "/"),
    "slot6": os.path.join(SLOTS_DIR, "slot6").replace("\\", "/"),
    "slot7": os.path.join(SLOTS_DIR, "slot7").replace("\\", "/"),
    "slot8": os.path.join(SLOTS_DIR, "slot8").replace("\\", "/"),
    "slot9": os.path.join(SLOTS_DIR, "slot9").replace("\\", "/"),
    "slot10": os.path.join(SLOTS_DIR, "slot10").replace("\\", "/"),
}
SLOTS_FILES_EXTENSION = ".json"
SLOTS_FILES_NAME = ("{slot_name}_{TIMESTAMP}" + SLOTS_FILES_EXTENSION).replace("\\", "/")
SLOTS_FILES = {}
for slot_name, folder in SLOTS_FOLDERS.items():
    SLOTS_FILES[slot_name] = os.path.join(folder, SLOTS_FILES_NAME.format(
        slot_name=slot_name, TIMESTAMP=TIMESTAMP)).replace("\\", "/")
DATA_DIR = os.path.join(GAME_DIR, "data").replace("\\", "/")
SCRIPTS_DIR = os.path.join(DATA_DIR, "scripts").replace("\\", "/")
_scripts = __import__(f"{_PKG}.data.scripts.file_checks", fromlist=["file_checks"])
FILE_CHECK_FILE = getattr(_scripts, "file_check", None) or getattr(_scripts, "FILE_CHECKS")
MENUS_DIR = os.path.join(GAME_DIR, "menus").replace("\\", "/")
_menus_main = __import__(f"{_PKG}.menus.main", fromlist=["main"])
_menus_save = __import__(f"{_PKG}.menus.save", fromlist=["save"])
_menus_load = __import__(f"{_PKG}.menus.load", fromlist=["load"])
_menus_options = __import__(f"{_PKG}.menus.options", fromlist=["options"])
_menus_credits = __import__(f"{_PKG}.menus.credits", fromlist=["credits"])
_menus_pause = __import__(f"{_PKG}.menus.pause", fromlist=["pause"])
MENUS_FILES = {
    "main_menu": getattr(_menus_main, "MainMenu"),
    "save_menu": getattr(_menus_save, "SaveMenu"),
    "load_menu": getattr(_menus_load, "LoadMenu"),
    "options_menu": getattr(_menus_options, "OptionsMenu"),
    "credits_menu": getattr(_menus_credits, "CreditsMenu"),
    "pause_menu": getattr(_menus_pause, "PauseMenu"),
}

# App-related (loaded last to avoid circular import)
_app = __import__(f"{_PKG}.app.progree_bar_clicker_app", fromlist=["progree_bar_clicker_app"])
APP_FILE = getattr(_app, "ProgressBarClickerApp")
# These are instance methods - use unbound methods from the class
SWITCH_SCREEN_COMMAND = getattr(APP_FILE, "switch_screen")
SWITCH_MENU_COMMAND = getattr(APP_FILE, "switch_menu")
CHECK_SAVE_FILE_COMMAND = getattr(APP_FILE, "check_save_file")
RUN_COMMAND = getattr(APP_FILE, "run")
QUIT_COMMAND = getattr(APP_FILE, "quit_game")

__all__ = [
    "ROOT_DIR",
    "SRC_DIR",
    "GAME_DIR",
    "APP_DIR",
    "APP_FILE",
    "SWITCH_SCREEN_COMMAND",
    "SWITCH_MENU_COMMAND",
    "RUN_COMMAND",
    "CHECK_SAVE_FILE_COMMAND",
    "QUIT_COMMAND",
    "SCREENS_DIR",
    "SCREENS_FILES",
    "SAVE_DIR",
    "SLOTS_DIR",
    "SLOTS_FOLDERS",
    "SLOTS_FILES_EXTENSION",
    "SLOTS_FILES_NAME",
    "TIMESTAMP",
    "SLOTS_FILES",
    "DATA_DIR",
    "SCRIPTS_DIR",
    "FILE_CHECK_FILE",
    "MENUS_DIR",
    "MENUS_FILES",
]
