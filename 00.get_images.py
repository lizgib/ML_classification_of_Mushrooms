from selenium import webdriver
import urllib
import urllib.request
import os, sys

outfile = open("data/image_links.txt", "w")
browser = webdriver.Firefox()
browser.get("http://mushroom.pro/c_galleries/a_1k/pages/Agaricus_augustus.htm")
img = browser.find_element_by_xpath("/html/body/div/center[2]/a/img")
src = img.get_attribute('src')
outfile.write(src + "\n")
next_page = browser.find_elements_by_xpath("/html/body/div/center[1]/table/tbody/tr/td[2]/a")
next_page[0].click()
while len(next_page) > 0:
  img = browser.find_element_by_xpath("/html/body/div/center[2]/a/img")
  src = img.get_attribute('src')
  outfile.write(src + "\n")
  next_page = browser.find_elements_by_xpath("/html/body/div/center[1]/table/tbody/tr/td[3]/a")
  if len(next_page) > 0:
    next_page[0].click()
outfile.close()

f = open('data/image_links.txt')
lines = f.readlines()

os.chdir('images')
for url in lines:
    name = url.split('/')[-1].strip()
    urllib.request.urlretrieve(url, name)
