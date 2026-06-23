"""Prediction helpers for saved baseline models."""

from __future__ import annotations

from pathlib import Path

import joblib

from sentiment_project.labels import ID_TO_LABEL


def load_baseline(output_dir: str | Path):
    """Load a saved sklearn model and vectorizer from an output directory."""

    output_dir = Path(output_dir)
    model = joblib.load(output_dir / "model.joblib")
    vectorizer = joblib.load(output_dir / "vectorizer.joblib")
    return model, vectorizer


def predict_texts(texts: list[str], output_dir: str | Path) -> list[str]:
    """Predict human-readable sentiment labels for raw text inputs."""

    model, vectorizer = load_baseline(output_dir)
    features = vectorizer.transform(texts)
    predictions = model.predict(features)
    return [ID_TO_LABEL[int(label)] for label in predictions]
