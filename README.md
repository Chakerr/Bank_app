# bank_app

**Proyecto taller:** Aplicación de línea de comandos para gestión bancaria.

## Objetivo del taller

En este taller se desarrolló una pequeña aplicación en Python con los siguientes propósitos:

- Practicar la creación y uso de un entorno virtual.
- Diseñar y generar una base de datos SQLite con las tablas necesarias.
- Implementar la lógica de negocio para operaciones bancarias básicas.
- Manejar errores comunes (clientes no existentes, saldos insuficientes, emails duplicados).
- Construir una interfaz de línea de comandos interactiva y presentar resultados en tablas.

## Funcionalidades implementadas

1. **Inicialización de la base de datos (`db.py`):**
   - Conexión a `banco.db` y creación de tablas para clientes, cuentas y transacciones.
2. **Lógica de negocio (`operations.py`):**
   - Creación, consulta y listado de clientes y cuentas.
   - Depósitos y retiros con validación de saldo.
   - Registro de cada operación en la tabla de transacciones.
3. **Interfaz de línea de comandos (`run.py`):**
   - Menú interactivo que guía al usuario por las distintas operaciones.
   - Captura de entrada y despliegue de resultados con la biblioteca `tabulate`.
   - Gestión de excepciones y mensajes claros ante errores.
4. **Script de ejecución (`setup.sh`):**
   - Automatiza la creación del entorno virtual, instalación de dependencias y arranque de la aplicación.

## Estructura del proyecto

```bash
bank_app/
├── .venv/                  # entorno virtual
├── banco.db               # base de datos SQLite generada por db.py
├── db.py                  # inicialización de la base de datos
├── operations.py          # lógica de negocio
├── run.py                 # interfaz CLI principal
├── setup.sh               # script de configuración y ejecución
├── requirements.txt       # dependencias del proyecto
└── README.md              # este archivo
```

## Uso rápido

Para arrancar la aplicación, ejecuta:
```bash
bash setup.sh
```
Sigue las indicaciones del menú para crear clientes, abrir cuentas y realizar transacciones.

## Licencia

Este proyecto se entregó como parte de un taller académico y no tiene licencia asignada.