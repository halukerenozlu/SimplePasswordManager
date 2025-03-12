import random


def sifre_ekle(*args):
    sifreler.append(args[0])
    return args[0]


def sifre_sil():
    if sifreler:
        return sifreler.pop()
    else:
        return "Silinecek sifre yok!"


def sifre_listele() -> list:
    print(sifreler)
    return sifreler


def sifre_random():
    x = random.randint(1000, 9999)
    sifre_ekle(x)
    return x


sifreler = []
random_sifre = None
sifre = None
print('Kurallar: En az 4 haneli ve sayisal')
while True:
    cevap = input('Random sifre olustur (Y/n): ')
    if cevap == 'Y':
        random_sifre = sifre_random()
        print(f'Random sifre: {random_sifre}')
        sifre_listele()
        break
    elif cevap == 'n':
        sifre = int(input('Lutfen sifre girin: '))
        sifre_ekle(sifre)
        sifre_listele()
        break
    else:
        print('Geçersiz giriş! Lütfen sadece "Y" veya "n" girin.')

cevap = input("Şifre silmek ister misiniz? (Y/n): ")
if cevap == 'Y':
    deleted_sifre = sifre_sil()
    print(f'Silinen şifre: {deleted_sifre}')
    sifre_listele()

# sorun var
while True:
    if sifre is not None and sifre in sifreler:
        if 1000 <= sifre <= 9999:
            print(f'Sifre: {sifre} eklendi.')
        else:
            print(f'Sifreniz: {sifre} kurallara uymuyor')
    else:
        print('İşlem tamam')
    break
