import pyperclip
import sys

def memeText(memeText):

    editedText = []
    editedText = [v.upper() if i % 2 != 0 else v.lower() for i,v in enumerate(memeText)]
    meme = ''.join(editedText)
    pyperclip.copy(meme)
    print(meme)

try:
    memeText(sys.argv[1])
except:
    print('Invalid argument')