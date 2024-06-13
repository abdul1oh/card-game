import random

class Karta():
    def __init__ (self, rang, raqam):
        self.rang = rang
        self.raqam = raqam

    def rangi(self):
        return self.rang

    def raqam(self):
        return self.raqam

    def __repr__(self) -> str:
        '''
        Print qilganda chiroyliroq turgani.
        Bu metodsiz print() ishlatsangiz <__main__.Karta object at 0x0000025A6EBF7310> deb chiqaradi.
        __repr__ print qilganda nima ko'rsatsin degani.
        Endi print ishlatsangiz "rang - raqam" qilib ko'rsatadi kartani.
        '''
        return f"{self.rang} - {self.raqam}"
    def __eq__(self,boshqa_karta):
        return self.rang == boshqa_karta.rang and self.raqam == boshqa_karta.raqam

class Kartalar():
    def __init__(self):
        self.kartalar = []
        for rang in ["qizil", "sariq", "yashil", "ko'k"]:
            for raqam in range(10):
                self.kartalar.append(Karta(rang, raqam))

    def aralashtirish(self):
        """
        Saralangan kartalarni aralashtirib yuborish. Hechnima qaytarmaydi! self.kartalarni o'zgartiring holos!

        Yordam:
        list = [1, 2, 3, 4]
        random.shuffle(list)
        print(list) # listga nima bo'ldi?

        """
        # Ko'd shuyerga yozing
        random.shuffle(self.kartalar)


    def saralash(self):
        '''
        Hamma kartalarni yana saralab qo'yish. Hechnima qaytarmaydi! self.kartalarni o'zgartiring holos!
        __init__ da qilganingizni qayta ishlatsangiz bo'laveradi.
        '''
        self.__init__()


    def karta_olish(self):
        """
        Eng tepasidagi kartani qaytarib beradi. Kartalar ichidan chiqarib yuborish kerak.
        """
        return self.kartalar.pop(0)

    def boshmi(self):
        """
        Kartalar borligini tekshirib beradi. Hamma kartalarni ishlatib yuborgan bo'lsa, self.kartalar bo'sh bo'lishi kerak.
        self.kartalar bo'sh bo'lsa True
        self.kartalar bo'shmas bo'lsa False
        """
        if len(self.kartalar) == 0:
            return True
        elif len(self.kartalar) != 0:
            return False

    def toplash(self):
        """
        Agar kartalarni tarqatib yuborgan bo'lsak, hammasini to'plagani metod. self.kartalar yana to'ldirib qo'ying.
        __init__ bilan saralash metodda qilganingizni qayta ishlatsangiz bo'laveradi.
        """
        self.__init__()



def aralashtirib_ikkiga_bolish(kartalar):
    kartalar.aralashtirish()
    odam1 = []
    odam2 = []
    son = 1
    while  kartalar.boshmi() != True:
        if son % 2 == 1:
            odam1.append(kartalar.karta_olish())
        elif son % 2 == 0:
            odam2.append(kartalar.karta_olish())
        son += 1
    '''Kartalarni aralashtirib, ikkala odamga tarqating
    Birinchi karta odam1ga, ikkinchi karta odam2ga, uchunchi karta odam1ga,'''

    return odam1, odam2

def karta_bormi(kartalar_list, tanlagan_karta):
    if tanlagan_karta in kartalar_list:
        return True
    else:
        return False

kartalar = Kartalar()
odam1, odam2 = aralashtirib_ikkiga_bolish(kartalar)
tanlangan_karta1 = Karta("sariq",1)

def ishlatish(odam1, odam2):
    while odam1 and odam2:
        karta1 = random.choice(odam1)
        odam1.remove(karta1)
        print(odam2)
        karta2_rang= input("Karta rangini tanlang:")
        karta2_raqam = int(input("endi raqamini tanlang:"))
        karta2 = Karta(karta2_rang, karta2_raqam)
        # karta2 = Karta(*karta2.split(" - "))
        print("O'yin:", karta1, "va", karta2)
        if karta_bormi(odam2,karta2) == True:
            if karta1.raqam < int(karta2.raqam):
                odam1.append(karta1)
                odam1.append(karta2)
                print("Siz yutdingiz!")
            else:
                odam2.append(karta1)
                odam2.append(karta2)
                print("Odam 1 yutdi!")
            print("Odam 1:", len(odam1), "Odam 2:", len(odam2), "kartalar")
        else:
            print("bunday karta mavjud emas")
    if not odam1:
        return "Siz yutdingiz!"
    else:
        return "Odam 1 yutdi!"
javob = ishlatish(odam1, odam2)
print(javob)
















