import requests
from bs4 import BeautifulSoup
import os

os.makedirs('output', exist_ok=True)
os.makedirs('output/images', exist_ok=True)

def extract_content_from_html(html_content):
    """
    Extracts the text content from the <p class="c_d"> tag.
    
    Parameters:
    - html_content (str): The HTML content to extract data from.
    
    Returns:
    - str: The extracted text content.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    p_tag = soup.find('p', class_='c_d')

    return p_tag.get_text(strip=True) if p_tag else "No content in <p class='c_d'>"

def download_image(image_url, article_title):
    """Downloads an image and saves it in output/images/."""
    if not image_url:
        return None

    image_name = f"{article_title.replace(' ', '_')}.jpg" 
    image_path = os.path.join('output/images', image_name)

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return image_path
        else:
            print(f"Failed to download {image_url} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")

    return None

def fetch_articles():
    url = 'https://elpais.com/opinion/'
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        raise Exception("Failed to retrieve webpage")

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')[:5] 

    article_data = []

    with open('output/spanish_titles_and_content.txt', 'w', encoding='utf-8') as f:
        for article in articles:
            title = article.find('h2').get_text(strip=True) if article.find('h2') else 'No title'

            article_link = article.find('a')['href'] if article.find('a') else None

            img_tag = article.find('img')
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

            image_path = download_image(img_url, title) if img_url else "No image"

            content = extract_content_from_html(response.text)

            if content and content != "No content in <p class='c_d'>":
                f.write(f"Title: {title}\n")
                f.write(f"Content: {content}\n")
                f.write(f"Image: {image_path}\n")
                f.write("\n" + "-"*80 + "\n")

            article_data.append((title, content, image_path))

    return article_data

fetch_articles()
