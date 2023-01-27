import os.path
import PySimpleGUI as sg
import re

source_folder_column = [
    [
        sg.Text("Source Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(key="-SOURCEFOLDER-"),
    ]
]

target_folder_column = [
    [
        sg.Text("Target Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(key="-TARGETFOLDER-"),
    ]
]

project_name = [
    sg.Text('Project Name'),
    sg.Input(key="-PROJECTNAME-")
]

user_initials = [
    sg.Text('User Initials'),
    sg.Input(key="-USERINITIALS-")
]

instrument_used = [
    sg.Text('Instrument Used'),
    sg.Input(key="-INSTRUMENTUSED-")
]

# ----- Full layout -----
layout = [
    [source_folder_column],
    [target_folder_column],
    [user_initials],
    [project_name],
    [instrument_used],
    [sg.Button('Rename Folder')]
]

window = sg.Window("Gredig Lab File Renamer", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Rename Folder":
        folder = values["-SOURCEFOLDER-"]
        saveFolder = values["-TARGETFOLDER-"]
        proj = values["-PROJECTNAME-"]
        initials = values["-USERINITIALS-"]
        tData = values["-INSTRUMENTUSED-"]


        date = "20" + folder[-6:]
        pRAW = os.listdir(folder)
        

        for f in pRAW:
            if f.endswith('.txt'):
                splitString = f.split('_')
                sampleName = splitString[0][0:2]+'20'+splitString[0][2:]
                endPhrase = splitString[1][:-4]
                addInfo = re.findall(r'[A-Za-z]+', endPhrase)[0]
                if addInfo == 'Pos':
                    addInfo = 'Post'
                elif addInfo == 'Pra':
                    addInfo = 'Practice'
                
                imNum = re.findall(r'[^(A-Za-z)]+', endPhrase[0])[0][-2:]
                newName = "_".join([date, proj, initials, tData, sampleName, prepost, imNum]) + '.ibw'
                newName = os.path.join(saveFolder, newName)
                oldName = os.path.join(folder, f)
                print(f"Old Name: {oldName}")
                print(f"New Name: {newName}")
                os.rename(oldName, newName)


window.close()
