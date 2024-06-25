# included japanese and chinese characters
# included special characters such as musical note

import re
import os
directory = os.getcwd()
'''testing comment'''

for filename in os.listdir(directory):
    '''name of this script must be excluded'''
    if filename != "srt_to_vtt.py":
        f = open(filename, "r+")
        y = re.sub(r'\n([一-龯\u3040-\u309F\u30A0-\u30FFa-zA-Z"\'.,;:!♪\-（?])', r"\1", f.read())
        x = re.sub(r"\n0", "0", y)
        f.close()
        f = open(filename, "w")
        f.write(x)
print(x)