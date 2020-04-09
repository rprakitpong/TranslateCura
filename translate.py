from googletrans import Translator
import polib
import os
import json

# initialize file names
files = [('cura.pot','cura.po','cura.mo','cura.json'), ('fdmextruder.def.json.pot','fdmextruder.def.json.po','fdmextruder.def.json.mo','fdmextruder.def.json.json'), ('fdmprinter.def.json.pot','fdmprinter.def.json.po','fdmprinter.def.json.mo','fdmprinter.def.json.json'), ('uranium.pot','uranium.po','uranium.mo','uranium.json')]
# pot: original
# po: to be read
# mo: to be saved
# json: for saving translation progress

# create po and json files
for _file in files:
    potFile = _file[0]
    poFile = _file[1]
    jsonFile = _file[3]

    # rename pot to po
    if os.path.exists(potFile):
        os.rename(potFile, poFile)
        print(potFile + 'successfully renamed to ' + poFile + '.')
    else:
        if not os.path.exists(poFile):
            print(potFile + ' doesnt exist in directory. Please add it to the directory before continuing.')
            input('Press any key to end.')
            exit()
        else:
            print(poFile + ' already exist in directory.')
    
    # create json
    if not os.path.exists(jsonFile):
        with open(jsonFile,'w') as wf:
            json.dump({" ":" "}, wf) # need to write placeholder entry or json.load will fail

# initialize translator
translator = Translator()
destLang = 'th'

# translate each po file
for _file in files:
    print('') # blank line makes it easier to see

    poFile = _file[1]
    moFile = _file[2]
    jsonFile = _file[3]

    print('Initializing ' + poFile + '...')
    # open po file
    po = polib.pofile(poFile)

    # load translation progress from json, into dictionary 
    enToDestLang = dict()
    with open(jsonFile, 'r') as fp:
        enToDestLang = json.load(fp)

    # create array of texts from po file, to do bulk translation
    textsEN = [[]]
    maxLen = 50 
        # i got maxLen from trial and error, so far I've tried:
        # maxLen, # of arrays, total
        # 20, 15, 300 
        # 30, 11, 330
        # 40, 9, 360
        # you can probably go higher and not get kicked
    for entry in po:
        # if text is not already translated
        if entry.msgid not in enToDestLang:
            # if current text array is not maxed out
            if len(textsEN[-1]) > maxLen:
                textsEN.append([entry.msgid])
            else:
                textsEN[-1].append(entry.msgid)

    print('Start translating...')
    try:
        # for all text arrays
        for arrayInd, arrayVal in enumerate(textsEN): 
            # bulk translation of each text array
            print('Translating array number: ' + str(arrayInd))
            translations = translator.translate(arrayVal, destLang)
            for translation in translations:
                # save each translation to dictionary
                enToDestLang[translation.origin] = translation.text
    except json.decoder.JSONDecodeError:
        # this error gets thrown once you hit limit 
        print('Error with googletrans. Probably exceeded translation limit. Try again in a few days.')
        if len(enToDestLang) == 0:
            # nothing got translated, so just end program
            input('Press any key to end.')
            exit()
    except:
        # this is for some other error
        print('Some error with googletrans. Check internet?')
        if len(enToDestLang) == 0:
            # nothing got translated, so just end program
            input('Press any key to end.')
            exit()
    
    # save all translations so far
    print('Translation done. Saving backup.')
    with open(jsonFile, 'w') as wf:
        json.dump(enToDestLang, wf)

    # enter translationed text into po 
    print('Editting po file.')
    for entry in po:
        if entry.msgid in enToDestLang:
            entry.msgstr = enToDestLang[entry.msgid]

    # save po and mo 
    po.save()
    po.save_as_mofile(moFile)
    print('Saved as mo file.')

# everything is translated. yay :D
input('Press any key to end.')