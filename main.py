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
x = [ 1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10] 

a = x[0] #1
b = x[4] # 5
n = 4

ReimannSum.midpoint_calculation(x, y, a, b, n)