import time
from rollasback import HttpResponse, RESPONSEMEMETYPES, HTTPRESPONSECODES


class Redirect(HttpResponse):
    def __init__(self, response_message, response_headers, location, blink_sec=1, status=302,
                 last_modified=time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())):
        if status < 300 or status > 399:
            raise Exception("Invalid status code for Blink response!")
        self.location = location
        self.blink_sec = blink_sec
        super().__init__(
            response_message=response_message,
            response_headers=response_headers,
            mimetype=RESPONSEMEMETYPES.text_html,
            status=status,
            last_modified=last_modified
        )

    def __str__(self):
        string_response = f"{self.http_version} {self.status} {HTTPRESPONSECODES.RESPONSE_MESSAGES[self.status]}\n"
        string_response += f"Location: {self.location}\n"
        string_response += f"Date: {self.date}\nConnection: close\n"
        string_response += "Server: RollAsBack V.0.0.1 beta (CodeWiki.org)\nAccept-Ranges: bytes\n"
        string_response += f"Content-Type: {self.mimetype}\nContent-Length: {self.content_length}\nLast-Modified: {self.last_modified}"
        for key, value in self.response_headers.items():
            string_response += f"{key}: {value}\n"
        string_response += "Injected-Header: True\n"
        string_response += "\n"
        string_response += "<html><head><meta http-equiv=\"refresh\" content=\"{}; url={}\"></head></html>".format(
            self.blink_sec, self.location)

        return string_response

    def __repr__(self):
        return self.__str__()

    def __bytes__(self):
        return self.__str__().encode("utf-8")


class Blink(HttpResponse):
    def __init__(self, response_message, response_headers, location, blink_sec=1,
                 last_modified=time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())):
        self.status = 200
        self.location = location
        self.blink_sec = blink_sec
        self.response_message = response_message
        super().__init__(
            response_message=response_message,
            response_headers=response_headers,
            mimetype=RESPONSEMEMETYPES.text_html,
            status=self.status,
            last_modified=last_modified
        )

    def __str__(self):
        string_response = f"{self.http_version} {self.status} {HTTPRESPONSECODES.RESPONSE_MESSAGES[self.status]}\n"
        string_response += f"Location: {self.location}\n"
        string_response += f"Date: {self.date}\nConnection: close\n"
        string_response += "Server: RollAsBack V.0.0.1 beta (CodeWiki.org)\nAccept-Ranges: bytes\n"
        string_response += f"Content-Type: {self.mimetype}\nContent-Length:zzz \nLast-Modified: {self.last_modified}"
        for key, value in self.response_headers.items():
            string_response += f"{key}: {value}\n"
        string_response += "Injected-Header: true\n"
        string_response += "\n"
        string_response += "<p>{}</p>".format(self.response_message)
        string_response += "<script>setTimeout(function()"
        string_response += "{window.location.href = \"{xxx}\";}, {yyy});</script>"
        string_response = string_response.replace("{xxx}", str(self.location))
        string_response = string_response.replace("{yyy}", str(self.blink_sec * 1000))
        # modify yhe content length
        string_response = string_response.replace("zzz", str(len(string_response.split("\n\n")[1])))

        print(string_response)

        return string_response

    def __repr__(self):
        return self.__str__()

    def __bytes__(self):
        return self.__str__().encode("utf-8")
