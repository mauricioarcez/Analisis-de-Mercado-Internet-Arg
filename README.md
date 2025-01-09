# Análisis del Mercado de Internet en Argentina

## Introducción

Este repositorio contiene un análisis exhaustivo sobre el mercado de Conectividad a Internet en Argentina, enfocado en identificar tendencias y oportunidades en el uso de tecnologías, velocidades de conexión y cobertura. Incluye procesos de **ETL** (Extracción, Transformación y Carga de datos), un **Análisis Exploratorio de Datos (EDA)** para la comprensión inicial del dataset, y conclusiones del estudio con un **dashboard** interactivo en formato **.PBIX** con KPI medibles y filtros para su necesidad.


## Tabla de Contenido
- [Introducción](#Introducción)
- [Instalación y Requisitos](#instalación-y-requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Datos y Fuentes](#datos-y-fuentes)
- [Metodología](#metodología)
- [Reporte y KPIs](#reporte-y-kpis)
- [Autor y Licencia](#autor-y-licencia)


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

### En la carpeta ETL.
1. Separacion del Excel en Paginas.
2. Conversión del tipo de dato y corrección de errores
3. Combinación de datos de Inflación e Ingresos en una sola tabla.
4. Exportar los archivos a la carpeta **data**

### En la carpeta EDA.
1. Análisis del Crecimiento Total de Conectividades por Año.
2. Análisis de Crecimiento de Conexiones por provincias. (2014-2024).
3. Distribución Tecnológica en la actualidad.
4. Análisis de Tecnologías por provincias destacadas.
5. Evolución de Tecnologías.
6. Accesos Dial up.
7. accesos por provincias.
8. Accesos por Hogares.
9. Ingresos antes y despues de inflación.

## Reporte y KPIs

El reporte  incluye la evolución de las tecnologías utilizadas, las velocidades de conexión, y la cobertura regional  desde 2014 hasta 2024. El dashboard interactivo en formato PBIX proporciona una vista detallada y visual de estos aspectos, permitiendo al usuario navegar fácilmente por las métricas más importantes, proporcionando una base sólida para la toma de decisiones estratégicas.



### KPI Visualización

![imagen](https://github.com/user-attachments/assets/14125ee2-8abf-4c1d-bed0-ab29ef576451)

### KPIs Elegidos

Los KPIs seleccionados para este análisis son los de mayor oportunidad de una expansion exitosa, Seleccionando objetivos no explotados:

1. **Reducción de accesos dial-up en Buenos Aires**  
    - Este KPI monitorea la disminución del uso de conexiones de dial-up, una tecnología obsoleta que sigue siendo utilizada ampliamente por Buenos Aires. El objetivo es migrar a los usuarios hacia tecnologías más modernas como banda ancha. Puede lograrse de diversas formas:
        - **Incentivos**: Subvenciones o descuentos para usuarios que todavía usan dial-up y deseen cambiar a una nueva tecnologia.
        - **Publicidad de nicho**: Iniciar campañas de marketing dirigidas específicamente a los clientes que aún utilizan dial-up, resaltando las ventajas de las tecnologías más modernas

2. **Aumento de la velocidad promedio en el sur de Argentina**  
    - Este indicador mide el crecimiento de las velocidades de internet en las provincias del sur, una región históricamente rezagada en términos de velocidad. El KPI permite rastrear mejoras en la velocidad y comparar objetivos.
        - **Infraestructura**: Evaluar las necesidades de infraestructura en las provincias del sur y desarrollar acuerdos con proveedores locales o nacionales para mejorar la capacidad de red. Se pueden lanzar nuevas ofertas comerciales enfocadas en aumentar las velocidades a través de la actualización de equipos o la expansión de la cobertura

3. **Mejora de la conectividad en el norte del país**  
    - Este KPI evalúa el crecimiento en la cantidad de accesos a internet en las provincias del norte de Argentina, una región con menor penetración de internet historicamente. El objetivo es aumentar la cobertura y reducir la brecha digital en comparación con otras regiones del país.
        - **Inversion de expansion**: Desarrollar iniciativas de conectividad que incluyan promociones para nuevos clientes en zonas rurales o acuerdos con organizaciones locales. Invertir en la expansión de infraestructura en regiones estratégicas con baja penetración de internet, buscando apoyo gubernamental o financiamiento externo si es necesario.

## Autor y Licencia
Este Análisis fue desarrollado por **Mauricio Arce**. Si tienes preguntas o deseas conectar, no dudes en contactarme a través de [LinkedIn](https://www.linkedin.com/in/mauricioarcez/).

### Licencia
Este proyecto está licenciado bajo la [Licencia MIT](./LICENSE). Si deseas más detalles sobre lo que implica esta licencia, puedes revisar el archivo de la licencia en este repositorio.
