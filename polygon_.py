#ALIŞTIRMA 2:

'''
poligon çizen bir fonksiyon yaratalım.
fonksiyonun parametreleri, kaplumbağa, mesafe ve kenar sayısı olacak.
not: turtle.resetscreen()= t.clear()= ikisi de ekranı boşaltır.

'''
# cozum 2:

import turtle
t = turtle.Turtle() # bu satırla bir kaplumbaga yarattık

def poligon(t, uzunluk, n):
    '''
    kaplumbaga ile poligon cizen fonksiyon. 
    t= turtle tipinde nesne
    uzunluk= int tipinde mesafe
    n= int tipinde kenar sayısı
    donus derecesi = 360 / kenar sayısı almalıyız
    '''
    aci = 360/n
    for i in range(n):
        t.fd(uzunluk)
        t.lt(aci)
poligon(t, 100, 10)

turtle.mainloop()
