import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"

def save_file(path):
    r = requests.get("")
    with open(path, 'wb') as f:
        f.write(r.content)