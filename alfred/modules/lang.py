import importlib.util
from configparser import ConfigParser


def load_language(language_code):
    langp = "./lang/"
    try:
        language_path = f"{langp}{language_code}.py"
        print(f"Attempting to load language file: {language_path}")
        spec = importlib.util.spec_from_file_location(language_code, language_path)
        language_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(language_module)
        return language_module
    except FileNotFoundError:
        print(f"Language file not found for {language_code}. Using default.")
        return None


def getLang(config):
    config.read("./config/config.ini")
    lang = config.get("main", "language")
    return lang
