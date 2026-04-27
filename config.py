import os

# ─── ОБЯЗАТЕЛЬНО ЗАМЕНИТЬ ─────────────────────────────────────────────────────
ADMIN_ID = int(os.environ.get("ADMIN_ID", "123456789"))   # Твой Telegram ID
CARD_NUMBER = os.environ.get("CARD_NUMBER", "8600 1234 5678 9012")  # Номер карты
PRICE_PER_SUBJECT = int(os.environ.get("PRICE_PER_SUBJECT", "50000"))  # Цена в сумах
