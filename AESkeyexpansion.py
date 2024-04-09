Nk = 4  # Độ dài của khóa key (16 byte)
Nb = 4  # Độ dài của một khối (4 byte)
Nr = 10 # Số vòng lặp rounds (10, 12, hoặc 14)
from testfunctioninkeyexpansion import SubWord
from testfunctioninkeyexpansion import RotWord
from testfunctioninkeyexpansion import Rcon
from testfunctioninkeyexpansion import xor_with_rcon
def KeyExpansion(key):
    w = [0] * Nb * (Nr + 1)
    i = 0
    while i < Nk:
        w[i] = word(key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
        i += 1
    
    i = Nk
    while i < Nb * (Nr + 1):
        temp = w[i-1]
        if i % Nk == 0:
            temp = xor_with_rcon(SubWord(RotWord(temp)),i/Nk)
        elif Nk > 6 and i % Nk == 4:
            temp = SubWord(temp)
        
        w[i] = w[i-Nk] ^ temp
        i += 1
    
    return w

def word(b0, b1, b2, b3):
    return (b0 << 24) | (b1 << 16) | (b2 << 8) | b3




# Thực hiện key expansion cho key bất kỳ
key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]
expanded_key = KeyExpansion(key)
# def ConvertKeyScheduleToList(key_schedule):
#     key_schedule_list = []
#     for i in range(len(key_schedule) // Nb):
#         round_key = key_schedule[i * Nb:(i + 1) * Nb]
#         key_schedule_list.append(round_key)
#     return key_schedule_list
# key_schedule_list = ConvertKeyScheduleToList(expanded_key)
print(expanded_key)
