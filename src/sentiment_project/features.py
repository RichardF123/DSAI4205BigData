"""Feature extraction utilities."""

from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer


def build_tfidf_vectorizer(
    max_features: int = 5000,
    ngram_range: tuple[int, int] = (1, 2),
) -> TfidfVectorizer:
    """Create the default TF-IDF vectorizer used by baseline models."""

    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        stop_words="english",
    )
