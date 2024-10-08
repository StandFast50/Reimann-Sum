import matplotlib.pyplot as plt
import ReimannSum

# Functions
def f(x): 
    return pow(x, 2)
  
def plot(x, y):
    plt.plot(x, y)
    plt.title("X vs Y")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Coordinates
x = [0, 1, 2, 3, 4]
y = [10, 20, 5, 7, 30] 

a = 0 #1
b = 4 # 5
n = 4

ReimannSum.midpoint_calculation(x, y, a, b, n)
