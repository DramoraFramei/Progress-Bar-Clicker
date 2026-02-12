# pylint: disable=line-too-long
"""
Imports for the Progress Bar Clicker App
This file is used to import all the necessary modules for the Progress Bar
Clicker App in order to avoid circular imports.
"""

import datetime
import os

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
ROOT_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))).replace("\\", "/")
SRC_DIR = os.path.join(ROOT_DIR, "src").replace("\\", "/")
GAME_DIR = os.path.join(SRC_DIR, "game").replace("\\", "/")
APP_DIR = os.path.join(GAME_DIR, "app").replace("\\", "/")
APP_FILE = getattr(
    __import__(os.path.basename(APP_DIR).replace(".py", "")), "ProgressBarClickerApp")
SWITCH_SCREEN_COMMAND = getattr(
    __import__(os.path.basename(APP_DIR).replace(".py", "")), "switch_screen")
SWITCH_MENU_COMMAND = getattr(
    __import__(os.path.basename(APP_DIR).replace(".py", "")), "switch_menu")
CHECK_SAVE_FILE_COMMAND = getattr(
    __import__(os.path.basename(APP_DIR).replace(".py", "")), "check_save_file")
RUN_COMMAND = getattr(
    __import__(os.path.basename(APP_DIR).replace(".py", "")), "run")
QUIT_COMMAND = getattr(
    __import__(os.path.basename(APP_DIR).replace(".py", "")), "quit_game")
SCREENS_DIR = os.path.join(GAME_DIR, "screens").replace("\\", "/")
SCREENS_FILES = {
    "main_game_screen": getattr(
        __import__(os.path.basename(SCREENS_DIR).replace(".py", "")), "MainGameScreen"),
    "quit_game_screen": getattr(
        __import__(os.path.basename(SCREENS_DIR).replace(".py", "")), "QuitGameScreen"),
    "upgrades_screen": getattr(
        __import__(os.path.basename(SCREENS_DIR).replace(".py", "")), "UpgradesScreen"),
    "rebirth_screen": getattr(
        __import__(os.path.basename(SCREENS_DIR).replace(".py", "")), "RebirthScreen"),
    "prestige_screen": getattr(
        __import__(os.path.basename(SCREENS_DIR).replace(".py", "")), "PrestigeScreen"),
    "reincarnation_screen": getattr(
        __import__(os.path.basename(SCREENS_DIR).replace(".py", "")), "ReincarnationScreen"),
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
SLOTS_FILES_NAME = str.format(
    str("{slot_name}_{TIMESTAMP}"), SLOTS_FILES_EXTENSION).replace("\\", "/")
SLOTS_FILES = {}
for slot_name, folder in SLOTS_FOLDERS.items():
    SLOTS_FILES[slot_name] = os.path.join(folder, str.format(
        SLOTS_FILES_NAME, slot_name)).replace("\\", "/")
DATA_DIR = os.path.join(GAME_DIR, "data").replace("\\", "/")
SCRIPTS_DIR = os.path.join(DATA_DIR, "scripts").replace("\\", "/")
FILE_CHECK_FILE = getattr(
    __import__(os.path.basename(SCRIPTS_DIR).replace(".py", "")), "file_check")
MENUS_DIR = os.path.join(GAME_DIR, "menus").replace("\\", "/")
MENUS_FILES = {
    "main_menu": getattr(
        __import__(os.path.basename(MENUS_DIR).replace(".py", "")), "MainMenu"),
    "save_menu": getattr(
        __import__(os.path.basename(MENUS_DIR).replace(".py", "")), "SaveMenu"),
    "load_menu": getattr(
        __import__(os.path.basename(MENUS_DIR).replace(".py", "")), "LoadMenu"),
    "options_menu": getattr(
        __import__(os.path.basename(MENUS_DIR).replace(".py", "")), "OptionsMenu"),
    "credits_menu": getattr(
        __import__(os.path.basename(MENUS_DIR).replace(".py", "")), "CreditsMenu"),
    "pause_menu": getattr(
        __import__(os.path.basename(MENUS_DIR).replace(".py", "")), "PauseMenu"),
}

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
