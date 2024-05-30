import approvaltests

from text_tote_embedder.cli import request_service


def test_retrieves_content():
    # Arrange
    url = 'https://en.wikipedia.org/wiki/Java_(programming_language)'

    # Act
    content: bytes = request_service.get(url)

    # Assert
    approvaltests.verify(content)


def test_fails_when_status_code_is_not_200():
    # Arrange
    url = 'https://en.wikipedia.org/wiki/Non-existent-page'

    # Act
    try:
        request_service.get(url)
    except Exception as e:
        # Assert
        approvaltests.verify(e)
