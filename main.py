from pathlib import Path
import base64

treatment = []
sanitized = []
flag = []

for p in Path( '.' ).rglob( '*' ):
    txt = str(p)
    dirArray = txt.split('/')
    for char in dirArray:
        try:
            if len(dirArray) > 2:
                if dirArray[2] not in treatment:  
                    treatment.append(dirArray[2])  
                    sanitized.append([dirArray[1], dirArray[2]])
        except:
            pass


counter = 1
while len(flag) < len(sanitized):
    for part in sanitized: 
        if int(part[1]) == counter:
            print(f'[+] Value for position {counter}: {part[0]}')
            flag.append(part[0])
            counter += 1
        else:
            pass

print('\n[+] Encoded Flag: ', ''.join(flag))

print('\n[+] Decoded Flag: ', str(base64.b64decode(''.join(flag)), "utf-8"))




