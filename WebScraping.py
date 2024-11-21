import requests
from bs4 import BeautifulSoup

# Target URL to scrape
url = 'https://rajeev.pythonanywhere.com'  # Replace with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract and print all headings (h1 tags)
    headings = soup.find_all('h1')
    print("Headings:")
    for heading in headings:
        print(heading.text.strip())

    # Example: Extract and print all paragraph texts
    paragraphs = soup.find_all('p')
    print("\nParagraphs:")
    for paragraph in paragraphs:
        print(paragraph.text.strip())

    # Example: Extract and print all links
    links = soup.find_all('a', href=True)
    print("\nLinks:")
    for link in links:
        print(f"{link.text.strip()} - {link['href']}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
