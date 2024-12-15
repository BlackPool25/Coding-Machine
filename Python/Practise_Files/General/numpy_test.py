import Python.Practise_Files.General.numpy_test as np

# Define matrix A
A = np.array([
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 3]
])

# Define identity matrix I
I = np.eye(3)

# Compute powers of A
A2 = np.matmul(A, A)  # A^2
A3 = np.matmul(A2, A)  # A^3
A4 = np.matmul(A3, A)  # A^4

# Evaluate the given equations
eq1 = A3 - 6 * A  # A^3 - 6A
eq2 = A4 + 14 * A2 - 19 * A + 44 * I  # A^4 + 14A^2 - 19A + 44I
eq3 = A4 - 4 * A + 11 * I  # A^4 - 4A + 11I
eq4 = A4 - 38 * A2 + 72 * I  # A^4 - 38A^2 + 72I

# Check if any of these equal 0
results = {
    "Equation 1": np.allclose(eq1, 0),
    "Equation 2": np.allclose(eq2, 0),
    "Equation 3": np.allclose(eq3, 0),
    "Equation 4": np.allclose(eq4, 0),
}

results
