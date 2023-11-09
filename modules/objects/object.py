from abc import ABC, abstractmethod
from pygame_gui.ui_manager import IUIManagerInterface
from modules.dependencies.surcharge import surcharge

class Object(ABC):
    

    def __init__(self, surface : IUIManagerInterface, x : float, y : float, width : float, height : float,  background_color : tuple[int,int,int] | str) -> None:
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = background_color
        self.__surface = surface

    # GETTERS 


    @property
    def x(self) -> float:
        return self.__x
    

    @property
    def y(self) -> float:
        return self.__y
    

    @property
    def width(self) -> float:
        return self.__width
    

    @property
    def height(self) -> float:
        return self.__height
    

    @property
    def color(self) -> tuple[int, int, int] | str:
        return self.__color
    

    @property
    def surface(self) -> IUIManagerInterface:
        return self.__surface

    # SETTERS


    @x.setter
    def x(self, value) -> None:
        if type(value) == int or type(value) == float:
            self.__x = value
    

    @x.setter
    def y(self, value) -> None:
        if type(value) == int or type(value) == float:
            self.__y = value
    

    @width.setter
    def width(self, value) -> None:
        if type(value) == int or type(value) == float:
            self.__width = value


    @height.setter
    def height(self, value) -> None:
        if type(value) == int or type(value) == float:
            self.__height = value


    @color.setter
    def color(self, value) -> None:
        if type(value) == tuple or type(value) == str:
            self.__color = value

    
    @surface.setter
    def surface(self, value) -> None:
        if type(value) != IUIManagerInterface:
            self.__surface = value


    @abstractmethod
    def creer_object(self) -> None:
        pass


    def __str__(self) -> str:
        return f"La position de l'objet en x : {self.__x}\nLa position de l'objet en y: {self.__y}\nLa largeur de l'objet: {self.__width}\nLa hauteur de l'objet: {self.__height}\nLa couleur de l'objet: {self.__color}"
    




    



    
    



    



