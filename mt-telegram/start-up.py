# Rights Reserved, 2024 ©
# All rights reserved  Creator : Ali Rahman - 1.0 Beta -Usename Telegarm :- @lvvvlvv.
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions, and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following disclaimer in the documentation and/or other materials provided with the distribution.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from flask import request
import requests
from rich.console import Console
from time import sleep  
import datetime
import webbrowser
console = Console()
def search_word(url, word):      
    count = 0
    while True:
        try:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            console.print("|| [black]Starting Tracking in :[/black] " , current_time)
            while True:
                response = requests.get(url)
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
                if word in response.text:
                    count += 1
                    console.print(f"|| [green]{current_time}[/green] || [bright_blue]@ {username}[/bright_blue] ==> [green][200][/green] User Can take !!. | {count} |")
                else:
                    count += 1
                    console.print(f"|| [magenta]{current_time}[/magenta] || [bright_blue]@ {username}[/bright_blue] ==> [red][400][/red] User Failed   !!. | {count} |")
                sleep(1)
        except Exception as e:
            console.print(f"|| [bright_red]ERROR: The Server Disable Connection Foe You ! {e}[/bright_red]")
console.print("""[bright_blue]                                                                                                                                                      
                           +                                                             =        
                         .#                                                              =*       
                         %+                                                              :%.      
                        .%#                                                              -%=      
                        .%%.                                                             #%+      
                         %%%                                                            +%%=      
                         %%%%                                                          =%%%:      
                         -%%%%:                                                       %%%%%       
                          #%%%%%                          --=                       #%%%%%        
                           *%%%%%%.                     @@@@@@@@-                 #%%%%%%         
                            -%%%%%%%*.                 +@@@@@@%--=             =%%%%%%%#          
                          =.  *%%%%%%%%*               +@@@@@.              -%%%%%%%%%.  +        
                           #%   +%%%%%%%%%%   .%       @@@@@@.      =*   +%%%%%%%%%%   +%.        
                            %%%.   *%%%%%%%%%%   @@@@@@@@@@@@@@@@@@-  +%%%%%%%%%%.   *%%:         
                             *%%%%=   :%%%%%%%%%:  %@@@@@@@@@@@@@.  #%%%%%%%%+   :#%%%%.          
                               #%%%%%%#-=#%%%%%%%#   @@@@@@@@@@:  -%%%%%%%%=-+%%%%%%%-            
                                 .#%%%%%%%%%%%%%%%%   =@@@@@@@   =%%%%%%%%%%%%%%%%+               
                                #-    .#%%%%%%%%%%%=    @@@@.    %%%%%%%%%%%%-     %:             
                                  %%%%%##%#%%%%%%%%%     @@:    #%%%%%%%%#%###%%%%-               
                                    .=%%%%%%%%%%%%%%      .     %%%%%%%%%%%%%%*:                  
                                            -*%%%%%%   #     *  %%%%%%%=.                         
                                          :#%%%%%%%=  *@+  .@@   %%%%%%%%+                        
                                                 -%   @@@: @@@*  =%                               
                                                 #   @@@@@@@@@@=  -+                              
                                                .  =@@@@@@@@@@@@@   :                             
                                                  @@@%@@@@@@@@@#@@-                               
                                                @@@= @@@@@@@@@@- @@@.                             
                                              :@@%  @@:@@@@@@+@@  :@@#                            
                                              @@   @@= @@@@@@+ @@*  %@.                           
                                              @  =@@  #@@  #@@  @@@  #.                           
                                                 @@  .@@    @@@  +@+                              
                                                 @   @@*     @@.  @*                              
                                                 -   @@      #@+   :                              
                                                     @@      +@+                                  
                                                     #@      #@                                   
                                                      +%    :@ [/bright_blue]   
                                              
                  ||[b][green] Username Telegram Tracking MT Tools[/green][/b]  |   [green][b]Creator : Ali Rahman - 1.0 Beta[/green][/b] ||
                                                                                   
                                                ||[b][red] Ctrl + C to Exit  [/b][/red]||                                          
                                                                                                  """)
console.print("\n\n")

check = console.input("||[b][dark_blue] Disclaimer: Use at own risk ![/dark_blue][/b]\n|| [b][magenta]The speed of the tool depends on the Internet and your processor[/magenta][/b]           \n|| [b][green]1) Single Username Tracking [Fast][/b][/green]\n|| [b][green]2) Multi Username Tracking [/b][/green]\n|| 3) [b][red]To Exit Tool  [/b][/red] \n||\n|| [b][magenta]Please Enter Your Choice: [/b][/magenta]")
url_word = "Telegram"
if check == '1':
    username = console.input("|| [b][red]Please Enter Username: [/red][/b]")
    url = f"https://fragment.com/username/{username}"
    word = "Unavailable"
    search = console.input("|| [b][magenta]Do You Want Simple Search For The Usernamr [ [green]yes[/green] | [red] no {Skip} [/red] ]: [/magenta][/b]")
    if search == 'yes':
        url_search = "https://t.me/" + username
        webbrowser.open(url_search)
        sleep(5)
        search_word(url, word)
    elif search == 'no':
        search_word(url, word)
elif check == '2':
    username = console.input("|| [b][red]Please Enter Username: [/red][/b]")
    url = f"https://fragment.com/username/{username}"
    console.print("|| [yellow]Soon ...[/yellow]")
elif check == '3':
    console.print("|| [yellow]THX Using My Too .. Bye ! [/yellow]  ")
else:
    console.print("|| [bright_red]ERROR: Invalid choice. Please enter either 1 or 2 or Exit.[/bright_red]")