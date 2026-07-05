# buscador_unidades.py

from Unidades import unidades

def buscar_por_codigo(codigo):
    return unidades.get(codigo.upper(), "No encontrado")

def buscar_por_texto(texto):
    texto = texto.lower()
    resultados = {c: d for c, d in unidades.items() if texto in d.lower()}
    return resultados if resultados else "No se encontraron coincidencias"

if __name__ == "__main__":
    while True:
        print("\n=== BUSCADOR DE UNIDADES ===")
        opcion = input("Buscar por (1) Código o (2) Texto, (q) salir: ").strip()
        
        if opcion == "1":
            codigo = input("Ingrese código (ej: U9646): ")
            print(buscar_por_codigo(codigo))
        elif opcion == "2":
            texto = input("Ingrese parte de la descripción: ")
            resultados = buscar_por_texto(texto)
            if isinstance(resultados, dict):
                for c, d in resultados.items():
                    print(f"{c} -> {d}")
            else:
                print(resultados)
        elif opcion.lower() == "q":
            break
        else:
            print("Opción inválida.")