import hashlib
import os
import colorama
from pystyle import *
from colorama import Fore

intro = '''
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░██╗███████╗░█████╗░██████╗░  
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔════╝██╔══██╗██╔══██╗  
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░███████║█████╗░░███████║██║░░██║  
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔══██║██╔══╝░░██╔══██║██║░░██║  
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗██║░░██║███████╗██║░░██║██████╔╝  
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░  

██╗░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
███████║███████║╚█████╗░███████║██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
██║░░██║██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
                        Press Enter >>>
'''

Anime.Fade(
    Center.Center(intro),
    Colors.green_to_red,
    Colorate.Vertical,
    interval=0.035,
    enter=True,
)

print(f'''{Fore.LIGHTGREEN_EX}                        by Blackheadn1ga
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

while True:
    print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Choose an option:")
    print("")
    print(f"{Fore.WHITE}[{Fore.MAGENTA}1{Fore.WHITE}] {Fore.LIGHTGREEN_EX}HASH CRACKER")
    print(f"{Fore.WHITE}[{Fore.MAGENTA}2{Fore.WHITE}] {Fore.LIGHTGREEN_EX}HASH GENERATOR")
    print(f"{Fore.WHITE}[{Fore.MAGENTA}3{Fore.WHITE}] {Fore.LIGHTGREEN_EX}HASH TYPE CHECKER")
    print("")
    option = input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}')
#hash cracker
    if option == "1":
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Running this code...\n")

        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Type Of Hash You Want To Crack (md5, sha1, sha256, sha512)")
        type_of_hash = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}]{Fore.MAGENTA} '))

        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Path Of The File To Crack With")
        file_path = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX} '))

        print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Hash Value To Crack')
        hash_to_decrypt = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}'))

        if os.path.exists(file_path) == False:
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}]{Fore.LIGHTGREEN_EX} That Path Does not Exist')

        with open(file_path, 'r') as file:
            for line in file.readlines():
                if type_of_hash == 'md5':
                    hash_object = hashlib.md5(line.strip().encode())
                    hashed_word = hash_object.hexdigest()
                    if hashed_word == hash_to_decrypt:
                        print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}MD5 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())

                elif type_of_hash == 'sha1':
                    hash_object = hashlib.sha1(line.strip().encode())
                    hashed_word = hash_object.hexdigest()
                    if hashed_word == hash_to_decrypt:
                        print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}SHA1 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())

                elif type_of_hash == 'sha256':
                    hash_object = hashlib.sha256(line.strip().encode())
                    hashed_word = hash_object.hexdigest()
                    if hashed_word == hash_to_decrypt:
                        print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}SHA256 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())

                elif type_of_hash == 'sha512':
                    hash_object = hashlib.sha512(line.strip().encode())
                    hashed_word = hash_object.hexdigest()
                    if hashed_word == hash_to_decrypt:
                        print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Found {Fore.MAGENTA}SHA512 {Fore.LIGHTGREEN_EX}Password: ' + line.strip())
#hash generator
    elif option == "2":
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Running Hash Generator...\n")

        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter Text To Hash")
        text = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}'))
        print("")
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Choose Type Of Hash (md5, sha1, sha256, sha512)")
        type_of_hash = str(input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}'))

        if type_of_hash == 'md5':
            hash_object = hashlib.md5(text.encode())
            hashed_text = hash_object.hexdigest()
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}MD5 Hash: ' + hashed_text)

        elif type_of_hash == 'sha1':
            hash_object = hashlib.sha1(text.encode())
            hashed_text = hash_object.hexdigest()
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}SHA1 Hash: ' + hashed_text)

        elif type_of_hash == 'sha256':
            hash_object = hashlib.sha256(text.encode())
            hashed_text = hash_object.hexdigest()
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}SHA256 Hash: ' + hashed_text)

        elif type_of_hash == 'sha512':
            hash_object = hashlib.sha512(text.encode())
            hashed_text = hash_object.hexdigest()
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}SHA512 Hash: ' + hashed_text)
    
#hash type checker
    elif option == "3":
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Running Hash Type Checker...\n")

        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Enter a Hash Value")
        hash_value = input(f'{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] {Fore.LIGHTGREEN_EX}')
        print("")

        if len(hash_value) == 32:
            print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hash Type: MD5")
        elif len(hash_value) == 40:
            print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hash Type: SHA1")
        elif len(hash_value) == 64:
            print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hash Type: SHA256")
        elif len(hash_value) == 128:
            print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Hash Type: SHA512")
        else:
            print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Unknown Hash Type")

    else:
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Invalid Option. Please Choose Either 1, 2, or 3")
