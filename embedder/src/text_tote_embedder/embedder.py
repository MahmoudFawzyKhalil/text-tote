from sentence_transformers import SentenceTransformer
from torch import Tensor

# https://www.sbert.net/examples/applications/semantic-search/README.html#symmetric-vs-asymmetric-semantic-search
# Model chosen because our queries are asymmetric queries
MODEL_NAME = 'msmarco-MiniLM-L-6-v3'
VECTOR_SIZE = 384

model = None


def lazy_load_model() -> SentenceTransformer:
    global model
    if not model:
        model = SentenceTransformer(MODEL_NAME)
    return model


def embed(sentences: str | list[str], show_progress_bar: bool = False) -> list[Tensor]:
    return lazy_load_model().encode(sentences, show_progress_bar=show_progress_bar)
