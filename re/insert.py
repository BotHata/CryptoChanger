import sqlite3
import time


db = sqlite3.connect('db/main.db')

with db:
	db.execute("INSERT INTO reviews (id, name, cont, time) VALUES (24, 'Имран', 'Нашёл этот обменник, так как тут была самая низкая коммисия. Обменял, перевели не так уж быстро, всё заняло часа два.', (?))", (time.time(),))
	db.execute("INSERT INTO reviews (name, cont, time) VALUES ('олололл', 'Обменяли норм', (?))", (time.time(),))
	db.execute("INSERT INTO reviews (name, cont, time) VALUES ('александр', 'можно было бы и побыстрее', (?))", (time.time(),))
	db.execute("INSERT INTO reviews (name, cont, time) VALUES ('Corsair', 'Сволочи кинули на 3000 рублей и вату катают', (?))", (time.time(),))
	db.execute("INSERT INTO reviews (name, cont, time) VALUES ('Служба поддержки', 'Corsair, уважаемый клиент! Вам уже не один раз объяснили, что Вы совершили ошибку и при обмене вместо указанных банков (Сбербанк, Тинькофф, Альфа-банк, ВТБ), предоставили номер Райффайзен банка. Вам вернули деньги за вычетом комиссии банка, впредь будьте внимательными!', (?))", (time.time(),))

# db.execute("INSERT INTO news (id, cont, time) VALUES (28, 'Александр', 'Заебись обменник', (?))", (time.time(),)c