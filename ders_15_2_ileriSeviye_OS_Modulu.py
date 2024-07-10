import os # OS(Operating Systems)
import datetime
result = os.name # işletim sistemi (nt) = (Windows nt)

# ****** Dizin Değiştirme
# os.chdir('C:\\') # aşağıdaki işlemleri C klasörüdnde gerçekleştirir.
# os.chdir('..') # Bir üst klasöre geçer (C:\Users\mesut_rhuqwru\Desktop\Codesl)
# os.chdir('..\..') # İki üst klasöre geçer (C:\Users\mesut_rhuqwru\Desktop)

# ***** Klasör Oluşturma
# os.mkdir("Deneme_sil") # Klasör oluşturur.
# os.makedirs("Silll/bunu_da_sil2") # klasör içerisinde klasör oluşturma
# os.rename('Deneme_sil', "Silll") # Klasör ismi değiştirme
# os.rmdir("Silll/bunu_da_sil") # klasör silme
# os.removedirs("Silll/bunu_da_sil") # klasör silme

# ****** Listeleme
# result = os.listdir() # Bu klasördeki dosyalar
# result = os.listdir('C:\\') # C klasöründeki dosyalar
# for dosya in os.listdir():
#     if dosya.endswith('.py'): # sadece .py uzantılı dosyaları listeler.
#         print(dosya)

#******** Etkin Dizin Gösterme
# result = os.getcwd() # bu dosyanın hangi klasörde bulunduğunu gösterir (C:\Users\mesut_rhuqwru\Desktop\Codes\Vs Code)

# ******* Dosya Bilgilerine Erişme
result = os.stat('ders_8_3_OOP_class_method.py') # dosya hakkında bazı bilgiler
# result = result.st_size/1024 #kb türünde dosya boyutu
# result = datetime.datetime.fromtimestamp(result.st_ctime) # dosyanın oluşturulma zamanı
# result = datetime.datetime.fromtimestamp(result.st_atime) # dosyaya son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # dosyanın son değiştirilme tarihi

# os.system("notepad.exe") # notepad açar


# ******** Path
# result = os.path.abspath("ders_8_6_OOP_class_Quiz_app.py") # İstenen dosyanın path'ini verir
# result = os.path.dirname("c:/Users/mesut_rhuqwru/Desktop/Codes/Vs Code/ders_15_2_ileriSeviye_OS_Modulu.py") # dosyanın dizin ismini verir
# result = os.path.dirname(os.path.abspath("ders_8_6_OOP_class_Quiz_app.py")) # dosyanın dizin ismi için iki kod ie içe kuullanılır (C:\Users\mesut_rhuqwru\Desktop\Codes\Vs Code)
# result = os.path.exists("ders_8_6_OOP_class_Quiz_app.py") # dosya/klasör var mı yok mu kontrol eder (True/False)
# result = os.path.isdir("c:/Users/mesut_rhuqwru/Desktop/Codes/Vs Code2")# klasör mü değil mi veya klasör var mı yok mu (true/false)
# result = os.path.isfile("c:/Users/mesut_rhuqwru/Desktop/Codes/Vs Code/ders_15_2_ileriSeviye_OS_Modulu.py") # dosya mı değil mi veya dosya var mı yok mu (true/false)
result = os.path.join("C:\\", "deneme1", "deneme2")# yapay path oluşturma (C:\deneme1\deneme2)
result = os.path.split("C:\\deneme1")# pathi ayırma (('C:\\', 'deneme1'))
result = os.path.splitext("ders_8_6_OOP_class_Quiz_app.py") # dsoya adı ve uzantısını ayırır
print(result)