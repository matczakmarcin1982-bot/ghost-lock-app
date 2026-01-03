import streamlit as st

st.set_page_config(page_title="GHOST LOCK 5.0")

st.title("⬢ GHOST LOCK 5.0")
st.write("Operator: **MARCIN MATCZAK**")

# Kalkulator
kapital = st.number_input("Aktualny Kapitał (PLN)", value=1000.0)
wejscie = st.number_input("Cena Wejścia", format="%.5f", value=1.17191)
sl_pips = st.number_input("Stop Loss (Pipsy)", value=20.0)

# Logika ryzyka 5%
ryzyko_pln = kapital * 0.05
pip_value = 40.0 
lot = ryzyko_pln / (sl_pips * pip_value) if sl_pips > 0 else 0

st.divider()
st.subheader(f"LOT: {lot:.2f}")
st.write(f"Ryzyko (5%): {ryzyko_pln:.2f} PLN")

# Schodkowanie
if kapital >= 40000:
    st.warning("TRYB: SCHODKOWANIE")
else:
    st.info("TRYB: KULA ŚNIEŻNA")

# Poziomy
one_r = sl_pips * 0.0001
st.subheader("Plan Schodków")
st.write(f"🎯 Cel TP 4R: {wejscie + (4 * one_r):.5f}")
st.write(f"🛡️ SL @ 1R (gdy cena 2R): {wejscie + (1 * one_r):.5f}")
st.write(f"🛡️ SL @ 2R (gdy cena 3R): {wejscie + (2 * one_r):.5f}")
