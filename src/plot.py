import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from utils import get_repo_path
from config import DATA_PATH, FILE

PLOT_SEPAL = ['sepal_length', 'sepal_width']
PLOT_PETAL = ['petal_length', 'petal_width']

SPECIES_COLOR = {'setosa': 'red',
                 'versicolor': 'blue',
                 'virginica': 'green'}

df = pd.read_csv(get_repo_path() / Path(DATA_PATH) / FILE)


def prepare_plot(x_data: pd.Series, y_data: pd.Series, species: pd.Series,
                 title: str, x_axis: str, y_axis: str) -> plt.Figure:
    fig = plt.figure()

    # Data to plot
    df = pd.DataFrame({'x': x_data, 'y': y_data, 'species': species})

    # List of plots
    plots = []
    for species, color in SPECIES_COLOR.items():
        species_data = df[df['species'] == species]
        scatter = plt.scatter(species_data['x'], species_data['y'],
                              c=color)
        plots.append(scatter)

    # Set legend
    plt.legend(plots, SPECIES_COLOR.keys())

    # Set labels
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    # Set title
    plt.title(title)

    return fig


fig_sepal = prepare_plot(x_data=df[PLOT_SEPAL[0]], y_data=df[PLOT_SEPAL[1]],
                         species=df['species'],
                         title='Sepal length vs Sepal width',
                         x_axis='Sepal length', y_axis='Sepal width')

fig_petal = prepare_plot(x_data=df[PLOT_PETAL[0]], y_data=df[PLOT_PETAL[1]],
                         species=df['species'],
                         title='Petal length vs Petal width',
                         x_axis='Petal length', y_axis='Petal width')


fig_sepal.savefig(get_repo_path() / Path('plots/sepal.png'))
fig_petal.savefig(get_repo_path() / Path('plots/petal.png'))


