import argparse

import pandas as pd

import classifiers


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True, choices=['twitter-roberta', 't5', 'goemotion-bert'])
    parser.add_argument('--task', required=True, choices=['emotion', 'sentiment'])
    parser.add_argument('--eval-data', type=str, default='../data/evaluation_volunteer_text_1000.csv',
                        help='csv data to load. must have text column')
    parser.add_argument('--save-path', required=True, type=str, help='csv save path')
    args = parser.parse_args()
    return args


def get_classifier(args) -> classifiers.Classifier:
    if args.model == 'twitter-roberta':
        if args.task == 'emotion':
            return classifiers.TwitterEmotionClassifier()
        if args.task == 'sentiment':
            return classifiers.TwitterSentimentClassifier()
    if args.model == 't5':
        if args.task == 'emotion':
            return classifiers.T5EmotionClassifier()
    if args.model == 'goemotion-bert':
        if args.task == 'emotion':
            return classifiers.GoEmotionBertClassifier()
    raise Exception(f'Combination {args.model} and {args.task} not available')


def main():
    args = parse_args()
    df = pd.read_csv(args.eval_data)
    clf = get_classifier(args)
    scores = []
    for text in df['text']:
        scores.append(clf.classify_scores(text))
    df = pd.DataFrame(scores, columns=clf.labels)
    df.to_csv(args.save_path)


if __name__ == '__main__':
    main()
