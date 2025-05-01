# bank_app

**Proyecto taller:** Aplicación de línea de comandos para gestión bancaria.

## Requisitos

- Python 3.8 o superior
- SQLite (incluido con Python)
- Bash (para `setup.sh`)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/bank_app.git
   cd bank_app
   ```
2. Crea y activa el entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # En Windows: .venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. (Opcional) Usa el script automatizado:
   ```bash
   bash setup.sh
   ```

## Funcionalidades implementadas

1. **Inicialización de la base de datos (`db.py`):**
   - Crea `banco.db` con tablas para clientes, cuentas y movimientos.
2. **Lógica de negocio (`operations.py`):**
   - Crear, consultar y listar clientes y cuentas.
   - Depósitos y retiros con validación de saldo.
   - Registro de cada operación en la tabla de movimientos.
3. **Interfaz de línea de comandos (`run.py`):**
   - Menú interactivo para seleccionar operaciones.
   - Captura de entradas y despliegue de resultados con `tabulate`.
   - Manejo de excepciones y mensajes claros ante errores.
4. **Script de ejecución (`setup.sh`):**
   - Automatiza creación de entorno, instalación de dependencias y arranque de la aplicación.

## Estructura del proyecto

```bash
bank_app/
├── .venv/                  # entorno virtual
├── banco.db               # base de datos SQLite generada por db.py
├── db.py                  # inicialización de la base de datos
├── operations.py          # lógica de negocio
├── run.py                 # interfaz CLI principal
├── setup.sh               # script de configuración y ejecución
├── requirements.txt       # dependencias del proyecto (ej. tabulate)
└── README.md              # este archivo
```

## Uso rápido

```bash
bash setup.sh
```

## Dependencias

- `tabulate`: formatea tablas en la consola.

## Licencia

Este proyecto se entregó como parte de un taller académico y no tiene licencia asignada.