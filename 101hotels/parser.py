import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.io/')
c.perform()
c.close()

body = buffer.getvalue()
print(body.decode('iso-8859-1'))
