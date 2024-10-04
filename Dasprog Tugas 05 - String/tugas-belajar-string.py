#Create String
str0 = "Fazle Mawla Wahyuhanda"
str1 = "5054241020"
str2 = "Semarang"

#Print String
print("Nama saya " + str0)
print("NRP saya " + str1)
print("Saya berasal dari " + str2)

#Print String with Index
print("Inisial saya adalah " + str0[0] + str0[6] + str0[12])

#Print String with Slicing
print("Nama depan saya adalah " + str0[:5])
print("Nama tengah saya adalah " + str0[6:11])
print("Nama belakang saya adalah " + str0[12:])

#Print String with Concatenation
print("Reverse nama saya adalah " + str0[::-1])

#Update String
string3 = "Saya mahasiswa RKA"
list3 = list(string3)
list3[4] = " bukan "
string3 = "".join(list3)
string3 = string3[0:20] + " RPL"
print(string3)

#Print String with replace
string4 = "Saya mahasiswa RKA"
string4 = string4.replace("mahasiswa RKA", "bukan mahasiswa RPL")
print(string4)

# tugas implementasi
# 1. deletting a character di implementasikan di kota asal, misalkan di kata "Semarang" di hilangkan p jadi "emarang"
# 2. escape sequencing in python
# 3. python string formating (contoh: 1, 2, 3, 4)

#1. Deleting Character in string
str2 = "Semarang"
str2 = str2[0:4] + str2[6:]
print(str2)

#2. Escape Sequencing
# Initial String
a = '''Hello my name is "Fazle"'''
print(a)

# Escaping Single Quote
b = 'It\'s a nice day'
print(b)

# Escaping Double Quotes
c = "Hello my name is \"Fazle\""
print(c)

# Printing Paths with the
# use of Escape Sequences
d = "My course directory is in C:\\Users\\ender\\OneDrive - Institut Teknologi Sepuluh Nopember\\"
print(d)

# Printing Paths with the
# use of Tab
e = "I pressed \ttabs"
print(e)

# Printing Paths with the
# use of New Line
f = "I pressed\nenter"
print(f)

# Printing hello in octal
oktal = "\110\151\40\111\47\155\40\106\141\172\154\145"
print(oktal)

# Using raw String to
# ignore Escape Sequences
notoktal = r"This is \106\141\172\154\145"
print(notoktal)

# Printing Geeks in HEX
hexa = "This is \x46\x61\x7a\x6c\x65 from \x49\x54\x53"
print(hexa)

# Using raw String to
# ignore Escape Sequences
nothexa = r"This is \x46\x61\x7a\x6c\x65 from \x49\x54\x53"
print(nothexa)

#3. Python String Formating
# Python Program for
# Formatting of Strings

# Default order
urut = "{} {} {}".format('I', 'Love', 'ITS')
print(urut)

# Positional Formatting
posisional = "{2} {0} {1}".format('I', 'Love', 'ITS')
print(posisional)

# Keyword Formatting
keyword = "{C} {B} {A}".format(A='I', B='Love', C='ITS')
print(keyword)

# Formatting of Integers
biner = "{0:b}".format(2024)
print("Aku masuk ITS di tahun biner " + biner)

# Formatting of Floats
pi = "{0:e}".format(3.141592653589793238462643383279502884197)
print("Exponent representation of Pi number is " + pi)

# Rounding off Integers
Pibulet = "{0:.2f}".format(3.141592653589793238462643383279502884197)
print("This is Pi number if i rounded it up -> " + Pibulet )

# String alignment
alignment = "|{:<7}|{:^12}|{:>15}|".format('Kanan',
                                          'Tengah', 
                                          'Kiri')
print(alignment)

# To demonstrate aligning of spaces
align = "I was born in {:^16} and now I'm in {:<10}!".format("Semarang","Surabaya")
print(align)

# Python Program for
# Old Style Formatting
# of Integers

angka = 123.3456789
print(angka)
print('Rounded and only show 2 numbers after comma %3.2f' % angka)
print('Rounded and only show 4 numbers after comma %3.4f' % angka)
