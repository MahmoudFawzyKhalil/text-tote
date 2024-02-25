import torch
from sentence_transformers import SentenceTransformer

from text_tote_embedder.configuration import config

model = None


def lazy_load_model() -> SentenceTransformer:
    global model
    if not model:
        model = SentenceTransformer(config.model_name)
    return model


def embed(text: str | list[str], show_progress_bar: bool = False) -> torch.Tensor:
    embedding = lazy_load_model().encode(text, show_progress_bar=show_progress_bar, convert_to_tensor=True)
    return embedding


def mean_pool(embeddings: torch.Tensor) -> torch.Tensor:
    return torch.mean(embeddings, dim=0)
