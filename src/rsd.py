import re
import urllib
from json import dumps

from bs4 import BeautifulSoup

release_style = re.compile("float: left; width: 203px; text-align: center;")
rsd = "http://www.recordstoreday.co.uk/exclusive-products/2014/?p="
pmax = 16
json = []

## Paginate
for p in xrange(1, pmax):
    page = "{0}{1}".format(rsd, p)
    soup = BeautifulSoup(urllib.urlopen(page).read())
    ## Find release
    for div in soup.article.find_all('div', style=release_style):
        ## Get release data
        release = [i.strip().replace('\r', '') for i in str(div).split('\n')]
        ## Extract relevant infos
        title, infos = release[2:4]
        artist, title = ' - ' in title and [i.strip() for i in title.split(' - ')][0:2] or (title, title)
        label, format = ' - ' in infos and [i.strip() for i in infos.split(' - ')][0:2] or ('', '')
        details = ''.join(release[4:-1]) if len(release) > 4 else ''
        ## Add to JSON
        json.append({
            'artist' : artist,
            'title' : title,
            'label' : label,
            'format' : format,
            'details' : details,
            'url' : page,
        })

print dumps(json, indent=4, separators=(',', ': '))
