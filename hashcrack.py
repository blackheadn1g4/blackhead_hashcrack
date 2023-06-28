import hashlib, os
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
                

        else:
            print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Type Of Hash Is Incorrect')
            

    print(f'{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Password Is Not In File.')

print(f"{Fore.LIGHTGREEN_EX}If you want to {Fore.RED}exit{Fore.LIGHTGREEN_EX}, {Fore.LIGHTGREEN_EX}type {Fore.LIGHTGREEN_EX}'{Fore.MAGENTA}x{Fore.LIGHTGREEN_EX}'. {Fore.LIGHTGREEN_EX}If not and you would like to continue, press {Fore.LIGHTGREEN_EX}'{Fore.MAGENTA}Enter{Fore.LIGHTGREEN_EX}' {Fore.LIGHTGREEN_EX}key.")     
print("")

exit_stay = str(input(f"{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] "))

if exit_stay == "x":
  active = False
