#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:47:39 2018

@author: buckz
"""
import urllib.request
import urllib.error
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
import http.client # Error BadStatusLine
from socket import timeout # Error timeout

# Extract data from column to form a list
def extract_values(colname):
    file = 'dfv5.xls'
    df = pd.read_excel(file)
    a = []
    for i in df[colname]:
        a.append(i)
    return a

# Create new list, remove None values and check if url is Valid.
def check_url(l):
    global newl
    newl = []
    for lien in l:
        newl.append(lien)
        if lien == 'None':
            newl.remove(lien)
    for url in newl:
        try:
            urllib.request.urlopen(url, timeout=15)
            print("OK : " + url)
            get_urlimages(url)
        except urllib.error.HTTPError as e:
            print("ERROR " + str(e.code) + " : " + url)
            newl.remove(url)
        except urllib.error.URLError as e:
            print("ERROR " + str(e.args) + " : " + url)
            newl.remove(url)
        except timeout:
            pass
            
#Prepare soup 
def make_soup(url):
    global html_page
    html_page = urllib.request.urlopen(url)
    return BeautifulSoup(html_page, "lxml")

#Get src and stock in list 'images'. Regex to catch 'Logos'.
def get_urlimages(url):
    soup = make_soup(url)
    global images
    images = []
    for img in soup.findAll('img'):
        imgurl = img.get('src')
        if re.search(r"[Ll]+[ogo]+[s]?", str(imgurl)):
            if re.search(r"^http.+", str(imgurl)): # If start 'http://'
                images.append(str(imgurl))
            elif re.search(r"^[/].*", str(imgurl)): # if start '/'
                re.sub(r"[/]$","", url) # sub last '/' in url
                images.append(url + imgurl)
            elif str(imgurl) == 'None':
                pass
            else:
                images.append(url + str(imgurl)) # if start without '/'
    path = '/home/buckz/Data/img' #To dl in /img
    lien2 = str(url).replace('/', '_') # Rename url with '_' to name dir
    # Create dir to each url and dl img 
    try:
        os.mkdir(path+'/' + lien2)
        os.chdir(path+'/' + lien2)
        for i in images:
            try:
                urllib.request.urlretrieve(i, os.path.basename(i))
            except urllib.error.URLError:
                continue
            except UnicodeEncodeError:
                continue
            except http.client.BadStatusLine:
                continue
        os.chdir(path)
    except FileExistsError:
        pass
    
pageweb = extract_values('PageWeb')
check_url(pageweb)


    
    
        
