import os, sys, time
def main (kata):
        for e in kata:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.2)

main("""
\033[1;32mSilahkan Masukkan Username & Password Anda

\033[1;92matau silahkan Hubungi MRR \033[1;37mwa 083177336282
""")

username = 'Dona'      

password = 'Maref'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;33mLogin berhasil !!..", 

			sys.exit()



		else:

			print "\033[1;91mMaaf Masukkan password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;91mMaaf Masukkan Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
