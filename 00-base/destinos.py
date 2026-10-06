destinos = [
    {"ciudad": "Bolonia", "pais": "Italia", "idioma": "italiano", "coste_mensual": 850},
    {"ciudad": "Lisboa", "pais": "Portugal", "idioma": "portugués", "coste_mensual": 900},
    {"ciudad": "Roma", "pais": "Italia", "idioma": "italiano", "coste_mensual": 950},
]

for destino in destinos:
    print(f"{destino['ciudad']} ({destino['pais']}) · idioma: {destino['idioma']} · {destino['coste_mensual']} € al mes")
    if destino['coste_mensual'] < 900:
        print("   → Presupuesto asequible")
    else:
        print("   → Presupuesto alto")
        