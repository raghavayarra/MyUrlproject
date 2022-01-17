import subprocess
# read the input text file

with open('input.txt') as f:
    command_list=[line.rstrip() for line in f]

# get list of commands from input file.
cmds=[]
for command in command_list:
    cmds.append(command)

# executing the commands and sae the console output in new file
s=open('output.txt','wb')
for cmd in cmds:
    out=subprocess.check_output(cmd,shell=True)
    s.write(out)
s.close()
