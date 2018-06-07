import socket
import requests
import json
def get_hostname():
    return socket.gethostname()

def get_ip():
     res = requests.get('https://ipinfo.io/')
     return json.loads(res.text)["ip"]
