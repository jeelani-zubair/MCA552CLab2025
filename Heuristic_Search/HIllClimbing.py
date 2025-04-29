import random
import numpy as np
import matplotlib.pyplot as plt

# f(x)=−(x−3)^2 +9 is a parabola opening downward.
# The maximum of this function happens at 𝑥 = 3, where 𝑓(3) = 9
# The goal of hill climbing is to find 𝑥 that gives the highest value of 𝑓(𝑥).


# Define the function to maximize
def f(x):
    return -(x - 3) ** 2 + 9


# Function to plot f(x)
def plot_function():
    # Generate 100 points between -2 and 8
    x = np.linspace(-2, 8, 100)
    y = f(x)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='f(x) = -(x-3)^2 + 9', color='blue')
    plt.title('Plot of f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


# Call the plot function
plot_function()


# Hill Climbing Algorithm
# The hill_climbing function tries to maximize f
# x_start is the starting point
# stepsize is how much we change x in each move (small jumps left or right)
# max_iter is the maximum number of iterations
def hill_climbing(f, x_start, stepsize=0.1, max_iter=1000):
    current_x = x_start
    current_f = f(current_x)

    for i in range(max_iter):
        # Try a small change
        next_x = current_x + random.choice([-stepsize, stepsize])
                            # randomly selects -0.1 or +0.1.
        next_f = f(next_x)

        # If the new solution is better, move to it
        if next_f > current_f:
            current_x, current_f = next_x, next_f

    return current_x, current_f


# Starting point (random)
# Pick a random starting point between -10 and 10.
# This simulates not knowing where the good solution is initially.
x_start = random.uniform(-10, 10)


# Run hill climbing
# Function f itself as an argument to the hill_climbing function.
# x_start is the starting point (initial solution)
best_x, best_f = hill_climbing(f, x_start)

print(f"Best solution found: x = {best_x:.4f}, f(x) = {best_f:.4f}")