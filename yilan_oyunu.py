# Yılan Oyunu - Pygame ile Geliştirildi
# Seviye Sistemi, Hız Artışı, Bomba Engeli ve MOBİL SWIPE Kontrolleri Eklendi.

import pygame
import time
import random

# Pygame'i başlat
pygame.init()

# --- Oyun Ayarları ---
GENISLIK = 800
YUKSEKLIK = 600
EKRAN = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Yılan Oyunu - Mobil Uyumlu")

# --- Renkler (RGB) ---
SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
KIRMIZI = (213, 50, 80)     # Yiyecek
KOYU_YESIL = (0, 150, 0)    # Yılan
BOMBA_RENGI = (255, 255, 0) # Bomba (Sarı)
ARKA_PLAN = (10, 20, 30)    # Koyu Arka Plan
SKOR_RENGI = (255, 255, 100)
SWIPE_ESIK_DEGERI = 20 # Swipe (kaydırma) olarak algılanması için minimum hareket pikseli

# Yılan ve Yiyecek boyutları
YILAN_BLOK_BOYUTU = 20
BASLANGIC_HIZI = 15

# Fontlar
FONT_STIL = pygame.font.SysFont("bahnschrift", 25)
SKOR_FONTU = pygame.font.SysFont("comicsansms", 35)

# Oyun Hızı Kontrolü
SAAT = pygame.time.Clock()

def puan_goster(skor, seviye):
    """Skoru ve Seviyeyi ekranın sol üst köşesine yazar."""
    puan_text = SKOR_FONTU.render("Puan: " + str(skor), True, SKOR_RENGI)
    seviye_text = SKOR_FONTU.render("Seviye: " + str(seviye), True, BEYAZ)
    
    EKRAN.blit(puan_text, [10, 10])
    EKRAN.blit(seviye_text, [10, 50])

def yilanimizi_ciz(yilan_liste):
    """Yılanın tüm parçalarını ekrana çizer."""
    for x in yilan_liste:
        pygame.draw.rect(EKRAN, KOYU_YESIL, [x[0], x[1], YILAN_BLOK_BOYUTU, YILAN_BLOK_BOYUTU])

def bomba_ciz(bombalar):
    """Tüm bombaları ekrana çizer."""
    for b in bombalar:
        pygame.draw.circle(EKRAN, BOMBA_RENGI, (b[0] + YILAN_BLOK_BOYUTU // 2, b[1] + YILAN_BLOK_BOYUTU // 2), YILAN_BLOK_BOYUTU // 2)

def mesaj_goster(msg, renk):
    """Oyun bitiminde mesajı ekranda ortalar."""
    mesaj = FONT_STIL.render(msg, True, renk)
    # Mesajı ekranın ortasına konumlandırır
    EKRAN.blit(mesaj, [GENISLIK / 6, YUKSEKLIK / 3])

def rastgele_pozisyon_uret(engellenen_alanlar):
    """Yiyecek veya bomba için, yılanın veya diğer engellerin olmadığı rastgele bir pozisyon üretir."""
    while True:
        pos_x = round(random.randrange(0, GENISLIK - YILAN_BLOK_BOYUTU) / YILAN_BLOK_BOYUTU) * YILAN_BLOK_BOYUTU
        pos_y = round(random.randrange(0, YUKSEKLIK - YILAN_BLOK_BOYUTU) / YILAN_BLOK_BOYUTU) * YILAN_BLOK_BOYUTU
        yeni_pozisyon = [pos_x, pos_y]
        
        # Üretilen pozisyonun engellenen alanlarda (yılan, diğer bombalar) olup olmadığını kontrol et
        if yeni_pozisyon not in engellenen_alanlar:
            return pos_x, pos_y

def oyun_dongusu():
    """Oyunun ana döngüsü."""
    oyun_bitti = False
    oyun_kapanisi = False
    
    # --- Seviye ve Hız Ayarları ---
    seviye = 1
    yilan_hizi = BASLANGIC_HIZI
    hedef_puan = 15 
    bomba_sayisi = 0 

    # Yılanın başlangıç pozisyonu
    x1 = GENISLIK / 2
    y1 = YUKSEKLIK / 2

    # Yılanın başlangıçtaki hareket değişikliği (hız)
    x1_degisiklik = 0
    y1_degisiklik = 0

    # Yılan listesi ve uzunluğu
    yilan_liste = []
    yilan_uzunlugu = 1

    # Bomba pozisyon listesi
    bombalar = []

    # Swipe başlangıç pozisyonu (Touch/Fare Başlangıcı)
    swipe_start_pos = None

    # İlk yiyecek pozisyonu 
    yiyecekx, yiyeceky = rastgele_pozisyon_uret(yilan_liste)
    
    # --- Ana Oyun Döngüsü ---
    while not oyun_bitti:

        # --- Oyun Bitti Ekranı ---
        while oyun_kapanisi == True:
            EKRAN.fill(ARKA_PLAN)
            
            final_skor = yilan_uzunlugu - 1
            mesaj_goster(f"Oyun Bitti! Puanınız: {final_skor} | Son Seviye: {seviye}", KIRMIZI) # KIRMISI düzeltildi -> KIRMIZI
            mesaj_goster("Yeniden Oynamak için R'ye, Çıkmak için Q'ya Basın.", BEYAZ)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        oyun_bitti = True
                        oyun_kapanisi = False
                    if event.key == pygame.K_r:
                        oyun_dongusu() 
                if event.type == pygame.QUIT:
                    oyun_bitti = True
                    oyun_kapanisi = False

        # --- Kontrol ve Hareket ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            
            # 1. KLAVYE KONTROLLERİ (Masaüstü için)
            if event.type == pygame.KEYDOWN:
                # Hareket yönünün tersine gitmeyi engelle
                if event.key == pygame.K_LEFT and x1_degisiklik == 0:
                    x1_degisiklik = -YILAN_BLOK_BOYUTU
                    y1_degisiklik = 0
                elif event.key == pygame.K_RIGHT and x1_degisiklik == 0:
                    x1_degisiklik = YILAN_BLOK_BOYUTU
                    y1_degisiklik = 0
                elif event.key == pygame.K_UP and y1_degisiklik == 0:
                    y1_degisiklik = -YILAN_BLOK_BOYUTU
                    x1_degisiklik = 0
                elif event.key == pygame.K_DOWN and y1_degisiklik == 0:
                    y1_degisiklik = YILAN_BLOK_BOYUTU
                    x1_degisiklik = 0

            # 2. DOKUNMATİK/SWIPE KONTROLLERİ (Mobil Uyumluluk İçin)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Sürükleme (Swipe) başlangıç pozisyonunu kaydet
                swipe_start_pos = event.pos

            elif event.type == pygame.MOUSEBUTTONUP and swipe_start_pos:
                swipe_end_pos = event.pos
                dx = swipe_end_pos[0] - swipe_start_pos[0]
                dy = swipe_end_pos[1] - swipe_start_pos[1]
                
                if abs(dx) > SWIPE_ESIK_DEGERI or abs(dy) > SWIPE_ESIK_DEGERI:
                    
                    # Yatay mı dikey mi?
                    if abs(dx) > abs(dy): # Yatay hareket (Sağ/Sol)
                        # Sadece mevcut yönün tersi değilse yön değiştir
                        if dx > 0 and x1_degisiklik <= 0:
                            x1_degisiklik = YILAN_BLOK_BOYUTU
                            y1_degisiklik = 0
                        elif dx < 0 and x1_degisiklik >= 0:
                            x1_degisiklik = -YILAN_BLOK_BOYUTU
                            y1_degisiklik = 0
                    
                    else: # Dikey hareket (Yukarı/Aşağı)
                         # Sadece mevcut yönün tersi değilse yön değiştir
                        if dy > 0 and y1_degisiklik <= 0:
                            y1_degisiklik = YILAN_BLOK_BOYUTU
                            x1_degisiklik = 0
                        elif dy < 0 and y1_degisiklik >= 0:
                            y1_degisiklik = -YILAN_BLOK_BOYUTU
                            x1_degisiklik = 0
                
                swipe_start_pos = None # Swipe işlemini sıfırla
            

        # Duvarlara çarpma kontrolü
        if x1 >= GENISLIK or x1 < 0 or y1 >= YUKSEKLIK or y1 < 0:
            oyun_kapanisi = True

        # Yeni pozisyonu hesapla
        x1 += x1_degisiklik
        y1 += y1_degisiklik
        
        # --- Çizim ve Güncelleme ---
        EKRAN.fill(ARKA_PLAN)
        
        # Yiyeceği çiz
        pygame.draw.rect(EKRAN, KIRMIZI, [yiyecekx, yiyeceky, YILAN_BLOK_BOYUTU, YILAN_BLOK_BOYUTU])
        
        # Bombaları çiz
        if seviye >= 2:
            bomba_ciz(bombalar)
        
        # Yılanın yeni baş pozisyonunu listeye ekle
        yilan_basi = [x1, y1]
        yilan_liste.append(yilan_basi)
        
        # Yılanın uzunluğunu koru (kuyruk silinir)
        if len(yilan_liste) > yilan_uzunlugu:
            del yilan_liste[0]

        # --- Çarpışma Kontrolleri ---
        
        # 1. Kendine çarpma kontrolü
        for x in yilan_liste[:-1]:
            if x == yilan_basi:
                oyun_kapanisi = True
        
        # 2. Bombalara çarpma kontrolü (2. seviyeden itibaren)
        if seviye >= 2:
            for b in bombalar:
                if b == yilan_basi:
                    oyun_kapanisi = True # Bomba çarptı, oyun bitti!

        # Yılanı çiz
        yilanimizi_ciz(yilan_liste)
        
        # Puanı ve Seviyeyi göster
        skor = yilan_uzunlugu - 1
        puan_goster(skor, seviye)
        
        # Ekranı güncelle
        pygame.display.update()

        # --- Yiyecek Yeme Kontrolü ---
        if x1 == yiyecekx and y1 == yiyeceky:
            
            # 1. Yılanı uzat
            yilan_uzunlugu += 1 

            # 2. Seviye Kontrolü (15 puana ulaşıldı mı?)
            if skor + 1 >= hedef_puan and seviye == 1:
                seviye += 1
                yilan_hizi += 5 # Hızı artır
                bomba_sayisi = 4 # 2. Seviyede 4 bomba ekle
                
                # Oyuncuya seviye atladığını bildir
                for _ in range(3): 
                    EKRAN.fill(ARKA_PLAN)
                    mesaj = SKOR_FONTU.render("SEVİYE 2 BAŞLADI! BOMBALARA DİKKAT!", True, SKOR_RENGI) 
                    EKRAN.blit(mesaj, [GENISLIK/2 - mesaj.get_width()/2, YUKSEKLIK/2 - mesaj.get_height()/2])
                    pygame.display.update()
                    time.sleep(1) 
            
            # 3. Yeni Bomba ve Yiyecek Pozisyonları
            
            # Engellenen alanları (yılan gövdesi + bombalar) topla
            engellenen_alanlar = yilan_liste + bombalar 
            
            # Yeni yiyecek pozisyonu oluştur
            yiyecekx, yiyeceky = rastgele_pozisyon_uret(engellenen_alanlar)

            # Bombaları yeniden konumlandır (Sadece seviye 2 ve sonrası için)
            if seviye >= 2:
                bombalar = [] 
                for _ in range(bomba_sayisi):
                    # Yeni bomba pozisyonu oluştur
                    bomba_x, bomba_y = rastgele_pozisyon_uret(engellenen_alanlar + [[yiyecekx, yiyeceky]]) 
                    bombalar.append([bomba_x, bomba_y])
                    # Yeni bombanın yılanı veya yiyeceği engellememesi için engellenen listeyi güncelle
                    engellenen_alanlar.append([bomba_x, bomba_y]) 
            
        # Oyun hızını ayarla
        SAAT.tick(yilan_hizi)

    # Pygame'den çık
    pygame.quit()
    quit()

# Oyun döngüsünü başlat
oyun_dongusu()