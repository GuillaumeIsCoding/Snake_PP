from sys import executable
from subprocess import check_call, DEVNULL
from pkg_resources import working_set


class Install():
    """
    
    """


    def __init__(self,error) -> None:
        self.__error = error
    

    def __pygame_error(self,missing) -> None:
        python = executable
        check_call([python,'-m', 'pip', 'install', *missing], stdout=DEVNULL)


    def __pygame_gui_error(self,missing) -> None:
        python = executable
        check_call([python,'-m', 'pip', 'install', *missing], stdout=DEVNULL)
    
    
    def __pyqt6_error(self,missing) -> None:
        python = executable
        check_call([python, '-m', 'pip', 'install', *missing],stdout=DEVNULL)


    def error_handling(self) -> None:
        try:
            required = {self.__error}
            installed = {pkg.key for pkg in working_set}
            missing = required - installed
            if missing:
                raise(ImportError)
        except ImportError:
            match self.__error:
                case 'pygame':
                    self.__pygame_error(missing)
                case 'pygame_gui':
                    self.__pygame_gui_error(missing)
                case 'pyqt6':
                    self.__pyqt6_error(missing)
        else:
            None
        