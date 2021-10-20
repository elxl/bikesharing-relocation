# bikesharing-relocation
This is a repository for processing trip data into flow data between OD and visualize the demand fluctuation on certain day. The region is discretized into cells and flow is count by cell. See the following picture for a example of the partition of the region:
![image info](partition_example.png)

In the above picture, density is count by cells. We do the similar thing for flow by using the discretized cells as origin and destination of trips.
## Getting started

### Dependencies
The scripts are implemented in python. Pandas, Numpy, matplotlib are required for execution.

### Data description
The sample_data.csv is composed of trip data. In the data file, every row stands for a trip and has the following fields:
* bike_id, a unique string for each bike
* time_stamp_ori,time_stamp_dst: the start and end time of the trip in seconds from 1970-1-1
* lng0, lat0: longitude and latitude of the start position in WGS84 coordinate system
* lng1, lat1: longitude and latitude of the start position in WGS84 coordinate system
* time_duration: time duration of the trip in seconds
* trip_distance: distance of trip in km
* speed: average speed of trip in km/s, calculated by trip_distance/time_duration

The output flow data file has the following field:
* cell_start, cell_end:

### Executing
* run get_demand.py, you can get a new csv file named flow_result.csv which stores the flow between OD
* after run get_demand.py, Run demand_visulization.py and you can get an image in the same directory named "demand_fluctuation_on_(date you choose).png"

To get the flow result from other original data (need to be in the same form with sample_data.csv), put the data file and get_demand.py in one folder. If your file is with a different name, go to get_demand.py and change the first line of reading file. If you want to get image of demand fluctuation, go into demand_visualization.py and change the date you want to visualiza

### Authors
[@Xinling Li](li.xinling@epfl.ch)

### License
CC-BY

### Acknowledgments

The processing and discritization is inspired by a paper of Yu Shen. Click the link for more information:
[Understanding the usage of dockless bike sharing in Singapore](https://www.tandfonline.com/doi/abs/10.1080/15568318.2018.1429696)
