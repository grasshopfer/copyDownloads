#! python3

# copyDownloads.py is a personal script to copy files in ~/Downloads to a
#   external hard disk. 

import os, shutil

downloadDir = os.path.expanduser('~/Downloads/')
extDir = os.path.abspath('/mnt/mybook/Downloads/')
logFile = r'/home/capn/bin/copyDownloads.log'
logText = []

# TODO add check for remaining space in target
# TODO add timing information to log
# TODO figure out timestamping
# TODO check external directory for writability

# Get list of files in ~/Downloads and externalDir
os.chdir(downloadDir)           # now running in ~/Downloads
dls = os.listdir(downloadDir)
target = os.listdir(extDir)
    
# Compare the files in Downloads against external files to avoid duplication
#   set().intersection() gives the common elements of the two sets
dupes = list(set(dls).intersection(set(target)))
# TODO check for more recent access time, if more recent, overwrite file at dest
for file in dupes:
    if file in dls:
        logText.append(file + ' already exists in ' + extDir + ', excluding. . .')
        dls.remove(file)

# Move files from home dir to external dir
for file in dls:
    logText.append('Moving ' + file + ' to ' + extDir + '. . .')
    shutil.move(file, extDir)

# Write out log file (TODO make method and write immediately)
writeLog = open(logFile,'w')
for line in logText:
    writeLog.write(line + '\n')
writeLog.close()
