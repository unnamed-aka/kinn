import os,os.path
import getpass
import requests
import wget

# Find username

user = getpass.getuser()

while True:
    # User input for select and install mod
    modsel = input('Enter mod name for automatic install: ').lower()
    
    # Create URL for mod install
    url = f'https://raw.githubusercontent.com/unnamed-aka/mod-repo/main/{modsel}.zip'
    
    # Get status code
    r = (requests.get(f'https://github.com/unnamed-aka/mod-repo/blob/main/{modsel}.zip')).status_code
    
    # Check status code
    if r != 404:
        # Delete old mod if exists
        if os.path.exists(f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods/{modsel}.zip'):
            os.remove(f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods/{modsel}.zip')
            
        # Install new mod
        wget.download(url,out = f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods')
        print('\nDone')
    else:
        # Error
        print(f'Error: {modsel}.zip not found')