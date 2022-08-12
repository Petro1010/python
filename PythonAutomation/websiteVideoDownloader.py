import requests
import shutil
from bs4 import BeautifulSoup
from sys import argv

url = argv[1]  # get the link where the video source is from command line
html_response = requests.get(url)
soup = BeautifulSoup(html_response.text, 'html.parser')

# - - Get the .mp4 url and the filename
# - - Find the source elements and get their video source attribute
for vid in soup.find_all('source'):
    vid_url = vid['src']
    filename = vid['src'].split('/')[-1]

# - - Get the video 
response = requests.get(vid_url, stream=True)

# - - Staus is ok
if response.status_code == 200:
    # - - Make sure the file size is not 0
    response.raw.decode_content = True

    with open(filename, 'wb') as f:
        #  - - Take the data from response.raw and transfer it to the file
        shutil.copyfileobj(response.raw, f)
    print('Downloaded file')
else:
    print('Download failed')
