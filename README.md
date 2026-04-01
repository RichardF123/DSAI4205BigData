[DSAI4205BigData - English Text 3-Class Sentiment Classification.md](https://github.com/user-attachments/files/26415975/DSAI4205BigData.-.English.Text.3-Class.Sentiment.Classification.md)
# DSAI4205BigData - English Text 3-Class Sentiment Classification

This repository contains trained models and Colab notebook code for English text 3-class sentiment classification, developed for the DSAI4205 Big Data course project.

## 📋 Project Overview

- **Task**: 3-class sentiment classification of English text

- **Sentiment Labels**: 
        

    - -1: Negative Sentiment

    - 0: Neutral Sentiment

    - 1: Positive Sentiment

- **Best Model Accuracy**: 0.8967

- **Key Highlight**: Positive sample recall, precision, and F1-score all reach 1.000 (no misclassification)

## 📂 Repository Content

1. **Trained Models**: Multiple versions of sentiment classification models, including:
        

    - BERTweet Series: `bertweet_3class`, `bertweet_3class_final`, `bertweet_3class_tokenizer`

    - LoRA Series (single-stage & two-stage): `lora_stage1`, `lora_stage2`, and related optimized versions

    - Qwen1.5 Series: `qwen15_3class`, `qwen15_3class_final`, `qwen15_3class_tokenizer`

2. **Code**: Colab notebook (.ipynb) containing full training, optimization, and inference code

## 📊 Model Performance

|Sentiment Class|Precision|Recall|F1-Score|
|---|---|---|---|
|Negative (-1)|0.856|0.830|0.843|
|Neutral (0)|0.835|0.860|0.847|
|Positive (1)|1.000|1.000|1.000|
|**Overall**|**0.897**|**0.897**|**0.897**|
## 🚀 How to Use

1. Clone this repository:
`git clone https://github.com/RichardF123/DSAI4205BigData.git`

2. Open the Colab notebook (.ipynb) in Google Colab to view/run the full code.

3. Use the trained models for inference directly in the notebook.

## 📝 Notes

- All models are trained for English text sentiment classification only.

- The Colab notebook includes the complete workflow: data preprocessing, model training, multi-round optimization, and performance evaluation.

- Model weights and tokenizers are stored in their respective folders for direct use.

## 👤 Maintainer

RichardF123

Project for DSAI4205 Big Data Course
> （注：文档部分内容可能由 AI 生成）
