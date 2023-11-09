from os import makedirs, path


class Path():
    """
    
    """
    

    def __init__(self, main_directory, target_directory, target_file,type_dict) -> None:
        self.main_dir = main_directory
        self.target_dir = target_directory
        self.target_file = target_file
        self.path_to = ""
        self.type_dict = type_dict
    

    def get_file_path(self) -> str:
        return __file__
    

    def split_file_path(self) -> list[str]:
        return self.get_file_path().split("\\")


    def rebuild_app_path(self) -> str:
        for indice in self.split_file_path():
            self.path_to = "{}{}\\".format(self.path_to,indice)
            if (indice == self.main_dir):
                break
        return self.path_to


    def make_target_path(self) -> str:
        self.path_to = self.rebuild_app_path()
        for indice in self.target_dir:
            self.path_to = "{}{}\\".format(self.path_to, indice)
        return self.path_to
    

    def set_target_path(self) -> tuple[str,bool]:
        isPathCreated = True
        target = self.make_target_path()
        if path.isdir(target) == False:
            makedirs(target)
            isPathCreated = False
        return (target, isPathCreated)


    