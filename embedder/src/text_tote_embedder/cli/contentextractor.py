"""
Extracts the main content of a URL (article or YouTube video) as stripped-down HTML and plain text.
"""

import requests
from readability import Document
from bs4 import BeautifulSoup

from dataclasses import dataclass

@dataclass
class Content:
    title: str
    summary: str
    clean_text: str
    html: str
    url: str
    source: str
    source_url: str
    source_name: str
    source_logo: str
    source_favicon: str
    source_description: str
    source_language: str
    source_country: str
    source_category: str
    source_subcategory: str
    source_published_date: str
    source_last_updated_date: str
    source_author: str
    source_author_url: str
    source_author_image: str
    source_author_bio: str
    source_author_location: str
    source_author_website: str
    source_author_social_links: str
    source_author_social_media: str
    source_author_social_media_platforms: str
    source_author_social_media_accounts: str
    source_author_social_media_accounts_urls: str
    source_author_social_media_accounts_platforms: str
#
def extract_content(url) -> Content:
#     """
#     Extracts the main content of a URL (article or YouTube video) as stripped-down HTML and plain text.
#
#     Args:
#         url (str): The URL to extract content from.
#
#     Returns:
#         tuple: A tuple containing the title and clean text summary of the URL content.
#     """

    url = 'https://www.kdnuggets.com/sql-simplified-crafting-modular-and-understandable-queries-with-ctes'

    # Fetch the HTML content of the URL
    response = requests.get(url)
    html = response.content

    # Parse the HTML using readability
    doc = Document(html)

    # Extract the main content
    title = doc.title()
    summary = doc.summary(html_partial=True)

    print()
    print("Title:", title)

    # Convert HTML summary to plain text

    soup = BeautifulSoup(summary, 'html.parser')
    clean_text = soup.get_text(separator='\n')
    print("Clean Text:", clean_text)
