# Numerical arrays
import numpy as np

# Import Pandas
import pandas as pd

# Time the algorithms
import time

# plotting
import matplotlib.pyplot as plt

# Change default style sheet
plt.style.use('fivethirtyeight')

# Change the default parameters
plt.rcParams['figure.figsize'] = [10, 6]

# Use the numpy python package to generate random arrays
def numpy_random(n):
    rng = np.random.default_rng()
    arr = rng.integers(1, 101, size = n)
    return(arr)

# Function used to time each algorithm
def benchmarking(algorithms, array_size, runs):
    # Variables to append the output to
    elapsed_times = [] # 10 elapsed times for each inner loop
    input_size =[] # Record array size used for each run
    trials =[] # Record the current trial number for each algorithm
    type =[] #  Record the name of the sorting algorithm used


    # For loop to run the 5 algorithms 
    for i in algorithms:
        print(f"Running {i}...") # Shows the stage of the current runtime        
        # For loop that iterates through each array size
        for size in array_size:
            # Test each algorithm 10 times (runs=10)
            for run in range(runs):
                # Generate random arrays
                x = numpy_random(size)
                
                # Iterate through the 5 algorithms
                algorithm = algorithms[i]
                # Start of the code to record the time of the algorithm
                start_time = time.time()
                algorithm(x)
                end_time = time.time()
                # Start of the code to record the time of the algorithm
                time_elapsed = (end_time - start_time)*1000 # Milliseconds
                
                # Append time elapsed to the empty array elapsed_times 
                elapsed_times.append(time_elapsed)               
                # Append run+1 to the empty array trials
                trials.append(run+1)
                # Append size to the empty array input_size
                input_size.append(size)
                # Append i to the empty array type
                type.append(i) 

    # Use pandas to create a dataFrame with the raw times for each trial            
    df = pd.DataFrame({"algorithm":type, "array_size":input_size, "average_elapsed_times":elapsed_times, "trial_num":trials})
    return df

def average_run_times(df):
    # Set the index column to array_size
    df.set_index('array_size', inplace = True)
    # Using pandas iloc method, select all rows and select the first 3 columns (index 0-2)
    # Use pandas groupby method to group the data by algorithm and the array size. By default, 
    # group by splits along rows (parameter axix = 0)
    # Calculate the averages for each sorting algorithm by using pandas mean method for each of 
    # the input sizes
    # Use pandas round method to round the data to 3 decimal places
    means = (df.iloc[:, :2].groupby(by = ['algorithm','array_size']).mean()).round(3)
    # Use pandas unstack method to get the array sizes to display across the rows instead of 
    # the columns
    return means.unstack()

def plot_algorithm_averages(df_plot):
    df_trans = df_plot.T
    df_trans.plot(lw=2, colormap='nipy_spectral', marker='.', markersize=12)
    plt.title("Benchmarking 5 Sorting Algorithms (Average Times)")
    plt.ylabel("Running Time (milliseconds)")
    plt.xlabel("Array Size")
    #plt.show()
    # Save image
    plt.savefig('averages_plotted.png', bbox_inches='tight')
    # The bbox_inches(bounding box inches) parameter stops the figure being cut off