import string

def transcribe(word,p):
 code = word.maketrans(p,' ','')
 return word.translate(code)

dct, lst = {}, []
fr = open('rough_work.txt')
for line in fr:
 line = line.split()
 word,freq = line[:][0], line[:][1]
 for p in string.punctuation:
 	if p in word: 
 		word = transcribe(word, p)
 		line.append('Marked')
 
 
 if len(line)<3: dct[word.strip().lower()] = int(freq)
 else:
 	for word in f'{word} '.split():
 		dct[word.strip().lower()] = dct.get(word.strip().lower(), 0) + 1
 
lst,lst2 = [],[]
for key in dct.copy(): 
 	dct[key.strip().capitalize()] = dct[key]
 	dct.pop(key)
 
 
fr.close()

fc = open('clean_work.txt','w')
[ fc.write(f'{k} {v}\n') for v,k in sorted([ (v, k) for k,v in dct.items()], reverse = True) ]
fc.close()
