import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def get_search_results(query, num_results=10):
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://www.google.com/search?q={query}&num={num_results}"
    response = requests.get(search_url, headers=headers)
    response.raise_for_status()
    return response.text

def extract_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and '/url?q=' in href:
            parsed_url = urlparse(href)
            url = parse_qs(parsed_url.query).get('q')
            if url:
                urls.append(url[0])
    return urls

def main():
    keyword = input("Enter the keyword to search for: ")
    html_content = get_search_results(keyword)
    urls = extract_urls(html_content)
    print("\nURLs found:")
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()
