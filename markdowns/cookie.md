## Cookie Class Documentation

### Class: `Cookie`

#### Constructor: `__init__(self, key, value, expires=None, path=None, domain=None, secure=False, httponly=False)`

- **Parameters:**
  - `key` (str): The key of the cookie.
  - `value` (str): The value of the cookie.
  - `expires` (str, optional): The expiration date and time of the cookie in string format. Defaults to `None`.
  - `path` (str, optional): The path to which the cookie is applicable. Defaults to `None`.
  - `domain` (str, optional): The domain to which the cookie is applicable. Defaults to `None`.
  - `secure` (bool, optional): Indicates if the cookie should only be sent over secure connections. Defaults to `False`.
  - `httponly` (bool, optional): Indicates if the cookie is accessible only through HTTP requests and not through JavaScript. Defaults to `False`.

#### Method: `__str__(self)`

- **Returns:**
  - `str`: A string representation of the cookie suitable for HTTP headers.

#### Method: `__repr__(self)`

- **Returns:**
  - `str`: A string representation of the cookie, equivalent to calling `str(self)`.

#### Method: `__eq__(self, other)`

- **Parameters:**
  - `other` (Cookie): Another cookie object to compare with.

- **Returns:**
  - `bool`: `True` if both cookies have the same key and value, `False` otherwise.

#### Method: `__hash__(self)`

- **Returns:**
  - `int`: Hash value of the cookie based on its key.

#### Method: `__setattr__(self, key, value)`

- **Parameters:**
  - `key` (str): The attribute key.
  - `value` (various): The value to be set.

- **Raises:**
  - `TypeError`: If the provided value is not of the expected type for the corresponding attribute.

#### Method: `__getattr__(self, key)`

- **Parameters:**
  - `key` (str): The attribute key.

- **Returns:**
  - Various: The value of the requested attribute.

- **Raises:**
  - `AttributeError`: If the requested attribute is not available.

#### Method: `__delattr__(self, key)`

- **Parameters:**
  - `key` (str): The attribute key.

- **Raises:**
  - `AttributeError`: If the requested attribute is not deletable.

#### Method: `__contains__(self, key)`

- **Parameters:**
  - `key` (str): The attribute key.

- **Returns:**
  - `bool`: `True` if the key exists as an attribute, `False` otherwise.

### Class: `CookieJar`

#### Constructor: `__init__(self)`

- **Attributes:**
  - `cookies` (list): A list to store `Cookie` objects.

#### Method: `add_cookie(self, cookie)`

- **Parameters:**
  - `cookie` (Cookie): The `Cookie` object to add to the jar.

#### Method: `__str__(self)`

- **Returns:**
  - `str`: A string representation of all cookies in the jar.

#### Method: `get_cookie(self, key)`

- **Parameters:**
  - `key` (str): The key of the cookie to retrieve.

- **Returns:**
  - `Cookie` or `None`: The cookie object if found, otherwise `None`.

#### Method: `get_cookies(self)`

- **Returns:**
  - `list`: A list of all cookies in the jar.

#### Method: `get_cookie_string(self)`

- **Returns:**
  - `str`: A string representation of all cookies in the jar suitable for HTTP headers.

#### Method: `delete_cookie(self, key)`

- **Parameters:**
  - `key` (str): The key of the cookie to delete.

- **Returns:**
  - `bool`: `True` if the cookie was deleted, `False` otherwise.

#### Method: `delete_cookies(self)`

- **Description:**
  - Clears all cookies from the jar.

#### Method: `update_cookie(self, cookie)`

- **Parameters:**
  - `cookie` (Cookie): The updated `Cookie` object.

- **Returns:**
  - `bool`: `True` if the cookie was updated, `False` otherwise.

#### Method: `set_cookie(self, key, value, expires=None, path=None, domain=None, secure=False, httponly=False)`

- **Parameters:**
  - Same as the `Cookie` constructor.

- **Description:**
  - Creates a new `Cookie` object and updates it in the jar.

#### Method: `set_cookies(self, cookies)`

- **Parameters:**
  - `cookies` (list): A list of `Cookie` objects to update in the jar.

#### Method: `get_cookie_header(self)`

- **Returns:**
  - `str`: A string representation of all cookies in the jar suitable for HTTP headers.

#### Method: `get_cookie_dict(self)`

- **Returns:**
  - `dict`: A dictionary mapping cookie keys to their values.