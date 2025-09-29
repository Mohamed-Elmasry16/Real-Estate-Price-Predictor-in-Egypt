import requests
from bs4 import BeautifulSoup
import pandas as pd 
import time
import random 

def card_info(url,new_id=0):

    page = requests.get(url)
    src = page.content
    soup = BeautifulSoup(src, 'lxml') 
    
    cards = soup.findAll("li",{"class":"_92ae6bf0"}) # every card
    
    id = new_id
    local_cards = []
    
    def safe_extract(card, selector, attr=None):
        el = card.find(*selector) if isinstance(selector, tuple) else card.find(selector)
        if el:
            return el[attr] if attr else el.text.strip()
        return None
    
    for card in cards:
        id += 1
        
        price = safe_extract(card, ("span", {"class":"eff033a6"}))
        type_ = safe_extract(card, ("span",{"class":"c377cd7b _3002c6fb","aria-label": "Type"}))   
        n_beds = safe_extract(card, ("span",{"class":"c377cd7b _3002c6fb","aria-label": "Beds"}))
        n_baths = safe_extract(card, ("span",{"class":"c377cd7b _3002c6fb","aria-label": "Baths"}))
        area = safe_extract(card, ("h4",{"class":"_60820635 _07b5f28e"}))
        location = safe_extract(card, ("h3",{"class":"_51c6b1ca"}))
        link = safe_extract(card, ("a",{"class":"_8969fafd","aria-label": "Listing link"}), "href")
        
        local_cards.append({
            "id": id,
            "price": price,
            "type": type_,
            "number_of_beds": n_beds,
            "number_of_baths": n_baths,
            "area": area,
            "location": location,
            "internal_link": link
        })
    
    return local_cards, id


# main loop with saving each page
id = 0
file_path = "d:\\houses.csv"

for i in range(1, 2100):  
    if i == 1:
        url1 = "https://www.bayut.eg/عقارات-للبيع/مصر/?completion_status=ready"
        data, id = card_info(url1)
        df = pd.DataFrame(data)
        df.to_csv("d:\\houses.csv", index=False) 
    else:
        page_num = i
        url2 = f"https://www.bayut.eg/صفحة-{page_num}/عقارات-للبيع/مصر/?completion_status=ready"
        d2, id2 = card_info(url2, id)
        id = id2
        df = pd.DataFrame(d2)
        df.to_csv("d:\\houses.csv", index=False, mode='a', header=False)  

    print(f"✅ Finished page {i} / 2100")  # progress
    
    time.sleep(random.uniform(2, 4)) 


   

















