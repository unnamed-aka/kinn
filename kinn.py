import os,os.path
import getpass
import requests
import wget

# Find username

user = getpass.getuser()

while True:
    # User input for select and install mod
    modsel = input('Enter mod name for automatic install: ').lower()
    
    # Check mod exist and index 
    url1 = f'https://raw.githubusercontent.com/unnamed-aka/mod-index/main/{modsel}.txt'
    if (requests.get(url1)).status_code == 404:
        print('Error: mod not exists')
        continue
    else:
        # Get mod index
        modindex = (requests.get(url1)).text
        
        # Delete old mod if exists
        if os.path.exists(f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods/{modindex}'):
            os.remove(f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods/{modindex}')
        
        # Download and install mod
        url = f'https://raw.githubusercontent.com/unnamed-aka/mod-repo/main/{modindex}'
        wget.download(url,out = f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods')
        print('\nDone')
    
    