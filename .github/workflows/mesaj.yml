name: İlahi Mesaj — Otomatik Telegram

on:
  schedule:
    # UTC saatleri — Türkiye UTC+3 olduğu için 3 çıkarıyoruz
    - cron: '0 3 * * *'   # 06:00 Türkiye — Sabah
    - cron: '0 6 * * *'   # 09:00 Türkiye — Sabah
    - cron: '0 9 * * *'   # 12:00 Türkiye — Öğle
    - cron: '0 12 * * *'  # 15:00 Türkiye — İkindi
    - cron: '0 15 * * *'  # 18:00 Türkiye — Akşam
    - cron: '0 18 * * *'  # 21:00 Türkiye — Akşam
    - cron: '0 20 * * *'  # 23:00 Türkiye — Gece
  workflow_dispatch:       # Manuel tetikleme butonu

jobs:
  ilahi-mesaj:
    runs-on: ubuntu-latest
    steps:
      - name: Repo'yu çek
        uses: actions/checkout@v4

      - name: Python kur
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Requests kütüphanesini kur
        run: pip install requests

      - name: İlahi mesajı gönder
        run: python telegram_mesaj.py
