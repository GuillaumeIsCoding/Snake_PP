from pygame import Rect
from pygame_gui.ui_manager import IUIManagerInterface
from modules.objects.object import Object
from abc import ABC, abstractmethod

class Prop(Object, ABC):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str) -> None:
        super().__init__(surface, x, y, width, height, background_color)
    

    @abstractmethod
    def afficher_object(self) -> Rect:
        pass

