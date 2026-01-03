import streamlit as st

# Konfiguracja sesji Ghost Lock
st.set_page_config(page_title="GHOST LOCK 5.0", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #050505; color: #00FFC2; }
    .stNumberInput { background-color: #111 !important; }
    .stButton>button { 
        background-color: #00FFC2; color: black; border-radius: 10px; font-weight: bold; width: 100%;
        box-shadow: 0px 0px 15px #00FFC2;
    }
    .result-card { border: 2px solid #00FFC2; padding: 20px; border-radius: 10px; background-color: #0A0A0A; }
    </style>
    """, unsafe_allow_input=True)

st.title("⬢ GHOST LOCK 5.0")
st.write("Operator: **MARCIN MATCZAK**")

# Kalkulator wejścia
kapital = st.number_input("Aktualny Kapitał (PLN)", value=1000.0, step=100.0)
wejscie = st.number_input("Cena Wejścia", format="%.5f", value=1.17191)
sl_pips = st.number_input("Stop Loss (Pipsy)", value=20.0, step=1.0)

# Logika ryzyka 5%
ryzyko_pln = kapital * 0.05
pip_value = 40.0 # Stała dla EUR/USD
lot = ryzyko_pln / (sl_pips * pip_value) if sl_pips > 0 else 0

st.markdown('<div class="result-card">', unsafe_allow_input=True)
st.subheader("OBLICZENIA POZYCJI")
st.write(f"RYZYKO 5%: **{ryzyko_pln:.2f} PLN**")
st.markdown(f"<h1 style='color:#00FFC2;'>LOT: {lot:.2f}</h1>", unsafe_allow_input=True)
st.markdown('</div>', unsafe_allow_input=True)

# Schodkowanie
if kapital >= 40000:
    st.warning("⚠️ SYSTEM: AKTYWNE SCHODKOWANIE")
else:
    st.info("ℹ️ SYSTEM: TRYB KULA ŚNIEŻNA")

# Twój plan Trailing SL
one_r = sl_pips * 0.0001
st.subheader("Plan Schodków (TP 4R)")
st.write(f"🎯 TP 4R: **{wejscie + (4 * one_r):.5f}**")
st.write(f"🛡️ SL @ 1R (gdy cena 2R): **{wejscie + (1 * one_r):.5f}**")
st.write(f"🛡️ SL @ 2R (gdy cena 3R): **{wejscie + (2 * one_r):.5f}**")
st.write(f"🛡️ SL @ 3R (gdy cena 3.5R): **{wejscie + (3 * one_r):.5f}**")
