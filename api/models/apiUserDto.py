from final_project.api.models.baseObj import BaseObj


class ApiUserDto(BaseObj):
    def __init__(self, email: str, password: str, firstName:str,lastNmae:str):
        self._email = None
        self._password = None
        self._firstName = None
        self._lastName = None

        if not isinstance(email, str):
            raise TypeError("email must be string")
        self._email = email

        if not isinstance(password, str):
            raise TypeError("password must be string")
        if 4 > len(password) > 15:
            raise ValueError("password must be between 4-15 char")
        self._password = password

        if not isinstance(firstName, str):
            raise TypeError("firstName must be string")
        self._firstName = firstName

        if not isinstance(lastNmae, str):
            raise TypeError("lastNmae must be string")
        self._lastName = lastNmae

    @property
    def email(self):
        """
        A function that return email property
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """
        A function that set email property
        :param email: str, updated email
        """
        self._email = email

    @property
    def password(self):
        """
        A function that return password property
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """
        A function that set email property
        :param password: str, updated password
        """
        self._password = password



