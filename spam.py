import requests

nomor = input("Nomor : ")
jumlah = int(input("Jumlah : "))
for i in range(jumlah):
      url = requests.get(f"https://darkteam.my.id/minispam/spamsms.php?nomor= ")