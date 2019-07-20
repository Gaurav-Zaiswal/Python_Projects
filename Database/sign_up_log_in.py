'''sign up page. create a user for the database'''

import mysql.connector


class Datastore:

    def __init__(self):
        self.mydb = mysql.connector.connect(
        host='localhost',
        user='gaurav',
        passwd='1234qwer',
        database='neosphere',
        )


    def sign_up(self, email, passwd):
        cursor_var = self.mydb.cursor()
        cursor_var.execute('SELECT password FROM users WHERE email = %s;', (email,))
        store_if_avilable = self.cursor_var.fetchone()
        if store_if_avilable == None:
            self.cursor_var.execute('INSERT INTO USERS(email, password) VALUES(%s, %s);', (email, passwd,))
            self.mydb.commit()
            print('Your entry has been registered!')
        else:
            print('email should be unique...')

    def log_in(self):
        cursor_var1 = self.mydb.cursor()
        login_email = input('enter your email:')
        login_pass = input('enter your password')
        cursor_var1.execute('SELECT password FROM users WHERE email = %s;', (login_email,))
        user_pass = cursor_var1.fetchone()
        # print(user_pass)
        if user_pass == None:
            print('Login Failed. Either you are not registered or your login credential didnt match...')

        elif user_pass[0] == login_pass:
            print('Login Successful!!!')

    def password_reset(self):
        cursor_var2 = self.mydb.cursor()
        cursor_var3 = self.mydb.cursor()
        login_email = input('enter your email:')
        cursor_var2.execute('SELECT password FROM users WHERE email = %s;', (login_email,))
        current_pass_from_db = cursor_var2.fetchone()
        if current_pass_from_db == None:
            print('Email not found..')
        else:
            current_pass = input('Enter your current Password:')
            if current_pass_from_db[0] == current_pass:
                new_pass = input('Enter New Password')
                cursor_var3.execute('UPDATE password =%s FROM users WHERE email =  %s;', (new_pass, login_email,))
                print('apple')
                self.mydb.commit()
                print('Password Reset Successful!')
            else:
                print("Password didn't match..")

conn = Datastore()
# conn.log_in()
# conn.sign_up('ghj@ghj.com', '12345')
conn.password_reset()
