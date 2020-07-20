import requests
from bs4 import BeautifulSoup

from openpyxl import Workbook
wb = Workbook()
ws = wb.active

sayfalar = [21,22,23,24,25,26,27,28,29,30,31,32,33]

for sayfa in sayfalar:
    r = requests.get("http://www.tureb.org.tr/tr/RehberVeritabani/AraOda?odaId={}".format(sayfa))
    soup = BeautifulSoup(r.content,"html.parser")
    gelen_veri = soup.find_all("table",{"class":"display"})
    rehberler = gelen_veri[0].contents[3]
    rehberler_tr = rehberler.find_all("tr")
    for rehber in rehberler_tr:
        rehber_bilgileri = rehber.find_all("td")
        rehber_isimleri = rehber_bilgileri[0].text
        rehber_odasi = rehber_bilgileri[1].text
        rehber_dili = rehber_bilgileri[2].text
        rehber_no = rehber_bilgileri[3].text
        rehber_eposta = rehber_bilgileri[4].text
        rehber_durum = rehber_bilgileri[5].text
        print(rehber_isimleri,rehber_odasi,rehber_dili,rehber_no,rehber_eposta,rehber_durum)
        ws.append([rehber_isimleri,rehber_odasi,rehber_dili,rehber_no,rehber_eposta,rehber_durum])
    wb.save("hepsi.xlsx")