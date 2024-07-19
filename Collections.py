# Dictionary
# Sözlük veri tipi anahtar-değer çiftlerinden oluşur. Her bir anahtar bir değeri temsil eder ve bu değerlere erişim anahtar üstünden olur.
# Bir sözlük içinde aynı anahtara sahip birden fazla anahtar-değer çifti bulunamaz. Bu özellik sayesinde anahtarlar ile değerlere erişim sağlanır.
# Bu veri tipi anahtar ile erişimi sayesinde, büyük ve karmaşık verilerle çalışırken veriye daha hızlı erişmemizi sağlar.
# Dictionary veri tipi değiştirilebilir (mutable) bir veri tipidir. Yani anahtar-değer çiftleri eklenebilir, güncellenebilir veya silinebilir.
# Anahtar kısmı için immutable (değiştirilemez) veri tipleri kullanılır. Çünkü anahtarlar benzersiz olmalıdır. Anahtar kısmında string, integer,float,boolean,tuple dictionary anahtarları olarak kullanılabilir. Değer kısmı için ise tüm veriler kullanılabilir.

dictionary = {"çilek": 40, "erik": 50, "ananas": 100}
print(dictionary.get("erik"))

# Tuple
# Python’da “tuple” (demet), birden çok veri öğesini bir araya getirmek için kullanılan ve değiştirilemez (immutable) veri tiplerinden biridir.
# Tuple’lar, parantezler içinde tanımlanır ve virgülle ayrılan öğelerden oluşur.
# Tuple’lar, listelere benzerdir ancak değiştirilemez özellikleri vardır, yani bir kez oluşturulduktan sonra öğelerini değiştiremezsiniz.
# Tuple’lar, verilerin değiştirilmesini önlemek için kullanılır.

my_tuple = ("bird", 1, "pencil", 1.5, 2)
print(my_tuple)

# Boş liste oluşturma
my_empty_list = []

# liste oluşturma

fruits = ["banana", "apple", "watermelon"]
print(fruits[1])

# Set
# Python’da set veri tipi, benzersiz ve sırasız elemanların bir koleksiyonunu temsil eder.
# Setler, süslü parantezler içinde tanımlanır ve virgülle ayrılan öğelerden oluşur.
# Bir set, her bir elemandan yalnızca bir tane içerir.
# Set veri tipi de dictionary ve liste gibi değiştirilebilir (mutable) bir veri tipidir.
# Elemanları ekleme, çıkarma ve değiştirme gibi işlemlerle değiştirilebilir.
# Setler, matematiksel küme işlemlerini destekleyen bir veri tipidir.
# İki veya daha fazla seti birleştirme, kesişimini bulma, farkını bulma gibi işlemleri gerçekleştirmek için setler kullanılabilir.

my_number = {"1", "2", "3"}
print(my_number)
