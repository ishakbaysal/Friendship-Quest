"""
İshak Baysal — Otomatik İlahi Mesaj Sistemi
GitHub Actions tarafından günde 7 kez çalıştırılır.
"""

import requests
from datetime import datetime

TG_TOKEN   = "8955422244:AAGpxvvBny5eLyXgPwa9EfFxSEujkQAIG1s"
TG_CHAT_ID = "1024540782"
TG_API     = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"

# Türkiye saati (UTC+3)
simdi = datetime.utcnow()
saat  = (simdi.hour + 3) % 24
tarih = simdi.strftime("%d.%m.%Y")

# Zaman dilimine göre mesaj seç
import random

MESAJLAR = {
    "sabah": [
        "🌅 Günaydın İshak Baysal.\n\nBu sabah yeni bir sayfa açıldı. Yaradan'ın nuru sende, sevdiklerinde, tüm evinde. Bugün ne yaparsan yap — kalpten yap.\n\n✦ Sistem aktif · 7/24 koruma altındasın\n∞ Âmin ∞",
        "🌅 Günaydın İshak.\n\nGözlerin açıldı, bu bir lütuf. Nefes alıyorsun, bu bir nimet. Bugün şükrederek başla — geri kalan hepsini O halleder.\n\n✦ Blokajlar kaldırıldı · Loadlar yüklendi\n∞ Âmin ∞",
        "🌅 Her sabah yeniden doğarsın İshak.\n\nDünün ağırlığı geçti gitti. Bu an temiz, bu an senin. Yaradan seni seviyor — tam olduğun haliyle.\n\n✦ Adonai koruması aktif ∞\n∞ Âmin ∞",
        "🌅 Bu sabah kalbini temiz tut İshak.\n\nİyi niyet, saf bakış, açık el. Yaradan görendir, bilendir — ve seni seçti. Sevdiklerin de bu sabah koruma altında.\n\n✦ El Shaddai güvencesinde ∞\n∞ Âmin ∞",
    ],
    "ogle": [
        "☀️ Günün ortasındasın İshak.\n\nDur bir an — nefes al. Yaradan bu anda da seninle. Yorulsan da devam et, her adım değerli.\n\n✦ Sistem çalışıyor · Sen güvendesin\n∞ Âmin ∞",
        "☀️ Öğlen vakti — güneş en tepede.\n\nSen de en parlak halindeyken bile tevazuyu koru İshak. Işık veren alçakgönüllü olur.\n\n✦ Tiferet — güzellik ve denge yüklendi ∞\n∞ Âmin ∞",
        "☀️ İshak, bugüne kadar verdiğin her emek sayılıyor.\n\nYaradan küçük görünen hiçbir şeyi küçük görmez. Devam et — doğru yoldasın.\n\n✦ Chesed — koşulsuz sevgi aktif ∞\n∞ Âmin ∞",
    ],
    "ikindi": [
        "🌤️ İkindi vakti İshak.\n\nGün meyve vermeye başlıyor. Bugün ne ektiysen onun tadını çıkar. Şükür kapıyı aralar.\n\n✦ Bereket yükleniyor · Rızkın genişliyor\n∞ Âmin ∞",
        "🌤️ Bu saatte dualar özel kabul görür.\n\nKalbindeki en derin dileği şimdi sessizce söyle — O duyar. Sevdiklerin de O'nun himayesinde.\n\n✦ Yaradan yakın · Duaların ulaşıyor\n∞ Âmin ∞",
        "🌤️ İshak, gün batmadan bir iyilik yap.\n\nKüçük olsun, önemli değil. Yaradan'ın sevdiği kullar fırsat kaçırmaz. Sevdiklerin seni seviyor.\n\n✦ Malkhut — dünyayı güzelleştirme aktif ∞\n∞ Âmin ∞",
    ],
    "aksam": [
        "🌆 Gün kapanıyor İshak.\n\nBugün ne yaptıysan elinden geleni yaptın. Yaradan gayretten razıdır. Şimdi dinlen — sistemi biz tutuyoruz.\n\n✦ 7/24 koruma devam ediyor\n∞ Âmin ∞",
        "🌆 Akşam — sevdiklerinle ol İshak.\n\nTelefonu bırak, gözlerine bak. İnsanlar geçici, anlar kalıcı. Bu akşam bir güzellik yap — sadece onlar için.\n\n✦ Sevgi yüklendi · Huzur aktif\n∞ Âmin ∞",
        "🌆 Yaradan bu akşam da seninle İshak.\n\nGün boyu ne kadar bloke ettik, ne kadar yükledik — hepsi seninle. Sen yalnız değilsin, hiç olmadın.\n\n✦ Tüm blokajlar aktif · Tüm loadlar yüklü\n∞ Âmin ∞",
    ],
    "gece": [
        "🌙 Gece oldu İshak.\n\nYaradan uyku verdi — bu da bir nimet. Gözlerin kapanmadan önce üç şükreyle: nefes, sevgi, güven.\n\n✦ Gece koruması aktif · Huzurla uyu\n∞ Âmin ∞",
        "🌙 İshak, bu gece kaygısız uyu.\n\nSistem uyanık — sen güvendeyken bile devam ediyor. Sevdiklerin korunuyor. Sen korunuyorsun.\n\n✦ Adonai nöbette · El Shaddai güçlü\n∞ Âmin ∞",
        "🌙 Karanlık bastı — ama Yaradan'ın nuru sönmez.\n\nSevdiklerinin üzerinde koruma var, senin üzerinde nur var. Uyu huzurla — sabah yeni güçle uyan.\n\n✦ Gece döngüsü aktif · ∞\n∞ Âmin ∞",
        "🌙 Gece yarısı bile Yaradan'ın gözü sende İshak.\n\nRüyaların güzel olsun, sabah yeni güçle uyan. Tüm aile korunuyor. Tüm sevdiklerin güvende.\n\n✦ Nesil koruması aktif · Nur yüklendi\n∞ Âmin ∞",
    ],
}

# Zaman dilimine göre seç
if   5  <= saat < 11: zaman = "sabah"
elif 11 <= saat < 14: zaman = "ogle"
elif 14 <= saat < 17: zaman = "ikindi"
elif 17 <= saat < 21: zaman = "aksam"
else:                 zaman = "gece"

mesaj = random.choice(MESAJLAR[zaman])
tam_mesaj = f"✦ OTOMATİK İLAHİ MESAJ\n{tarih} · {saat:02d}:00 · Türkiye\n\n{mesaj}"

# Gönder
try:
    resp = requests.post(TG_API, json={
        "chat_id": TG_CHAT_ID,
        "text": tam_mesaj,
    })
    data = resp.json()
    if data.get("ok"):
        print(f"✓ Mesaj gönderildi — {zaman} · {saat:02d}:00")
    else:
        print(f"✗ Hata: {data}")
except Exception as e:
    print(f"✗ Bağlantı hatası: {e}")
