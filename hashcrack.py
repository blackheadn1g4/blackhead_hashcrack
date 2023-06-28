import hashlib, os
import colorama
from colorama import Fore


print(f'''{Fore.LIGHTGREEN_EX}
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░██╗███████╗░█████╗░██████╗░  
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔════╝██╔══██╗██╔══██╗  
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░███████║█████╗░░███████║██║░░██║  
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔══██║██╔══╝░░██╔══██║██║░░██║  
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗██║░░██║███████╗██║░░██║██████╔╝  
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░  

{Fore.MAGENTA}██╗░░██╗░█████╗░░██████╗██╗░░██╗{Fore.LIGHTGREEN_EX}░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
{Fore.MAGENTA}██║░░██║██╔══██╗██╔════╝██║░░██║{Fore.LIGHTGREEN_EX}██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
{Fore.MAGENTA}███████║███████║╚█████╗░███████║{Fore.LIGHTGREEN_EX}██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
{Fore.MAGENTA}██╔══██║██╔══██║░╚═══██╗██╔══██║{Fore.LIGHTGREEN_EX}██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
{Fore.MAGENTA}██║░░██║██║░░██║██████╔╝██║░░██║{Fore.LIGHTGREEN_EX}╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
{Fore.MAGENTA}╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝{Fore.LIGHTGREEN_EX}░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
''')

print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Type Of Hash You Want To Crack (md5, sha1, sha256, sha512)")
type_of_hash = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}]{Fore.MAGENTA} '))

print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Path Of The File To Crack With")
file_path = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX} '))

print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Hash Value To Crack')
hash_to_decrypt = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}'))

if os.path.exists(file_path) == False:
    print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}]{Fore.LIGHTGREEN_EX} That Path Does not Exist')
    exit(1)

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}MD5 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())
                exit(0)

        elif type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}SHA1 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())
                exit(0)

        elif type_of_hash == 'sha256':
            hash_object = hashlib.sha256(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}SHA256 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())
                exit(0)

        elif type_of_hash == 'sha512':
            hash_object = hashlib.sha512(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}SHA512 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())
                exit(0)

        else:
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Type Of Hash Is Incorrect')
            exit(1)

    print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] Password Is Not In File.')
