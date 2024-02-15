"""
Author(s): CodeWiki
File name: cookie.py
Date: 16th January 2024

Description: Web backend framework written in Python named as RollAsBack.

Disclaimer: This software is provided "as is" without warranty of any kind,
express or implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose, and noninfringement. In no event shall the authors
or copyright holders be liable for any claim, damages, or other liability,
whether in an action of contract, tort, or otherwise, arising from, out of, or in connection
with the software or the use or other dealings in the software.

Copyright @ CodeWiki by MIT License
"""


class Cookie:
    def __init__(self, key, value, expires=None, path=None, domain=None, secure=False, httponly=False):
        self.key = key
        self.value = value
        self.expires = expires
        self.path = path
        self.domain = domain
        self.secure = secure
        self.httponly = httponly

    def __str__(self):
        cookie = f"{self.key}={self.value}"
        if self.expires:
            cookie += f"; Expires={self.expires}"
        if self.path:
            cookie += f"; Path={self.path}"
        if self.domain:
            cookie += f"; Domain={self.domain}"
        if self.secure:
            cookie += "; Secure"
        if self.httponly:
            cookie += "; HttpOnly"
        return cookie

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value

    def __hash__(self):
        return hash(self.key)

    def __setattr__(self, key, value):
        if key == "key":
            if not isinstance(value, str):
                raise TypeError("Key must be a string")
        elif key == "value":
            if not isinstance(value, str):
                raise TypeError("Value must be a string")
        elif key == "expires":
            if not isinstance(value, str):
                raise TypeError("Expires must be a string")
        elif key == "path":
            if not isinstance(value, str):
                raise TypeError("Path must be a string")
        elif key == "domain":
            if not isinstance(value, str):
                raise TypeError("Domain must be a string")
        elif key == "secure":
            if not isinstance(value, bool):
                raise TypeError("Secure must be a boolean")
        elif key == "httponly":
            if not isinstance(value, bool):
                raise TypeError("HttpOnly must be a boolean")
        self.__dict__[key] = value

    def __getattr__(self, key):
        if key == "key":
            return self.key
        elif key == "value":
            return self.value
        elif key == "expires":
            return self.expires
        elif key == "path":
            return self.path
        elif key == "domain":
            return self.domain
        elif key == "secure":
            return self.secure
        elif key == "httponly":
            return self.httponly
        else:
            raise AttributeError(f"Cookie has no attribute {key}")

    def __delattr__(self, key):
        if key == "key":
            del self.key
        elif key == "value":
            del self.value
        elif key == "expires":
            del self.expires
        elif key == "path":
            del self.path
        elif key == "domain":
            del self.domain
        elif key == "secure":
            del self.secure
        elif key == "httponly":
            del self.httponly
        else:
            raise AttributeError(f"Cookie has no attribute {key}")

    def __contains__(self, key):
        return key in self.__dict__


class CookieJar:
    def __init__(self):
        self.cookies = []

    def add_cookie(self, cookie):
        self.cookies.append(cookie)

    def __str__(self):
        cookie_string = ""
        for cookie in self.cookies:
            cookie_string += str(cookie) + "\n"
        return cookie_string

    def get_cookie(self, key):
        for cookie in self.cookies:
            if cookie.key == key:
                return cookie
        return None

    def get_cookies(self):
        return self.cookies

    def get_cookie_string(self):
        cookie_string = ""
        for cookie in self.cookies:
            cookie_string += str(cookie) + "; "
        return cookie_string[:-2]

    def delete_cookie(self, key):
        for cookie in self.cookies:
            if cookie.key == key:
                self.cookies.remove(cookie)
                return True
        return False

    def delete_cookies(self):
        self.cookies = []

    def update_cookie(self, cookie):
        for c in self.cookies:
            if c.key == cookie.key:
                c.value = cookie.value
                c.expires = cookie.expires
                c.path = cookie.path
                c.domain = cookie.domain
                c.secure = cookie.secure
                c.httponly = cookie.httponly
                return True
        return False

    def set_cookie(self, key, value, expires=None, path=None, domain=None, secure=False, httponly=False):
        cookie = Cookie(key, value, expires, path, domain, secure, httponly)
        self.update_cookie(cookie)

    def set_cookies(self, cookies):
        for cookie in cookies:
            self.update_cookie(cookie)

    def get_cookie_header(self):
        cookie_header = ""
        for cookie in self.cookies:
            cookie_header += str(cookie) + "; "
        return cookie_header[:-2]

    def get_cookie_dict(self):
        cookie_dict = {}
        for cookie in self.cookies:
            cookie_dict[cookie.key] = cookie.value
        return cookie_dict

    def get_all_cookies(self):
        return self.cookies

    def __len__(self):
        return len(self.cookies)
