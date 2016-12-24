'''
Created on Dec 8, 2016

@author: erexsha
'''

import urllib
from xml.etree import cElementTree as ElementTree 

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    capture = False
    addrs = []
    
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            if attr[1] == 'streetAddress':
                self.capture = True
                print "match!!!!!!"
            print "     attr:", attr

    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
        if self.capture:
            self.addrs.append(data)
            self.capture = False
        print "Data     :", data
        

    def handle_comment(self, data):
        print "Comment  :", data

    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data
        
    def output(self):
        print self.addrs



link = 'http://www.zillow.com/homes/for_sale/Los-Altos-CA-94022/97513_rid/globalrelevanceex_sort/37.406642,-122.050467,37.293106,-122.235003_rect/12_zm/'
f = urllib.urlopen(link)           
myfile = f.read()  

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(myfile)
parser.output()

#print(myfile)

#response = ElementTree.fromstring(myfile)