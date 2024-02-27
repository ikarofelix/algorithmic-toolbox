# import sys
# n = int (sys.argv[1])
# print(n)
# print("-".join(str(i*2) for i in range(n)))

import random
import sys
import os

# Accept the number of tests and parameter for tests as command-line parameters
tests = int(sys.argv[1])
n = int(sys.argv[2])

# Loop through the tests
for i in range(tests):
    print("Test#" + str(i))

    # Run the generator gen.py with parameters n and the seed i
    os.system("python3 gen.py " + str(n) + " " + str(i) + " > input.txt")

    # Run the model solution model.py
    # Notice that it is not necessary that the solution is implemented in
    # Python; you can run ./model <input.txt >model.txt for a C++ solution.
    os.system("python3 model.py < input.txt > model.txt")

    # Run the main solution
    os.system("python3 main.py < input.txt > main.txt")

    # Read the output of the model solution
    with open('model.txt') as f:
        model = f.read()
    print("Model:", model)

    # Read the output of the main solution
    with open('main.txt') as f:
        main = f.read()
    print("Main:", main)

    # Check if the output of the model and main solutions match
    if model != main:
        break
