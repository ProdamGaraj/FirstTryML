import seaborn as sns
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

file = "winemag-data_first150k.csv"
dateparse = lambda x: dt.strptime(x, '%Y-%m-%d %H:%M:%S')
df = pd.read_csv(file,delimiter=',')
#df=df.sort_values(['episodes'])
print(df.columns)
#flights_data = sns.load_dataset(df)
#print(flights_data.head())
#print(df['age'])
plot=sns.lineplot(data=df,x=df['price'],y=df['points'], sort=True)
plot.set_xticklabels(plot.get_xticklabels())
plt.tight_layout()
plt.show()