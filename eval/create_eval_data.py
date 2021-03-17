import argparse

import numpy as np
import pandas as pd


def get_text_series(csv_path="./data/sorted_new.csv", role='volunteer'):
    df = pd.read_csv(csv_path)
    if role == 'volunteer':
        text_only = df[df['ParticipantRole'] == 'Agent']['Text'].dropna()
    elif role == 'buyer':
        text_only = df[df['ParticipantRole'] == 'Visitor']['Text'].dropna()
    else:
        raise NotImplementedError(f'Role {role} not available, try volunteer or buyer instead')
    return text_only


def save_text(text_list, save_path):
    df = pd.DataFrame(text_list, columns=['text'])
    df.to_csv(save_path)


def main(save_path, data_path, n=1000, seed=None):
    text_series = get_text_series(csv_path=data_path)
    np.random.seed(seed)
    sample_text = np.random.choice(text_series.to_list(), size=(n,))
    save_text(sample_text, save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=1000, help='number of texts to sample')
    parser.add_argument('--save-path', type=str, default='../data/evaluation_volunteer_text_1000.csv', help='save path')
    parser.add_argument('--data-path', type=str, default='../data/sorted_new.csv', help='path to data csv')
    parser.add_argument('--seed', type=int, default=0, help='random seed')
    args = parser.parse_args()
    main(args.save_path, args.data_path, n=args.n, seed=args.seed)
