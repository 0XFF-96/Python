import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def PlotData():
    
    df = pd.read_json('user_study.json')

    data = df.groupby('user_id').sum().head(100)

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.set_title('Study Data')
    ax.plot(data.index, data.minutes)

if __name__ == '__main__':
    data_plot()

