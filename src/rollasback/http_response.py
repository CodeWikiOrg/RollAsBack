"""
Author(s): CodeWiki
File name: http_response.py
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
import time
from dataclasses import dataclass


@dataclass
class HTTPRESPONSECODES:
    """
    Enum-like class representing standard HTTP response codes.

    Attributes:
        CONTINUE (int): 100 - Continue
        SWITCHING_PROTOCOLS (int): 101 - Switching Protocols
        PROCESSING (int): 102 - Processing
        EARLY_HINTS (int): 103 - Early Hints
        OK (int): 200 - OK
        ...

    RESPONSE_MESSAGES (dict): A dictionary mapping response codes to their corresponding messages.
    """
    # 1xx informational response – the request was received, continuing process
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101
    PROCESSING = 102
    EARLY_HINTS = 103
    # 2xx successful – the request was successfully received, understood, and accepted
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    ALREADY_REPORTED = 208
    IM_USED = 226
    # 3xx redirection – further action needs to be taken in order to complete the request
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308
    # 4xx client error – the request contains bad syntax or cannot be fulfilled
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    PAYLOAD_TOO_LARGE = 413
    URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451
    # 5xx http_lib error – the http_lib
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    VARIANT_ALSO_NEGOTIATES_EXPERIMENTAL = 506
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    NOT_EXTENDED = 510
    NETWORK_AUTHENTICATION_REQUIRED = 511

    RESPONSE_MESSAGES = {
        100: "Continue",
        101: "Switching Protocols",
        102: "Processing",
        103: "Early Hints",
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        207: "Multi-Status",
        208: "Already Reported",
        226: "IM Used",
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        304: "Not Modified",
        305: "Use Proxy",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Payload Too Large",
        414: "URI Too Long",
        415: "Unsupported Media Type",
        416: "Range Not Satisfiable",
        417: "Expectation Failed",
        418: "I'm a teapot",
        421: "Misdirected Request",
        422: "Unprocessable Entity",
        423: "Locked",
        424: "Failed Dependency",
        425: "Too Early",
        426: "Upgrade Required",
        428: "Precondition Required",
        429: "Too Many Requests",
        431: "Request Header Fields Too Large",
        451: "Unavailable For Legal Reasons",
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
        506: "Variant Also Negotiates",
        507: "Insufficient Storage",
        508: "Loop Detected",
        510: "Not Extended",
        511: "Network Authentication Required",
    }


@dataclass
class RESPONSEMEMETYPES:
    """
       Enum-like class representing common HTTP response content types.

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


class HttpResponse:
    def __init__(self, response_message, response_headers, status=200, mimetype=RESPONSEMEMETYPES.text_plain,
                 last_modified=time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())):
        """
        Represents an HTTP response.

        Attributes:
            response_message: The response to send to the client (str, dict, list, etc.).
            response_headers (dict): A dictionary containing HTTP response headers.
            status (int): The HTTP status code (default is 200).
            mimetype (str): The mimetype of the response (default is "text/plain").
            last_modified (str): The last modification time (default is the current GMT time).

        Methods:
            get_response(): Returns the HTTP response as a string object.
            __str__(): Returns a string representation of the HttpResponse object.
        """
        # Encode the response as bytes if it's a string
        if isinstance(response_message, str):
            response_message = response_message.encode("utf-8")

        elif isinstance(response_message, dict):
            response_message = json.dumps(response_message).encode("utf-8")

        elif isinstance(response_message, list):
            response_message = json.dumps(response_message).encode("utf-8")

        elif isinstance(response_message, tuple):
            response_message = json.dumps(response_message).encode("utf-8")

        else:
            # Control that object has a method that can convert it to string
            if not hasattr(response_message, '__str__'):
                raise Exception("Object has no method __str__")
            response_message = response_message.__str__().encode("utf-8")

        self.date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        self.connection = "close"
        self.response_headers = response_headers
        # control that if the Server property is not set, set it
        if "Server" not in self.response_headers:
            self.response_headers["Server"] = "RollAsBack Python Server"
        if "Accept-Ranges" not in self.response_headers:
            self.response_headers["Accept-Ranges"] = "bytes"
        self.last_modified = last_modified
        self.content_length = len(response_message)
        self.content_type = mimetype
        self.message = response_message
        self.status = status
        self.mimetype = mimetype
        self.http_version = "HTTP/1.1"

    def __str__(self):
        """
               Returns a string representation of the HttpResponse object.

               Returns:
                   str: A string representation of the HttpResponse object.
        """
        string_response = f"{self.http_version} {self.status} {HTTPRESPONSECODES.RESPONSE_MESSAGES[self.status]}\n"
        string_response += f"Date: {self.date}\nConnection: close\n"
        string_response += "Server: RollAsBack V.0.0.1 beta (CodeWiki.org)\nAccept-Ranges: bytes\n"
        string_response += f"Content-Type: {self.mimetype}\nContent-Length: {self.content_length}\nLast-Modified: {self.last_modified}"
        for key, value in self.response_headers.items():
            string_response += f"{key}: {value}\n"
        string_response += "\n"
        string_response += self.message.decode("utf-8")
        return string_response

    def set_cookie(self, cookie):
        """
        Set a cookie to the response.

        Args:
            cookie (Cookie): Cookie object to set.
        """
        self.response_headers["Set-Cookie"] = str(cookie)

    def set_cookie_jar(self, cookie_jar):
        """
        Set a cookie jar to the response.

        Args:
            cookie_jar (CookieJar): CookieJar object to set.
        """
        self.response_headers["Set-Cookie"] = cookie_jar

    def __repr__(self):
        return self.__str__()

    def __contains__(self, item):
        return item in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
