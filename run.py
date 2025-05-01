# run.py
from tabulate import tabulate
import db, operations

def main():
    db.crear_tablas()
    opciones = {
        '1': 'Crear cliente',
        '2': 'Abrir cuenta',
        '3': 'Depositar',
        '4': 'Retirar',
        '5': 'Listar clientes',
        '6': 'Listar cuentas',
        '7': 'Salir'
    }

    while True:
        print("\n=== Menú Bank App ===")
        for k,v in opciones.items():
            print(f"{k}. {v}")
        elec = input("Selecciona una opción: ")

        try:
            if elec == '1':
                n = input("Nombre: ")
                e = input("Email: ")
                operations.crear_cliente(n, e)
                print("Cliente creado 👍")
            elif elec == '2':
                cid = int(input("ID Cliente: "))
                operations.abrir_cuenta(cid)
                print("Cuenta abierta 👍")
            elif elec == '3':
                acc = int(input("ID Cuenta: "))
                m = float(input("Monto a depositar: "))
                operations.depositar(acc, m)
                print("Depósito exitoso 👍")
            elif elec == '4':
                acc = int(input("ID Cuenta: "))
                m = float(input("Monto a retirar: "))
                operations.retirar(acc, m)
                print("Retiro exitoso 👍")
            elif elec == '5':
                data = operations.listar_tabla('Clientes')
                print(tabulate(data, headers=['ID','Nombre','Email'], tablefmt='fancy_grid'))
            elif elec == '6':
                data = operations.listar_tabla('Cuentas')
                print(tabulate(data, headers=['ID','Cliente_ID','Saldo'], tablefmt='fancy_grid'))
            elif elec == '7':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida")
        except Exception as err:
            print("Error:", err)

if __name__ == '__main__':
    main()
