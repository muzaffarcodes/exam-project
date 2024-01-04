import sqlite3
import time

contact = sqlite3.connect("music_archive.db")

index = contact.cursor()

def enter_table():
	index.execute("CREATE TABLE IF NOT EXISTS music_archive (Nomi Text, Yili Text, Davlati Text, Vaqti Text, Bastakori Text, Turi Text, Olchami Text)")
	contact.commit()
enter_table()

def add_infos(nomi,yili,davlati,vaqti,bastakori,turi,olchami):
	index.execute("INSERT INTO music_archive VALUES (?,?,?,?,?,?,?)",(nomi,yili,davlati,vaqti,bastakori,turi,olchami))
	contact.commit()

def get_all():
	index.execute("SELECT * FROM music_archive")
	info = index.fetchall()
	print("Sabr...")
	print("\n")
	time.sleep(2)
	for i in info:
		print(*i)

def get_one():
	index.execute("SELECT * FROM music_archive WHERE Nomi = ?",(input("Qaysi Musiqani Ko'rasiz?:"),))
	info = index.fetchall()
	print("Sabr...")
	print("\n")
	time.sleep(2)
	for i in info:
		print(*i)

def update_nom():
	index.execute("UPDATE music_archive SET Nom = ? WHERE Nomi = ?",(input("Qanday nomga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def update_yil():
	index.execute("UPDATE music_archive SET Yili = ? WHERE Nomi = ?",(input("Qaysi yilga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def update_dav():
	index.execute("UPDATE music_archive SET Davlati = ? WHERE Nomi = ?",(input("Qanday davlatga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def update_time():
	index.execute("UPDATE music_archive SET Vaqti = ? WHERE Nomi = ?",(input("Qanday vaqtga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def update_musician():
	index.execute("UPDATE music_archive SET Bastakori = ? WHERE Nomi = ?",(input("Qanday bastakorga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def update_type():
	index.execute("UPDATE music_archive SET Turi = ? WHERE Nomi = ?",(input("Qanday turga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def update_size():
	index.execute("UPDATE music_archive SET Bastakori = ? WHERE Nomi = ?",(input("Qanday o'lchamga: "),input("Qaysi Musiqani o'zgartiray: "),))
	contact.commit()

def del_one():
	index.execute("DELETE FROM music_archive WHERE Nomi = ?",(input("Qaysi Musiqani O'chiray?: "),))
	contact.commit()

def del_all():
	index.execute("DELETE FROM music_archive")
	contact.commit()

def write_only1():
	index.execute("SELECT * FROM music_archive WHERE Nomi = ?",(input("Qaysi Musiqa'ning ma'lumotini yozdirmoqchsiz?: "),))
	info = index.fetchall()
	with open("one_music.txt","a") as face:
		for i in info:
			string = str(i)
			face.write(string)
			face.write("\n")

def write_all():
	index.execute("SELECT * FROM music_archive")
	info = index.fetchall()
	with open("all_musics.txt","a") as face:
		for i in info:
			string = str(i)
			face.write(string)
			face.write("\n")

def password_show():
	print("""Password: 1122
Hech kimga aytmang!!!""")

def tizimga_kir():
	db_login = 'gulchapchap'
	db_passwd = 1122
	login = input("Loginni kiriting: ")
	passwd = int(input("Password'ni kiriting: "))
	if login == db_login and passwd != db_passwd:
		print("\nPassword xato!")
	elif login != db_login and passwd == db_passwd:
		print("\nUser xato!")
	elif login != db_login and passwd != db_passwd: 
		print("\nPassword va User ham xato!")
	else:
		print("\nTizimga Xush Kelibsiz!!!")
	while True:
		admin_tanlovi = int(input("""\n -> Zemeister Xush kelibsiz <-
Menu:
1. Ma'lumot qo'shish;
2. Hamma musiqa haqidagi ma'lumotni o'chirish;
3. Bitta musiqa haqidagi ma'lumotni o'chirish;
4. Ma'lumotlarni hammasini ko'rish;
5. Ma'lumotlarni bittasini ko'rish;
6. Ma'lumotlarni yangilash;
7. Bitta musiqani faylga yozdirish;
8. Hamma musiqani faylga yozdirish;

0. Chiqish uchun ->

Tanlang: """))
		if admin_tanlovi == 1:
			nomi = input("Nomi: ")
			yili = input("Yili: ")
			davlati = input("Davlati: ")
			vaqti = input("Vaqti: ")
			bastakori = input("Bastakori: ")
			turi = input("Turi: ")
			olchami = input("O'lchami: ")
			add_infos(nomi,yili,davlati,vaqti,bastakori,turi,olchami)
			print("\nMa'lumotlar qo'shildi!")
		elif admin_tanlovi == 2:
			del_all()
			print("\nHamma musiqaning ma'lumotlari o'chirildi!")
		elif admin_tanlovi == 3:
			del_one()
			print("\nBitta musiqa haqidagi ma'lumot o'chirildi!")
		elif admin_tanlovi == 4:
			get_all()
		elif admin_tanlovi == 5:
			get_one()
		elif admin_tanlovi == 6:
			update_tanlovi = int(input(""" Qaysi Ma'lumotni yangilay:
1. Nomni yangilash;
2. Yilni yangilash;
3. Davlatni yangilash;
4. Vaqtni yangilash;
5. Bastakorni yangilash;
6. Turni yangilash;
7. O'lchamini yangilash;

Tanlang: """))
			if update_tanlovi == 1:
				update_nom()
			elif update_tanlovi == 2:
				update_yil()
			elif update_tanlovi == 3:
				update_dav()
			elif update_tanlovi == 4:
				update_time()
			elif update_tanlovi == 5:
				update_musician()
			elif update_tanlovi == 6:
				update_type()
			elif update_tanlovi == 7:
				update_size() 
			else: 
				print("1-7 orasida son kiriting!")

		elif admin_tanlovi == 7:
			write_only1()
			print("\n1 musiqa faylga yozdirildi!")
		elif admin_tanlovi == 8:
			write_all()
			print("\nHamma musiqa faylga yozdirildi!")
		elif admin_tanlovi == 0:
			print("\nAdmin paneldan chiqdingiz!!!")
			break

while True:
	tanlov = int(input("""\n -$- Music Archive'ga xush kelibsiz -$- \n
1. Ma'lumotlarni ko'rish;
2. Tizimga kirish;
3. Password'ni olish;

0. Chiqish uchun ->

Tanlang: """)) 
	if tanlov == 1:	
		get_all()
	elif tanlov == 2:
		tizimga_kir()
	elif tanlov == 3:
		password_show()
	elif tanlov == 0:
		print("\nHayr, salomat bo'ling!")
		break

contact.close()