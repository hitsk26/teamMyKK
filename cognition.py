#!/usr/bin/python
from __future__ import print_function

import json
import sys
PY3 = sys.version_info[0] == 3

if PY3:
  from urllib.parse import urlencode
  from http.client import HTTPSConnection
else:
  from urllib import urlencode
  from httplib import HTTPSConnection
  
def cognition(image_url):

  list =[["green", "salad", "broccoli", "fruit", "different types of food", "vegetables"], ["french friesa", "pile of fries", "fries" ,"bananas", "pasta dish", "hot dogs", "french fries"]]
  headers = {
    'Content-Type':  'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'dd270ab4b6f7415e9c6122af838f2eb8',
  }
  params = urlencode({'visualFeatures': 'Description'})
  try:
    conn = HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, open(image_url, 'rb').read(), headers)
    response = conn.getresponse()
    data = response.read()
    data_json = json.loads(data)
    result = data_json['description']['captions'][0]['text'].split(" ")
    print(data_json['description']['captions'][0]['text'])
    count=0
    for i in [0,1]:
      for text in result:
        if text in list[i]:
          count=count+1
      if count>0:
        print(i)
      count=0
    conn.close()
  except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
                
