import importlib.util
from configparser import ConfigParser

config = ConfigParser()
CONFIG_INI_PATH = "./config/config.ini"
LANG_PATH = "./lang/"


def load_language(language_code):
    try:
        language_path = f"{LANG_PATH}{language_code}.py"
        print(f"Attempting to load language file: {language_path}")
        spec = importlib.util.spec_from_file_location(language_code, language_path)
        language_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(language_module)
        return language_module
    except FileNotFoundError:
        print(f"Language file not found for {language_code}. Using default.")
        return None


def get_language(config):
    try:
        with open(CONFIG_INI_PATH, "r") as config_file:
            config.read_file(config_file)
        lang = config.get("main", "language")
    except FileNotFoundError:
        print("The configuration file was not found.")
        raise
    except KeyError:
        print("Language File Error. Please Restart Alfred To Fix This")
        raise
    return lang


language_code = get_language(config)
language_m = load_language(language_code)
