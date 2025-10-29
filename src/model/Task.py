

class Task:
    def __init__(self, title: str = "Empty",
                 description: str = "Empty",
                 priority: int = 1,
                 is_ready: bool = False,
                 x: int = 50,
                 y: int = 100) -> None:
        self.__title = title
        self.__description = description
        self.__priority = priority
        self.__is_ready = is_ready
        self.__x = x
        self.__y = y

    def __call__(self, *args, **kwargs):
        return { "title": self.__title,
                "description": self.__description,
                "priority": self.__priority,
                "is_ready": self.__is_ready,
                "x": self.__x,
                "y": self.__y
        }

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def priority(self):
        return self.__priority

    @property
    def is_ready(self):
        return self.__is_ready

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
