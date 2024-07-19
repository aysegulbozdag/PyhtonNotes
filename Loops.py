# While

x = 1
while x <= 100:
    if x % 2 == 1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift: {x}')
    x += 1

print('bitti...')

# For

my_colours = ["Red", "Blue", "Yellow", "Purple"]

for i in my_colours:
    print(i)

# Range function
# range() fonksiyonu belirli aralıkta bulunan sayıları göstermek için kullanılır.

# range(5) 0'dan başlayıp 5'e kadar olan sayıları(5 hariç) ifade eder
for i in range(5):
    print(i)

# range(2,5) 2'den başlayıp 5'e kadar olan sayıları(5 hariç) ifade eder

for i in range(2, 5):
    print(i)

# range(2,5,2) fonksiyonu ise 2'den başlayıp 5'e kadar 2'şer artırarak devam eder, 2,4 değerlerini ifade eder.

for i in range(2, 5, 2):
    print(i)
