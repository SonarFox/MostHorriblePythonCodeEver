import logging

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Simulate user input
user_input = input("Enter a message: ")

# Log the user input directly
logging.info(user_input)