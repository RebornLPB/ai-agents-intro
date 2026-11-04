## HTTP Status Codes
HTTP status codes are three-digit numbers that provide information about the outcome of an HTTP request.

### Key Concepts
- **Request**: A message sent by a client to a server to perform an action, such as retrieving a web page.
- **Response**: A message sent by a server to a client in response to a request.
- **Status Code**: A three-digit number that provides information about the outcome of the request.

### Simple Example
Here are a few common HTTP status codes:

- **200 OK**: The request was successful, and the server returned the requested data.
```bash
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 12345

<html>...</html>
```
- **404 Not Found**: The requested resource was not found on the server.
```bash
HTTP/1.1 404 Not Found
Content-Type: text/html
Content-Length: 12345

<html>...</html>
```
- **500 Internal Server Error**: The server encountered an unexpected condition that prevented it from fulfilling the request.
```bash
HTTP/1.1 500 Internal Server Error
Content-Type: text/html
Content-Length: 12345

<html>...</html>
```
Note: These are just a few examples of HTTP status codes. There are many more, each with its own specific meaning.