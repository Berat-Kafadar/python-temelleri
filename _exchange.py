import requests
import json

api_key = "10382383fb135ec9925423e1"
api_url =  f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü: ") # usd, try
alinan_döviz = input("Alınan döviz türü: ") # TRY
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ")) # ne kadar USD

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alinan_döviz])

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_döviz], alinan_döviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz,miktar * sonuc_json["conversion_rates"][alinan_döviz], alinan_döviz))