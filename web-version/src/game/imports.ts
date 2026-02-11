// Import 'path' module for path operations
import * as path from 'path';

// ROOT_DIR is the root directory of the project
export const ROOT_DIR = path.resolve(__dirname, '..', '..');
// SRC_DIR is the directory of the src
export const SRC_DIR = path.resolve(ROOT_DIR, 'src');
// GAME_DIR is the directory of the game
export const GAME_DIR = path.resolve(SRC_DIR, 'game');
// MENU_DIR is the directory of the menu
export const MENU_DIR = path.resolve(GAME_DIR, 'menu');
// MAIN_DIR is the directory of the main
export const MAIN_DIR = path.resolve(MENU_DIR, 'main');
// MAIN_HTML_DIR is the directory of the main html
export const MAIN_HTML_DIR = path.resolve(MAIN_DIR, 'html');
// MAIN_SCRIPTS_DIR is the directory of the main scripts
export const MAIN_SCRIPTS_DIR = path.resolve(MAIN_DIR, 'scripts');
// MAIN_STYLESHEETS_DIR is the directory of the main stylesheets
export const MAIN_STYLESHEETS_DIR = path.resolve(MAIN_DIR, 'stylesheets');
// SAVE_DIR is the directory of the save
export const SAVE_DIR = path.resolve(MENU_DIR, 'save');
// LOAD_DIR is the directory of the load
export const LOAD_DIR = path.resolve(MENU_DIR, 'load');
// OPTIONS_DIR is the directory of the options
export const OPTIONS_DIR = path.resolve(MENU_DIR, 'options');
// CREDITS_DIR is the directory of the credits
export const CREDITS_DIR = path.resolve(MENU_DIR, 'credits');
// GAME1_DIR is the directory of the game menu
export const GAME_MENU_DIR = path.resolve(MENU_DIR, 'game');
// CONFIG_DIR is the directory of the config
export const CONFIG_DIR = path.resolve(GAME_DIR, 'config');

// MAIN_MENU_HTML_FILE is the file of the main menu
export const MAIN_MENU_HTML_FILE = path.resolve(
	MAIN_HTML_DIR,
	'main_menu.html'
);
// MAIN_MENU_JS_FILE is the file of the main menu
export const MAIN_MENU_JS_FILE = path.resolve(MAIN_SCRIPTS_DIR, 'main_menu.js');
// MAIN_MENU_STYLESHEETS_FILE is the file of the main menu
export const MAIN_MENU_STYLESHEETS_FILE = path.resolve(
	MAIN_STYLESHEETS_DIR,
	'main_menu.css'
);
// SAVE_MENU_HTML_FILE is the file of the save
export const SAVE_MENU_HTML_FILE = path.resolve(SAVE_DIR, 'save.html');
// SAVE_MENU_JS_FILE is the file of the save
export const SAVE_MENU_JS_FILE = path.resolve(SAVE_DIR, 'save.js');
// SAVE_MENU_STYLESHEETS_FILE is the file of the save
export const SAVE_MENU_STYLESHEETS_FILE = path.resolve(SAVE_DIR, 'save.css');
// LOAD_MENU_HTML_FILE is the file of the load
export const LOAD_MENU_HTML_FILE = path.resolve(LOAD_DIR, 'load.html');
// LOAD_MENU_JS_FILE is the file of the load
export const LOAD_MENU_JS_FILE = path.resolve(LOAD_DIR, 'load.js');
// LOAD_MENU_STYLESHEETS_FILE is the file of the load
export const LOAD_MENU_STYLESHEETS_FILE = path.resolve(LOAD_DIR, 'load.css');
// OPTIONS_MENU_HTML_FILE is the file of the options
export const OPTIONS_MENU_HTML_FILE = path.resolve(OPTIONS_DIR, 'options.html');
// OPTIONS_MENU_JS_FILE is the file of the options
export const OPTIONS_MENU_JS_FILE = path.resolve(OPTIONS_DIR, 'options.js');
// OPTIONS_MENU_STYLESHEETS_FILE is the file of the options
export const OPTIONS_MENU_STYLESHEETS_FILE = path.resolve(
	OPTIONS_DIR,
	'options.css'
);
// CREDITS_MENU_HTML_FILE is the file of the credits
export const CREDITS_MENU_HTML_FILE = path.resolve(CREDITS_DIR, 'credits.html');
// CREDITS_MENU_JS_FILE is the file of the credits
export const CREDITS_MENU_JS_FILE = path.resolve(CREDITS_DIR, 'credits.js');
// CREDITS_MENU_STYLESHEETS_FILE is the file of the credits
export const CREDITS_MENU_STYLESHEETS_FILE = path.resolve(
	CREDITS_DIR,
	'credits.css'
);
// GAME_MENU_HTML_FILE is the file of the game menu
export const GAME_MENU_HTML_FILE = path.resolve(
	GAME_MENU_DIR,
	'game_menu.html'
);
// GAME_MENU_JS_FILE is the file of the game menu
export const GAME_MENU_JS_FILE = path.resolve(GAME_MENU_DIR, 'game_menu.js');
// GAME_MENU_STYLESHEETS_FILE is the file of the game menu
export const GAME_MENU_STYLESHEETS_FILE = path.resolve(
	GAME_MENU_DIR,
	'game_menu.css'
);
