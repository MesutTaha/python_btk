import json
import os

class User:
    def __init__(self, username,password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:

    def __init__(self):
        self.users = [] # .json dosyası içindeki kullanıcılara erişmek için
        self.isLoggedIn= False
        self.currentUser= {}


        # load users from .json file
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as f:
                users = json.load(f) # liste tipinde kullanıcılara ulaşılıyor, bir dosya nesnesidir liste içerisinde istenen veriye ulaşılamaz
                # direkt olarak username: mesut verisine ulaşılamadığı için veri dictionary yapısına çevrilmeli.
                # print(type(users)) # <class 'list'>
                # print(users[0]) # {"username": "mesut", "password": "1234", "email": "mmm"}
                for user in users:
                    # json formatını çevirerek python içinde dictionary olarak ulaşabilmek için:
                    user = json.loads(user)
                    # print(type(user)) # <class 'dict'>
                    # print(user) # {'username': 'mesut', 'password': '1234', 'email': 'mmm'}
                    newUser = User(username=user['username'], password=user['password'], email=user['email']) # kullanıcı bilgileri sınıflarına ayrılıyor.
                    self.users.append(newUser) # .json dosyası içindeki kullanıcılara sınıflarına bölünmüş bir şekilde erişiliyor.


    def register(self, user: User): # user verisi User classında kullanılıyor.
        self.users.append(user)
        self.savetoFile()
        print('Kullanici olusturuldu')

    def login(self, username, password):

        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login yapildi')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Cikis yapildi")

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Giris yapilmadi')

    def savetoFile(self):
        list = []

        for user in self.users:
            # user listesini tamamen sözlük (dictionary) yapısına çeviriyor
            list.append(json.dumps(user.__dict__))
            
        with open('users.json', 'w') as f:
            json.dump(list, f) # kullanıcı verilerini .json dosyasına ekliyor

repository = UserRepository()

while True:
    print('Menü'.center(50, '*'))
    secim = int(input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n Seciminiz: '))
    if secim == 5:
        break
    else:
        if secim == 1:
            username = input("User-Name: ")
            password = input("Password: ")
            email = input("E-mail: ")

            user = User(username= username, password= password, email= email)
            repository.register(user=user)
        elif secim == 2:
            username = input("User-Name: ")
            password = input("Password: ")

            repository.login(username=username, password=password)
        elif secim == 3:
            repository.logout()
        elif secim == 4:
            repository.identity()
        else:
            print("Hatali islem yaptiniz lutfen tekrar deneyin.")
            secim = int(input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n Seciminiz: '))


