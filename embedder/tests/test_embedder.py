import approvaltests

from src.text_tote_embedder import embedder


def test_correct_model_used():
    vector = embedder.embed("Hello, world!", show_progress_bar=True)
    approvaltests.verify(vector)
