from sklearn import datasets
import pandas as pd


COLUMN_NAMES = ['sepal_length',
                'sepal_width',
                'petal_length',
                'petal_width']

iris = datasets.load_iris()
df = pd.DataFrame(iris['data'])
df.columns = COLUMN_NAMES
print(df)

