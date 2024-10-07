import matplotlib.pyplot as plt

# Functions
def f(x): 
    return pow(x, 2)

def calculate_midpoint(x1, x2):
    return (x1 + x2) / 2

        
def plot(x, y):
    plt.plot(x, y)
    plt.title("X vs Y")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Coordinates
x = [0, 1, 2, 3, 4]
y = [50, 75, 32, 46, 1500] 

a = 0
b = 2
n = 4

# Calculating Delta X (Width)
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
    x1 = x_subintervals[i]
    x2 = x_subintervals[i+1]
    y1 = y[i]
    y2 = y[i + 1]
    calculation = y1 + ((x_value - x1) / (x2 - x1)) * (y2 - y1)
    y_subintervals[i] = calculation
    print(f"x: {x_value}")
    print(f"x1: {x1}")
    print(f"x2: {x2}")
    print(f"y1: {y1}")
    print(f"y2: {y2}")
    print(f"calculation { calculation}")
    print("**************")
                                
