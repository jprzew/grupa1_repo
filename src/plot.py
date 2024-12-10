import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from utils import get_repo_path
from config import DATA_PATH, FILE

PLOT_SEPAL = ['sepal_length', 'sepal_width']
PLOT_PETAL = ['petal_length', 'petal_width']

df = pd.read_csv(get_repo_path() / Path(DATA_PATH) / FILE)

fig_sepal = plt.figure()
plt.scatter(df[PLOT_SEPAL[0]], df[PLOT_SEPAL[1]],
            c=df['species'].replace({'setosa': 'red',
                                     'versicolor': 'blue',
                                     'virginica': 'green'}))
#
# fig_petal = plt.figure()
# plt.scatter(df[PLOT_PETAL[0]], df[PLOT_PETAL[1]], c=df['species'])

fig_sepal.savefig(get_repo_path() / Path('plots/sepal.png'))
# fig_petal.savefig(get_repo_path() / Path('plots/petal.png'))



