from bs4 import BeautifulSoup
import concurrent.futures
import requests


output_file = open("Results/CrawlerResults.txt", "w", encoding="utf-8")


def ItemParser(item):
    elementPage = BeautifulSoup(requests.get(item["href"]).content, "html.parser") 
    # -> parsarea paginii fiecarui anunt

    title = str(item.find("strong"))[8:-9]
    # -> slice de dupa "<strong>", pana inainte de "</strong>" pentru a gasi titlul anuntului

    description = str(elementPage.select("html body div#root div.css-50cyfj div.css-1on7yx1 div.css-1d90tha div.css-dwud4b div.css-1wws9er div.css-1m8mzwg div.css-g5mtbi-Text")).replace('<br/>', '')[30:-7]
    # -> eliminare <br/>  +  slice de dupa "[<div class="css-g5mtbi-Text">", pana inainte de "</div>]" pentru a gasi descrierea anuntului
    
    elementInfo = "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n" + title + "\n" + description + "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n\n"
    
    output_file.write(elementInfo)


for pageNr in range(1, 26):
    htmlContent = BeautifulSoup(requests.get(f"https://www.olx.ro/casa-gradina/?page={pageNr}").content, "html.parser")
    # -> parsarea fiecarei pagini de anunturi
    
    allElements = htmlContent.find_all("a", class_="marginright5 link linkWithHash detailsLinkPromoted linkWithHashPromoted", href = True) + htmlContent.find_all("a", class_="marginright5 link linkWithHash detailsLink", href = True)
    # -> gasirea fiecarui anunt din pagina
  
    concurrent.futures.ThreadPoolExecutor().map(ItemParser, allElements)
    # -> rulare in paralel (multithread) pentru fiecare anunt in parte
    
output_file.close()