## HTTP Response Module Documentation

### Module Information

- **Author(s):** CodeWiki
- **File name:** http_response.py
- **Date:** 16th January 2024
- **Description:** Web backend framework written in Python named as RollAsBack.

### Disclaimer

This software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

### Copyright Information

Copyright @ CodeWiki by MIT License

### Classes

#### Class: `HTTPRESPONSECODES`

Enum-like class representing standard HTTP response codes.

- **Attributes:**
  - `CONTINUE (int): 100` - Continue
  - `SWITCHING_PROTOCOLS (int): 101` - Switching Protocols
  - `PROCESSING (int): 102` - Processing
  - `EARLY_HINTS (int): 103` - Early Hints
  - ... (Other HTTP status codes)
  
- **Response Messages (dict):**
  - A dictionary mapping response codes to their corresponding messages.

#### Class: `RESPONSEMEMETYPES`

Enum-like class representing common HTTP response content types.

- **Attributes:**
  - `text_plain (str): "text/plain"`
  - `text_html (str): "text/html"`
  - `application_json (str): "application/json"`
  - ... (Other common content types)

  Default values represent commonly used content types.

#### Class: `HttpResponse`

Represents an HTTP response.

- **Attributes:**
  - `response_message`: The response to send to the client (str, dict, list, etc.).
  - `response_headers (dict)`: A dictionary containing HTTP response headers.
  - `status (int)`: The HTTP status code (default is 200).
  - `mimetype (str)`: The mimetype of the response (default is "text/plain").
  - `last_modified (str)`: The last modification time (default is the current GMT time).

- **Methods:**
  - `get_response()`: Returns the HTTP response as a string object.
  - `__str__()` : Returns a string representation of the HttpResponse object.

- **Setters:**
  - `set_cookie(cookie)`: Set a cookie to the response.
  - `set_cookie_jar(cookie_jar)`: Set a cookie jar to the response.

- **Notes:**
  - The `HTTPRESPONSECODES` and `RESPONSEMEMETYPES` classes are used as enum-like structures for HTTP response codes and content types.

### Example Usage

```python
response = HttpResponse("Hello, World!", {"Content-Language": "en"}, status=200, mimetype=RESPONSEMEMETYPES.text_plain)
response.set_cookie(cookie=Cookie(key="session_id", value="123456789", expires="2024-01-30", path="/app",
                                  domain="example.com", secure=True, httponly=True))
print(response)
```

This example creates an HTTP response object with a message "Hello, World!", additional headers, status code 200, and the "text/plain" mimetype. A cookie is also set in the response. The `__str__()` method is then called to obtain a string representation of the response.