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
subintervals = [0] * (n)
interval = 0
for i in range(n):
    subintervals[i] = [interval, interval + dx]
    interval+=dx
print(subintervals)
# Calculating the Midpoints
midpoints = [0] * n
for i in range(n):
    x1 = subintervals[i][0]
    x2 = subintervals[i][1]
    midpoints[i] = calculate_midpoint(x1, x2)

print(midpoints)