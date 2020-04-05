from googletrans import Translator
import polib
import os
import json

print(os.getcwd())

potFiles = ['cura.pot']
#potFiles = ['cura.pot', 'fdmextruder.def.json.pot', 'fdmprinter.def.json.pot', 'uranium.pot']
poExtension = '.po'
moExtension = '.mo'
poFiles = []
moFiles = []
for toRename in potFiles:
    pre, ext = os.path.splitext(toRename)
    newName = pre + poExtension
    if os.path.exists(toRename):
        os.rename(toRename, newName)
        print(toRename + 'successfully renamed to ' + newName + '.')
    else:
        if not os.path.exists(newName):
            print(pre + ' doesnt exist in directory. Please add ' + toRename + ' into directory before continuing.')
            exit()
        else:
            print(newName + ' already exist in directory.')
    poFiles.append(newName)
    moFiles.append(pre + moExtension)

translator = Translator()
destLang = 'th'

for ind in range(len(poFiles)):
    poFile = poFiles[ind]
    moFile = moFiles[ind]

    print('Translating ' + poFile + '...')
    po = polib.pofile(poFile)

    textsEN = [[]]
    currInd = 0
    currIndCharCount = 0
    maxCharCount = 12000 # 15000 is limit, but we go a little under
    print("Current EN text array: " + str(currInd))
    for entry in po:
        if currIndCharCount > maxCharCount:
            currInd = currInd + 1
            currIndCharCount = 0
            textsEN.append([entry.msgid])
            print("Current EN text array: " + str(currInd))
        else:
            textsEN[currInd].append(entry.msgid)
            currIndCharCount = currIndCharCount + len(entry.msgid)
        #print("Appended: " + entry.msgid)
    
    print("Start translating.")
    enToDestLang = dict()
    try:
        for arrayInd, arrayVal in enumerate(textsEN): 
            print("Translating array number: " + str(arrayInd))
            translations = translator.translate(arrayVal, destLang)
            for translation in translations:
                enToDestLang[translation.origin] = translation.text
    except json.decoder.JSONDecodeError:
        print("Error with googletrans. Probably exceeded translation limit. Try again in a few days.")
        if len(enToDestLang) == 0:
            exit()
    except:
        print("Some error with googletrans. Check internet?")
        if len(enToDestLang) == 0:
            exit()
    
    print("Translation done. Saving backup.")
    print(enToDestLang)
    backup = open(poFile + ".txt", "w")
    backup.write(str(enToDestLang))
    backup.close()

    print("Editting po file.")
    for entry in po:
        if entry.msgid in enToDestLang:
            entry.msgstr = enToDestLang[entry.msgid]

    po.save()
    po.save_as_mofile(moFile)
    print("Saved as mo file.")

print('success')