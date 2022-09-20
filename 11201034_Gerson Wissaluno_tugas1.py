
#1.Buatlah fungsi sum_squares yang menerima sebuah list integer dan mengembalikan sebuah integer yang merupakan penjumlahan dari kuadrat elemen list input!
#>>>sum_squares(1,2,3)
#...     14
#jawaban
def sum_squares (x,y,z):
  return x**2 + y**2 + z**2
x,y,z = [1,2,3]
hasil = sum_squares(x,y,z)
print(hasil)

#2.Bilangan triangular adalah penjumlahan bilangan positif tersebut dengan seluruh bilangan bulat positif sebelumnya. Contohnya bilangan triangular ke-5 adalah 5+4+3+2+1. Buatlah fungsi triangular yang menerima bilangan bulat positif n dan mengembalikan bilangan triangular yang ke-n!
#>>> triangular(5)
#...    15
#jawaban

def triangular(n):
    total = 0
    if n < 0:
        return "only accept positive number"
    if n == 1:
        return 1
    while n > 0:
        total += n
        n -= 1
    return total


print(triangular(5))

#3.Buatlah fungsi pangkat tanpa menggunakan fungsi pangkat yang sudah ada default bahasa pemrograman, input dibatasi hanya untuk bilangan bulat positif
#>>> pangkat(3, 2)
#...    9

def pangkat(x,y):
  if y == 0:
    return 1
  else:
    return x* pangkat(x,y-1)

x  = int(input("masukan x:"))
y  = int(input("masukan y:"))

print("%d dipangkatkan %d =%d" % (x,y,pangkat(x,y)))


#4.Palindrome adalah kata yang dibaca sama dari depan ataupun belakang. Contohnya “Madam, I’m Adam”, “No lemon, no melon” dan lain-lain. Buatlah sebuah fungsi yang menerima string dan mengembalikan Boolean untuk mengecek apakah string tersebut palindrome atau tidak.
#>>> is_palindrome ("rotator")
#...     True

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
s = "hello world"
testing = reverse(s)

print ("string awal:",end="")
print(s)

print(reverse(s))
if reverse(testing):
  print("true")
else:
  print("false")
