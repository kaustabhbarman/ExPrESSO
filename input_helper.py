import hashlib
def string_to_fields(input_string):
    # Convert string to ASCII values
    ascii_values = [ord(c) for c in input_string]

    # Pad with zeros to make the total length a multiple of 32 (256 bits = 4 fields x 64 bits)
    while len(ascii_values) % 32 != 0:
        ascii_values.append(0)

    # Pack ASCII values into 4 fields
    fields = []
    for i in range(0, len(ascii_values), 8):  # Each field holds 8 bytes (64 bits)
        packed = 0
        for j in range(8):  # Pack 8 bytes into one field
            packed = (packed << 8) | ascii_values[i + j]
        fields.append(packed)

    # Ensure exactly 4 fields
    return fields[:4]

def string_to_int_hash(input_string):
    hash_value = hashlib.sha256(input_string.encode()).hexdigest()

    # Split 256bit hash into two 128bit parts
    part1 = hash_value[:32]
    part2 = hash_value[32:]

    # convert into int
    return [int(part1, 16), int(part2, 16)]

# Input string
#input_string = "Hello World"
input_string = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRJRCI6ImtieXVGRGlkTExtMjgwTEl3VkZpYXpPcWpPM3R5OEtIIiwiY3JlYXRlZF9hdCI6IjIwMjUtMDEtMDhUMTU6NDY6MTMuNjE5WiIsImVtYWlsIjoia2F1c3RhYmguYmFybWFuQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmYW1pbHlfbmFtZSI6IkJhcm1hbiIsImdpdmVuX25hbWUiOiJLYXVzdGFiaCIsImlkZW50aXRpZXMiOlt7InByb3ZpZGVyIjoiZ29vZ2xlLW9hdXRoMiIsInVzZXJfaWQiOiIxMTUzODUyMzA2MDYzMDIzNjgwMTIiLCJjb25uZWN0aW9uIjoiZ29vZ2xlLW9hdXRoMiIsImlzU29jaWFsIjp0cnVlfV0sIm5hbWUiOiJLYXVzdGFiaCBCYXJtYW4iLCJuaWNrbmFtZSI6ImthdXN0YWJoLmJhcm1hbiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NJMTRBT2VtNjVBVG1wRGx3YlBNajhmVXAyUnRzRmVkVEJLVHFaZWpRRzdZbmxSa2hVPXM5Ni1jIiwidXBkYXRlZF9hdCI6IjIwMjUtMDEtMDhUMTU6NTM6MDIuMzExWiIsInVzZXJfaWQiOiJnb29nbGUtb2F1dGgyfDExNTM4NTIzMDYwNjMwMjM2ODAxMiIsInVzZXJfbWV0YWRhdGEiOnt9LCJhcHBfbWV0YWRhdGEiOnt9LCJpc3MiOiJodHRwczovL3NhbXBsZXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTE1Mzg1MjMwNjA2MzAyMzY4MDEyIiwiYXVkIjoia2J5dUZEaWRMTG0yODBMSXdWRmlhek9xak8zdHk4S0giLCJpYXQiOjE3MzYzNTE2NzMsImV4cCI6MTczNjM4NzY3M30.3QzoreX2xmdUdNiyPeXvIz1JRIjKRU7vF1uaX8E1HxI"



# Convert to 4 fields
fields = string_to_fields(input_string)
int_hash = string_to_int_hash(input_string)
print(fields)
print(int_hash)
