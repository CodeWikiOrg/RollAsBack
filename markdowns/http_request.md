
## HTTP Response Class Documentation

The provided example demonstrates the usage of the HttpRequest class, a part of the RollAsBack web backend framework.
It showcases how to create an HTTP request object by parsing a request string and printing its
representation in dictionary format.

```python
import HttpRequest
request_string = "GET http://localhost:8080/tienda1/imagenes/1.gif HTTP/1.1\n" \
                    "User-Agent: Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)\n" \
                    "Pragma: no-cache\n" \
                    "Cache-control: no-cache\n" \
                    "Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\n" \
                    "Accept-Encoding: x-gzip, x-deflate, gzip, deflate\n" \
                    "Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5\n" \
                    "Accept-Language: en\n" \
                    "Content-Type: text/plain\n" \
                    "Host: localhost:8080\n" \
                    "Cookie: JSESSIONID=1822709F57BDDFA1ADA9D0BAAED0D4B3\n" \
                   "Connection: close\n" \
                      " \n"\
                    "{'key': 'value'}"



http_request = HttpRequest(request_string)
print(http_request.to_dict())
```

```bash
{'method': 'GET', 'headers': {'User-Agent': 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)', 'Pragma': 'no-cache', 'Cache-control': 'no-cache', 'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5', 'Accept-Encoding': 'x-gzip, x-deflate, gzip, deflate', 'Accept-Charset': 'utf-8, utf-8;q=0.5, *;q=0.5', 'Accept-Language': 'en', 'Content-Type': 'text/plain', 'Host': 'localhost:8080', 'Cookie': 'JSESSIONID=1822709F57BDDFA1ADA9D0BAAED0D4B3', 'Connection': 'close'}, 'path': 'http://localhost:8080/tienda1/imagenes/1.gif', 'http_version': 'HTTP/1.1', 'body': "{'key': 'value'}"}
```

## HTTP Request Class and Supporting Classes

### HTTP Methods Enum

```
- GET: HTTP GET method
- POST: HTTP POST method
- PUT: HTTP PUT method
- PATCH: HTTP PATCH method
- DELETE: HTTP DELETE method
- HEAD: HTTP HEAD method
- OPTIONS: HTTP OPTIONS method
```

### Content Types Enum

```
- text_plain: "text/plain"
- text_html: "text/html"
- application_json: "application/json"
- application_xml: "application/xml"
- image_jpeg: "image/jpeg"
- image_png: "image/png"
- text_css: "text/css"
- text_javascript: "text/javascript"
- text_csv: "text/csv"
- application_x_www_form_urlencoded: "application/x-www-form-urlencoded"
- multipart_form_data: "multipart/form-data"
```

### Methods:

#### parse_content_type(content_type, request_body)

> Parses the request body based on the content type.

#### parse_json(request_body)

> Parses the JSON string.

#### parse_xml(request_body)

> Parses the XML string.

#### parse_urlencoded(request_body)

> Parses the URL encoded data.

## HTTP Request Class

Represents an HTTP request.

### Attributes:

- method (str): The HTTP method (e.g., GET, POST).
- headers (dict): A dictionary containing HTTP headers.
- path (str): The path of the requested resource.
- http_version (str): The HTTP version (default is "HTTP/1.1").
- body (str): The body of the HTTP request.

### Methods:

#### __init__(request_string)

Initializes an HttpRequest object.

#### \_\_str__()

Returns a string representation of the HttpRequest object.

#### to_dict()

Returns a dictionary representation of the HttpRequest object.

#### \_\_eq__(other)

Checks if two HttpRequest objects are equal.

#### \_\_ne__(other)

Checks if two HttpRequest objects are not equal.

#### \_\_hash__()

Returns the hash value of the HttpRequest object.

#### \_\_repr__()

Returns a string representation of the HttpRequest object.

#### \_\_len__()

Returns the length of the HttpRequest object.

#### \_\_contains__(item)

Checks if the HttpRequest object contains the given item.

#### \_\_getattr__(attr)

Returns an HttpRequest object for the given attribute.


