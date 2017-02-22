import re
import time
import csv
start=[]
success=[]
fail=[]
dict1={}#starttime
dict2={}#successtime
dict3={}



f=open("test.txt")
line=f.readline()
while line:
   # print line
    line=f.readline()
    if "configiso.pl" in line and "RESPONSE" not in line :
       start.append(line)
       #print(line)
       instr=re.search('hostname=.*isotype',line)
       #print(line[:9])
       #if instr:
        #print('instr')
        #print(instr.group(0)[9:-8])
       dict1[instr.group(0)[9:-8]]=line[:8]


    if "Installation on" in line and "successful" in line:
       success.append(line)
       instr=re.search('on i.*su',line)
       print(instr.group(0))
       dict2[instr.group(0)[3:-3]]=line[:8]




    if "Installation on" in line and "fail" in line: fail.append(line)
f.close()
print('start')
#print(start)
#print(start[0])
#print(start[1])
#print(start[2])
print(dict1)

print(len(start))
print(len(success))
#print(len(fail))

print("success")
#print(success)
print(dict2)
#print('fail')
#print(fail)
#a='2017-1-1 21:08:19'
#b='2017-1-1 21:20:06'
#a1=time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
#a2=time.mktime(time.strptime(b,'%Y-%m-%d %H:%M:%S'))

#print(a1)
#print(a2)
#print(a2-a1)
#c=a2-a1
#print(str(int(c/3600))+":"+str(int((c%3600))/60)+':'+str(int(((c%3600)%60))))


r=[["Appliance","configiso",'done','Deploy Time']]
for keys in dict1:
    a="2017-1-1 "+dict1[keys]
    b="2017-1-1 "+dict2[keys]
    a1 = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
    a2 = time.mktime(time.strptime(b,'%Y-%m-%d %H:%M:%S'))
    c = a2 - a1
    d=str(int(c/3600))+":"+str(int((c%3600))/60)+':'+str(int(((c%3600)%60)))
    tmp=[]
    tmp.append(keys)
    tmp.append(dict1[keys])
    tmp.append(dict2[keys])
    tmp.append(d)
    r.append(tmp)
    tmp=[]
print(r)

with open('apple.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    for t in r:
        spamwriter.writerow(t)