import requests as req

url = 'https://api.remarkets.primary.com.ar/auth/getToken'

x = req.post(url, headers  = {"X-Username": "pythonparatraders5353", "X-Password":"ztibgZ0&"} )

token = x.headers["X-Auth-Token"]
token
