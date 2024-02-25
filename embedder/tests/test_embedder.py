import approvaltests

from text_tote_embedder.embeddings import embedder


def test_correct_model_used():
    embedding = embedder.embed("Hello, world!", show_progress_bar=True)
    approvaltests.verify(embedding)


def test_mean_pools_two_embeddings_correctly():
    embeddings = embedder.embed(["Hello, world!", "Hey, world!"], show_progress_bar=True)
    mean = embedder.mean_pool(embeddings)
    approvaltests.verify(mean)