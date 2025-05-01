# operations.py
import sqlite3
from datetime import datetime

DB = 'banco.db'

def conectar():
    return sqlite3.connect(DB)

def crear_cliente(nombre, email):
    conn = conectar()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO Clientes (nombre, email) VALUES (?, ?)', (nombre, email))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise ValueError("Email duplicado") from e
    finally:
        conn.close()

def abrir_cuenta(cliente_id):
    conn = conectar()
    c = conn.cursor()
    # Verificar cliente existe
    c.execute('SELECT id FROM Clientes WHERE id = ?', (cliente_id,))
    if not c.fetchone():
        conn.close()
        raise ValueError("ID de cliente inexistente")
    c.execute('INSERT INTO Cuentas (cliente_id) VALUES (?)', (cliente_id,))
    conn.commit()
    conn.close()

def depositar(cuenta_id, monto):
    if monto <= 0:
        raise ValueError("Monto debe ser positivo")
    conn = conectar(); c = conn.cursor()
    c.execute('SELECT saldo FROM Cuentas WHERE id = ?', (cuenta_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        raise ValueError("ID de cuenta inexistente")
    nuevo = row[0] + monto
    c.execute('UPDATE Cuentas SET saldo = ? WHERE id = ?', (nuevo, cuenta_id))
    # Registro de movimiento
    c.execute('''
      INSERT INTO Movimientos (cuenta_id, tipo, monto, fecha)
      VALUES (?, 'depósito', ?, ?)
    ''', (cuenta_id, monto, datetime.now().isoformat()))
    conn.commit(); conn.close()

def retirar(cuenta_id, monto):
    if monto <= 0:
        raise ValueError("Monto debe ser positivo")
    conn = conectar(); c = conn.cursor()
    c.execute('SELECT saldo FROM Cuentas WHERE id = ?', (cuenta_id,))
    row = c.fetchone()
    if not row:
        conn.close()
        raise ValueError("ID de cuenta inexistente")
    if row[0] < monto:
        conn.close()
        raise ValueError("Saldo insuficiente")
    nuevo = row[0] - monto
    c.execute('UPDATE Cuentas SET saldo = ? WHERE id = ?', (nuevo, cuenta_id))
    c.execute('''
      INSERT INTO Movimientos (cuenta_id, tipo, monto, fecha)
      VALUES (?, 'retiro', ?, ?)
    ''', (cuenta_id, monto, datetime.now().isoformat()))
    conn.commit(); conn.close()

def listar_tabla(nombre_tabla):
    conn = conectar(); c = conn.cursor()
    c.execute(f'SELECT * FROM {nombre_tabla}')
    datos = c.fetchall()
    conn.close()
    return datos
