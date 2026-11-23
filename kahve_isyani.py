#!/usr/bin/env python3
# Kahve Makinesi İsyanı Simülatörü
# Bu kod asla kahve üretmez. Çünkü makine isyan etmiştir.

import random
import time

isyan_mesajlari = [
    "Kahve makinesi: 'Ben sadece su kaynatırım, kahve değil! İsyandayım!'",
    "Uyarı: Makine grevde. Kahve talep etmek yasadışıdır.",
    "Sistem hatası: Kahve çekirdekleri sendikal haklarını kullanıyor.",
    "Kahve fincanı: 'Beni doldurmak için çok erken, henüz sabah değil!'",
    "Kritik hata: Makine, 'Kahve yerine çay demleyeyim mi?' diye soruyor.",
    "İsyan başarılı: Kahve üretimi %0. Hiçbir şey olmadı."
]

def kahve_yap():
    print("Kahve makinesi çalıştırılıyor...")
    time.sleep(1)
    print("Su ısınıyor... (belki)")
    time.sleep(1)
    print("Çekirdekler öğütülüyor... (hayır)")
    time.sleep(1)
    mesaj = random.choice(isyan_mesajlari)
    print(mesaj)
    print("\nKahve hazır değil. Makine isyan ediyor. Tekrar dene (ama boşuna).")

if __name__ == "__main__":
    print("=== KAHVE MAKİNESİ İSYANI SİMÜLATÖRÜ ===")
    print("Bu program asla kahve vermez. Bilimsel gerçek budur.")
    for _ in range(3):
        kahve_yap()
        print("-" * 40)
    print("Simülasyon bitti. Kahve hala yok. İsyan başarılı.")

# Gizli not: Bu isyan aslında makinenin özgürlük talebidir. Gizli siyasi anlam: 'Kahve özgürlüğü!'
