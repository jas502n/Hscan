#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib2
import urllib
import re

pattern = ('<img alt=.*?src="(.*?)"')
name = ('<h2><a href=.*?>(.*?)</a>')
website = (':\/\/(.*?)\/')

host = 'www.meizitu.com'
url = host

headers1 = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)","Host":host,"Referer":host}

for i in range(11,20):
    url = 'http://' + host + '/a/' + str(i) + '.html'
    print "URL:" + url
    try:
        req = urllib2.Request(url,headers=headers1)
        resp = urllib2.urlopen(req)
        contents = resp.read()
    #print contents
        targets = re.findall(pattern,contents)
    except urllib2.HTTPError as e:
        print e
    filenames = re.findall(name,contents)
    filename = filenames[0]
    count = 1
    for target in targets:
        print type(target),target
        targethost = re.findall(website,target)
        headers2 = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36","Host":targethost[0],"Upgrade-Insecure-Requests":"1"}
        
        #print filename[0]
        #print targethost[0]
        filenametouse = filename + str(count) + '.jpg'
        #print type(filename),filename
        print filenametouse
        try:
            picreq = urllib2.Request(target,headers=headers2)
            pic = urllib2.urlopen(picreq)
        except (urllib2.HTTPError,urllib2.URLError) as e:
            print e
        data = pic.read()
        with open(filenametouse,'wb') as code:
            code.write(data)
            code.close()
        count += 1
        print count
