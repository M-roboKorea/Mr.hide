
# coding: utf-8

# In[6]:


def download_img () :

    import requests
    from bs4 import BeautifulSoup 
    url = str('https://1.base.maps.api.heremaps.kr/maptile/2.1/maptile/newest/normal.day/15/'
              +  input('lag :') + '/' + input('long :') + '/' '512/png8?app_id=eJBbvmVzCel4EqtBmISb&app_code=CvN3VyRHj5orQg2-DtvDEg')

    html = urllib.request.urlopen(url)
    urllib.request.urlretrieve(url,'location.png')
    print('Image download complete')

