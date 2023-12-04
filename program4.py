import requests
from bs4 import BeautifulSoup

# URL of the page
url = "https://thehackernews.com"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the "Next Page" link
    next_page_link = soup.find("a", class_="blog-pager-older-link-mobile")
    print("Next Page Link Type ", type(next_page_link))
    # Check if the link is found
    if next_page_link:
        print("Next Button Found")
        # Extract the URL of the next page
        next_page_url = next_page_link["href"]

        # Print or use the next page URL as needed
        print("Next Page URL:", next_page_url)
    else:
        print("No 'Next Page' link found on the current page.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
