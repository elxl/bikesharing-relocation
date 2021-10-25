'''
author: xinling Li
19-10-2021
This is the code to get trip data as input and output the demand for each cell
'''
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('sample_data.csv')# change file name here

#---------data preprossing by time duration, trip distance and speed using interquatile range------#
# get IQR
df1 = df.loc[:,['time_duration','trip_distance','speed']]
q1 = df1.quantile(0.25)
q3 = df1.quantile(0.75)
iqr = q3-q1

# get trip data that is within the interquatile range
index0 = df1[~((df1 < (q1 - 1.5 * iqr)) |(df1 > (q3 + 1.5 * iqr))).any(axis=1)].index
df = df.iloc[index0,:]

df = df.drop(columns=['time_duration','trip_distance','speed'])

#-------------------------------------------------------------------------------------------------#


#---------------------compute cell id for departure and destination points------------------------#

def linear_referencing(locpair):

    '''
    This is a function to allocate point to cell
    input: list, location of a point in [latitude, longitude]
    output: int, cell id
    '''

    x_min = 103.605414
    y_max = 1.470763
    lon_diff = 0.00269582
    lat_diff = 0.00271293

    cell_id = math.floor((locpair[1]-x_min)/lon_diff) + \
        180 * math.floor((y_max-locpair[0])/lat_diff)
    return cell_id

# get the start cell id and end cell id for each trip
df['cell_start'] = df.apply(lambda x:linear_referencing((x['lat0'],x['lng0'])),axis = 1)
df['cell_end'] = df.apply(lambda x:linear_referencing((x['lat1'],x['lng1'])),axis = 1)
df = df.drop(columns = ['lng0','lat0','lng1','lat1'])

#--------------------------------------------------------------------------------------------------#


#----------------------------------time format transformation--------------------------------------#
# transform time from absolute seconds to timestamp (in Singapore)
start_timestamp = pd.to_datetime(df['time_stamp_ori'],unit='s')# convert seconds to timestamp
df['time_start'] = start_timestamp.dt.tz_localize('UTC')\
                                   .dt.tz_convert('Singapore')# convert time zone to Singapore

end_timestamp = pd.to_datetime(df['time_stamp_dst'],unit='s')
df['time_end'] = end_timestamp.dt.tz_localize('UTC')\
                              .dt.tz_convert('Singapore')

df=df.drop(columns=['time_stamp_ori','time_stamp_dst'])# delete time in seconds in original data

# get date, start hour, day of week for each trip
df['start_hour'] = df['time_start'].dt.hour
df['date'] = df['time_start'].dt.date
df['dayofweek']=df['time_start'].dt.dayofweek

#-------------------------------------------------------------------------------------------------#


# output file for visualization of demand fluctuation
df.to_csv("demand_visualization_data.csv", index = False)


#get flow of each OD pair for each date and start hour
flow = df.groupby(by = ['cell_start','cell_end','dayofweek','date','start_hour']).count()
flow = flow.reset_index()
flow = flow.drop(columns=['time_end','time_start'])

# output flow
flow.to_csv("flow_result.csv",index = False)