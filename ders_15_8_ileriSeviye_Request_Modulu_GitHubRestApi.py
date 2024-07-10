import requests

class GitHub:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'

    def getUser(self, username):
        response = requests.get(self.api_url + '/users/'+username)
        return response.json()
    
    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/'+ username+'/repos')
        return response.json()
    def createRepository(self, name):
        headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {
                "name": name,  # Depo adı
                "description": "This is a new repository",  # Depo açıklaması
                "private": False,  # Depoyu herkese açık yapmak için False, özel yapmak için True
        }
        response = requests.post(f'{self.api_url}/user/repos', json=data, headers=headers)
        return response.json()
github = GitHub()
while True:
    secim = input('1- Find USer\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeciminiz: ')
    if secim =='4':
        break
    else:
        if secim == '1': # find User
            username = input('username: ')
            result = github.getUser(username=username)
            print(f"name: {result['name']}\npublic repos: {result['public_repos']}\nfollowers:{result['followers']}")
        elif secim == '2': # Get Repositories
            username = input('username: ')
            result = github.getRepositories(username=username)
            for repo in result:
                print(repo['name'])
        elif secim  == '3': # Creaete Repository
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("Yanlis Girdi")

