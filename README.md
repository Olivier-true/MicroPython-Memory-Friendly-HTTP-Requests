# MicroPython Memory-Friendly HTTP Requests

A lightweight and memory-efficient HTTP client module for MicroPython, optimized for use cases on resource-constrained devices such as ESP32.

## Features
- Minimal memory footprint: Designed to conserve memory resources, making it suitable for embedded systems and IoT devices.
- Low-memory usage: Provides efficient memory management during HTTP requests, minimizing memory allocation and deallocation.
- Support for GET and POST requests: Easily make HTTP GET and POST requests with customizable headers and data.
- HTTPS Support: Securely communicate with servers using the ssl protocol.
- Ideal for MicroPython: Specifically crafted for MicroPython environments, enabling seamless integration.

## Tags
- micropython
- esp32
- requests
- memory-efficient
- low-memory
- http-client
- iot
- embedded
- lightweight
- nanoframework

## Installation
1. Clone this repository: `https://github.com/Olivier-true/MicroPython-Memory-Friendly-HTTP-Requests.git`
2. Copy `krequests.py` to your MicroPython device.
3. Start using the module in your MicroPython projects!
## Usage
Import the module:
```python
import krequests as requests
```

### HTTP GET Request
```requests.get(url -> str, headers={} -> dict, recvsize=1024 -> int) -> return tuple (headers -> dict, response -> bytes)```
```python
# Perform an HTTP GET request
response_headers, response_data = requests.get("http://httpbin.org/")
print("Server Headers:", response_headers)
print("Response Data:", response_data)
```
```python
# Perform an HTTP GET request with custom headers
custom_headers = {"headerName": "headerValue"}
response_headers, response_data = requests.get("http://httpbin.org/", headers=custom_headers)
print("Server Headers:", response_headers)
print("Response Data:", response_data)
```
```python
# Perform an HTTP GET request and specify the received data size
response_headers, response_data = requests.get("http://httpbin.org/", recvsize=2048)
print("Server Headers:", response_headers)
print("Response Data:", response_data)
```
### HTTP POST Request
`requests.post(url -> str, data={} -> dict, data=b"" -> bytes, headers={} -> dict, recvsize=1024 -> int) -> return tuple (headers -> dict, response -> bytes)`
```python
# Perform an HTTP POST request with form data
form_data = {"key": "value", "int": 7}
response_headers, response_data = requests.post("http://httpbin.org/post", data=form_data)
print("Server Headers:", response_headers)
print("Response Data:", response_data)
```
```python
# Perform an HTTP POST request with JSON data
json_data = "{'key': 'value'}".encode()
custom_headers = {"Content-Type": "application/json"}
response_headers, response_data = requests.post("http://httpbin.org/post", data=json_data, headers=custom_headers)
print("Server Headers:", response_headers)
print("Response Data:", response_data)
```
```python
# Perform an HTTP POST request with binary data and specify the received data size
binary_data = b"some data"
response_headers, response_data = requests.post("http://httpbin.org/", data=binary_data, recvsize=2048)
print("Server Headers:", response_headers)
print("Response Data:", response_data)
```

Feel free to contribute to this project and make it even better for memory-conscious MicroPython development! If you encounter any issues or have suggestions, please submit an issue or pull request on GitHub.

Made with ❤️ for MicroPython developers and IoT enthusiasts by Olivier.

<p align="center"><img src="https://ipipip-gh.0xsql.repl.co/friendly-requests/views.png" alt="Visitors"></a></p>
