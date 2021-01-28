import Webscraping_Tool, Make_Translation
import sqlite3 as sql

conet = sql.connect('web_scrape.sqlite')
cur = conet.cursor()


cur.execute('DROP TABLE IF EXISTS USA_ANALYTICS')
cur.execute('CREATE TABLE USA_ANALYTICS (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Word TEXT, Frequency INTEGER)')


for line in open('clean_work.txt'):
	line = line.split()
	cur.execute('INSERT INTO USA_ANALYTICS (Word, Frequency) VALUES (?,?)',(line[0], line[1]))
	#cur.execute(f'INSERT INTO USA_ANALYTICS (Word, Frequency) VALUES ({line[0]}, {line[1]})')


#Save database
conet.commit()
cur.close()
