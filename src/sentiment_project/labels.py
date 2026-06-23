"""Label normalization utilities for 3-class sentiment classification."""

from __future__ import annotations


LABEL_TO_ID = {
    "negative": 0,
    "-1": 0,
    "neutral": 1,
    "0": 1,
    "positive": 2,
    "1": 2,
}

ID_TO_LABEL = {
    0: "negative",
    1: "neutral",
    2: "positive",
}


def normalize_label(value: object) -> int:
    """Map text or numeric sentiment labels to integer class ids.

    The project uses three classes:
    0 = negative, 1 = neutral, 2 = positive.
    Unknown labels default to neutral because it is the least extreme class.
    """

    key = str(value).strip().lower()
    return LABEL_TO_ID.get(key, 1)
