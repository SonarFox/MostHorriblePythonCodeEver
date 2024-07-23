import re
import time

# Vulnerable regular expression
regex = re.compile(r'(a+)+$')

# Malicious input designed to cause catastrophic backtracking
malicious_input = 'a' * 100000 + 'b'

# Measure the time taken to process the input
start_time = time.time()

try:
    # This will hang or take a very long time to process
    match = regex.match(malicious_input)
    if match:
        print("Match found!")
    else:
        print("No match found.")
except re.error as e:
    print(f"Regex error: {e}")

end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
