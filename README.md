# bikesharing-relocation
This is a repository for processing trip data into flow data between OD and visualize the demand fluctuation on certain day.
## Getting started

### Dependencies
The scripts are implemented in python. Pandas, Numpy, matplotlib are required for execution.

### Executing
To get the flow result from original data, put the data file and get_demand.py in one folder. If your file is with a different name, go to get_demand.py and change the first line of reading file. 

*run get_demand.py, you can get a new csv file named flow_result.csv which stores the flow between OD
*after run get_demand.py, go into demand_visualization.py and change the date you want to visualiza. Run demand_visulization.py and you can get an image in the same directory named "demand_fluctuation_on_(date you choose).png"

