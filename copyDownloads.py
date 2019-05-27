#! python3

# copyDownloads.py is a personal script to copy files in ~/Downloads to a
#   external hard disk. 

import os, shutil, sys

myName = sys.argv[0]
downloadDir = os.path.abspath(os.path.expanduser('~/Downloads/'))
extDir = os.path.abspath('/mnt/mybook/Downloads/')
logFile = os.path.join(os.path.dirname(os.path.realpath(__file__)),myName+'.log')

# TODO accept args for to and from
# TODO add check for writability and remaining space in target
# TODO add timing information to log
# TODO figure out timestamping

# Write to log file as messages occur
def writeLog(text):
    log = open(logFile,'a')
    log.write(text + '\n')
    log.close()

writeLog('Beginning script')
# Get list of files in ~/Downloads and externalDir
target = os.listdir(extDir)
dls = os.listdir(downloadDir)
    
# Compare the files in Downloads against external files to avoid duplication
#   set().intersection() gives the common elements of the two sets
dupes = list(set(dls).intersection(set(target)))
# TODO check for more recent access time, if more recent, overwrite file at dest
for file in dupes:
    if file in dls:
        writeLog('\t' + file + ' already exists in ' + extDir + ', excluding. . .')
        dls.remove(file)

# Move files from home dir to external dir
for file in dls:
    writeLog('\tMoving ' + file + ' to ' + extDir + '. . .')
    shutil.move(file, extDir)

writeLog('Terminating script.')
