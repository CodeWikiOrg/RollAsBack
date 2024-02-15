from pathlib import Path
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


class HtmlRenderError(Exception):
    """
    Exception class for HTML rendering errors.
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


def render_html_from_path(path_string: str):
    """
    Render HTML content from a file path.
    :param path_string: The path to the HTML file.
    :return: HTML content as a string.
    """
    try:
        path = Path(path_string)
        with path.open('r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    except Exception as exception:
        return 'Html File Not Found on given absoulute path or an error occured ' + str(exception)

