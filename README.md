# 1. Table Of Contents

- [1. Table Of Contents](#1-table-of-contents)
- [2. Getting Started](#2-getting-started)
  - [2.1. Installing Requirements](#21-installing-requirements)
  - [2.2. Running the Code](#22-running-code)
    - [2.2.1. Docker Instructions](#221-docker)
    - [2.2.2. Notebooks](#222-notebooks)
    - [2.2.3. Scripts](#223-scripts)
- [3. Input File Requirements](#3-input-file-requirements)
- [4. EPIK Project SMS Sentiment Analysis](#4-epik-project-sms-sentiment-analysis)
- [5. Why is this tool needed](#5-why-is-this-tool-needed)
- [6. End goal of this tool](#6-end-goal-of-this-tool)
  - [6.1. Current State](#61-current-state)
  - [6.2. Next Steps](#62-next-steps)
- [7. Big Overview of Tool](#7-big-overview-of-tool)
- [8. The Pipeline](#8-pipeline)
  - [8.1. CSV Inputs, Outputs](#81-csv)
  - [8.2. Cleaning Data](#82-cleaning)
  - [8.3. Pre-trained Models](#83-pretrained-models)
  - [8.4. Analyzing/Categorizing Results](#84-analyzing-results)
- [9. Dataset and Sample Results](#9-dataset-and-sample-results)
  - [9.1. Sample Dataset & Results](#91-sample-dataset-results)
- [10. Alternative Methods Tried](#10-alternative-methods-tried)
- [11. Extra Resources](#11-extra-resources)
  - [11.1. EDA](#111-eda)
  - [11.2. Sentiment Analysis Tools](#112-sentiment-analysis-tools)
  - [11.3. Presentations](#113-presentations)

# 2. Getting Started

## 2.1. Running the Code

## 2.2. Docker Instructions

We recommend running the following scripts and notebooks using Docker.
First, open a terminal window and navigate to the project directory.
From there, you need to build the Docker image by running `docker build -t <image-name> .`.
You can name the image whatever you like.

Then you can run the image as a Docker container by executing `docker run -it <image-name> bash`.
This will allow you to access the container in the interactive mode so you can run the scripts and notebooks by using the instructions above.

### 2.3. Notebooks

In the `notebooks` folder, you can run the cells of the notebooks in jupyter notebook.
Make sure `jupyter` is installed with `pip install jupyter`.
To run jupyter, run `jupyter notebook` and follow the printed instruction to launch a browser window.

### 2.4. Scripts

We have some python scripts in this repository that can be run.
First, you need to set your `PYTHONPATH` environment variable to this directory.
On Linux, you can do so with `export PYTHONPATH=$PYTHONPATH:$(pwd)`.
On Windows, `set "PYTHONPATH=%PYTHONPATH%;%cd%"`.

You can find python scripts in the `scripts` folder.  
For example, to use GoEmotionBert to classify texts, you can run

```
python scripts/classify_scores.py --model=goemotion-bert --task=emotion --eval-data=data/evaluation_volunteer_text_1000.csv --save-path=data/test.csv
```

# 3. Input File Requirements

CSV file formatting...

# 4. EPIK Project SMS Sentiment Analysis

This project is conducted in conjuction with EPIK and utilizes ML to analyze text conversations between volunteers at EPIK and responders to their fake ads.

EPIK is a nonprofit working to mobilize male allies in disrupting the commercial sex market by equipping them with the knowledge to combat the roots of exploitation and encouraging them to collaborate effectively with the wider anti-trafficking movement.

# 5. Why this tool is needed

With EPIK's recent shift in approach from scripted to unscripted volunteer conversations, in addition to their longtime policy of a non shaming approach to buyers, the organization needed some research into their methods to determine efficiency. This tool provides the necessary feedback on their methods by conducting analysis on the communication style of the volunteers and the conversation between volunteers and buyers as a whole.

# 6. Goal

## 6.1. Current State

scripts that can be run on conversation inputs and output informative stats on sentiment of conversations. Provide a general idea of how volunteers are doing.

## 6.2. Future

Build a ML classifier specific for EPIK's needs.

# 7. Big Overview of Tool

# 8. The Pipeline

## 8.1. CSV Inputs, Outputs

## 8.2. Cleaning Data

## 8.3. Pre-trained Models

## 8.4. Analyzing/Categorizing Results

analyzing most common sentiments, accuracy of sentiments, how well sentiments aligned with EPIK's 4 emotional dispositions

# 9. Dataset and Sample Results

Unfortunately, we are not able to provide the actual dataset. Instead, we've included a sample dataset below, along with the results from running it through our pipeline.

## 9.1. Sample Dataset & Results

# 10. Alternative Methods Tried

# 11. Extra Resources

## 11.1. EDA

[Sentiment EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/eda_sentiment.ipynb)

[Volunteer Patrol Schedule EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/patrol_eda.ipynb)

## 11.2. Sentiment Analysis Tools

[Watson NLU](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#analyze) - joy, anger, sadness, fear, disgust, positive, negative, neutral
[NRCLex](https://pypi.org/project/NRCLex/) - joy, anger, sadness, fear, disgust, surprise, trust
[Roberta](https://github.com/pytorch/fairseq/tree/master/examples/roberta) - joy, anger, sadness, optimism
[T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) - joy, anger, sadness, fear, surprise, love, other
[GoEmotion Bert](https://github.com/google-research/google-research/tree/master/goemotions) - 28 classes

## 11.3. Presentations

[Midterm](https://docs.google.com/presentation/d/1bsh7GIwzoliqG5u5qOp3M0s78mT2d3Bi201Olb0s6VE/edit?usp=sharing)
