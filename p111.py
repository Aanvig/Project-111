import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("p111.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data],["Reading Time"],show_hist=False)
fig.show()

mean = statistics.mean(data)
st_dev = statistics.stdev(data)
print("Mean of Population: ",mean)
print("Standard Deviation of Population: ",st_dev)

def randomMeanSet(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

meanList=[]
def setup():    
    for i in range(0,100):
        meanSet = randomMeanSet(30)
        meanList.append(meanSet)
    show_fig(meanList)

def show_fig(meanList):
    df = meanList
    fig = ff.create_distplot([df],["Reading Time"],show_hist=False)
    fig.show()

stdev = statistics.stdev(meanList)
sampleMean = statistics.mean(meanList)
print("Mean of Sampling Distribution: ",sampleMean)
print("Standard Deviation of Sampling Fistribution: ",stdev)

stdev1Start,stdev1End = sampleMean-stdev,sampleMean+stdev
stdev2Start,stdev2End = sampleMean-(2*stdev),sampleMean+(2*stdev)
stdev3Start,stdev3End = sampleMean-(3*stdev),sampleMean+(3*stdev)

print("std1 ",stdev1Start,stdev1End)
print("std2 ",stdev2Start,stdev2End)
print("std3 ",stdev3Start,stdev3End)

df1 = pd.read_csv("sample_2.csv")
sample1Data = df1["reading_time"].tolist()
sample1Mean = statistics.mean(sample1Data)
print("Mean of the Sample: ",sample1Mean)
fig = ff.create_distplot([meanList], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1.4], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sample1Mean,sample1Mean], y=[0, 1.4], mode="lines", name="Sample of reading time"))
fig.add_trace(go.Scatter(x=[stdev1End,stdev1End], y=[0, 1.4], mode="lines", name="STDEV 1 end"))
fig.add_trace(go.Scatter(x=[stdev2End,stdev2End], y=[0, 1.4], mode="lines", name="SSTDEV 2 end"))
fig.add_trace(go.Scatter(x=[stdev3End,stdev3End], y=[0, 1.4], mode="lines", name="STDEV 3 end"))
fig.show()

z_score1 =(sample1Mean - sampleMean)/stdev
print("The Z score of the sample: ",z_score1)