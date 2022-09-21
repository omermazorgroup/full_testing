from final_project.api.models.bookDto import BookDto
from final_project.api.models.baseObj import BaseObj


class AuthorsDto(BaseObj):
    def __init__(self, name: str, homeLatitude:float, homeLongitude:float, books:[BookDto]):
        self._id = None
        self._name = None
        self._homeLatitude = None
        self._homeLongitude = None
        self._books = None

        if not isinstance(name, str):
            raise TypeError("name must be string")
        self._name = name

        if not isinstance(homeLatitude, float):
            raise TypeError("homeLatitude must be integer")
        self._homeLatitude = homeLatitude

        if not isinstance(homeLongitude, float):
            raise TypeError("homeLongitude must be string")
        self._homeLongitude = homeLongitude

        if not isinstance(books, list):
            raise TypeError("books must be list")
        for book in books:
            if not isinstance(book, BookDto):
                TypeError("one or more of the books not BookDto type")
        self._books = books


    @property
    def id(self):
        """
        A function that return id property
        """
        return self._id

    @property
    def name(self):
        """
        A function that return name property
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        A function that set name property
        :param name: str, updated name
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if not isinstance(name, str):
            raise TypeError("name must be string!")
        self._name = name




