

# Redirect Class

Represents an HTTP Redirect response with a refresh mechanism. ( Why to use ? If you want blink in your app to show a message before redirect)

## Attributes

- `response_message`: The message to be displayed in the response.
- `response_headers`: Additional headers to be included in the response.
- `location`: The URL to redirect to.
- `blink_sec`: The time (in seconds) for the automatic refresh.
- `status`: The HTTP status code (default is 302 - Found).
- `last_modified`: The last modified timestamp (default is the current GMT time).

## Constructor

```python
def __init__(self, response_message, response_headers, location, blink_sec=1, status=302,
             last_modified=time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())):
```

Initializes a Redirect object.

Raises:
- `Exception`: If the provided status code is not in the 3xx range.

## Methods

### `__str__(self)`

Returns a string representation of the Redirect response.

### `__repr__(self)`

Returns a string representation of the Redirect response.

### `__bytes__(self)`

Returns the byte representation of the Redirect response.

# Blink Class

Represents an HTTP response that triggers an automatic refresh (blink).

## Attributes

- `response_message`: The message to be displayed in the response.
- `response_headers`: Additional headers to be included in the response.
- `location`: The URL to redirect to after the blink.
- `blink_sec`: The time (in seconds) for the automatic refresh.
- `last_modified`: The last modified timestamp (default is the current GMT time).

## Constructor

```python
def __init__(self, response_message, response_headers, location, blink_sec=1,
             last_modified=time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())):
```

Initializes a Blink object.

## Methods

### `__str__(self)`

Returns a string representation of the Blink response.

### `__repr__(self)`

Returns a string representation of the Blink response.

### `__bytes__(self)`

Returns the byte representation of the Blink response.
