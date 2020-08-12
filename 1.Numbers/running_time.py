def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time an
    d number of runs."""
    number_of_runs = 0
    total_time = 0
    while True:
        one_run_timing = input('Enter 10 km run time: ')
        if not one_run_timing:
            break
        number_of_runs += 1
        total_time += float(one_run_timing)
    average_time = total_time / number_of_runs
    print('Average of {}, over {} runs'.format(average_time,number_of_runs))

run_timing()