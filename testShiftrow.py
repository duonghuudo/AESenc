Nb = 4  # Số cột trong mỗi hàng của State
shift_values = [0, 1, 2, 3]  # Giá trị dịch chuyển cho từng hàng

def shift_rows(state):
    for row in range(1, 4):  # Dịch chuyển từ hàng thứ 2 đến hàng thứ 4
        state[row] = shift_row(state[row], row)
    return state

def shift_row(row, shift_amount):
    return row[shift_amount:] + row[:shift_amount]

# Ví dụ về cách sử dụng hàm shift_rows với State là một mảng 2D 4x4
state = [
    [0x00, 0x01, 0x02, 0x03],
    [0x04, 0x05, 0x06, 0x07],
    [0x08, 0x09, 0x0A, 0x0B],
    [0x0C, 0x0D, 0x0E, 0x0F]
]

result = shift_rows(state)
for row in result:
    print(row)
