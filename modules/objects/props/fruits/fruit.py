from pygame import Rect
from pygame_gui.ui_manager import IUIManagerInterface
from modules.objects.props.prop import Prop
from modules.objects.props.fruits.fruit_types import FruitTypes
from abc import ABC, abstractmethod


class Fruit(Prop,ABC):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str, type : FruitTypes) -> None:
        super().__init__(surface, x, y, width, height, background_color)
        self.__type = type

    # GETTER 


    @property
    def type(self) -> FruitTypes:
        return self.__type
    

    @abstractmethod
    def effacer_object(self) -> None:
        pass


class Apple(Fruit):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str, type: FruitTypes) -> None:
        super().__init__(surface, x, y, width, height, background_color, type)
    

    def creer_object(self) -> None:
        pass


    def afficher_object(self) -> Rect:
        pass
    

    def effacer_object(self) -> None:
        pass


class Chery(Fruit):

    def __init__(self, surface: IUIManagerInterface, x: float, y: float, width: float, height: float, background_color: tuple[int, int, int] | str, type: FruitTypes) -> None:
        super().__init__(surface, x, y, width, height, background_color, type)
    

    def creer_object(self) -> None:
        pass
    

    def afficher_object(self) -> Rect:
        pass
    
    def effacer_object(self) -> None:
        pass