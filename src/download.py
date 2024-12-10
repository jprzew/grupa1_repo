from sklearn import datasets
import pandas as pd
from pathlib import Path
from utils import get_repo_path
from config import DATA_PATH, FILE, COLUMN_NAMES, TARGET


def main():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris['data'])
    df.columns = COLUMN_NAMES

    df[TARGET] = iris['target']

    df[TARGET] = df[TARGET].replace(
        {index: name for index, name in enumerate(iris['target_names'])})

    df.to_csv(get_repo_path() / Path(DATA_PATH) / FILE, index=False)


if __name__ == '__main__':
    main()
