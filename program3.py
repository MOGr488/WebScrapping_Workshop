import requests
from bs4 import BeautifulSoup

def get_hacker_news_blog_posts():
    # Send a GET request to the Hacker News website
    url = 'https://thehackernews.com'
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the divs with class 'body-post'
        body_posts = soup.find_all('div', class_='body-post')
        # Iterate through each body-post div
        for body_post in body_posts:
            # Find the h2 tag with class 'home-title' within each body-post div
            home_title_tag = body_post.find('h2', class_='home-title')
            home_desc_tag = body_post.find('div', class_='home-desc')
            # Extract and print the text content of the h2 tag
            if home_title_tag:
                home_title = home_title_tag.text.strip()
                home_desc = home_desc_tag.text.strip()
                print(f'Blog Title: {home_title}\n')
                print(f'Description: {home_desc}\n')
            else:
                print('Error: Home title not found in the current body-post div.')

    else:
        print(f'Error: Unable to fetch the page. Status code: {response.status_code}')

if __name__ == '__main__':
    get_hacker_news_blog_posts()
