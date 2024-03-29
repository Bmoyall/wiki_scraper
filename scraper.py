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
    image_url = soup.find('img', {'alt': 'Lionel Messi'})['src']
    image_url = re.sub(r'//', 'https://', image_url)
    
    # Save the image
    image_response = requests.get(image_url)
    with open('image.jpg', 'wb') as f:
        f.write(image_response.content)
    
    # Define the HTML template for the personal information and image
    html_template = '''
    <html>
      <head>
        <title>Lionel Messi</title>
        <style>
          .personal-info {{
            margin: 0 auto;
            width: 50%;
          }}
        </style>
      </head>
      <body>
        <div class="personal-info">
          {}
            <div class="image">
                <img src="image.jpg">
            </div>
        </div>
      </body>
    </html>
    '''
    
    # Format the HTML template with the personal information
    # Save the formatted HTML to a file
    with open('index.html', 'w', encoding = 'utf-8') as f:
        f.write(html_template.format(personal_info))

scrape_personal_info()
