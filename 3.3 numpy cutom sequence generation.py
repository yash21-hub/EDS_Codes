import numpy as np

# Take user input for the start, stop, and step of the sequence
start = int(input())
stop = int(input())
step = int(input())
a= np.arange(start, stop, step)
print(a)
# Generate the sequence using np.arange()

# Print the generated sequence