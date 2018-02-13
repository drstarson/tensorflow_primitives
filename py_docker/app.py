import requests

city = 'Los Angeles'

print 'I am from {}'.format(city)

r = requests.get('http://www.google.com')

print r.status_code
