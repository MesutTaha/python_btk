import requests


class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNWU0YTllZjZjMDQ1YmYyMzljNTNlNDY2NzA2NjkyMCIsInN1YiI6IjY2NjIzYWE4YmJhODJkMWZiNzc1ZmUyZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.X-GwRadKZB3tcB_472b9pZOrbozFl-9pPNJj29t3uNA"
        # self.api_key ="e5e4a9ef6c045bf239c53e4667066920"
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
            }
    def getPopulars(self, sayfa):
        response = requests.get(self.api_url + f"movie/popular?language=en-US&page={sayfa}", headers=self.headers)
        return response.json()
    
    def getSearch(self, keyword, sayfa):
        response = requests.get(self.api_url +  f"/search/keyword?query={keyword}&page={sayfa}", headers=self.headers)
        return response.json()

class NextPage:
    def __init__(self):
        self.sayfa = 1
        self.dongu = True

    def nextPage(self, next_pg):      
        if next_pg == "y":

            self.dongu = True
            self.sayfaArttir()
        elif next_pg == "n":
            self.sayfa = 1
            self.donguDurumu()
        else:
            print("Lutfen sadece y veya n yi tuslayin")
            return next_pg
    
    def sayfaArttir(self):
        self.sayfa += 1
        return self.sayfa
    
    def donguDurumu(self):
        self.dongu = False
        return self.dongu
      
film = theMovieDb()
next_page = NextPage()
while True:
    secim = int(input("1-Popular movies\n2- Search Movies\n3- Exit\nSecim: "))
    if secim == 3:
        break
    else :
        if secim == 1:
            sayfa = 1 
            dongu = True
            while True and dongu == True:
                    result = film.getPopulars(sayfa)
                    for movie in result["results"]:
                        print(movie["title"] + ": " + str(movie["vote_average"]))
                    next_pg = input("Diger Sayfayi Gormek Istiyor Musunuz?(y/n)    ")
                    next_page.nextPage(next_pg)
                    sayfa = next_page.sayfa
                    # print(sayfa)
                    dongu = next_page.dongu
                    # print(dongu)
                    
        elif secim == 2:
            sayfa = 1 
            dongu = True
            while True and dongu == True:                 
                    if sayfa >= 2: # amaç, her sayfada tekrar keyword girmemek
                        result = film.getSearch(keyword, sayfa)
                        for movie in result["results"]:
                            print(movie["name"])
                        next_pg = input("Diger Sayfayi Gormek Istiyor Musunuz?(y/n)    ")
                        next_page.nextPage(next_pg)
                        sayfa = next_page.sayfa
                        # print(sayfa)
                        dongu = next_page.dongu
                        # print(dongu)
                    else:
                        keyword = input("Anahtar Kelime Giriniz: ") # sadece ilk sayfada keyword giriyos
                        result = film.getSearch(keyword, sayfa)
                        for movie in result["results"]:
                            print(movie["name"])
                        next_pg = input("Diger Sayfayi Gormek Istiyor Musunuz?(y/n)    ")
                        next_page.nextPage(next_pg)
                        sayfa = next_page.sayfa
                        # print(sayfa)
                        dongu = next_page.dongu
                        # print(dongu)
                
