import logging

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')

def log_user_action(user_id, action):
    logging.info(f"User {user_id} performed action: {action}")

def main():
    # Simulate user input
    user_id = input("Enter user ID: ")
    action = input("Enter action: ")

    # Log the user action directly
    log_user_action(user_id, action)

if __name__ == "__main__":
    main()
