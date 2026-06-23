# Project Structure Guide

This document explains how to turn the original course experiment repository
into a maintainable Python/NLP project.

## Current Situation

The repository currently contains:

- Colab notebooks and exported Python code.
- Many trained checkpoint directories.
- Final adapter/tokenizer folders for different transformer experiments.
- A short README.

This is enough for preserving experiment history, but it is hard for another
person to understand how to install, run, train, and evaluate the project.

## Suggested Organization

```text
src/sentiment_project/
```

Reusable Python package code. Put data loading, label mapping, feature
extraction, training, evaluation, and prediction code here.

```text
scripts/
```

Command-line entry points. Scripts should be short and call functions from
`src/sentiment_project/`.

```text
notebooks/
```

Exploration and experiment notebooks. Notebooks are useful for research, but
they should not be the only way to run the project.

```text
data/
```

Local datasets. Large course datasets should stay out of Git and be documented
in the README.

```text
outputs/
```

Generated models, metrics, figures, and predictions.

```text
models/
```

Metadata or final lightweight artifacts. Large checkpoints are better stored in
GitHub Releases, Google Drive, Hugging Face Hub, or another artifact store.

## Cleanup Recommendations

1. Keep the existing notebooks as experiment records.
2. Move reusable code into `src/sentiment_project/`.
3. Move run commands into `scripts/`.
4. Add `requirements.txt` for reproducible installation.
5. Add `.gitignore` so local data, outputs, and future checkpoints do not bloat
   the repository.
6. Move very large historical checkpoint folders out of Git in a later cleanup
   PR. Do this carefully because deleting model artifacts changes what the repo
   can reproduce directly.

## Portfolio Version

For internship applications, the most readable version is:

- README with task, data format, model list, best result, and run commands.
- One clean baseline script that runs from command line.
- One notebook or report showing experiments.
- A clear result table.
- Links to large model weights instead of committing all checkpoints.
