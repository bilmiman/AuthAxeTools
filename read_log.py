from cryptography.fernet import Fernet

key = b''
cipher = Fernet(key)


with open('log.log', 'r', encoding='utf-8') as file:
    encrypted_lines = file.readlines()

for line in encrypted_lines:
    encrypted_data = line.strip()

        # Расшифровка данных
    decrypted_data = cipher.decrypt(encrypted_data.encode('utf-8'))

        # Вывод расшифрованного содержимого
    print(decrypted_data.decode('utf-8'))

