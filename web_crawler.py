import requests
from bs4 import BeautifulSoup

def web_crawler(seed_url):
    visited_urls = set()
    queue = [seed_url]

    while queue:
        # Get the next URL from the queue
        current_url = queue.pop(0)

        # Skip if URL has already been visited
        if current_url in visited_urls:
            continue

        try:
            # Send a GET request to the current URL
            response = requests.get(current_url)

            # Add the URL to the set of visited URLs
            visited_urls.add(current_url)

            # Process the web page content
            process_web_page(response.text)

            # Extract links from the web page
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')

            # Add new URLs to the queue
            for link in links:
                new_url = link.get('href')
                if new_url and new_url not in visited_urls:
                    queue.append(new_url)

        except requests.exceptions.RequestException:
            # Handle any errors that occurred while fetching the URL
            print(f"Error occurred while fetching URL: {current_url}")

def process_web_page(html_content):
    # Do something with the web page content
    # You can parse the HTML content or extract information here
    # This function can be customized based on your specific needs
    # For example, you can save the content to a file or perform data extraction

    # Example: Print the length of the HTML content
    print(f"Web page content length: {len(html_content)}")

# Usage example
seed_url = 'https://example.com'
web_crawler(seed_url)
