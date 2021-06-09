action = str(input("""                                 Choose your actions: ٩(｡•́‿•̀｡)۶
			|	1) Authorise(A)                    |
			|	2) Register(R)                     |
			|	3) Quit the programme(Q)           |
			|	4) Change the login to another (T) |
			
			 
		Your choice: """))

import time
import sqlite3
rare = sqlite3.connect('test.db')

def crypt_xor_func(plaintext, key):
	ciphertext = ''
	for i in plaintext:
		try:
			ciphertext+=chr(ord(i)^ord(key))
		except TypeError:
			ciphertext+=chr(ord(i)^key)
			
	return ciphertext

def sql_update(con,choice_new_login,choose_login):
	asd = "UPDATE users SET login = '"
	asd += choice_new_login
	asd +="' WHERE login = '"
	asd +=choose_login
	asd +="';"
	time.sleep(1)
	print(1)
	time.sleep(1)
	print(2)
	time.sleep(1)
	print(3)
	time.sleep(1)
	print(4)
	time.sleep(1)
	print(5)
	cursorObj = con.cursor()
	cursorObj.execute(asd)
	con.commit()

def sql_update2(con,choice_new_name,choose_login):
	asd = "UPDATE users SET name '"
	asd += choice_new_name
	asd +="' WHERE name = '"
	asd +=choose_login
	asd +="';"
	print(asd)
	time.sleep(1)
	print(1)
	time.sleep(1)
	print(2)
	time.sleep(1)
	print(3)
	time.sleep(1)
	print(4)
	time.sleep(1)
	print(5)
	cursorObj = con.cursor()
	cursorObj.execute(asd)
	con.commit()

while (True):
  if (action == "Q"):
	  exit() 
  elif (action == "T"):
	  choose_login = input("Введите логин который хотите поменять: ")
	  choice_new_login = input("На какой логин вы хотите поменять?: ")  
	  sql_update(rare,choice_new_login,choose_login)
	  print("Success")
	  exit()
  elif (action == "L"):
	  choose_login = input("Введите логин который хотите поменять: ")
	  choice_new_name = input("На какое имя вы хотите поменять?: ")  
	  sql_update2(rare,choice_new_name,choose_login)
	  print("Success")
	  exit()
  elif (action == "A"):
	  import aut 
	  break
  elif (action == "R"):
	  import reg_new 
	  break
  else:
      print("Try again")
      break

	