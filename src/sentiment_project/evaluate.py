"""Evaluation helpers for sentiment classification."""

from __future__ import annotations

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def classification_metrics(y_true, y_pred) -> dict:
    """Return common classification metrics in a serializable dictionary."""

    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "classification_report": classification_report(y_true, y_pred, digits=4),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }
