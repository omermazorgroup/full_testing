from final_project.api.models.baseObj import BaseObj


class AuthResponseDto(BaseObj):
    def __init__(self, userId: str, token: str, refreshToken:str):
        self._userId = None
        self._token = None
        self._refreshToken = None

        if not isinstance(userId, str):
            raise TypeError("id must be string")
        self._userId = userId

        if not isinstance(token, str):
            raise TypeError("token must be string")
        self._token = token

        if not isinstance(refreshToken, str):
            raise TypeError("refreshToken must be string")
        self._refreshToken = refreshToken

    @property
    def userId(self):
        """
        A function that return userId property
        """
        return self._userId

    @property
    def token(self):
        """
        A function that return token property
        """
        return self._token

    @property
    def refreshToken(self):
        """
        A function that return refreshToken property
        """
        return self._refreshToken

    @userId.setter
    def userId(self, userId: str):
        """
        A function that set userId property
        :param userId: str, updated userId
        """
        self._userId = userId

    @token.setter
    def token(self, token: str):
        """
        A function that set token property
        :param token: str, updated token
        """
        self._token = token

    @refreshToken.setter
    def refreshToken(self, refreshToken: str):
        """
        A function that set refreshToken property
        :param refreshToken: str, updated refreshToken
        """
        self._refreshToken = refreshToken

