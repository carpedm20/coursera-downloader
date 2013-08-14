from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib2

course_url = "https://class.coursera.org/algo-004/lecture/"
extensions = ['_typed.pdf','.mp4']

base_url = (course_url)
soup = BeautifulSoup(urlopen(base_url).read())

resources = soup.find_all("div", "course-lecture-item-resource")
#resource_urls = [div.a["href"] for div in resources]
hrefs = [u for divs in resources for u in divs.findAll('a')]

count = 1

for u in hrefs:
  file_name = str(count) + '_' + str(u.div.text).split('for ')[1].replace(' ','_')
  u = u['href']

  for ex in extensions:
    if u.find(ex) != -1:
      print '[*] file : ' + file_name + ex
      response = urllib2.urlopen(u)
      f = open(file_name + ex,'w')
      f.write(response.read())
      f.close()

      if ex is exs[len(exs) - 1]:
        count += 1
