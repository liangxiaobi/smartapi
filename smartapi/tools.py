'''
Created on 2012-12-21

@author: lion
'''
from django.http import HttpResponse
import inspect
import json
import logging
import pprint
def getXmlValue(dom,tagName):
    try:
        x=dom.getElementsByTagName(tagName)
        return x[0].childNodes[0].nodeValue
    except:
        return None
def render2json(obj):
    return HttpResponse(json.dumps(obj), mimetype='application/json',content_type="application/json")
def render2html(html):
    return HttpResponse(html, mimetype='text/html',content_type="text/html")
def l(msg=None):
    a=inspect.stack()[1]
    logging.debug("Function: %s" % a[3])
    if msg:
        logging.debug("MSG: %s" % msg)
    else:
        logging.debug("MSG: None")
def haskeys(mydict,*args):
    if(len(mydict)>0):
        for i in range(len(args)):
            if not mydict.has_key(args[i]):
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    a={
       'a':'',
       'b':'',
       }
    #print haskeys(a,'a','a')
    print json.dumps(a)