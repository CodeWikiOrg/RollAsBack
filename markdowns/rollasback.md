## REST Endpoint Framework Documentation

### Module Information

- **Author(s):** CodeWiki
- **File name:** rest_endpoint.py
- **Date:** 16th January 2024
- **Description:** Web backend framework written in Python named RollAsBack.

### Disclaimer

This software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

### Copyright Information

Copyright @ CodeWiki by MIT License

### Dependencies

- **Logging:** Python logging module is used for logging purposes.
- **Socket:** The `socket` module is utilized for handling socket connections.
- **HttpResponse Class:** The `HttpResponse` class is imported from the `http_response` module.
- **HttpRequest Class:** The `HttpRequest` class is imported from the `http_request` module.
- **Cookie Class:** The `Cookie` class is imported from the `src.rollasback.cookie` module.

### Class: `Route`

#### Constructor: `__init__(self, path, func)`

- **Parameters:**
  - `path` (str): The path of the REST endpoint associated with the route.
  - `func` (function): The function to be executed when the route is accessed.

### Class: `RollAsBack`

#### Constructor: `__init__(self, backlog: int = 50, **kwargs)`

- **Parameters:**
  - `backlog` (int, optional): The maximum number of queued connections. Default value is 50.
  - `kwargs` (dict, optional): Additional arguments to configure the REST endpoint.

#### Method: `__setup_logger(self) -> Logger`

- **Returns:**
  - `Logger`: Configured instance of the Python logging `Logger` class.

#### Method: `endpoint(self, path) -> Callable`

- **Parameters:**
  - `path` (str): The path of the REST endpoint.

- **Returns:**
  - `Callable`: A decorator function to associate a route with a specific function.

#### Method: `start_server(self, host, port)`

- **Parameters:**
  - `host` (str): The IP address or hostname to bind the server to.
  - `port` (int): The port number to bind the server to.

- **Description:**
  - Starts the REST endpoint server and listens for incoming connections.

#### Method: `stop_server(self)`

- **Description:**
  - Stops the REST endpoint server.

### Example Route Definition

```python
@api.endpoint("/asd")
def func(request):
    if request.method != "PUT":
        response = HttpResponse("Method not allowed!", response_headers={}, status=405)
        response.set_cookie(cookie=Cookie(key="session_id", value="123456789", expires="2024-01-30", path="/app",
                                          domain="example.com", secure=True, httponly=True))
        return response
    return HttpResponse({"merhaba": "deneme"}, response_headers={}, status=200)

# Start the REST endpoint server
api.start_server("127.0.0.1", 8888)
```

This example demonstrates the definition of a route ("/asd") associated with the `func` function. The function handles incoming requests and sends appropriate HTTP responses. The server is then started on IP address "127.0.0.1" and port 8888.