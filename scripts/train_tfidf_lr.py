"""CLI for training the TF-IDF + Logistic Regression baseline."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from sentiment_project.train_baseline import train_tfidf_logistic_regression


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train a TF-IDF + Logistic Regression sentiment baseline."
    )
    parser.add_argument("--train-path", required=True, help="Path to train_dataset.csv")
    parser.add_argument("--test-path", required=True, help="Path to test_dataset.csv")
    parser.add_argument("--output-dir", default="outputs/baseline_lr")
    parser.add_argument("--max-features", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    metrics = train_tfidf_logistic_regression(
        train_path=args.train_path,
        test_path=args.test_path,
        output_dir=args.output_dir,
        max_features=args.max_features,
    )
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(metrics["classification_report"])


if __name__ == "__main__":
    main()
