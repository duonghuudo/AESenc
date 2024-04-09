def mix_columns(state):
    # Define the fixed polynomial a(x) = 0x03 * x^3 + 0x01 * x^2 + 0x01 * x + 0x02
    a = [[0x02, 0x03, 0x01, 0x01],
         [0x01, 0x02, 0x03, 0x01],
         [0x01, 0x01, 0x02, 0x03],
         [0x03, 0x01, 0x01, 0x02]]

    # Create a new state matrix to store the result
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(4):  # for each column in the state
        for j in range(4):  # for each row in the state
            new_state[j][i] = (
                gf_mult(a[j][0], state[0][i]) ^
                gf_mult(a[j][1], state[1][i]) ^
                gf_mult(a[j][2], state[2][i]) ^
                gf_mult(a[j][3], state[3][i])
            )

    return new_state

def gf_mult(a, b):
    # Multiply two numbers in GF(2^8) modulo x^4 + 1
    result = 0
    for _ in range(8):
        if b & 1:  # If the least significant bit of b is set
            result ^= a  # Add a to the result
        a <<= 1  # Left shift a
        if a & 0x100:  # If a overflows past 8 bits
            a ^= 0x11B  # XOR with the irreducible polynomial x^8 + x^4 + x^3 + x + 1
        b >>= 1  # Right shift b
    return result

# Test the mix_columns function
state = [[0xdb, 0x13, 0x53, 0x45],
         [0xf2, 0xc5, 0x41, 0x00],
         [0x12, 0x24, 0x35, 0x00],
         [0xc2, 0xc6, 0x4f, 0x00]]

new_state = mix_columns(state)
for row in new_state:
    print([hex(val) for val in row])
