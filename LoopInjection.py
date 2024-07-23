def vulnerable_function(iterations):
    # Loop based on user-provided iteration count
    for i in range(iterations):
        print(f"Iteration {i}")

if __name__ == "__main__":
    user_input = input("Enter the number of iterations: ")
    iterations = int(user_input)
    vulnerable_function(iterations)
