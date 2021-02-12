import requests
from requests_html import HTMLSession

url = 'https://www.carpartstuning.com/index.php?numprod=side-grilles-fog-lamp-covers-suitable-for-audi-a1-8x-2010-up-rs1-black-edition&detalii=5986180&categorie=10'

try:
    session = HTMLSession()
    response = session.get(url)
    
    response.html.render(sleep=0.5)
    title =  response.html.find('span.availability_status', first=True)

    print(title.text)

     
except requests.exceptions.RequestException as e:
    print(e)


