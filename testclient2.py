import socket
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as file:
        image_data = file.read()
    
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(image_data, AES.block_size))
    
    with open('encrypted_image.jpg', 'wb') as file:
        file.write(encrypted_data)

    print("Hình ảnh đã được mã hóa thành công!")

key = b"ThisIsA16ByteKey"  # Chuyển khóa thành bytes
image_path = 'hinhanh.jpg'
encrypt_image(image_path, key)

encrypted_image_path = 'encrypted_image.jpg'

# Thiết lập kết nối
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9999
client_socket.connect((host, port))

# Gửi file
with open(encrypted_image_path, 'rb') as image_file:
    # Gửi kích thước file trước
    file_size = os.path.getsize(encrypted_image_path)
    client_socket.sendall(file_size.to_bytes(8, 'big'))
    
    # Gửi dữ liệu file
    while (data := image_file.read(1024)):
        client_socket.sendall(data)

print("File đã được gửi.")
