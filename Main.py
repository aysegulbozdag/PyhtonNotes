import ModuleExample

# a = input('Adınızı giriniz')
# print("Merhaba", a)

# yorum satırı


# String oluşturmak için  tek tırnak (‘ ‘) veya çift tırnak (” “) kullanılabilir.
# Birden çok satırlı string oluşturmak için üç tırnak (“”” “””) kullanılır.

name = "Ayşegül"
print("name değerinin bir karakteri: ", name[0])

# Negatif indeks sayesinde, karakterlere sağdan sola negatif değerler ile de erişebilirsiniz.
# Negatif indeks -1 ile başlar. En sondaki karakter, aynı zamanda sağdan sola bakıldığında ilk karakterdir.
# Bu karaktere -1 değeri ile ulaşabilirsiniz.

surname = "Bozdağ"
print(surname[-1])

# stringdeki ilk üç ve son üç karaktere erişmek için:

ornek_a = "kasaba"
print(ornek_a[:3], ornek_a[3:])

# String’de birden çok karaktere ulaşmak için dilimleme (slicing) işlemleri uygulanır.
# Dilimleme işlemi sırasında köşeli paranteze başlangıç ve bitiş indeksi değerleri girilmelidir.
# Bu işlem sırasında, başlangıç indeksinin dahil olarak sayıldığı, bitiş indeksinin ise dahil olarak sayılmadığı unutulmamalıdır.

print(surname[2:5])

# Bazı durumlarda, string içerisinde almak istediğiniz dilimi belirli bir aritmetik kurala göre almak isteyebilirsiniz.
# Mesela, belirlediğiniz aralıktaki tüm karakterleri değil, başlangıç karakterinden 2 karakter arayla almak isteyebilirsiniz.
# Bunu yapabilmek için başlangıç, bitiş indeks değerlerinin yanı sıra aralık değerini belirtmeniz gerekmektedir

ornek_a = "kasaba"
print(ornek_a[1:6:2])

# String Güncelleme

surname = "Fırat"
print(surname)

# String uzunluk ölçülmesi

print(len(surname))

# String dönüştürme

sayi = 90
print(str(sayi))

print('Module example: ' + ModuleExample.name)


