import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = " your_api_key_here"  # 

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/movie?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSeçim: ")

    if secim == "3":
        print("Çıkış yapılıyor...")
        break
    elif secim == "1":
        movies = movieApi.getPopulars()
        if 'results' in movies:
            for movie in movies['results']:
                print(movie['title'])
    elif secim == "2":
        keyword = input("Aranacak film adı: ")
        movies = movieApi.getSearchResults(keyword)
        if 'results' in movies:
            for movie in movies['results']:
                print(movie['title'])
    else:
        print("Hatalı seçim.")