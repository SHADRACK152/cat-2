def func(x):
    return x**2 - x - 2

def double_regula_falsi(a, b, iterations, tol):
    fa = func(a)
    fb = func(b)

    for i in range(iterations):
        # Calculate x using the Regula Falsi formula
        x = (fa * b - fb * a) / (fa - fb)
        fx = func(x)

        # Print the current iteration and the value of x
        print(f"Iteration {i+1}: x = {x}, f(x) = {fx}")

        # Check if the result is within the tolerance
        if abs(fx) < tol:
            return x

        # Update the interval [a, b]
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    return -1  # Return -1 if the root was not found within the given iterations

# Initial guesses
a = 1
b = 3
iterations = 3
tol = 1e-5

# Find the root
root = double_regula_falsi(a, b, iterations, tol)
print(f"Root: {root}")
