#Url library request over the internet


url=input('Input URL\n')
#url = 'http://data.pr4e.org/romeo.txt'
#url = 'https://www.py4e.com/data_space/content.sqlite.zip'

#url = 'https://analytics.usa.gov/'

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen(url)
counts = dict()

fhtm = open('webscrape.html','w')
for line in fhand:
 #print(line)
 try: fhtm.write(f'{line.decode()}')
 except: continue
 try: words = line.decode().split()
 except: continue
 for word in words:
  counts[word] = counts.get(word, 0) + 1

sh=sorted([(v,k) for k,v in counts.items()],reverse=True)

co, lst = 0, []
fh = open('rough_work.txt','w') 
try: [ fh.write(f'{i[1]} {i[0]}\n') for i in sh]
except Exception as e:
	lst.append(e)
	co+=1

if co<2: print(f'{co} issue...')
else: print(f'{co} issues...')
[print(f'{i}') for i in lst],print()


fhtm.close()
fh.close()
print('File Written...\n')
