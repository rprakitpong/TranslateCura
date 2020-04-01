from googletrans import Translator
#from translate import Translator

t = Translator()
s = t.translate('haha',dest='th')
if s:
    print(s.text)