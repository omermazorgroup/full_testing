from final_project.api.models.baseObj import BaseObj


class LoginDto(BaseObj):
    def __init__(self, email: str, password: str):
        self._email = None
        self._password = None

        if not isinstance(email, str):
            raise TypeError("email must be string")
        self._email = email

        if not isinstance(password, str):
            raise TypeError("password must be string")
        if 4 > len(password) > 15:
            raise ValueError("password must be between 4-15 char")
        self._password = password

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
        A function that set password property
        :param password: str, updated password
        """
        self._password = password


