def add_round_key(state, round_key):
    # Perform AddRoundKey operation by XORing each column of the state with the round key
    for col in range(len(state[0])):  # Iterate over columns
        for row in range(len(state)):  # Iterate over rows
            state[row][col] ^= round_key[row][col]  # XOR operation

# Example usage
state = [[0x32, 0x88, 0x31, 0xe0],
         [0x43, 0x5a, 0x31, 0x37],
         [0xf6, 0x30, 0x98, 0x07],
         [0xa8, 0x8d, 0xa2, 0x34]]

round_key = [[0x2b, 0x28, 0xab, 0x09],
             [0x7e, 0xae, 0xf7, 0xcf],
             [0x15, 0xd2, 0x15, 0x4f],
             [0x16, 0xa6, 0x88, 0x3c]]

add_round_key(state, round_key)

# Display the updated state after AddRoundKey operation
for row in state:
    print(row)
