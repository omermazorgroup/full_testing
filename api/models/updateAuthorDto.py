from final_project.api.models.baseObj import BaseObj


class UpdateAuthorDto(BaseObj):
    def __init__(self, name: str,homeLatitude:float,homeLongitude:float,id:int):
        self._id = None
        self._name = None
        self._homeLatitude = None
        self._homeLongitude = None

        if not isinstance(id, int):
            raise TypeError("id must be integer")
        self._id = id

        if not isinstance(name, str):
            raise TypeError("name must be string")
        self._name = name

        if not isinstance(homeLatitude, float):
            raise TypeError("homeLatitude must be float")
        self._homeLatitude = homeLatitude

        if not isinstance(homeLongitude, float):
            raise TypeError("homeLongitude must be float")
        self._homeLongitude = homeLongitude


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
            raise TypeError("user name must be string!")
        self._name = name




