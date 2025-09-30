import streamlit as st

st.title("Portfolio Allocator")

imp_tot = st.number_input("Importo totale (€)", min_value=0.0, value=150.0)

ETF_1 = st.number_input("MSCI World Min Volatility (%)", min_value=0.0, max_value=100.0, value=65.0)
ETF_2 = st.number_input("Global Aggregate Bond (%)", min_value=0.0, max_value=100.0, value=15.0)
ETF_3 = st.number_input("MSCI Europe SRI (%)", min_value=0.0, max_value=100.0, value=15.0)
ETF_4 = st.number_input("GOLD (%)", min_value=0.0, max_value=100.0, value=0.0)

total_percentage = ETF_1 + ETF_2 + ETF_3 + ETF_4

if total_percentage != 100:
    st.error(f"Le percentuali devono sommare a 100%. Totale attuale: {total_percentage}%")
else:
    val_eff_ETF1 = (ETF_1 / 100) * imp_tot
    val_eff_ETF2 = (ETF_2 / 100) * imp_tot
    val_eff_ETF3 = (ETF_3 / 100) * imp_tot
    val_eff_ETF4 = (ETF_4 / 100) * imp_tot

    st.write(f"### Investimento ETF calcolato su {imp_tot} €:")
    st.write(f"MSCI World Min Volatility: €{val_eff_ETF1:.2f}")
    st.write(f"Global Aggregate Bond: €{val_eff_ETF2:.2f}")
    st.write(f"MSCI Europe SRI: €{val_eff_ETF3:.2f}")
    st.write(f"GOLD: €{val_eff_ETF4:.2f}")
