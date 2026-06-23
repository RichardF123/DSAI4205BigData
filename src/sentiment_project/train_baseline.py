"""Training entry points for traditional ML baselines."""

from __future__ import annotations

import json
from pathlib import Path

import joblib
from sklearn.linear_model import LogisticRegression

from sentiment_project.data import load_sentiment_csv
from sentiment_project.evaluate import classification_metrics
from sentiment_project.features import build_tfidf_vectorizer


def train_tfidf_logistic_regression(
    train_path: str | Path,
    test_path: str | Path,
    output_dir: str | Path,
    max_features: int = 5000,
) -> dict:
    """Train and evaluate a TF-IDF + Logistic Regression baseline."""

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train_text, train_label = load_sentiment_csv(train_path)
    test_text, test_label = load_sentiment_csv(test_path)

    vectorizer = build_tfidf_vectorizer(max_features=max_features)
    x_train = vectorizer.fit_transform(train_text)
    x_test = vectorizer.transform(test_text)

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(x_train, train_label)

    y_pred = model.predict(x_test)
    metrics = classification_metrics(test_label, y_pred)

    joblib.dump(model, output_dir / "model.joblib")
    joblib.dump(vectorizer, output_dir / "vectorizer.joblib")
    (output_dir / "metrics.json").write_text(
        json.dumps(metrics, indent=2),
        encoding="utf-8",
    )
    (output_dir / "classification_report.txt").write_text(
        metrics["classification_report"],
        encoding="utf-8",
    )
    return metrics
