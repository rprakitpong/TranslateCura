from googletrans import Translator
import polib
import os
import json

files = [('cura.pot','cura.po','cura.mo','cura.json'), ('fdmextruder.def.json.pot','fdmextruder.def.json.po','fdmextruder.def.json.mo','fdmextruder.def.json.json'), ('fdmprinter.def.json.pot','fdmprinter.def.json.po','fdmprinter.def.json.mo','fdmprinter.def.json.json'), ('uranium.pot','uranium.po','uranium.mo','uranium.json')]
# pot, po, mo, json
for _file in files:
    potFile = _file[0]
    poFile = _file[1]
    jsonFile = _file[3]
    if os.path.exists(potFile):
        os.rename(potFile, poFile)
        print(potFile + 'successfully renamed to ' + poFile + '.')
    else:
        if not os.path.exists(poFile):
            print(potFile + ' doesnt exist in directory. Please add directory before continuing.')
            exit()
        else:
            print(poFile + ' already exist in directory.')
    if not os.path.exists(jsonFile):
        with open(jsonFile,'w') as wf:
            json.dump({" ":" "}, wf)


translator = Translator()
destLang = 'th'

for _file in files:
    poFile = _file[1]
    moFile = _file[2]
    jsonFile = _file[3]

    print('Translating ' + poFile + '...')
    po = polib.pofile(poFile)

    enToDestLang = dict()
    with open(jsonFile, 'r') as fp:
        enToDestLang = json.load(fp)

    textsEN = [[]]
    currInd = 0
    maxLen = 50 # trial and error, you get about 300 translations total
    # maxLen, # of arrays, total
    # 20, 15, 300 
    # 30, 11, 330
    # 40, 9, 360
    #print("Current EN text array: " + str(currInd))
    for entry in po:
        if entry.msgid not in enToDestLang:
            #print(entry.msgid)
            if len(textsEN[currInd]) > maxLen:
                currInd = currInd + 1
                textsEN.append([entry.msgid])
                #print("Current EN text array: " + str(currInd))
            else:
                textsEN[currInd].append(entry.msgid)
        #print("Appended: " + entry.msgid)
    
    print("Start translating.")
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
    #print(enToDestLang)
    with open(jsonFile, 'w') as wf:
        json.dump(enToDestLang, wf)

    print("Editting po file.")
    for entry in po:
        if entry.msgid in enToDestLang:
            entry.msgstr = enToDestLang[entry.msgid]

    po.save()
    po.save_as_mofile(moFile)
    print("Saved as mo file.")

print('success')