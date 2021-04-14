# 1. Table Of Contents

- [1. Table Of Contents](#1-table-of-contents)
- [2. Getting Started](#2-getting-started)
  - [2.1. Installing Requirements](#21-installing-requirements)
  - [2.2. Running the Code](#22-running-code)
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
  - [9.1. Example Data](#91-example-data)
  - [9.2. Sample Dataset & Results](#92-sample-dataset-results)
- [10. Alternative Methods Tried](#10-alternative-methods-tried)
- [11. Extra Resources](#11-extra-resources)
  - [11.1. EDA](#111-eda)
  - [11.2. Sentiment Analysis Tools](#112-sentiment-analysis-tools)
  - [11.3. Presentations](#113-presentations)

# 2. Getting Started

## 2.1. Installing Requirements

Before installing, if you can, make a python 3.7 virtual environment and activate it
(for help see [official docs](https://docs.python.org/3/tutorial/venv.html)).
Then you can run the following command to install all python requirements for the scripts.

```
pip install -r requirements.txt
```

If you have a GPU, you should follow the
[official pytorch installation instructions](https://pytorch.org/get-started/locally/)
and `pip install` each requirement individually.

## 2.2. Running Code

### 2.2.1. Docker Instructions

We recommend running the following scripts and notebooks using Docker.
First, open a terminal window and navigate to the project directory.
From there, you need to build the Docker image by running `docker build -t <image-name> .`.
You can name the image whatever you like.

Then you can run the image as a Docker container by executing `docker run -it <image-name> bash`.
This will allow you to access the container in the interactive mode so you can run the scripts and notebooks by using the instructions above.

### 2.2.2. Notebooks

In the `notebooks` folder, you can run the cells of the notebooks in jupyter notebook.
Make sure `jupyter` is installed with `pip install jupyter`.
To run jupyter, run `jupyter notebook` and follow the printed instruction to launch a browser window.

### 2.2.3. Scripts

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

# 5. Why this tool is needed

# 6. Goal

## 6.1. Current State

## 6.2. Future

# 7. Big Overview of Tool

# 8. The Pipeline

## 8.1. CSV Inputs, Outputs

## 8.2. Cleaning Data

## 8.3. Pre-trained Models

## 8.4. Analyzing/Categorizing Results

# 9. Dataset and Sample Results

## 9.1. Example Data

## 9.2. Sample Dataset & Results

# 10. Alternative Methods Tried

# 11. Extra Resources

## 11.1. EDA

## 11.2. Sentiment Analysis Tools

## 11.3. Presentations
