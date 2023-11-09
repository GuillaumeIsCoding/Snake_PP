from modules.dependencies.install import Install
from sys import argv


class Dimensions():

    def __init__(self) -> None:
        Install("pyqt6").error_handling()
        from PyQt6 import QtWidgets
        # Creates application object <- QtWidgets.QApplication
        self.__application = QtWidgets.QApplication(argv)

    def available_dimensions(self) -> tuple[int,int]:
        available_dimensions = self.__application.primaryScreen().availableGeometry()
        return (available_dimensions.width(), available_dimensions.height())


    def maximum_dimensions(self) -> tuple[int,int]:
        maximum_dimensions = self.__application.primaryScreen().size()
        return (maximum_dimensions.width(), maximum_dimensions.height())


    def get_dimensions_dictionary(self) -> dict[str, tuple[int,int]]:
        return {
            "available"     :   self.available_dimensions(),
            "maximum"       :   self.maximum_dimensions(),
        }


    def extract_dimensions(self, key) -> tuple[int, int]:
        return self.get_dimensions_dictionary()[key]
    
    def __del__(self) -> None:
        self.__application.deleteLater()
        

        