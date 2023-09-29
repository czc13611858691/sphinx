from os import system
from time import localtime, strftime
import re

nowTime = strftime('%Y-%m-%d %H:%M:%S', localtime())
f = open('./CHANGELOG.md', 'r+', encoding='UTF-8')
CommitMsgStr = []
verstr = ''

EnterGetMsgFlg = 0
for line in f.readlines():
    if EnterGetMsgFlg == 0:
        scan_res = re.search(r'##', line)
        if scan_res != None:
            EnterGetMsgFlg = 1
            res = re.findall("## (.*)", line)
            verstr = res[0]
    elif EnterGetMsgFlg == 1:
        scan_res = re.search(r'##', line)
        if scan_res != None:
            break
        if line != '\n':
            CommitMsgStr.append(line.replace('\n', ''))

# print(CommitMsgStr)
system('git add .')
temp = 'git commit -m'
temp = temp+' '+'"'+verstr+'"'
for i in CommitMsgStr:
    temp = temp+' -m '+'"'+i+'"'
system(temp)
temp = 'git tag -a '+verstr
for i in CommitMsgStr:
    temp = temp+' -m '+'"'+i+'"'
system(temp)
system('git push -tags')
