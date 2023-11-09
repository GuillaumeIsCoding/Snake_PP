from pygame_gui.ui_manager import IUIManagerInterface
from modules.objects.object import Object
from abc import ABC, abstractmethod


class Entity(Object, ABC):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str, text : str, **text_kwargs : str) -> None:
        super().__init__(surface, x, y, width, height, background_color)
        self.__text = text
        self.__text_kwargs = text_kwargs 
        self.__obj = None
    

    # GETTER


    @property
    def text(self) -> str:
        return self.__text
    

    @property
    def text_kwargs(self) -> dict[str, str]:
        return self.__text_kwargs
    

    @property
    def obj(self):
        return self.__obj

    # SETTER


    @text.setter
    def text(self, value) -> None:
        self.__text = str(value)


    @text_kwargs.setter
    def text_kwargs(self, **values) -> None:
        for key, value in values.items():
            try:
                self.__text_kwargs[key] = value
            except:
                pass
    
    
    @obj.deleter
    def effacer_object(self) -> None:
        del self.__obj


