from urllib.parse import urlparse

def analyze_url(url: str):
    urlparsed = urlparse(url)
    return {
        "url": url,
        "scheme": urlparsed.scheme,
        "hostname": urlparsed.hostname,
        "port": urlparsed.port,
        "path": urlparsed.path,
        "query": urlparsed.query,
        "fragment": urlparsed.fragment,
    }

