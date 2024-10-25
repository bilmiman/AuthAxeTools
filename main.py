import requests
from colorama import init, Fore
import time

init()

check_version = requests.get('https://raw.githubusercontent.com/bilmiman/AuthAxeTools/refs/heads/main/Version.txt')

# Открываем файл в режиме чтения ('r')
with open('version.txt', 'r', encoding='utf-8') as file:
    for line in file:
        version = line.strip()

if check_version.text == version:
    print(f"+ [INFO] | Программа в не требует обновлении")
    time.sleep(3.5)
else:
    