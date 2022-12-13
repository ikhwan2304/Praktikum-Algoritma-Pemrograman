#episode latihan logika dan komparasi


#membuat gabungan area rentang dari angka


#++++++3--------10++++++



inputuser=float(input("masukan angka yang bernilai\kurang dari 3\ataulebih besar dari 10\n:"))


# ++++++3---------------
#memeriksa angka kurang dari 3
isKurangDari=(inputuser<3)
print("kurang dari 3=",isKurangDari)

#--------10+++++++++++++
#memeriksa angka lebih besar dari 10
isLebihDari=(inputuser>10)
print("lebi dari 10=",isLebihDari)

#+++++++3-------10+++++++
isCorrect=isKurangDari or isLebihDari
print("angka yang anda masukan:",isCorrect)

#------3++++++++10-------
#kasus irisan
print("\n",10*"=","\n")
inputUser=float(input("masukan angka yang bernilai\nlebih dari 3\n dan\n kurang dari 10\n:"))

# -----3+++++++++++++++++
#lebih dari 3
isLebihDari=inputUser>3
print("lebih dari 3=",isLebihDari)

#+++++++++10------------
#kurang dari 10
isKurangDari=inputUser<10
print("kurang dari 10=",isLebihDari)

#------3++++++++10------
isCorrect=isKurangDari and isLebihDari
print("angka yang anda masukan:",isCorrect)