# def test_nltk():
#     import langchain.text_splitter as splitters
#     splitter = splitters.NLTKTextSplitter()
#     # splitter.split_text()


url = 'https://www.sbert.net/examples/applications/retrieve_rerank/README.html'

# url = 'https://www.foxnews.com/us/kansas-city-chiefs-fans-deaths-drugs-freezing-weather-could-have-created-lethal-conditions-experts-say'
url = 'https://vladmihalcea.com/jpa-entity-graph/'
url = 'https://www.atomicjar.com/2023/10/beyond-pass-fail-a-modern-approach-to-java-integration-testing/'
url = 'https://www.kdnuggets.com/sql-simplified-crafting-modular-and-understandable-queries-with-ctes'

#TODO test contentextractor.py
#TODO use nltk to chunk the text and embed it then mean pool the embeddings
def test_readability():
    import requests
    import readability

    # Fetch the HTML content of the URL
    response = requests.get(url)
    html: bytes = response.content

    # Parse the HTML using readability
    document = readability.Document(html)

    # Extract the main content
    title: str = document.title()
    summary: str = document.summary(html_partial=True)

    # Convert HTML summary to plain text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(summary, 'html.parser')
    clean_text = soup.get_text(separator='\n')
    print("Clean Text:", clean_text)
    print("Title:", title)


    import langchain.text_splitter as splitters
    import nltk

    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')

    splitter = splitters.NLTKTextSplitter(chunk_size=2048, chunk_overlap=256)
    sentences = splitter.split_text(clean_text)
    print("SENTENCES")
    print(sentences)
    # from nltk.tokenize import sent_tokenize
    # import nltk
    # nltk.download('punkt')
    # sentences: list[str] = sent_tokenize(summary)