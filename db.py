# db.py
import sqlite3

def crear_tablas():
    conn = sqlite3.connect('banco.db')
    c = conn.cursor()

    # Tabla Clientes
    c.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )''')

    # Tabla Cuentas
    c.execute('''
    CREATE TABLE IF NOT EXISTS Cuentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        saldo REAL NOT NULL DEFAULT 0.0,
        FOREIGN KEY(cliente_id) REFERENCES Clientes(id)
    )''')

    # Tabla Movimientos
    c.execute('''
    CREATE TABLE IF NOT EXISTS Movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cuenta_id INTEGER NOT NULL,
        tipo TEXT CHECK(tipo IN ('depósito','retiro')),
        monto REAL NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY(cuenta_id) REFERENCES Cuentas(id)
    )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    crear_tablas()
