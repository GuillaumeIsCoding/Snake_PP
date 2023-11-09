from pygame import Rect
from pygame_gui.ui_manager import IUIManagerInterface
from modules.objects.props.prop import Prop
from modules.objects.props.fruits.fruit_types import FruitTypes
from abc import ABC, abstractmethod


class Snake(Prop, ABC):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str) -> None:
        super().__init__(surface, x, y, width, height, background_color)
    

    def creer_object(self) -> None:
        pass
    

    def afficher_object(self) -> Rect:
        pass
    

    def collision_listener(self, fruit : FruitTypes) -> int:
        pass