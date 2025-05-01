import requests
from bs4 import BeautifulSoup
import lxml
import csv
import re
import time
import random

def web_scraping(url,file_name):
    
    print("Thank you sharing the url and file name!\n Reading the content")
    
    num = random.randint(3,7)
    
    time.sleep(num)
    
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}
    
    response = requests.get(url, headers=header)
    
    if response.status_code == 200:

        html_content = response.text
        
        soup = BeautifulSoup(html_content, "lxml")
        
        hotel_divs = soup.find_all("div", role="listitem")
        
        with open(f"{file_name}.csv", 'w', encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)
            
            writer.writerow(['hotel_name', 'location', 'hotel_price', 'rating', 'rating_score', 'review', 'link'])
        
            for hotel in hotel_divs:
                
                hotel_name = hotel.find("div", class_="b87c397a13 a3e0b4ffd1")
                hotel_name = hotel_name.text.strip() if hotel_name else "None"
                
                location = hotel.find("span", class_="d823fbbeed f9b3563dd4")
                location = location.text.strip() if location else "None"
                
                hotel_price = hotel.find("span", class_="b87c397a13 f2f358d1de ab607752a2")
                if hotel_price:
                    hotel_price = hotel_price.text.strip()
                    hotel_price = re.sub(r'[^\d.]', '', hotel_price) 
                else:
                    hotel_price = "None"
                
                rating = hotel.find("div", class_="f63b14ab7a f546354b44 becbee2f63")
                rating = rating.text.strip() if rating else "None"
                
                rating_score = hotel.find("div", class_="f63b14ab7a dff2e52086")
                rating_score = rating_score.text.strip() if rating_score else "None"
                
                review = hotel.find("div", class_="fff1944c52 fb14de7f14 eaa8455879")
                review = review.text.strip() if review else "None"
                
                link = hotel.find("a", href=True)
                link = link.get('href') if link else "None"
                            
                writer.writerow([hotel_name, location, hotel_price, rating, rating_score, review, link])
            
    else:
        print(f"Connection Failed! Status Code: {response.status_code}")
        
        
if __name__ == '__main__':
    url = input("Please Enter website url : ")
    file_name = input("Please give file name : ")
    
    web_scraping(url,file_name)