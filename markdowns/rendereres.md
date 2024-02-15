# http_request.py Documentation

**Author(s):** CodeWiki  
**File name:** http_request.py  
**Date:** 16th January 2024  

## HtmlRenderError

Exception class for HTML rendering errors.

### Methods:

#### \_\_init__(self, message)

Initializes an HtmlRenderError instance with the given error message.

- `message` (str): The error message.

#### \_\_str__(self)

Returns a string representation of the HtmlRenderError.

Returns:
- str: The error message.

## render_html_from_path(path_string)

Render HTML content from a file path.

This function reads the content of an HTML file located at the specified path
and returns the HTML content as a string.

### Arguments:

- `path_string` (str): The path to the HTML file.

### Returns:

- str: The HTML content as a string.

### Raises:

- HtmlRenderError: If the HTML file is not found or an error occurs during file reading.
