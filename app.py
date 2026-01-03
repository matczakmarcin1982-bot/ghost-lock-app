import streamlit as st

st.title("GHOST LOCK 5.0")
st.write("Operator: MARCIN MATCZAK")

# Dane
kapital = st.number_input("Kapitał (PLN)", value=1000.0)
wejscie = st.number_input("Cena Wejścia", format="%.5f", value=1.17191)
sl_pips = st.number_input("SL (Pipsy)", value=20.0)

# Obliczenia - Twoje zasady
ryzyko_pln = kapital * 0.05 [cite: 2025-12-17]
pip_value = 40.0 
lot = ryzyko_pln / (sl_pips * pip_value) if sl_pips > 0 else 0

st.subheader(f"REKOMENDOWANY LOT: {lot:.2f}")
st.write(f"Ryzyko kwotowe: {ryzyko_pln:.2f} PLN") [cite: 2025-12-17]

# Strategia
if kapital >= 40000:
    st.warning("⚠️ TRYB: SCHODKOWANIE") [cite: 2025-12-23]
else:
    st.info("ℹ️ TRYB: KULA ŚNIEŻNA")

# Poziomy TP/SL
one_r = sl_pips * 0.0001
st.write(f"🎯 TP 4R: {wejscie + (4 * one_r):.5f}")
st.write(f"🛡️ SL @ 1R: {wejscie + (1 * one_r):.5f}")
