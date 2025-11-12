# -*- coding: utf-8 -*-
import time
import random
from datetime import datetime

# ────── Tvoj AI Agent v1 ──────
AGENT_NAME = "SmeKerAI"
CLIENT_NAME = "subgirl"
NICHE = "AI usluge"
PRICE = "100EUR/mesec"

# Poruke (samo latinični karakteri!)
OUTREACH = [
    f"Cao! {AGENT_NAME} ovde. Pravim AI agenta za {CLIENT_NAME}. Trazi poslove, odgovara, reklamira. {PRICE}. Demo?",
    f"{CLIENT_NAME} trazi saradnju! {NICHE}. {PRICE}. DM open.",
    f"AI agent za {CLIENT_NAME} - radi sam. {PRICE}."
]

PROMO = [
    f"AI agent za {CLIENT_NAME} - 24/7 rad. {PRICE}",
    f"{AGENT_NAME} je napravio AI za {CLIENT_NAME}."
]

# Praćenje da ne šalje više puta u istom minutu
last_outreach = -1
last_promo = -1

# Funkcije
def outreach():
    msg = random.choice(OUTREACH)
    print(f"[{datetime.now().strftime('%H:%M')}] OUTREACH → {msg}")

def promote():
    msg = random.choice(PROMO)
    print(f"[{datetime.now().strftime('%H:%M')}] PROMO → {msg}")

# Start
print(f"AI AGENT v1 – STARTED za {CLIENT_NAME}")
print("─" * 50)
print("Ctrl+C za izlaz")

try:
    while True:
        now = datetime.now()
        minute = now.minute

        # Outreach svaka 2 minuta
        if minute % 2 == 0 and minute != last_outreach:
            outreach()
            last_outreach = minute

        # Promo svakih 5 minuta
        if minute % 5 == 0 and minute != last_promo:
            promote()
            last_promo = minute

        time.sleep(60)

except KeyboardInterrupt:
    print("\nAI Agent zaustavljen. Cao!")