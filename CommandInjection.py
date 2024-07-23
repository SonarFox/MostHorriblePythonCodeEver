import os

def vulnerable_function(user_input):
    os.system(f'echo {user_input}')

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    vulnerable_function(user_input)
