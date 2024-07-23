import logging

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

def divide(a, b):
    return a / b

def main():
    try:
        # Simulate user input
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))

        result = divide(a, b)
        logging.info(f"The result of the division is: {result}")
    except Exception as e:
        # Log the stack trace
        logging.exception("An error occurred:")

if __name__ == "__main__":
    main()
