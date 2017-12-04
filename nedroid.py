#nedroid.py - downloads every nedroid comic

import requests,bs4,os
from bs4 import BeautifulSoup

url = "http://nedroid.com/"

folderDir = 'nedroid'
os.makedirs(folderDir,exist_ok=True)

iterator = 1
#while the url is not the first comic
while(url != "http://nedroid.com/2005/09/2210-whee/"):
    page = requests.get(url)
    page.raise_for_status()
    soup = BeautifulSoup(page.content,'html.parser')    

    #find the comic image within the page
    comic = soup.find(id="comic")
    image = comic.find('img')['src']
    with open(os.path.join(folderDir,os.path.basename(image[1:])),'wb') as handler:
        img_data = requests.get(image).content
        handler.write(img_data) #write (save) the data to the disk
        print("Downloaded: " + str(image) )

    try:
        prevLink = soup.find(class_="nav-previous")
        url = prevLink.find('a')['href']
    except:
        print("",end="") #ignore any errors (videos instead of comics)

    iterator += 1

print("Done. " + str(iterator) + " total comics downloaded")
