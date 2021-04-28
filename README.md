# 1. Table Of Contents

- [1. Table Of Contents](#1-table-of-contents)
- [2. Getting Started - Running the Code](#2-getting-started---running-the-code)
  - [2.1. Docker Instructions](#21-docker-instructions)
  - [2.2. Notebooks](#22-notebooks)
  - [2.3. Scripts](#23-scripts)
- [3. Input File Requirements](#3-input-file-requirements)
- [4. EPIK Project SMS Sentiment Analysis](#4-epik-project-sms-sentiment-analysis)
- [5. Why this tool is needed](#5-why-this-tool-is-needed)
- [6. Project Scope](#6-project-scope)
  - [6.1. Current State](#61-current-state)
  - [6.2. Future](#62-future)
- [7. Big Overview of Tool](#7-big-overview-of-tool)
- [8. The Pipeline](#8-the-pipeline)
  - [8.1. Cleaning Data](#81-cleaning-data)
  - [8.2. Analyzing/Categorizing Results](#82-analyzingcategorizing-results)
- [9. Dataset and Sample Results](#9-dataset-and-sample-results)
- [10. Alternative Methods Tried](#10-alternative-methods-tried)
  - [10.1. Watson NLU](#101-watson-nlu)
  - [10.2. NRCLex](#102-nrclex)
  - [10.3. Roberta](#103-roberta)
  - [10.4. T5](#104-t5)
- [11 Final Analysis](#11-final-analysis)
  - [11.1 Scripted Data](#111-data-overview)
  - [11.2 Graphs](#112-graphs)
  - [11.3 Results Analysis](#113-results-analysis)
- [12. Extra Resources](#12-extra-resources)
  - [12.1. EDA](#121-eda)
  - [12.2. Sentiment Analysis Tools](#122-sentiment-analysis-tools)
  - [12.3. Presentations](#123-presentations)

# 2. Getting Started - Running the Code

## 2.1. Docker Instructions

We recommend running the following scripts and notebooks using Docker.
First, open a terminal window and navigate to the project directory.
From there, you need to build the Docker image by running `docker build -t <image-name> .`.
You can name the image whatever you like.

Then you can run the image as a Docker container by executing `docker run -it -p 8888:8888 <image-name> bash`.
This will allow you to access the container in the interactive mode so you can run the scripts and notebooks by using the instructions below.

## 2.2. Notebooks

In the `notebooks` folder, you can run the cells of the notebooks in jupyter notebook.
Make sure `jupyter` is installed with `pip install jupyter`.
To run jupyter, run `jupyter notebook` and follow the printed instruction to launch a browser window.

## 2.3. Scripts

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

Input requirements to the script are as followed:
CSV file with a column for text labeled "text"

# 4. EPIK Project SMS Sentiment Analysis

This project is conducted in conjuction with EPIK and utilizes ML to analyze text conversations between volunteers at EPIK and responders to their fake ads.

EPIK is a nonprofit working to mobilize male allies in disrupting the commercial sex market by equipping them with the knowledge to combat the roots of exploitation and encouraging them to collaborate effectively with the wider anti-trafficking movement.

# 5. Why this tool is needed

With EPIK's recent shift in approach from scripted to unscripted volunteer conversations, in addition to their longtime policy of a non shaming approach to buyers, the organization needed some research into their methods to determine efficiency. This tool provides the necessary feedback on their methods by conducting analysis on the communication style of the volunteers and the conversation between volunteers and buyers as a whole.

# 6. Project Scope

## 6.1. Current State

This tool currently relies on pre-trained models to provide the sentiment analysis on the conversations between volunteers and buyers. The analysis is run using scripts that take in csv files containing the SMS messages provided by EPIK. The scripts then analyze the sentiment results and output stats providing a general idea of how volunteers are doing.

## 6.2. Future

Future partners with EPIK could springboard off the work done in this project and build a ML classifier specific to EPIK's needs. While the pre-trained models provided a wide range of emotional analysis, they can be very general. Building an ML classfier from scratch would allow for a more tailored analysis fitted to EPIK's four emotional disposition quadrents and other organization specific terms. They may also want to take advantage of the stipends provided by Spark! in helping to build this ML classifier and in obtaining labelled data fitted to EPIK's needs.

# 7. Big Overview of Tool

The final output of our project will be the following: a script that will give an emotional rating of the emotions for go_emotion and rating of accountability from the labeled data from Justin. This tool will be used to compare ratings between scripted vs. unscripted, conversations (breaking down by volunteer and buyer as well), and by patrol unit.

# 8. The Pipeline

## 8.1. Cleaning Data

The data was cleaned at multiple different points. First the data was [Cleaned](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/cleaning.ipynb)
to organize the entire data set by conversation. From there, each conversation is in chronological order of when the messages where sent. After this, all of the null text messages where removed from the dataset as well.

From the calender data we received from Justin, we labeled each conversation thread with which unit was on call during the time of the [conversation](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/cleaned_patrols.csv).

Once we got the labeled data from Justin, we also cleaned the labels to be set up to go into our [models](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/labeled_data.ipynb). At this point we made each label consistent throughout in terms of spelling and capitalization.

## 8.2. Analyzing/Categorizing Results

The first step of analyzing the data was to run the pre-trained sentiment analysis model on the newly cleaned data. GoEmotion Bert, our pre-trained model of choice, returned the emotions detected within each individual message (from the 27 emotions + neutral labelled options they offered).

From the sentiment analysis, we then worked with Justin to add the label for "accountability", by working through a sample of 1000 rows of data to relabel texts Justin felt fulfilled the label "accountability'.

Finally, we went through the resulting data and analyzed the general sentiment of convesations as a whole, for the volunteer side of conversations, and for the buyer side of conversations.

# 9. Dataset and Sample Results

In our data folder, we have the following data sets avalible:

- [sorted_new.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/sorted_new.csv) - Dataset with all entries from Epik_2019A-Epik_2021A organized by conversation

- [patrol_data.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/patrol_data.csv) - the sorted_new data set with the patrol data appended

- [evaluation_volunteer_text_1000.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/evaluation_volunteer_text_1000.csv) - the random 1000 entries from sorted_new used to test each of our potential model options

- [t5_emotion_volunteer_1000.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/t5_emotion_volunteer_1000.csv) - the output of T5 on the random 1000 entries used for testing

- [goemotion_bert_volunteer_1000.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/goemotion_bert_volunteer_1000.csv) - the output of goemotion on the random 1000 entries used for testing

- [twiter_roberta_volunteer_1000.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/twiter_roberta_volunteer_1000.csv) - the output of Twitter Roberta on the random 1000 entries used for testing

- [watson_labeled.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/watson_labeled.csv) - the output of Watson NLU on the random 1000 entries used for testing

- [labeled_data_1000.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/labeled_data_1000.csv) - the cleaned and normalized version of Justin's responses of the random 1000 entries used for testing

- [feedback_goemotion.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/feedback_goemotion.csv) - the raw and uncleaned version of Justin's responses of the random 1000 entries used for testing

- [unique_messages.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/unique_messages.csv) - sorted_new with a column to identify if the text was from a script or not

- [test.csv](https://github.com/realmanisingh/epik-project-nlp/blob/main/data/test.csv) - sample output of our script

# 10. Alternative Methods Tried

All the links to these tools will be provided in [12.2. Sentiment Analysis Tools](#122-sentiment-analysis-tools)

The decision to used go_emotion also was influence by the comparisons between models in [compare_models.ipynb](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/compare_models.ipynb)

## 10.1. Watson NLU

Watson NLU gave a rating value for each of the following emotions: joy, anger, sadness, fear, disgust, positive, negative, neutral. We decided not to use this tool for our final analysis for the following reasons:

- it required longer text strings then many of the messages we were working with
- less emotion coverage than goemotion
- less accurate from our preliminary

## 10.2. NRCLex

NRCLex gave a rating value for each of the following emotions: joy, anger, sadness, fear, disgust, surprise, trust. We decided not to use this tool for our final analysis for the following reasons:

- it required longer text strings then many of the messages we were working with
- the frequency count made it confusing to use for analysis
- less accurate from our preliminary

## 10.3. Roberta

Roberta gave a rating value for each of the following emotions: joy, anger, sadness, optimism. We decided not to use this tool for our final analysis for the following reasons:

- the classifications for emotion only covered a small subset of possible emotions
- no neutral option
- less accurate from our preliminary

## 10.4. T5

T5 gave a rating value for each of the following emotions: joy, anger, sadness, fear, surprise, love, other. We decided not to use this tool for our final analysis for the following reasons:

- very biased for short texts
- no neutral option
- the classifications for emotion only covered a small subset of possible emotions
- less accurate from our preliminary

# 11 Final Analysis

## 11.1 Data Overview

From the set of 154,990 messages:

- 69,417 volunteer data points
- 84,573 buyer data points
- 3,203 are scripted
- 29,082 different conversations

## 11.2 Graphs

Descriptions for all the graphs in the graphs folder:

[freq_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/freq_preds.jpg): a large majority of instances are classified as "neutral" followed by "curiosity".

[mean_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/mean_preds.jpg): almost all emotion labels have mean scores greater than 0.4 with many greater than 0.7.

[occurs_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/occurs_preds.jpg): a large majority of instances are assigned one label.

[total_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/total_preds.jpg): from the instances that are assigned one label, a majority of them are "neutral".

[buyer_freq_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/buyer_freq_preds.jpg): examining the buyer side of the conversations, a large majority of instances are classified as "neutral" followed by "curiosity".

[buyer_mean_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/buyer_mean_preds.jpg): examining the buyer side of the conversations, almost all emotion labels have mean scores greater than 0.4 with many greater than 0.6.

[buyer_total_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/buyer_total_preds.jpg): examining the buyer side of the conversations, the majority were assigned only one emotion label.

[volunteer_freq_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/volunteer_freq_preds.jpg): examining the volunteer side of the conversations, a large majority of instances are classified as "neutral" followed by "curiosity".

[volunteer_mean_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/volunteer_mean_preds.jpg): examining the volunteer side of the conversations, almost all emotion labels have mean scores greater than 0.4 with many greater than 0.6.

[volunteer_total_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/volunteer_total_preds.jpg): examining the volunteer side of the conversations, the majority were assigned only one emotion label.

[script_freq_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/script_freq_preds.jpg): examining the scripted messages in the conversations, they showed the least variety in emotion, with a large majority of instances classified as "angry" followed by "curiosity" then "neutral".

[script_mean_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/script_mean_preds.jpg): examining the scripted messages in the conversations, almost all emotion labels have mean scores greater than 0.4 with many greater than 0.6.

[script_total_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/script_total_preds.jpg): examining the scripted messages in the conversations, the majority were assigned only one emotion label.

[unique_freq_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/unique_freq_preds.jpg): examining the unique, unscripted messages in the conversations, a large majority of instances are classified as "neutral" followed by "curiosity".

[unique_mean_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/unique_mean_preds.jpg): examining the unique, unscripted messages in the conversations, almost all emotion labels have mean scores greater than 0.4 with many greater than 0.7.

[unique_total_preds.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/unique_total_preds.jpg): examining the unique, unscripted messages in the conversations, the majority were assigned only one emotion label.

[city analysis](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/patrol_analysis.ipynb): see here for the graphs detailing the frequency of emotion labels, the mean score of emotion labels, and most common number of emotion labels for each city patrol.

## 11.3 Results Analysis

The scripted language is detected overwhelmingly higher on anger. This provides a stronger arguement towards getting away from that language.
Overall when an emotion was labeled, a strong majority of the time it was the only one labeled and had high confidence >.7.
The volunteers displayed a much higher degree of curiousity than the buyers.
Kansas City, Anchorage, Arizonia, Detroit, and Portland account for ~75% of messages.
San Antonio and Ancorchorage are the only patrols with anger in top 5.
All locations have the same emotional labels for the top 3 except Houston(their #4 is everyone elses #3).

# 12. Extra Resources

## 12.1. EDA

[monthly_scripted.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/monthly_scripted.jpg): the use of scripted messages decreased in 2021 to be around a quater of its use in 2019.

[patrol_activity.jpg](https://github.com/realmanisingh/epik-project-nlp/blob/main/graphs/patrol_activity.jpg): the Portland Patrol sent the most messages, followed by the Detroit Patrol then the Arizona Patrol.

[Volunteer Patrol Schedule EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/patrol_eda.ipynb): duration of the patrols in relation to each other, the number and average duration(counted by number of texts exchanged) of conversations conducted by the patrols in relation to each other.

[EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/eda.ipynb): general eda of the inital data given to us

[Sentiment EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/eda_sentiment.ipynb): Exploratory analysis of Roberta on the sample data set and analyzing the differences between volunteer and buyer text.

[Watson EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/watson_eda.ipynb): Exploratory analysis of the functioning of Watson NLU on the 1000 sample data set

[NRCLex EDA](https://github.com/realmanisingh/epik-project-nlp/blob/main/notebooks/sentiment_analysis.ipynb): Exploratory analysis of the functioning of NRCLex on the 1000 sample data set

## 12.2. Sentiment Analysis Tools

[Watson NLU](https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#analyze) - joy, anger, sadness, fear, disgust, positive, negative, neutral

[NRCLex](https://pypi.org/project/NRCLex/) - joy, anger, sadness, fear, disgust, surprise, trust

[Roberta](https://github.com/pytorch/fairseq/tree/master/examples/roberta) - joy, anger, sadness, optimism

[T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) - joy, anger, sadness, fear, surprise, love, other

[GoEmotion Bert](https://github.com/google-research/google-research/tree/master/goemotions) - 28 classes

## 12.3. Presentations

[Midterm](https://docs.google.com/presentation/d/1bsh7GIwzoliqG5u5qOp3M0s78mT2d3Bi201Olb0s6VE/edit?usp=sharing)

[Final](https://docs.google.com/presentation/d/1C67zqwiaVUveLbsmvFHEY0bG0NED_JZ4-AfquZnzqj4/edit#slide=id.gd518f7a43a_0_5)
