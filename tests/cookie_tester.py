import unittest
from datetime import datetime
from src.rollasback.cookie import Cookie, CookieJar


class TestCookie(unittest.TestCase):
    def test_cookie_creation(self):
        cookie = Cookie(
            key='session_id', value='123456789', expires='2024-01-30', path='/app', domain='example.com',
            secure=True, httponly=True
        )
        self.assertEqual(cookie.key, 'session_id')
        self.assertEqual(cookie.value, '123456789')
        self.assertEqual(cookie.expires, datetime(2024, 1, 30))
        self.assertEqual(cookie.path, '/app')
        self.assertEqual(cookie.domain, 'example.com')
        self.assertTrue(cookie.secure)
        self.assertTrue(cookie.httponly)

    def test_cookie_jar_operations(self):
        cookie1 = Cookie(
            key='session_id', value='123456789', expires='2024-01-30', path='/app', domain='example.com',
            secure=True, httponly=True
        )
        cookie2 = Cookie(
            key='user_token', value='abcdef12345', expires='2024-02-15', path='/api', domain='example.com'
        )

        cookie_jar = CookieJar()

        # Adding cookies to the cookie jar
        cookie_jar.add_cookie(cookie1)
        cookie_jar.add_cookie(cookie2)

        # Retrieving a cookie by key
        retrieved_cookie = cookie_jar.get_cookie('session_id')
        self.assertEqual(retrieved_cookie, cookie1)

        # Updating a cookie in the jar
        updated_cookie = Cookie(
            key='session_id', value='new_value', expires='2024-03-01', path='/app', domain='example.com',
            secure=True, httponly=True
        )
        cookie_jar.update_cookie(updated_cookie)

        # Verify that the cookie is updated
        updated_cookie = cookie_jar.get_cookie('session_id')
        self.assertEqual(updated_cookie.value, 'new_value')

        # Deleting a cookie from the jar
        deleted_cookie_key = 'user_token'
        cookie_jar.delete_cookie(deleted_cookie_key)

        # Verify that the deleted cookie is not in the jar
        deleted_cookie = cookie_jar.get_cookie(deleted_cookie_key)
        self.assertIsNone(deleted_cookie)

        # Verify that the jar only contains one cookie
        self.assertEqual(len(cookie_jar), 1)

        # Displaying all cookies in the cookie jar
        all_cookies_in_jar = cookie_jar.get_all_cookies()
        self.assertEqual(all_cookies_in_jar, [updated_cookie])

        # Getting the cookie header string
        cookie_header_string = cookie_jar.get_cookie_header()
        self.assertEqual(cookie_header_string, 'session_id=new_value; Expires=2024-03-01; Path=/app; Domain=example.com; Secure; HttpOnly')

        # Getting the cookie dictionary
        cookie_dict = cookie_jar.get_cookie_dict()
        self.assertEqual(cookie_dict, {'session_id': 'new_value'})


if __name__ == '__main__':
    unittest.main()
