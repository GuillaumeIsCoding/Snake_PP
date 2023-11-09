from modules.dependencies.install import Install



class Initialisation():

    def __init__(self) -> None:
        Install("pygame").error_handling()
        from pygame import FULLSCREEN, RESIZABLE, SCALED, SHOWN, DOUBLEBUF, OPENGL
        self._fullScreen = FULLSCREEN
        self._resizable = RESIZABLE
        self._scaled = SCALED
        self._shown = SHOWN
        self._doublebuf = DOUBLEBUF
        self._opengl = OPENGL
    
    def open_for_the_first_time(self) -> tuple[int, int]:
        flags = self._doublebuf | self._opengl
        vsync = 0                                                                # vsync disable when first open
        return flags, vsync
    

    def get_initialisation_dict(self) -> dict[str, tuple[int, int]]:
        return {
            "initialisation"    :   self.open_for_the_first_time(),
            "default"           :   self.open_for_the_first_time(),
            "user"              :   self.open_for_the_first_time(),
        }


    def extract_initialisation(self, key) -> tuple[int, int]:
        return self.get_initialisation_dict()[key]
    
    