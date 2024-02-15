# RollAsBack - Python Web Backend Framework

**Author(s):** CodeWiki

**File Name:** rest_endpoint.py

**Date:** 16th January 2024

## Description

RollAsBack is a web backend framework written in Python. It is designed to provide a simple and flexible solution for building web applications. This framework allows you to define routes and handle HTTP requests efficiently.

## Disclaimer

This software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

## Copyright

Copyright @ CodeWiki by MIT License

## Usage

RollAsBack provides a simple way to define and handle routes in your web application. It includes basic functionality for handling HTTP requests and responses.

## Features

- **Route Handling:** Define routes using the `@endpoint` decorator.
- **Request Parsing:** Parse HTTP requests and extract relevant information.
- **Response Generation:** Generate HTTP responses with ease.
- **Logging:** Log important events and messages.

## Example

```python
from src.rollasback import RollAsBack, HttpResponse, RESPONSEMEMETYPES

app = RollAsBack("MyApp")


@app.endpoint("/hello")
def hello(request):
    return HttpResponse("Hello, World!", status=200, mimetype=RESPONSEMEMETYPES.text_plain)


if __name__ == "__main__":
    app.start_server("127.0.0.1", 8000)
```

In this example, a simple "Hello, World!" route is defined. When the server is started, it listens on `127.0.0.1:8000` for incoming requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Note: Adjust the file structure and import paths according to your project setup.*

Feel free to extend RollAsBack based on your application's requirements. For more details on how to use and customize the framework, refer to the source code and additional documentation.

**Happy coding with RollAsBack!**