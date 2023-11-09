from json import load, dumps
from modules.dependencies.path import Path
# ==================== WINDOW ==================== #
from modules.window.dimensions import Dimensions
from modules.window.initialisation import Initialisation
# ====================== GUI ===================== #
from modules.colors.color import Color
from modules.colors.themeColor import ThemeColor
# =================== LANGUAGE =================== #
from modules.languages.language import Language


class Get(Path):
    """
    ATTRIBUTES
    - main_directory -> str \n
    - target_directory -> list[ str , ... , str ] \n
    - target_file -> name + .json \n
    - type_dict -> name 
    \n
    YOU HAVE TO INITIALIZE YOUR OWN KEYS AND KEYS ARGUMENTS \n
    - keys -> list[ str , ... , str ] \n
    - keys_arguments -> list[ str , ... , str ] \n
    \t HOW TO INITIALIZE KEYS VARIABLE
    \t \t get = GET(str, list[str, str , str], str, str) \n
    \t \t get.keys = [str, str , str] \n
    \t HOW TO INITIALIZE KEYS ARGUMENTS VARIABLE \n
    \t \t get = GET(str, list[str, str , str], str, str) \n
    \t \t get.keys_arguments = [str, str ,  str] \n

    """


    def __init__(self, main_directory, target_directory, target_file,type_dict) -> None:
        super().__init__(main_directory, target_directory, target_file,type_dict)
        self.keys = []
        self.keys_arguments = []


    def check_file(self) -> tuple[str,bool]:
        return self.set_target_path()
    

    def extract_file(self,path) -> dict[str, tuple[int,int]]:
        with open ("{}\{}".format(path,self.target_file),"r+") as json_file:
            dictionary = load(json_file)
        return dictionary


    def set_dictionary(self) -> dict[str, tuple[int, int]]:
        dictionary = {}
        for indice_a in self.keys:
            arg = 0
            match self.type_dict:
                case 'dimensions':
                    dim = Dimensions()
                    value_tuple = dim.extract_dimensions(indice_a)
                    dim.__del__()
                case 'initialisation':
                    value_tuple = Initialisation().extract_initialisation(indice_a)
                case 'color':
                    value_tuple = Color().extract_color(indice_a)
                case 'themeColor':
                    value_tuple = ThemeColor().extract_theme_color(indice_a)
                case 'language':
                    value_tuple = Language().extract_language(indice_a)
            for indice_b in self.keys_arguments:
                dictionary[f"{indice_a}_{indice_b}"] = value_tuple[arg]
                arg = arg + 1
        return dictionary
    

    def save_file(self,path,dictionary) -> None:
        with open("{}{}".format(path,self.target_file), "w+") as json_file:
            json_file.write(dumps(dictionary))


    def execute(self) -> dict:
        path = self.check_file()[0]
        dictionary = {}
        #if (isPathCreated == True):
        try:
            dictionary = self.extract_file(path)
        #elif (isPathCreated == False):
        except:
            dictionary = self.set_dictionary()
            self.save_file(path,dictionary)
        return dictionary
