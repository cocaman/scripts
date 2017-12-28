#!/usr/bin/env python

import urllib2
import json

URL = "https://api.koodous.com/apks"

req = urllib2.Request(URL)
req.add_header('Accept', 'application/json')
req.add_header('Content-Type', 'application/json')

    
resp = urllib2.urlopen(req)
content = resp.read()
jData = json.loads(content)

print "package_name,sha256,koodous,virustotal"
for apk_object in jData["results"]:
    print apk_object["package_name"] + "," + apk_object["sha256"] + "," + "https://koodous.com/apks/" + apk_object["sha256"] + "," + "https://www.virustotal.com/#/search/" + apk_object["sha256"]
