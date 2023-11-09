from pygame_gui.ui_manager import IUIManagerInterface
from modules.objects.entities.entity import Entity
from pygame_gui.elements import UILabel
from pygame import Rect



class Label(Entity):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str, text: str, **text_kwargs: str) -> None:
        super().__init__(surface, x, y, width, height, background_color, text, **text_kwargs)
    
    
    def creer_object(self) -> UILabel:
        self.__obj 