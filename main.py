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
x = [ 1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10] 

a = 0 #1
b = 4 # 5
n = 4

# Calculating Delta X (Width)
if isinstance(a, int) and isinstance(b, int):
    dx = (b - a) / n
elif isinstance(a, array) and isinstance(b, array):
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