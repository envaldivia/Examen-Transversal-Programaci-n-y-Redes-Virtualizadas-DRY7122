def clasificar_vlan(vlan_numero):

    if 1 <= vlan_numero <= 1005:
        rango = "normal"
    elif 1006 <= vlan_numero <= 4094:
        rango = "extendido"
    else:
        rango = "inválido"

    return f"La VLAN {vlan_numero} pertenece al rango {rango}."

if __name__ == "__main__":
    vlan_numero = int(input("Ingrese el número de VLAN: "))
    resultado_clasificacion = clasificar_vlan(vlan_numero)
    print(resultado_clasificacion)
