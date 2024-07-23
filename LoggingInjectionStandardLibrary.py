import logging
import sys

# Setup logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def main():
    if len(sys.argv) > 1:
        data = sys.argv[1]
        logger.log(logging.CRITICAL, "%s", data)  # Noncompliant
    else:
        print("No command-line parameter provided.")

if __name__ == "__main__":
    main()
