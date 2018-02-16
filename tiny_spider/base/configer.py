class Configer:
    def __init__(self, conf_path):
        self.__conf_path = conf_path

    @property
    def conf_path(self):
        return self.__conf_path

    @conf_path.setter
    def conf_path(self, conf_path):
        if isinstance(conf_path, str):
            self.__conf_path = conf_path
        else:
            print("Type invalid!!!")
            raise Exception


if __name__ == '__main__':
    c = Configer("jie")
    print(c.conf_path)
    c.conf_path = ("ming")
    print(c.conf_path)
