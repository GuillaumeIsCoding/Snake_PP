from enum import Enum

class FruitTypes(str, Enum):

    CHERRY = "CERISE"
    APPLE  = "POMME"


    def __str__(self) -> str:
        return self.value
    