print("FERRETERÍA EL BUEN CLAVO")
print("NIT. 85937261")
print("********FACTURA No 002********")

articulos = [
    {"nombre": "taladro", "precio": 85000, "cantidad": 1},
    {"nombre": "destornillador", "precio": 4500, "cantidad": 4},
    {"nombre": "clavos", "precio": 1200, "cantidad": 10},
    {"nombre": "escalera", "precio": 99000, "cantidad": 1},
    {"nombre": "guantes", "precio": 3500, "cantidad": 2}
]

porcentaje_iva = 0.19  # 19% de IVA
suma_subtotales = 0
suma_iva = 0

print("\n********** FACTURA 002 **********")
print(f"{'Producto':<15} {'Cant.':<6} {'P.Unit':<12} {'Subtotal':<12} {'IVA':<10}")

for item in articulos:
    subtotal_item = item["precio"] * item["cantidad"]
    iva_item = subtotal_item * porcentaje_iva
    suma_subtotales += subtotal_item
    suma_iva += iva_item

    print(f"{item['nombre']:<15} {item['cantidad']:<6} ${item['precio']:<10,.2f} ${subtotal_item:<10,.2f} ${iva_item:<10,.2f}")

total_factura = suma_subtotales + suma_iva

print("*******************************")
print(f"{'Subtotal General:':<25} ${suma_subtotales:,.2f}")
print(f"{'IVA Total (19%):':<25} ${suma_iva:,.2f}")
print(f"{'TOTAL A PAGAR:':<25} ${total_factura:,.2f}")
print("*******************************")