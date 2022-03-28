import requests
from bs4 import BeautifulSoup
#IF YOU HAVE MANY PAGES AND DO YOU WANT TO SEE CONTENT / detail /

# ÖRNEK 4

toplam_urun = 0
for sayfa_no in range(1,3):
    url = "https://www.n11.com/telefon-ve-aksesuarlari?pg=" + str(sayfa_no)
    r = requests.get(url)
    #print(r.status_code)
    #print(r.content)
    soup = BeautifulSoup(r.content, "lxml")
    #print(soup)
    urunler = soup.find_all("li", attrs={"class": "column"})

    for urun in urunler:
        urun_ismi = urun.a.get("title")
        urunLink = urun.a.get("href")
        print("ÜRÜN ADI: {}".format(urun_ismi))
        print("ÜRÜN LİNKİ: {}".format(urunLink))
        try:
            urun_r = requests.get(urunLink)
            toplam_urun += 1                              # Ürün detayına o an giremeyebilirdim. Doğrusu detayı görülmüş ürün olsun.Alında burada 404 de dönmüş olabilir. Doğrusu if 200 ise daha doğru olabilir.
        except Exception:
            print("Ürün Detayı Alınamadı")
        #print(urun_r.status_code)  ok 200
        urun_soup = BeautifulSoup(urun_r.content, "lxml")
        tum_teknik_ozelikler = urun_soup.find_all("li", attrs={"class": "unf-prop-list-item"})
        for i in tum_teknik_ozelikler:
            print(i.find("p", attrs={"class": "unf-prop-list-title"}).text)
            print(i.find("p", attrs={"class": "unf-prop-list-prop"}).text)
        print("#"*50)
print("Toplam ürün sayısı {}".format(toplam_urun))