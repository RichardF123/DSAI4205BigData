"""Data loading helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from sentiment_project.labels import normalize_label


def load_sentiment_csv(
    path: str | Path,
    text_col: str = "text",
    label_col: str = "text_sentiment",
) -> tuple[pd.Series, pd.Series]:
    """Load a sentiment CSV file and return text and normalized labels."""

    df = pd.read_csv(path)
    missing = {text_col, label_col} - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    texts = df[text_col].fillna("").astype(str)
    labels = df[label_col].apply(normalize_label)
    return texts, labels
