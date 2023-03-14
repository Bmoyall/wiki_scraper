import requests
from bs4 import BeautifulSoup
import re

def scrape_personal_info():
    # Define the URL to scrape
    url = "https://en.wikipedia.org/wiki/Lionel_Messi"
    
    # Send an HTTP request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the personal information section
    personal_info = soup.find('table', {'class': 'infobox vcard'})
    
    # Extract the image URL
    image_url = soup.find('img', {'alt': 'Lionel-Messi-Argentina-2022-FIFA-World-Cup (cropped).jpg'})['src']
    image_url = re.sub(r'//', 'https://', image_url)
    
    # Save the image
    image_response = requests.get(image_url)
    with open('image.jpg', 'wb') as f:
        f.write(image_response.content)
    
    # Save the personal information to an HTML file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Lionel Messi</title>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write(str(personal_info))
        f.write('<br>\n')
        f.write('<img src="image.jpg">\n')
        f.write('</body>\n')
        f.write('</html>\n')
    
    # Print the personal information to the console
    print(personal_info)

scrape_personal_info()
