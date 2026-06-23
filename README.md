# DSAI4205 Big Data Project - English Text Sentiment Classification

This repository contains experiments and reusable code for English 3-class
sentiment classification.

The task is to classify each text sample as:

| Label | Meaning |
| --- | --- |
| `-1` | Negative |
| `0` | Neutral |
| `1` | Positive |

## Project Highlights

- Traditional machine learning baselines with TF-IDF features.
- XGBoost and Random Forest experiments.
- Transformer fine-tuning experiments with BERT, DistilBERT, BERTweet, Qwen1.5,
  and LoRA adapters.
- Best recorded overall accuracy: **0.8967**.

## Recommended Repository Structure

```text
DSAI4205BigData/
  README.md
  requirements.txt
  .gitignore
  src/
    sentiment_project/
      __init__.py
      labels.py
      data.py
      features.py
      train_baseline.py
      evaluate.py
      predict.py
  scripts/
    train_tfidf_lr.py
  notebooks/
    4205PROJECT_MODEL_TRAIN.ipynb
  data/
    .gitkeep
  outputs/
    .gitkeep
  models/
    README.md
  docs/
    PROJECT_STRUCTURE.md
```

The current notebooks and generated training script are kept as experiment
records. New reusable code should go under `src/sentiment_project/`.

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Data

Place course datasets under `data/`:

```text
data/
  train_dataset.csv
  test_dataset.csv
```

Expected columns:

- `text`: input text
- `text_sentiment`: sentiment label, such as `negative`, `neutral`,
  `positive`, `-1`, `0`, or `1`

Large datasets should not be committed to GitHub. Keep them local or document
where to download them.

## Train A Baseline Model

Train a TF-IDF + Logistic Regression baseline:

```bash
python scripts/train_tfidf_lr.py ^
  --train-path data/train_dataset.csv ^
  --test-path data/test_dataset.csv ^
  --output-dir outputs/baseline_lr
```

The script saves:

- `outputs/baseline_lr/model.joblib`
- `outputs/baseline_lr/vectorizer.joblib`
- `outputs/baseline_lr/metrics.json`
- `outputs/baseline_lr/classification_report.txt`

## Existing Experiment Artifacts

The repository currently includes model folders such as:

- `bertweet_3class*`
- `lora_stage*`
- `qwen15_3class*`
- `models/`
- `results/`

These are preserved as experiment artifacts. For a cleaner long-term GitHub
portfolio, consider moving large checkpoints to GitHub Releases, Google Drive,
Hugging Face Hub, or another artifact store, then keeping only links and
metadata in the repository.

## Course

DSAI4205 Big Data

## Author

RichardF123
