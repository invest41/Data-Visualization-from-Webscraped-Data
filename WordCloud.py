import load_on_excel
import load_on_database

import sqlite3
import time
import zlib
import string




x, counts = [], {}
for line in open('clean_work.txt'):
	word = line.split()[0].strip()
	x.append(word)
	counts[word] = float(line.split()[1].strip())




highest = None
lowest = None
for k in x[:100]:
    if highest is None or highest < counts[k] :
        highest = counts[k]
    if lowest is None or lowest > counts[k] :
        lowest = counts[k]
print('Range of counts:',highest,lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('gword.js','w')
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first : fhand.write( ",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest) #Scale Conversion i.e. turning celcius to farhrenheit
    size = int((size * bigsize) + smallsize)  
    fhand.write("{text: '"+k+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

print("Output written to gword.js")
print("Open gword.htm in a browser to see the vizualization\n")
