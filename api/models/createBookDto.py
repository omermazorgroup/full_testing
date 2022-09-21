from final_project.api.models.baseObj import BaseObj


class CreateBookDto(BaseObj):
    def __init__(self, name: str,description:str,price:float,amountInStock:int,imageUrl:str,authorId:int):
        self.authorId = None
        self._id = None
        self._name = None
        self._description = None
        self._price = None
        self._amountInStock = None
        self._imageUrl = None
        self._authorId = None
        self._author = None

        # if not isinstance(id, int):
        #     raise TypeError("id must be integer")
        # self._id = id

        if not isinstance(name, str):
            raise TypeError("name must be string")
        self._name = name

        if not isinstance(description, str):
            raise TypeError("description must be string")
        self._description = description

        if not isinstance(price, int):
            raise TypeError("price must be int")
        self._price = price

        if not isinstance(amountInStock, int):
            raise TypeError("amountInStock must be integer")
        self._amountInStock = amountInStock

        if not isinstance(imageUrl, str):
            raise TypeError("imageUrl must be string")
        self._imageUrl = imageUrl

        if not isinstance(authorId, int):
            raise TypeError("authorId must be integer")
        if 2147483647 < authorId < 1:
            raise TypeError("authorId must be between 1-2147483647")
        self._authorId = authorId

    @property
    def name(self):
        """
        A function that return name property
        """
        return self._name

    @property
    def id(self):
        """
        A function that return id property
        """
        return self._id

    @name.setter
    def name(self,name:str):
        """
        A function that set name property
        :param name: str, updated name
        """
        self._name = name

    @property
    def authorId(self):
        """
        A function that return authorId property
        """
        return self._authorId

    @authorId.setter
    def authorId(self, authorId: str):
        """
        A function that set authorId property
        :param authorId: str, updated authorId
        """
        self._authorId = authorId


