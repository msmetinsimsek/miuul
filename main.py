import datetime as dt



print("Hello Word!")



def say_hello(isim):
    """
    isme selam verip o anki saati söyleyen fonksiyon
    :param isim: str
    :return:
    """
    print(f"Merhaba, {isim}")
    print(f"Şu anki saat{dt.datetime.now()}")


a = input("bir isim giriniz:")

say_hello(a)

print(3)



