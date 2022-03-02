import sys
import clipboard
import json

'''before you start your work you need to install xclip with below command
sudo apt-get install xclip
after installation you have to run it in terminal with command
xclip
'''

data = clipboard.paste()
print(data)