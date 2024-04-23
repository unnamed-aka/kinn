import subprocess
import os, os.path
import wget
import getpass
import PySimpleGUI as sg

i = None
pinglist = []
user = getpass.getuser()

sg.theme('light gray 3')

layout = [
    
    [sg.Text('Set path to install file for mod install')],
    [sg.InputText(key='path'), sg.FileBrowse(key='path')],
    [sg.Output(size=(50,15))],
    [sg.Button('Install')]
    
    ]


window = sg.Window('Kinn', layout, icon='icon.ico')

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Install':
        try:
            file = open(values['path'], 'r')
        except:
            print('Cant open file')
        else:
            print('Read file...')
            try:
                info = (file.read()).split('|')
                info[1] = info[1].split(',')
                print(info)
            except:
                print('Wrong file format')
                continue
            else:
                i = 0
                print('Request host...')
                while True:
                    try:
                        ping = (subprocess.run(['ping', '-c', '1', f'{info[0]}{info[1][i]}'], stdout=subprocess.PIPE)).returncode
                        pinglist.extend(ping)
                        i += 1
                    except:
                        break
                if sum(pinglist) != 0:
                    print('Cant connect with host')
                    continue
                else:
                    i = 0
                    while True:
                        try:
                            if os.path.exists(f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods/{info[1][i]}'):
                                os.remove(f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods/{info[1][i]}')
                            print(f'Downloading {info[1][i]}...')
                            wget.download(f'{info[0]}{info[1][i]}', out=f'C:/Users/{user}/AppData/Roaming/KinitoPET/mods')
                            i += 1
                        except:
                            print('Done')
                            break
                        continue
                        
         