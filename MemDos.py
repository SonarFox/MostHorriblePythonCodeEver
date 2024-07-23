def vulnerable_function(data):
    # Allocate memory based on user-provided data length
    buffer = bytearray(len(data) * 1024 * 1024)
    return buffer

if __name__ == "__main__":
    user_input = input("Enter some data: ")
    result = vulnerable_function(user_input)
    print(f"Allocated buffer of size: {len(result)} bytes")
