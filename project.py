import statistics
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
sd = statistics.stdev(data)

first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean - (2*sd), mean + (2*sd)
third_sd_start, third_sd_end = mean - (3*sd), mean + (3*sd)

data_within_one_sd = [result for result in data if result > first_sd_start and result < first_sd_end]
data_within_two_sd = [result for result in data if result > second_sd_start and result < second_sd_end]
data_within_three_sd = [result for result in data if result > third_sd_start and result < third_sd_end]

print("Mean is {}".format(mean))
print("Median is {}".format(median))
print("Mode is {}".format(mode))
print("Standard Deviation is {}".format(sd))

print("-------------------------")

print("{}% of data lies within 1 sd".format(len(data_within_one_sd)*100.0/len(data)))
print("{}% of data lies within 2 sd".format(len(data_within_two_sd)*100.0/len(data)))
print("{}% of data lies within 3 sd".format(len(data_within_three_sd)*100.0/len(data)))