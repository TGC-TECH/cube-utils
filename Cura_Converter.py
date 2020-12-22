
import os

filename = input('Enter the filename (including extension Ex: file.txt): ')
input_file = open(filename, 'r')
output = open('298ej231d928j98dh29f38fhg2983jhfsidklfj289o3jf023f823hjf9io23jf9283jf298f9283jf8sjd9f8j298fj23.txt', 'w')

for i, line in enumerate(input_file):
    if line.startswith('M101'):
        print(line)
        num=i
        break
output.write("^Firmware:V1.00\n^Minfirmware:V1.00\n^DRM:000000000000\n^PrinterModel:CUBEPRO\n^MaterialCodeE1:200\n^MaterialCodeE2:-1\n^MaterialCodeE3:-1\n^MaterialLengthE1:2.000\n^MaterialLengthE2:0.000\n^MaterialLengthE3:0.000\nG21\nG90\nM404 S40\nM542\nM104 S270\nM227 P296 S103\nM228 P23 S8\nM551 P1000 S100\nM543\nM108 S13\nM103\nG1 X13.24 Y-27 Z0.45 F9000\nG1 X13.24 Y-27 Z0.2 F210\nM101")

for i, line in enumerate(input_file):
    if i == 0:
        output.write(line)
    else:
        if line.startswith('M82'):
            output.write('M82')
        elif not line.startswith(';'):
            output.write(line)

input_file.close()
output.close()

os.remove(input_file.name)
os.rename(output.name, input_file.name)
os.system('cubepro-encoder.exe ' + input_file.name)