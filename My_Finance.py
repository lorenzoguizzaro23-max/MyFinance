imp_tot = float(input("Importo totale: "))
ETF_1 = float(input("MSCI World Min Volatility: "))
ETF_2 = float(input("Global Aggregate Bond: "))
ETF_3 = float(input("MSCI Europe SRI: "))
ETF_4 = float(input("GOLD: "))

total_percent = ETF_1 + ETF_2 + ETF_3 + ETF_4
if total_percent != 100:
    print(f"⚠️ Attenzione: le percentuali sommano a {total_percent}%, dovrebbero essere 100%")
else:
    val_eff_ETF1 = (ETF_1 / 100) * imp_tot
    val_eff_ETF2 = (ETF_2 / 100) * imp_tot
    val_eff_ETF3 = (ETF_3 / 100) * imp_tot
    val_eff_ETF4 = (ETF_4 / 100) * imp_tot

    print("----------------","\nIMPORTO TOTALE -->", imp_tot)
    print("MSCI World Min Volatility -->",val_eff_ETF1, "\nGlobal Aggregate Bond -->",val_eff_ETF2, "\nMSCI Europe SRI-->", val_eff_ETF3, "\nGOLD -->", val_eff_ETF4  )