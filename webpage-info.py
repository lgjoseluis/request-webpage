#!/usr/bin/env/ python
#_*_ coding: utf8 _*_$

#Packages
import requests
import argparse
from Wappalyzer import WebPage

parser = argparse.ArgumentParser(description="Get information for a web page.")
parser.add_argument('-t', '--target', help="Web page target")
parser = parser.parse_args()

def GetWebPageApps(urlWebPage=''):
    try:
        response = WebPage.WebPage(urlWebPage)
        
        print(' Info '.center(40, '='))
        #print(response.headers)
        print('Url:', response.url)
        print('Title web page:', response.title)
                
        print(' Meta '.center(40, '='))

        for m in response.meta:
            print(m, '==>', response.meta[m])

        print(' Apps '.center(40, '='))

        #apps = dict(response.info())
        for i in list(response.apps):
            print(i)
        
    except Exception as e:
        print('Error:', e)

def GetWebPageHeaders(urlWebPage =''):
    try:
        response = requests.get(urlWebPage)
        headers = dict(response.headers)
        #print(response.text)
        print(' Headers '.center(40, '='))

        for h in headers:
            print(h, '==>', headers[h])
    except Exception as e:
        print('Error:', e)

def main():
    if parser.target:        
        GetWebPageApps(parser.target)
        GetWebPageHeaders(parser.target)
    else:
        print("The domain target is required.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Break execute.")
    finally:
        print("End execute.")