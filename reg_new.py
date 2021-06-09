def check_login_func(db_name, table_name, login):
	import sqlite3
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	check_query = ('SELECT login FROM ' + table_name + ' WHERE login = \"' + login +"\"")
	cursor.execute(check_query)
	lgn = cursor.fetchone()
	conn.close()
	lgn = str(lgn)
	lgn = lgn[2:len(lgn)-3]
	
	if (lgn == login):
		result = 'EXIST'
	else:
		result = 'FREE'
	
	return result
	

def create_record_func(db_name, table_name, login, password, name, surname, status):
	result = '?????'
	import sqlite3
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	create_query = ('INSERT INTO ' + table_name + ' (login, password, name, surname, status) VALUES (\'' + login + '\', \'' + password + '\', \'' + name + '\', \'' + surname + '\', \'' + status + '\');')
	cursor.execute(create_query)
	conn.commit()

	check_query = ('SELECT login FROM ' + table_name + ' WHERE login = \"' + login +"\"")
	cursor.execute(check_query)
	lgn = cursor.fetchone()
	conn.close()
	
	lgn = str(lgn)
	lgn = lgn[2:len(lgn)-3]
	
	if (lgn == login):
		result = 'SUCCESS'
	else:
		result = 'FAILED'
	
	return result

def crypt_xor_func(plaintext, key):
	ciphertext = ''
	for i in plaintext:
		try:
			ciphertext+=chr(ord(i)^ord(key))
		except TypeError:
			ciphertext+=chr(ord(i)^key)
			
	return ciphertext

def hash_md5_func(text):
	import hashlib
	textUtf8 = text.encode("utf-8")
	hash_object = hashlib.md5(textUtf8)
	hash_text = hash_object.hexdigest()
	
	return hash_text
	
print("Please, complete the sign up form")
i = 1
while (i <= 5):
	scr_lgn = input("Login: ")
	check_login = check_login_func('test.db', 'users', scr_lgn)
	if (check_login == 'EXIST'):
		print('Login \"' + scr_lgn + '\" is already exist. \nYou have ' + str(5 - i) + ' tries to choose another login...')
		i = i + 1
	else:
		scr_psw = input("Password: ")
		hash_scr_psw = hash_md5_func(scr_psw)
				
		scr_name = input("Name: ")
		crypt_scr_name = crypt_xor_func(scr_name, len(scr_lgn))
		scr_surname = input("Surname: ")
		crypt_scr_surname = crypt_xor_func(scr_surname, len(scr_lgn))
		result = create_record_func('test.db', 'users', scr_lgn, hash_scr_psw, crypt_scr_name, crypt_scr_surname, 'A')
		print(result)
		break