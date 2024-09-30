# Análisis del Mercado de Internet en Argentina

## Introducción

Este repositorio contiene un análisis exhaustivo sobre el mercado de Conectividad a Internet en Argentina, enfocado en identificar tendencias y oportunidades en el uso de tecnologías, velocidades de conexión y cobertura. Incluye procesos de **ETL** (Extracción, Transformación y Carga de datos), un **Análisis Exploratorio de Datos (EDA)** para la comprensión inicial del dataset, y conclusiones del estudio con un **dashboard** interactivo en formato **.PBIX** con KPI medibles y filtros para su necesidad.


## Tabla de Contenido
- [Introducción](#Introducción)
- [Instalación y Requisitos](#instalación-y-requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Datos y Fuentes](#datos-y-fuentes)
- [Metodología](#metodología)
- [Resultados y Links al proyecto](#resultados-y-links-al-proyecto)
- [Autor](#autor)
- [Contribución y Colaboración](#contribución-y-colaboración)
- [Licencia](#licencia)


### Instalación y requisitos

1. **Clona el repositorio**:
2. **Navega al directorio del proyecto**
3. **Crea un entorno virtual** 
4. **Activa el entorno virtual**
5. **Instala las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

## Estructura del Proyecto

La estructura del proyecto es la siguiente:
  
- **data**: Almacena los archivos de datos Excel utilizados en el analisis, separados por paginas en formato csv.

- **notebooks/**: Contiene los notebooks Jupyter donde se realiza el ETL y el EDA. Necesarios para cada pagina.
    - **ETL**: Aplica transformaciones, limpieza de los archivos y separacion por paginas. Para ser enviados a la carpeta **data**. 
    - **EDA**: Aplica Análisis Exploratorio de los datos para encontrar datos interesantes.

- **dashboard**: Contiene el archivo dashboard visual con los KPI y analisis creados en Power BI.

- **requirements.txt**: Lista de dependencias y bibliotecas necesarias para ejecutar el ETL y EDA.

- **README.md**: Documentación del analisis con conclusiones y metodologias.

## Datos y Fuentes

- [**Enacom Internet**](https://indicadores.enacom.gob.ar/datos-abiertos): El ENACOM (Ente Nacional de Comunicaciones) es el organismo regulador en Argentina responsable de la política pública en el ámbito de las telecomunicaciones y la radiodifusión. Se encarga de regular, supervisar y controlar los servicios de telecomunicaciones en el país, incluyendo internet, telefonía fija y móvil, y servicios de radiodifusión.

- [**INDEC**](https://www.indec.gob.ar): El INDEC (Instituto Nacional de Estadística y Censos) es el organismo oficial de estadísticas de Argentina. De aqui recopilamos la inflacion desde 2017 para evaluar los ingresos reales.

- [**Diccionario de datos Enacom**](https://docs.google.com/document/d/1BYW0vT_DNIjjKM9v4hNg5KmqjRNOc7OBB1jCXc80gnI/edit#heading=h.hjukififf3ol): Diccionario con descripciones de las paginas disponibles en el dataset.

## Metodología

