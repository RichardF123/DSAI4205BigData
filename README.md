# DSAI4205 Big Data Project - English Text Sentiment Classification

This repository contains complete code, model weights, and experimental records for English text 3-class sentiment classification.

## Task Description
- **3-Class Sentiment Analysis**:
  - `-1`: Negative
  - `0`: Neutral
  - `1`: Positive

## Models Included
This project implements a wide range of machine learning and deep learning models:

### 1. Traditional Machine Learning Models
- Logistic Regression (LR)
- XGBoost

### 2. Advanced Two-Stage / Hybrid Ensemble Models
- Multiple secondary composite classification models
- Multi-model fusion & cascade structures

### 3. Deep Learning & Pre-trained Language Models
- BERT (full fine-tuning)
- DistilBERT (lightweight fine-tuning)
- BERTweet
- Qwen1.5
- LoRA fine-tuning (single-stage & two-stage)

## Best Performance
- **Overall Accuracy**: 0.8967
- Positive class: Precision = 1.0, Recall = 1.0, F1 = 1.0

## Repository Structure
- `*.ipynb`: Complete training, fine-tuning, inference, and evaluation code
- Model folders: Trained weights, tokenizers, and configuration files
- All experiments: Traditional ML, deep learning, fine-tuning, and ensemble models

## How to Use
1. Clone the repository
2. Open the `.ipynb` notebook in Google Colab
3. Run cells for training, fine-tuning, or inference

## Course
DSAI4205 Big Data

## Author
RichardF123

