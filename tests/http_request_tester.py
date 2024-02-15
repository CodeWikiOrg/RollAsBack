import unittest
import xml.dom.minidom

from src.rollasback import HttpRequest


class TestHttpRequest(unittest.TestCase):

    def test_valid_http_request(self):
        request_string = "GET /path/to/resource HTTP/1.1\r\nHost: example.com\r\n\r\n"
        http_request = HttpRequest(request_string)
        self.assertIsNotNone(http_request)
        self.assertEqual(http_request.method, "GET")
        self.assertEqual(http_request.path, "/path/to/resource")
        self.assertEqual(http_request.http_version, "HTTP/1.1")
        self.assertEqual(http_request.headers, {"Host": "example.com"})
        self.assertEqual(http_request.body, None)

    def test_invalid_http_request(self):
        # Test with an invalid request string
        invalid_request_string = "Invalid Request String"
        http_request = HttpRequest(invalid_request_string)
        # attributes should be None
        self.assertIsNone(http_request.method)
        self.assertIsNone(http_request.path)
        self.assertIsNone(http_request.http_version)
        self.assertEqual(http_request.headers, {})
        self.assertIsNone(http_request.body)

    def test_http_request_with_body(self):
        request_string = "POST /api/data HTTP/1.1\r\nContent-Type: application/json\r\n\r\n{'key': 'value'}"
        http_request = HttpRequest(request_string)

        self.assertIsNotNone(http_request)
        self.assertEqual(http_request.method, "POST")
        self.assertEqual(http_request.path, "/api/data")
        self.assertEqual(http_request.http_version, "HTTP/1.1")
        self.assertEqual(http_request.headers, {"Content-Type": "application/json"})
        self.assertEqual(http_request.body, {'key': 'value'})

    def test_http_request_with_multiple_headers(self):
        request_string = "GET /path HTTP/1.1\r\nHost: example.com\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
        try:
            HttpRequest(request_string)
            assert False
        except Exception as e:
            print(e)
            assert True

    def test_http_request_with_empty_body(self):
        request_string = "PUT /update HTTP/1.1\r\nContent-Type: text/plain\r\n\r\n"
        http_request = HttpRequest(request_string)

        self.assertIsNotNone(http_request)
        self.assertEqual(http_request.method, "PUT")
        self.assertEqual(http_request.path, "/update")
        self.assertEqual(http_request.http_version, "HTTP/1.1")
        self.assertEqual(http_request.headers, {"Content-Type": "text/plain"})
        self.assertEqual(http_request.body, None)

    def test_http_request_with_xml_body(self):
        xml_body = '<root><element>value</element></root>'
        request_string = f"POST /api/xml HTTP/1.1\r\nContent-Type: application/xml\r\n\r\n{xml_body}"
        http_request = HttpRequest(request_string)

        self.assertIsNotNone(http_request)
        self.assertEqual(http_request.method, "POST")
        self.assertEqual(http_request.path, "/api/xml")
        self.assertEqual(http_request.http_version, "HTTP/1.1")
        self.assertEqual(http_request.headers, {"Content-Type": "application/xml"})
        self.assertEqual(http_request.body, xml.dom.minidom.parseString(xml_body).toprettyxml())

    def test_http_request_with_urlencoded_body(self):
        urlencoded_body = 'key1=value1&key2=value2'
        request_string = f"PUT /update HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{urlencoded_body}"
        http_request = HttpRequest(request_string)

        self.assertIsNotNone(http_request)
        self.assertEqual(http_request.method, "PUT")
        self.assertEqual(http_request.path, "/update")
        self.assertEqual(http_request.http_version, "HTTP/1.1")
        self.assertEqual(http_request.headers, {"Content-Type": "application/x-www-form-urlencoded"})
        self.assertEqual(http_request.body, {"key1": "value1", "key2": "value2"})


if __name__ == '__main__':
    unittest.main()

######################################################
# Example usages of HttpRequest class
######################################################
request_string = "GET http://localhost:8080/tienda1/imagenes/1.gif HTTP/1.1\n" \
                 "User-Agent: Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)\n" \
                 "Pragma: no-cache\n" \
                 "Cache-control: no-cache\n" \
                 "Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\n" \
                 "Accept-Encoding: x-gzip, x-deflate, gzip, deflate\n" \
                 "Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5\n" \
                 "Accept-Language: en\n" \
                 "Content-Type: application/json\n" \
                 "Host: localhost:8080\n" \
                 "Cookie: JSESSIONID=1822709F57BDDFA1ADA9D0BAAED0D4B3\n" \
                 "Connection: close\n" \
                 " \n" \
                 "{'key': 'value'}"

http_request = HttpRequest(request_string)
print(http_request.to_dict())

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
                 " \n" \
                 "{'key': 'value'}"

http_request = HttpRequest(request_string)
print(http_request.to_dict())

request_string = "GET http://localhost:8080/tienda1/imagenes/1.gif HTTP/1.1\n" \
                 "User-Agent: Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)\n" \
                 "Pragma: no-cache\n" \
                 "Cache-control: no-cache\n" \
                 "Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\n" \
                 "Accept-Encoding: x-gzip, x-deflate, gzip, deflate\n" \
                 "Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5\n" \
                 "Accept-Language: en\n" \
                 "Content-Type: text/html\n" \
                 "Host: localhost:8080\n" \
                 "Cookie: JSESSIONID=1822709F57BDDFA1ADA9D0BAAED0D4B3\n" \
                 "Connection: close\n" \
                 " \n" \
                 "<html><body><h1>It works!</h1></body></html>"

http_request = HttpRequest(request_string)
print(http_request.to_dict())

request_string = "GET http://localhost:8080/tienda1/imagenes/1.gif HTTP/1.1\n" \
                 "User-Agent: Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.8 (like Gecko)\n" \
                 "Pragma: no-cache\n" \
                 "Cache-control: no-cache\n" \
                 "Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\n" \
                 "Accept-Encoding: x-gzip, x-deflate, gzip, deflate\n" \
                 "Accept-Charset: utf-8, utf-8;q=0.5, *;q=0.5\n" \
                 "Accept-Language: en\n" \
                 "Content-Type: application/xml\n" \
                 "Host: localhost:8080\n" \
                 "Cookie: JSESSIONID=1822709F57BDDFA1ADA9D0BAAED0D4B3\n" \
                 "Connection: close\n" \
                 " \n" \
                 "<root><element>value</element></root>"

http_request = HttpRequest(request_string)
print(http_request.to_dict())
