import sys, os

if len(sys.argv) < 2:
    print('usage: ' + sys.argv[0] + ' file.exe\n')
    sys.exit(0)

shellcode = ''
bytes_ = 0

for b in open(sys.argv[1], 'rb').read():
    print('\\' + hex(b), end="\r", flush=True)
    shellcode += '\\' + hex(b)
    #print(shellcode,flush=True)
    bytes_ += 1

print ('Number of bytes for file ' + sys.argv[1] + ': ' + str(bytes_) + '\n')

fp=open(sys.argv[0].split("\\")[len(sys.argv[0].split("\\")) - 1] + ".shell.txt", "w")
fp.write(shellcode)
fp.close()

print("Done!")
