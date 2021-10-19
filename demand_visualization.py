import pandas as pd
import datetime
import matplotlib.pyplot as plt

# read data file
df = pd.read_csv("demand_visualization_data.csv")

def demand_visualization(year, month, day):
    '''
    This function visualize the fluctuation of demand (in hour) for a certain date
    input: year, int
           month, int
           day, int
    output: generate a figure
    '''
    date = str(datetime.date(2017,10,4))#get date in string
    flow_in_hour = df[df['date']==date].groupby('start_hour')# group trips by hour
    flow_in_hour = flow_in_hour.count()['bike_id']# count trips
    flow_in_hour.plot()

    #save figure
    plt.savefig("demand_fluctuation_on_{}-{}-{}.png".format(year, month, day))

demand_visualization(2017, 10, 4)# change date here in year, month, day