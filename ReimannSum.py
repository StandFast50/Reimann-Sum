def find_value_in_array(array, value):
    if value in array:
        index = array.index(value)
        return index
    else:
        print(f"{value} was not found in array {array}")
        
def calculate_midpoint(x1, x2):
    return (x1 + x2) / 2


def midpoint_calculation(x, y, start_interval, end_interval, n, print_calculations=False):
    # Calculating Delta X (Width)
    if isinstance(start_interval, int) and isinstance(end_interval, int):
        a = find_value_in_array(x, start_interval)
        b = find_value_in_array(x, end_interval)
    else:
        a = start_interval
        b = end_interval
    dx = (x[b] - x[a]) / n

    # Calculating the Subintervals
    x_subintervals = [0] * (n + 1)
    x_interval = x[a]
    for i in range(n+1):
        x_subintervals[i] = x_interval
        x_interval+=dx

    # Calculating the Midpoints
    x_midpoints = [0] * n
    for i in range(n):
        x1 = x_subintervals[i]
        x2 = x_subintervals[i+1]
        x_midpoints[i] = calculate_midpoint(x1, x2)


    # Y Subintervals
    y_subintervals = [0] * (n)
    for i in range(n):
        x_value = x_midpoints[i]

        for j in range(len(x) - 1):
            if x[j] <= x_value <= x[j + 1]:
                x1 = x[j]
                x2 = x[j+1]
                y1 = y[j]
                y2 = y[j + 1]
                calculation = y1 + ((x_value - x1) / (x2 - x1)) * (y2 - y1)
                y_subintervals[i] = calculation
                if print_calculations == True:
                    print(f"x: {x_value}")
                    print(f"x1: {x1}")
                    print(f"x2: {x2}")
                    print(f"y1: {y1}")
                    print(f"y2: {y2}")
                    print(f"calculation { calculation}")
                    print("**************")
                break

    area = 0                               
    for i in range(len(y_subintervals)):
        area += (y_subintervals[i] * dx)
    print(f"area: {area}")