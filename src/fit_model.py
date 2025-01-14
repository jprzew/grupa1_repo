import numpy as np
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

import random
random.seed(RANDOM_SEED)

import json
import dvc.api
import pandas as pd
import config as cfg
from utils import get_repo_path
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

METRICS_FILE = 'eval/metrics.json'

models = {
    'rf': RandomForestClassifier(),
    'cart': DecisionTreeClassifier(),
    'svm': SVC(),
    'knn-2': KNeighborsClassifier(n_neighbors=2),
    'knn-3': KNeighborsClassifier(n_neighbors=3),
    'knn-5': KNeighborsClassifier(n_neighbors=5),
    'knn-7': KNeighborsClassifier(n_neighbors=7)
}


def read_data():
    return pd.read_csv(get_repo_path() / cfg.DATA_PATH / cfg.INPUT_FILE)


def prepare_data(df):

    # Shuffle the data
    df = df.sample(frac=1)

    X = df[cfg.COLUMN_NAMES]
    y = df[cfg.TARGET]

    return X, y


def evaluate_model(model, X, y):
    return cross_val_score(model, X, y, cv=5, scoring='accuracy')


def main():

    # Read parameters
    params = dvc.api.params_show()
    model_name = params['evaluate'][0]['model']

    df = read_data()
    X, y = prepare_data(df)

    avg_accuracy = np.mean(evaluate_model(models[model_name], X, y))
    with open(get_repo_path() / METRICS_FILE, 'w') as f:
        json.dump({'avg_accuracy': avg_accuracy}, f)


if __name__ == '__main__':
    main()
