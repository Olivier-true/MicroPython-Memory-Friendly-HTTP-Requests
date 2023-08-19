import usocket, ussl

def encode_url(s):
    ch = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~"
    r = ""
    for c in s:
        r += f"%{ord(c):02X}" if c not in ch else c
    return r

def parse_url(url):
    pe = url.find("://")
    pr = url[:pe]
    ru = url[pe + 3:]
    de = ru.find("/")
    dp = ru[:de]
    if ":" in dp:
        d, p = dp.split(":")
    else:
        d = dp
        p = 443 if pr == "https" else 80
    ph = ru[de:]
    return (pr, d, int(p), ph)

def post(url, data=b"", headers={}, recvsize=1024):
    if isinstance(data, dict):
        data = b"&".join([str(k).encode() + b"=" + encode_url(str(data[k])).encode() for k in data])
    pr, hn, p, ph = parse_url(url)
    sock = usocket.socket()
    sock.connect((hn, p))
    sock = ussl.wrap_socket(sock, server_hostname=hn) if pr == 'https' else sock
    headers1 = [
        b"POST " + ph.encode() + b" HTTP/1.1",
        b"Host: " + hn.encode() + b":" + str(p).encode(),
        b"Content-Type: application/x-www-form-urlencoded",
        b"Content-Length: " + str(len(data)).encode(),
        b"Connection: Close"
    ]
    sock.write(b"\r\n".join(headers1) + b"\r\n")
    for h in headers:
        sock.write(h.encode() + b": " + headers[h].encode() + b"\r\n")
    sock.write(b"\r\n")
    sock.write(data)
    header, body = sock.read(recvsize).split(b"\r\n\r\n")
    status_code = {"status_code": header.split(b"\r\n")[0].split(b" ")[1].decode()}
    dh = dict([x.split(b": ")[0].decode(), x.split(b": ")[1].decode()] for x in header.split(b"\r\n") if not x.startswith(b"HTTP/"))
    dh.update(status_code)
    sock.close()
    return (dh, body)


def get(url, headers={}, recvsize=1024):
    pr, hn, p, ph = parse_url(url)
    sock = usocket.socket()
    sock.connect((hn, p))
    sock = ussl.wrap_socket(sock, server_hostname=hn) if pr == "https" else sock
    sock.write(b"GET " + ph.encode() + b" HTTP/1.1\r\n")
    sock.write(b"Host: " + hn.encode() + b":" + str(p).encode() + b"\r\n")
    for h in headers:
        sock.write(h.encode() + b": " + headers[h].encode() + b"\r\n")
    sock.write(b"Content-Length: 0\r\n")
    sock.write(b"Connection: Close\r\n\r\n")
    header, body = sock.read(recvsize).split(b"\r\n\r\n")
    status_code = {"status_code": header.split(b"\r\n")[0].split(b" ")[1].decode()}
    dh = dict([x.split(b": ")[0].decode(), x.split(b": ")[1].decode()] for x in header.split(b"\r\n") if not x.startswith(b"HTTP/"))
    dh.update(status_code)
    sock.close()
    return (dh, body)
