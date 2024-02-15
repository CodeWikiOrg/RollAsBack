"""
Author(s): CodeWiki
File name: rest_endpoint.py
Date: 16th January 2024

Description: Web backend framework written in Python named RollAsBack.

Disclaimer: This software is provided "as is" without warranty of any kind,
express or implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose, and noninfringement. In no event shall the authors
or copyright holders be liable for any claim, damages, or other liability,
whether in an action of contract, tort, or otherwise, arising from, out of, or in connection
with the software or the use or other dealings in the software.

Copyright @ CodeWiki by MIT License
"""
import logging as log
import re
import socket
import time
from rollasback.http_response import HttpResponse, RESPONSEMEMETYPES
from rollasback.http_request import HttpRequest
from urllib.parse import urlparse, parse_qs


class Route:
    def __init__(self, path, func):
        self.path = path
        self.func = func
        self.regex_pattern = self.generate_regex_pattern()

    def generate_regex_pattern(self):
        """
        Generates a regex pattern from the path string.
        :return: Regex pattern string. It will be used to match the path. eg: /user/{user_id}
        !! IMPORTANT !!: This will not parse after the query parameters. eg: /user/{user_id}?name=deneme will not work for name=deneme
        """
        regex_pattern = re.escape(self.path)  # Escape special characters
        regex_pattern = regex_pattern.replace("\\{", "(?P<").replace("\\}", ">[^/]+)")

        # Handle optional path parameters enclosed in parentheses, e.g., /user/{user_id(\d+)}
        regex_pattern = re.sub(r'\\{([^\\}]+)\\}', r'(?P<\1>[^/]+)?', regex_pattern)

        # Allow a trailing slash at the end of the path
        regex_pattern += '/?$'
        return regex_pattern


class RollAsBack:
    static_routes = []

    def __init__(self, name, backlog: int = 50, **kwargs):
        self.__ip_address = None
        self.name = name
        self.config = {}
        self.routes = []
        self.backlog = backlog
        self.kwargs = kwargs
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.logger = self.__setup_logger()

    def __setup_logger(self):
        logger = log.getLogger(__name__)
        logger.setLevel(log.INFO)
        log.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
        logger.addHandler(log.StreamHandler())
        return logger

    def endpoint(self, path):
        def decorator(func):
            route = Route(path, func)
            self.routes.append(route)
            return func

        return decorator

    def start_server(self, host, port):
        self.__socket.bind((host, port))
        self.__socket.listen(5)
        self.__ip_address = self.__socket.getsockname()

        self.logger.info(
            "{} - {} Server started on : {} ".format(time.strftime('%Y-%m-%d %H:%M:%S'), self.name, self.__ip_address))
        try:
            while True:
                client_socket, addr = self.__socket.accept()
                request_data = b''

                while True:
                    chunk = client_socket.recv(1024)
                    if not chunk:
                        break
                    request_data += chunk

                    # Check if we reached the end of the HTTP request
                    if b'\r\n\r\n' in request_data:
                        break

                if len(request_data.decode("utf-8")) > 0:
                    request = HttpRequest(request_data.decode('utf-8'))
                    if request:
                        send_flag = False
                        for route in self.routes:
                            match = re.match(route.regex_pattern, request.path)
                            parsed_url = urlparse(request.path)  # Parse the URL
                            query_params = parsed_url.query  # Get the query parameters
                            request.query_params = parse_qs(
                                query_params)  # Add the query parameters to the request object
                            if match:
                                # Extract path parameters and add to the request object
                                groups = match.groups()
                                path_params = []
                                for i in range(len(groups)):
                                    if "?" in groups[i]:
                                        path_params.append(groups[i].split("?")[0])
                                    else:
                                        path_params.append(groups[i])
                                request.path_params = path_params
                                response = route.func(request)
                                client_socket.sendall(str(response).encode('utf-8'))
                                send_flag = True
                        if not send_flag:
                            client_socket.sendall(str(HttpResponse(
                                response_message="Not Found",
                                response_headers={},
                                mimetype=RESPONSEMEMETYPES.text_plain,
                                status=404
                            )).encode("utf-8"))
                    client_socket.close()
                else:
                    continue

        except KeyboardInterrupt:
            self.stop_server()

    def print_log(self, message, level="INFO"):
        if level == "INFO":
            self.logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {self.name} :{message}")
        elif level == "WARNING":
            self.logger.warning(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {self.name} :{message}")
        elif level == "ERROR":
            self.logger.error(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {self.name} :{message}")
        elif level == "DEBUG":
            self.logger.debug(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {self.name} :{message}")
        else:
            self.logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {self.name} :{message}")

    def stop_server(self):
        self.__socket.close()
