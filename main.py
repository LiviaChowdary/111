import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_set(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("Mean:",mean)
print("std: ", std_deviation)

std1_start, std1_end = mean-std_deviation, mean+std_deviation
std2_start, std2_end = mean-(2*std_deviation), mean+(2*std_deviation)
std3_start, std3_end = mean-(3*std_deviation), mean+(3*std_deviation)


df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

new_mean = statistics.mean(data)
print("New mean: ",new_mean)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.5], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[new_mean, new_mean], y=[0,1.5], mode="lines", name="new mean"))

fig.add_trace(go.Scatter(x=[std1_end,std1_end],y=[0,1.5],mode = 'lines', name = 'std1'))
fig.add_trace(go.Scatter(x=[std2_end,std2_end],y=[0,1.5],mode = 'lines', name = 'std2'))
fig.add_trace(go.Scatter(x=[std3_end,std3_end],y=[0,1.5],mode = 'lines', name = 'std3'))
fig.show()

z_score = (mean - new_mean)/std_deviation
print("Z-Score: ",z_score)
