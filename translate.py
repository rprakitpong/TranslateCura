from googletrans import Translator
import polib
import os

print(os.getcwd())

potFiles = ['cura.pot', 'fdmextruder.def.json.pot', 'fdmprinter.def.json.pot', 'uranium.pot']
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
dest_lang = 'th'

for ind in range(len(poFiles)):
    poFile = poFiles[ind]
    moFile = moFiles[ind]

    print('Translating ' + poFile + '...')
    po = polib.pofile(poFile)

    texts_en = []
    for entry in po:
        text_en = entry.msgid
        texts_en.append(text_en)
    

    po.save()
    po.save_as_mofile(moFile)

print('success')
a = input()