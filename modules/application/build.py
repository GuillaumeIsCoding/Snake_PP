from modules.dependencies.get import Get


class Build():
    """
    
    """


    def __init__(self) -> None:
        pass
    
    
    def __set_dimensions_dict(self) -> dict:
        getDimensions = Get("Simulation",["modules","application","configurations","dimensions"],"dimensions.json","dimensions")
        getDimensions.keys , getDimensions.keys_arguments = ["available","maximum"], ["width","height"]
        return getDimensions.execute()
    
    
    def __set_initialisation_dict(self) -> dict:
        getInitilisation = Get("Simulation",["modules","application","configurations", "initialisation"], "initialisation.json", "initialisation")
        getInitilisation.keys, getInitilisation.keys_arguments = ["initialisation","default","user"], ["flags", "vsync"]
        return getInitilisation.execute()
    

    def __set_themes_dict(self) -> dict:
        return {}
    

    def __set_colors_dict(self) -> dict:
        return {}
    

    def __set_languages_dict(self) -> dict:
        return {}


    def set_dictionary(self) -> dict:
        return {
            "Dimensions"        :   self.__set_dimensions_dict(),
            "Initialisation"    :   self.__set_initialisation_dict(),
            "Themes"            :   self.__set_themes_dict(),
            "Colors"            :   self.__set_colors_dict(),
            "Languages"         :   self.__set_languages_dict(),
        }
    



