import getpass

togri_parol = "python123"
urinishlar_soni = 0
maks_urinish = 3

while urinishlar_soni < maks_urinish:
    parol = getpass.getpass("Parolni kiriting: ")
    
    if parol == togri_parol:
        print("✅ Xush kelibsiz!")
        break
    else:
        urinishlar_soni += 1
        qoldi = maks_urinish - urinishlar_soni
        if qoldi > 0:
            print(f"❌ Noto‘g‘ri! Qayta urinib ko‘ring. Qolgan urinishlar: {qoldi}")
        else:
            print("⛔️ 3 marta noto‘g‘ri kiritdingiz. Kirish bloklandi.")

       
