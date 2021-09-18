import requests,time
import csv
from bs4 import BeautifulSoup
anim=requests.get("https://anime-online.su")
soup=BeautifulSoup(anim.text, "html.parser")

with open("deneme.csv",mode="w",encoding="utf-8") as file:
    ana_data=csv.DictWriter(file,["Name","year","количество серий","озвучили","сезон","жанры"])
    # for x in soup:
    #         print(x)
    #         file.write(str(x))
    z=soup.find_all("li")
    d=0
    for x in z:
        try:
            f=x.a["href"]
            
        except :
            continue

        if d>1:
            print(f)
            if f=="#":
                continue
            
            
            sayfasayi=1
            anim=requests.get("https://anime-online.su"+f)
            soup=BeautifulSoup(anim.text, "html.parser")
            # print(soup.find_all( class_="animebox"))
            try:
                k=soup.find(class_="navigation").find_all("a")
                a=k[-1].text
                print(a)
                
            except:
                continue
            while(sayfasayi<int(a)):







                if sayfasayi==1:
                    z=soup.find_all( class_="animebox-jstip")
                    
                    for x in z:
                        try:
                            animecik=x["href"]
                            print(animecik)
                            print("-----------------")
                            anime_page=requests.get(animecik)
                            anime_soup=BeautifulSoup(anime_page.text,"html.parser")
                            isim=anime_soup.find(class_="title").text
                            anime_konu_listesi={
                                    "Name":isim,
                                    "year":None,
                                    "количество серий":None,
                                    "озвучили":None,
                                    "сезон":None,
                                    "жанры":None
                            }
                            print("aaaaaaaaa")
                            
                            bilgi=anime_soup.find(class_="meta-list")
                            find=bilgi.find_all(class_="meta-list_item")
                            for r in find:
                                elements=r.find_all("span")
                                a=str(elements[0].text)
                                print(a)
                                if a=="год:":
                                    print("ili tapdin")
                                    anime_konu_listesi["year"]=elements[-1].text
                                elif a=="озвучили:":
                                    anime_konu_listesi["озвучили"]=elements[-1].text
                                elif a=="количество серий:":
                                    anime_konu_listesi["количество серий"]=elements[-1].text
                                    print("hi")
                                elif a=="жанры:":
                                    p=elements[-1].find_all("a")
                                    anime_konu_listesi["жанры"]=[nan.text for nan in p]
                                elif a=="сезон:":
                                    anime_konu_listesi["сезон"]=elements[-1].text
                                else:
                                    continue
                            print(anime_konu_listesi)
                        except :
                            continue
                    for x in z:
                        try:
                            print(x["href"])
                        except :
                            continue
                    sayfasayi+=1




                if(sayfasayi>1):
                    
                    sayfa=requests.get("https://anime-online.su"+f+"page/"+str(sayfasayi))
                    
                    print("bu sayfadaki:"+"https://anime-online.su"+f+"page/"+str(sayfasayi))
                    corpa=BeautifulSoup(sayfa.text,"html.parser")
                    z=corpa.find_all( class_="animebox-jstip")
                    sayfasayi+=1
                    for x in z:
                        try:
                            animecik=x["href"]
                            print(animecik)
                            print("-----------------")
                            anime_page=requests.get(animecik)
                            anime_soup=BeautifulSoup(anime_page.text,"html.parser")
                            isim=anime_soup.find(class_="title").text
                            anime_konu_listesi={
                                    "Name":isim,
                                    "year":None,
                                    "количество серий":None,
                                    "озвучили":None,
                                    "сезон":None,
                                    "жанры":None
                            }
                            print("aaaaaaaaa")
                            
                            bilgi=anime_soup.find(class_="meta-list")
                            find=bilgi.find_all(class_="meta-list_item")
                            for r in find:
                                elements=r.find_all("span")
                                a=str(elements[0].text)
                                print(a)
                                if a=="год:":
                                    print("ili tapdin")
                                    anime_konu_listesi["year"]=elements[-1].text
                                elif a=="озвучили:":
                                    anime_konu_listesi["озвучили"]=elements[-1].text
                                elif a=="количество серий:":
                                    anime_konu_listesi["количество серий"]=elements[-1].text
                                    print("hi")
                                elif a=="жанры:":
                                    p=elements[-1].find_all("a")
                                    anime_konu_listesi["жанры"]=[nan.text for nan in p]
                                elif a=="сезон:":
                                    anime_konu_listesi["сезон"]=elements[-1].text
                                else:
                                    continue
                            print(anime_konu_listesi)
                        except :
                            continue
        if f=="#":
            d+=1
            print(d)
        else:
            continue
        

 