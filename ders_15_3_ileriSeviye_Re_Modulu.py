# Regular expressions Python diye arat hepsi çıkıyor.

# https://docs.python.org/3/library/re.html


import re 

str = "Mesut Taha Dinleyici"

# ******* re.findall()
# result = re.findall('Mesut', str)
# result = len(result)

# ********re.split()
result = re.split(" ", str)

# ******** re.sub() # belirtilen karakteri istenen karakterle değişitirir
result = re.sub(" ","-", str) # Mesut-Taha-Dinleyici
result = re.sub("\s","?", str) # \s boşlukla aynı anlama gelir (Mesut?Taha?Dinleyici)

# ******* re.search() # istenen karakterlerin konumunu verir.
# result = re.search("Taha", str) # (<re.Match object; span=(6, 10), match='Taha'>)
# result = result.span() # (6, 10)
# result = result.start() # Taha kelimesinin hangi sıradan başladığını gösterir. (6)
# result = result.group() # aradığı grubu bize geri döndürür. (Taha)
# result = result.string # hangi string ifadeyi gönderdiğimizi gösterir. (Mesut Taha Dinleyici)


# result = re.findall("[Taha]", str) # köşeli parantez olarak aratılırsa karakterleri teker teker arar. (['T', 'a', 'h', 'a'])
# result = re.findall("Taha", str) # köşeli parantez olmadığında str içersinde Taha durumuna bakar. (['Taha'])
# result = re.findall("[aTha]", str) # ['T', 'a', 'h', 'a']
# result = re.findall("[a-s]", str) # köşeli paranntez kullanımında arada tire(-) varsa aralık ifade eder (a'dan s'ye) (['e', 's', 'a', 'h', 'a', 'i', 'n', 'l', 'e', 'i', 'c', 'i'])
# M harfini almadı çünkü harf büyük M 
# result = re.findall("[^aTha]", str) # köşeli parantezden hemen sonra (^) işareti varsa belirtilen harfler veya sayılar dışındaki karakterleri arar (['M', 'e', 's', 'u', 't', ' ', ' ', 'D', 'i', 'n', 'l', 'e', 'y', 'i', 'c', 'i'])

# *************************************************************************
""" 
findall içerisindeki nokta kullanimi kadar grup arar

örnek: 
re.findall("....", str) # ['Mesu', 't Ta', 'ha D', 'inle', 'yici']
re.findall("...", str) # ['Mes', 'ut ', 'Tah', 'a D', 'inl', 'eyi']
re.findall("..", str) # ['Me', 'su', 't ', 'Ta', 'ha', ' D', 'in', 'le', 'yi', 'ci']
"""
str2 = "Python Pardon Panthon Şelale, Parrrrmekaon"
result = re.findall("P...on", str2) # ['Python', 'Pardon']
#***************************************************************************************
"""
^ - Belirtilen string karakterle başlıyor mu?
^a => a: 1 match
      abc: 1 match
      bac: No match
"""
result = re.findall("^M", str) # ['M']
result = re.findall("^Mes", str) # ['Mes']
result = re.findall("^sut Taha", str) # []
result = re.findall("^Taha", str) # []
#**************************************************************************************

"""
$ - belirtilen karakterle bitiyor mu?
a$ => a: 1 match
      lamba: 1 match
      Python: No match

"""
result = re.findall("i$", str) # ['i']
result = re.findall("Taha Din$", str) # []
result = re.findall("Taha Dinleyici$", str) # ['Taha Dinleyici']

# ***************************************************************************************

"""
* - bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder
ma*n => mn: 1 match
        man: 1 match
        maaaaaan: 1 match
        main: No match (a'nın arkasından n gelmiyor)

"""

result = re.findall("Mes*ut", str) # ['Mesut']
result = re.findall("   *Taha", str) # [' Taha'] # Taha'dan önce 3 boşluk var
result = re.findall("Mesk*ut", str) # ['Mesut']

# *****************************************************************************************

"""
+ - bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder
ma+n => mn: No match
        man: 1 match
        maaaaaan: 1 match
        main: No match (a'nın arkasından n gelmiyor)

"""

result = re.findall("Mes+ut", str) # ['Mesut']
result = re.findall("   +Taha", str) # [' Taha'] # Taha'dan önce 3 boşluk var
result = re.findall("Mesk+ut", str) # []
# ******************************************************************************************
"""
? - bir karakterin sifir ya da bir kez olmasini kontrol eder
ma?n => mn: 1 match
        man: 1 match
        maaaaaan: No match
        main: No match (a'nın arkasından n gelmiyor)

"""

result = re.findall("Mes?ut", str) # ['Mesut']
result = re.findall("   ?Taha", str) # [] # Taha'dan önce 3 boşluk var
result = re.findall("Mesk?ut", str) # ['Mesut']
# ******************************************************************************************
"""
{} - karakter sayisini kontrol eder
al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlamali
al{2,3} => a karakterinin arkasına l karakteri en az 2, en fazla 3 kez tekrarlamali
[0-9]{2,4} => en az 2 en çok 4 basamkali sayilar.

"""
str3 = " saat 51 320"
result = re.findall("a{2}",str3)# ['aa']
result = re.findall("[0-9]{2}", str3) # ['51', '32']
print(result)