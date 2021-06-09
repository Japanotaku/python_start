
from sqlite3.dbapi2 import Error
import sqlite3
connect = sqlite3.connect('test.db')

def query_func(db_name, table_name, col_name, query_value):
    import sqlite3
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = 'SELECT ' + col_name + ' FROM ' + table_name + ' WHERE ' + col_name + ' = \"' + query_value +"\""
    cursor.execute(query)
    query_result = cursor.fetchone()
    conn.close()
    query_result = str(query_result)
    query_result = query_result[2:len(query_result)-3]
    return query_result


def crypt_xor_func(plaintext, key):
	ciphertext = ''
	for i in plaintext:
		try:
			ciphertext+=chr(ord(i)^ord(key))
		except TypeError:
			ciphertext+=chr(ord(i)^key)
			
	return ciphertext


#Функция хэширования	
def hash_md5_func(text):
	import hashlib
	textUtf8 = text.encode("utf-8")
	hash_object = hashlib.md5(textUtf8)
	hash_text = hash_object.hexdigest()
	
	return hash_text

def query_func2(db_name, table_name, col_name1,col_name2,query_value):
	import sqlite3
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	query = (' SELECT ' + col_name1 + ' FROM ' + table_name + ' WHERE ' +col_name2 + ' =\"' + query_value +"\"")
	cursor.execute(query)
	query_result = cursor.fetchone()
	conn.close()
	query_result = str(query_result)
	query_result = query_result[2:len(query_result)-3]
	
	
	return query_result



def delete_user(con,lgn):
	try:
		cursorObj = con.cursor()
		cursorObj.execute('DELETE FROM users WHERE login = ?', (lgn,))
		con.commit()
	except Error:
		print("Hey,you are bad guy", Error)
	finally:
	     if cursorObj:
							cursorObj.close()

scr_lgn = input("Login: ")


Warnings = ["Wrong password, You have two attempts left", "Wrong password, You have one attempts left", "Wrong password, You are blocked"]

flag = True

lgn = query_func('test.db','users','login',scr_lgn)



if (scr_lgn != lgn) or (len(scr_lgn) == 0):
	while (scr_lgn != lgn):
					scr_lgn = input("Login: ")
					lgn = query_func('test.db','users','login',scr_lgn)

if(scr_lgn == lgn):
    scr_psw = input("Password: ")
    psw = query_func('test.db','users','password',hash_md5_func(scr_psw))

    if (hash_md5_func(scr_psw) != psw) or (len(scr_psw) == 0):
        while(hash_md5_func(scr_psw) != psw and flag == True):
			        for i in Warnings:
												print(i)
												if(i == "Wrong password, You are blocked"):
																delete_user(connect,lgn)
																flag = False
														   
												if(i != "Wrong password, You are blocked" ):		  
													scr_psw = input("Password: ")
													psw = query_func('test.db','users','password',hash_md5_func(scr_psw))												
    if(hash_md5_func(scr_psw) == psw):
        surname = query_func2('test.db', 'users', 'surname','login',lgn)
        name = query_func2('test.db', 'users', 'name','login',lgn)
        print("Hello,"+ crypt_xor_func(surname,len(lgn)) + " " + crypt_xor_func(name,len(lgn)))