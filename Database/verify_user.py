import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='gaurav',
    passwd='1234qwer',
    database='neosphere',
)

curser = mydb.cursor()
curser.execute('SELECT * FROM users')
rows = curser.fetchall()
print(rows)

mail = input('enter email address')
password1 = input('enter password')


curser.execute("SELECT password FROM users WHERE email=%s", (mail,))
var1 = curser.fetchone()
# print(var1)
# print(type(var1))
if password1 == var1[0]:
    for row in rows:
        print(row)
else:
    print('password didnt match!')
