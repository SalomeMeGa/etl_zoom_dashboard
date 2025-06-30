# 📊 Proyecto: ETL Automatizado de Usuarios en Zoom con Visualizaciòn en AWS QuickSight
## Descripciòn

Este proyecto implementa un pipeline ETL automatizado para extraer informaciòn sobre usuarios y su estado de presencia desde la API de Zoom. Los datos se transforman, limpian y se almacenan en una base de datos relacional en AWS (RDS MySQL). Finalmente, se visualizan en un dashboard ejecutivo creado con Amazon QuickSight.

EL pipeline se ejecuta automàticamente cada 15 minutos gracias al uso de aws lambda y EvenBridge (CloudWatchEvents)

## 📚 Tabla de Contenidos

- [🎯 Objetivo](#-objetivo)
- [🧰 Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️  Instalación y Ejecución](#️-instalación-y-ejecución)
- [🧼 Preparación de Datos](#-preparación-de-datos)
- [📊 Visualizaciones Incluidas](#-visualizaciones-incluidas)
- [🎛️ Interacción](#️-interacción)
- [🧪 Requisitos del Entorno](#-requisitos-del-entorno)
- [🚀 Futuras Mejoras](#-futuras-mejoras)
- [📌 Consideraciones Finales](#-consideraciones-finales)
- [🧠 Autor(a)](#-autora)

---

## 🎯 Objetivo
- Automatizar la recolecciòn y anàlisis del estado de los usuarios de Zoom, facilitando la toma de decisiones sobre la actividad y conectividad del equipo.


## 🧰Tecnologias

- **Lenguajes**: Python 3.12+
- **API:** Zoom API
- **Base de Datos:** Amazon RDS(Mysql)
- **Dashboard:** Amazon QuickSight
- **Despliegue automatico:** AWS Lambda + Amazon EventBridge
- **Entorno virtual**: zoom_etl
- **Librerias**:
- requests
- pandas
- sqlalchemy
- Jupyter Notebooks (para anaàlisis exploratorio)
- tabulate
- pymysql
- **Visual Studio Code**: Como editor
- **Control de versiones**: Git / GitHub


## 📁Estructura del Proyecto
etl_zoom_dashboard/
- notebooks/ 
exploracion_zoom.ipynb
- scripts/
extract_data.py/load_data.py/db_connection.py/zoom_auth.py
-lambda_function/
lambda_function.py
- main.py
- README.md
- requirements.txt
- README.md
- .gitignore
- zoom_etl/

## ⚙️ Instalación y Ejecución

1. Clona este repositorio:
```bash
git https://github.com/SalomeMeGa/etl_zoom_dashboard.git
cd aetl_zoom_dashboard

```
2. Crea un entorno virtual:
```bash
python -m venv zoom_etl
source zoom_etl/bin/activate  
``` 
3. Instala las dependencias
```bash
pip install -r requirements.txt
```
4. Ejecuta el dashboard
```bash
python3 main.py
```
---

## 🧼 Preparación de Datos

- Extracciòn y preparaciòn de los Datos
- Atenticaciòn
- Extracciòn de los Usuarios
- Extracciòn del Estado de Presencia
- Limpieza y transformaciòn
- Validaciòn

## 📊 Visualizaciones Incluidas

- Presencia por Status por Usuario Zoom
- Porcentaje de Status por Usuario de Zoom
- Recuento de presencia de Status por Usuario Zoom
- Tabla de presencia por Status por Usuario Zoom

## 🎛️ Interacción

   - Puedes seleccionar entre los graficos representados en QuickSight, cada gràfico te permite visualizar el status, porcentaje, correo
   - La representaciòn en los gràficos te permite observar el comportamiento de los usuarios por porcentaje, por nùmero de usuarios, o por una tabla general con informaciòn complementaria.


## 🧪 Requisitos del Entorno

Contenido de requirements.txt

pandas
requests
SQLAlchemy
....

## 🚀 Futuras Mejoras

- Separar las credenciales en n archivo '.env' para mejorar la seguridad
- Agregar logs en archivos para facilitar el monitoreo
- Implementar pruebas unitarias para las funciones de conexiòn y carga
- Crear un dashboard en Streamlit o Dash como interfaz adicional de consulta
- Automatizar el despliegue cin Terraform o AWS CDK
- Permitir consultas històricas 
- Versionamiento de datos exportados


## 📌 Consideraciones Finales

- La extracciòn de datos depende de los lìmites de la API de Zoom
- La informaciòn obtenida puede cambiar ràpidamente (presencia en tiempo real)
- La ejecuciòn en AWS Lambda permite una automatizaciòn eficiente, pero se debe monitorear su desempeño.
- Se recomienda usar este flujo en entornos segros, cifrando credenciales y controlando accesos a RDS.


## 🧠 Autor(a)

    Nombre: Alberto Mendoza Garcìa
    Correo: [ing.albertomendozagarcia@gmail.com]
    Última actualización: 30 Junio 2025