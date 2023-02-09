import sqlite3

db = sqlite3.connect("rod.db")

c = db.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS user( 
surname txt,
name txt,
year_of_birth integer,
hobby txt,
scores integer
)

    """);

c.execute("INSERT INTO user VALUES ('Елсуков','Николай',2002,'футбол',10)")
c.execute("INSERT INTO user VALUES ('Токсонбаев','Ислам',2004,'Баскетбол',10)")
c.execute("INSERT INTO user VALUES ('Турдалиев','Асылбек',2006,'Genghin',8)")
c.execute("INSERT INTO user VALUES ('Жанышбеков','Нурсултан',2004,'FIFA2023',9)")
c.execute("INSERT INTO user VALUES ('Ташболот у','Ажибек',2006,'Genshin',10)")
c.execute("INSERT INTO user VALUES ('Огонбаев','Бакытбек',2006,'Шахмат',8)")
c.execute("INSERT INTO user VALUES ('Макамбаев','Самат',2006,'CS:GO',9)")
c.execute("INSERT INTO user VALUES ('Касымова','Захро',2006,'Не знаю',10)")
c.execute("INSERT INTO user VALUES ('Кадыров','Асхат',2005,'Python',10)")
c.execute("INSERT INTO user VALUES ('Райымжанов','Марлен',2006,'Не знаю',10)")


c.execute("UPDATE user SET scores = 'genius' WHERE scores >= 10")

c.execute("SELECT rowid, surname FROM user WHERE LENGTH(surname) >= 10 ")

c.execute("SELECT * FROM user where scores == 'genius'")

c.execute("DELETE FROM user WHERE rowid % 2 == 0")


print(c.fetchall())


item = c.fetchall()

for el in item:
    print(el)


db.commit()
db.close()