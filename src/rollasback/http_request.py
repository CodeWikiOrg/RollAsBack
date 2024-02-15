"""
Author(s): CodeWiki
File name: http_request.py
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
import json
import re
import urllib.parse
import xml.dom.minidom
from dataclasses import dataclass



class RequestParseError(Exception):
    """Raised when an error occurs parsing an HTTP request."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


@dataclass
class HTTPMETHODS:
    """
    Enum-like class representing common HTTP methods.
    Attributes:
        GET: HTTP GET method.
        POST: HTTP POST method.
        PUT: HTTP PUT method.
        PATCH: HTTP PATCH method.
        DELETE: HTTP DELETE method.
        HEAD: HTTP HEAD method.
        OPTIONS: HTTP OPTIONS method.
    """
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    PATCH: str = "PATCH"
    DELETE: str = "DELETE"
    HEAD: str = "HEAD"
    OPTIONS: str = "OPTIONS"


@dataclass
class CONTENTTYPES:
    """
       Enum-like class representing common HTTP request content types.

       Attributes:
           text_plain (str): "text/plain"
           text_html (str): "text/html"
           application_json (str): "application/json"
           ...

       Default values represent commonly used content types.
       """
    text_plain: str = "text/plain"
    text_html: str = "text/html"
    application_json: str = "application/json"
    application_xml: str = "application/xml"
    image_jpeg: str = "image/jpeg"
    image_png: str = "image/png"
    text_css: str = "text/css"
    text_javascript: str = "text/javascript"
    text_csv: str = "text/csv"
    application_x_www_form_urlencoded: str = "application/x-www-form-urlencoded"
    multipart_form_data: str = "multipart/form-data"

    @staticmethod
    def parse_content_type(content_type, request_body):
        """
        Parses the request body based on the content type.
        Args:
            content_type (str): The content type string.
            request_body (str): The request body to parse.
        Returns: CONTENTTYPES: A CONTENTTYPES enum value.
        """
        if content_type == CONTENTTYPES.application_json:
            return CONTENTTYPES.parse_json(request_body)
        elif content_type == CONTENTTYPES.application_xml:
            return CONTENTTYPES.parse_xml(request_body)
        elif content_type == CONTENTTYPES.application_x_www_form_urlencoded:
            return CONTENTTYPES.parse_urlencoded(request_body)
        else:
            return request_body

    @staticmethod
    def parse_json(request_body):
        """
        Parses the JSON string.
        Args:
            request_body:  The JSON string to parse.

        Returns: dict: A dictionary containing the parsed JSON string.

        """
        try:
            # Replace single quotes with double quotes in the JSON string
            json_string = request_body.replace("'", "\"")
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise RequestParseError(f"Error decoding JSON: {e}")

    @staticmethod
    def parse_xml(request_body):
        """
        Parses the XML string.
        Args:
            request_body:

        Returns:

        """
        try:
            # Prettified xml string
            # XML can contain <?xml ... delete this line if exists
            request_body = re.sub(r"<\?xml.*\?>", "", request_body)
            return xml.dom.minidom.parseString(request_body).toprettyxml()
        except Exception as e:
            raise RequestParseError(f"Error parsing XML: {e}")

    @staticmethod
    def parse_urlencoded(request_body):
        """
        Parses the URL encoded data.
        Args:
            request_body:  The URL encoded data to parse.

        Returns: dict: A dictionary containing the parsed URL encoded data.

        """
        try:
            return dict(urllib.parse.parse_qsl(request_body))
        except Exception as e:
            raise RequestParseError(f"Error parsing URL encoded data: {e}")


class HttpRequest:
    """
    Represents an HTTP request.
    Attributes:
        method (str): The HTTP method (e.g., GET, POST).
        headers (dict): A dictionary containing HTTP headers.
        path (str): The path of the requested resource.
        http_version (str): The HTTP version (default is "HTTP/1.1").
        body (str): The body of the HTTP request.
    """

    def __init__(self, request_string: str):
        """
        Initializes an HttpRequest object.
        Args:
            request_string (str): The HTTP request string.
        """

        self.request_string = request_string
        self.method = None
        self.headers = {}
        self.path_params = []
        self.query_params = {}
        self.path = None
        self.http_version = None
        self.body = None
        self.__parse_request()

    def __is_http_request(self):
        """
        Checks if the request string is an HTTP request and returns True or False.
        Returns: bool: True if the request string is an HTTP request.
        """
        # Define a regular expression pattern for a simple HTTP request
        http_request_pattern = re.compile(r'^(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s\S+\sHTTP/1\.1$')

        # Check if the string matches the pattern
        return bool(http_request_pattern.match(self.request_string.split("\n")[0].strip().replace("\r", "")))

    def __parse_request(self):
        """
        Parses the HTTP request string and sets the HttpRequest object attributes.
        Returns: None

        """
        try:
            if self.request_string is None or not self.__is_http_request():
                return None

            request_lines = [line.strip().replace("\r", "") for line in self.request_string.split("\n")]
            header_list = request_lines[0].split(" ")

            self.method, self.path, self.http_version = header_list
            self.headers = {header.split(": ")[0]: header.split(": ")[1] for header in request_lines[1:-2] if
                            header and ": " in header}
            content_type = self.headers.get("Content-Type", None)

            try:
                if content_type:
                    self.body = CONTENTTYPES.parse_content_type(content_type, request_lines[-1]) if request_lines[
                        -1] else None
                else:
                    self.body = CONTENTTYPES.parse_content_type(CONTENTTYPES.text_plain, request_lines[-1]) if \
                    request_lines[-1] else None
            except RequestParseError as e:
                print(e.message)

        except IndexError as e:
            raise RequestParseError(f"IndexError while parsing request: {e}")
        except Exception as e:
            raise RequestParseError(f"Unexpected error while parsing request: {e}")

        return None

    def __getattr__(self, attr):
        """
        Returns an HttpRequest object for the given attribute.
        Args:
            attr: The attribute name.
        Returns: Any: The value of the attribute.
        Raises: AttributeError: If the attribute is not found.
        """
        if attr in self.__dict__:
            return self.__dict__[attr]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")

    def __str__(self):
        """
        Returns a string representation of the HttpRequest object.
        Returns: str: A string representation of the HttpRequest object.
        """
        return self.request_string

    def to_dict(self):
        """
        Returns a dictionary representation of the HttpRequest object.
        Returns: dict: A dictionary representation of the HttpRequest object.
        """
        return {
            "method": self.method,
            "headers": self.headers,
            "path": self.path,
            "http_version": self.http_version,
            "body": self.body
        }

    def __eq__(self, other):
        """
        Checks if two HttpRequest objects are equal.

        Args:
            other: The other HttpRequest object.

        Returns:
            bool: True if the two HttpRequest objects are equal, otherwise False.
        """
        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        Checks if two HttpRequest objects are not equal.

        Args:
            other: The other HttpRequest object.

        Returns:
            bool: True if the two HttpRequest objects are not equal, otherwise False.
        """
        return self.to_dict() != other.to_dict()

    def __hash__(self):
        """
        Returns the hash value of the HttpRequest object.

        Returns:
            int: The hash value of the HttpRequest object.
        """
        return hash(self.to_dict())

    def __repr__(self):
        """
        Returns a string representation of the HttpRequest object.

        Returns:
            str: A string representation of the HttpRequest object.
        """
        return f"HttpRequest(method={self.method}, headers={self.headers}, path={self.path}, http_version={self.http_version}, body={self.body})"

    def __len__(self):
        """
        Returns the length of the HttpRequest object.
        Returns:
            int: The length of the HttpRequest object.
        """
        return len(self.to_dict())

    def __contains__(self, item):
        """
        Checks if the HttpRequest object contains the given item.

        Args:
            item: The item to check.

        Returns:
            bool: True if the item is in the HttpRequest object, otherwise False.
        """
        return item in self.to_dict()
