import requests
import re
response = requests.get('http://log.mmstat.com/eg.js').text
print response
re_obj = re.search('Etag="(.*)"', response)
cna = re_obj.group(1)
print cna

