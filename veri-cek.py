import requests
from bs4 import BeautifulSoup
url = "http://www.tureb.org.tr/tr/RehberVeritabani/AraOda?odaId=21"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

# Kütüphanelerimizi ve linklimizi ekledik

gelen_veri = soup.find_all("table",{"class":"display"})

# Burada gelen_veri'ye url'mizden bize dönen sayfadaki kaynakları arayıp "class'ı display olan <table> nesnesini buluyor"

# Şimdi ise <table>'ın içinde tam olarak neler var ve aslında bizim istediğimiz neler onlara bakacağız.

# print(len(gelen_veri[0].contents))
# print(gelen_veri[0].contents)

# çıktı olarak bize 5 adet eleman dönüyor(\n,<thead>,\n,<tbody> gibi) ve bizim aradığımız bilgiler <tbody> etiketleri arasında.

rehberler = gelen_veri[0].contents[3]
#print(rehberler)

# Burda 3. indisi seçmemizin sebebi <tbody> karşılık geliyor olmasındandır. Aradığımız bilgiler şayet <thead> arasında olsaydı 1. indisi seçmeliydik.

rehberler_tr = rehberler.find_all("tr")
#print(rehberler_tr)

# Artık dahada indirgemeye başladık. Aradığımız bilgiler <tbody> etiketleri arasındaki <tr> etiketleri arasında olduğu için bütün <tr>'leri getirdik.

for rehber in rehberler_tr:
    rehber_bilgileri = rehber.find_all("td")
    rehber_isimleri = rehber_bilgileri[0].text
    print(rehber_isimleri)

# Dahada indirgeyerek <td> etiketlerimizi bulduk ve "rehber_bilgileri" ne atadık. Ardından 0. indisindeki verileri yani ad ve soyadlarını "rehber_isimleri"'ne atayıp
# döngünün yardımıyla teker teker yazdırmayı başardık