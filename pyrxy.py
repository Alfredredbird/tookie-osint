import http.client as httplib
import urllib.parse

def url_code_status(url):
    try:
        protocol, host, path, query, fragment = urllib.parse.urlsplit(url)
        if protocol == "http":
            conntype = httplib.HTTPConnection
        elif protocol == "https":
            conntype = httplib.HTTPSConnection
        else:
            raise ValueError("unsupported protocol: " + protocol)
        conn = conntype(host)
        conn.request("HEAD", path)
        resp = conn.getresponse()
        conn.close()
        return resp.status
    except Exception as e:
        print(f'[ERROR]: {e}')
