import benchmark
import sorting_algorithms

# Code was inspired from:
# https://github.com/angela1C/Computational-Thinking-With-Algorithms-Project-2020/blob/master/scripts/benchmarking.py

# Main function
def main():

    # Variable to store the sorting algorithms in a dictionary object
    algorithms = {"insertion_sort": sorting_algorithms.insertion_sort,
    "quicksort":sorting_algorithms.quicksort, "counting_sort":sorting_algorithms.counting_sort, 
    "merge_sort":sorting_algorithms.mergesort, "bubble_sort":sorting_algorithms.bubble}

    # List of the array sizes to run the benchmarking test on
    size_array = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]

    # Variable to store the results
    results = benchmark.benchmarking(algorithms, size_array, 10)

    # Variable to store the results of the average run times for each algorithm
    df_avg = benchmark.average_run_times(results)

    # Rename axis and drop a level indexes to create the table results in the correct format
    df_avg.rename_axis(None, inplace = True)

    df_avg.columns = df_avg.columns.droplevel()

    # Print the results to the console
    print(df_avg)

    # Run the function to plot the average run times to a graph
    benchmark.plot_algorithm_averages(df_avg)



if __name__ == "__main__":
    main()