import requests
import pandas as pd
import io
from bs4 import BeautifulSoup

class DescargadorExcel:
    def __init__(self, url_base: str):
        """Inicializa el descargador de Excel con la URL base."""
        self.url_base = url_base  # Almacena la URL base

    def obtener_contenido_pagina(self, url: str) -> bytes:
        """Descarga el contenido de la página web y devuelve el contenido HTML.

        Args:
            url (str): La URL de la página a descargar.

        Returns:
            bytes: Contenido HTML de la página o None si ocurre un error.
        """
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
            return respuesta.content
        except requests.exceptions.RequestException as e:
            print(f"Error al acceder a la página: {e}")
            return None

    def extraer_url_excel(self, contenido_pagina: bytes, texto_enlace: str) -> str:
        """Extrae la URL del archivo Excel de la página HTML dada.

        Args:
            contenido_pagina (bytes): Contenido HTML de la página.
            texto_enlace (str): Texto del enlace que contiene la URL del archivo Excel.

        Returns:
            str: URL del archivo Excel o None si no se encuentra.
        """
        sopa = BeautifulSoup(contenido_pagina, 'html.parser')
        enlace = sopa.find('a', string=texto_enlace)
        
        if enlace and 'href' in enlace.attrs:
            return enlace['href']
        else:
            print("No se encontró el enlace.")
            return None

    def obtener_url_excel(self, url_pagina: str, texto_enlace: str) -> str:
        """Obtiene la URL del archivo Excel dado el URL de la página y el texto del enlace.

        Args:
            url_pagina (str): URL de la página que contiene el enlace.
            texto_enlace (str): Texto del enlace que contiene la URL del archivo Excel.

        Returns:
            str: URL del archivo Excel o None si no se encuentra.
        """
        contenido_pagina = self.obtener_contenido_pagina(url_pagina)
        if contenido_pagina:
            url_relativa = self.extraer_url_excel(contenido_pagina, texto_enlace)
            if url_relativa:
                # Combina la URL base con la URL relativa
                return f'{self.url_base}/{url_relativa.lstrip("/")}'
        return None

    def descargar_archivo(self, url: str) -> bytes:
        """Descarga un archivo desde la URL proporcionada y devuelve el contenido.

        Args:
            url (str): URL del archivo a descargar.

        Returns:
            bytes: Contenido del archivo descargado o None si ocurre un error.
        """
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()  # Lanza un error si la solicitud no fue exitosa
            return respuesta.content
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar el archivo de {url}: {e}")
            return None

    def leer_archivo_excel(self, contenido: bytes) -> dict:
        """Lee un archivo Excel desde el contenido descargado.

        Args:
            contenido (bytes): Contenido del archivo Excel.

        Returns:
            dict: Datos del archivo Excel o None si ocurre un error.
        """
        try:
            return pd.read_excel(io.BytesIO(contenido), sheet_name=None, engine='openpyxl')
        except Exception as e:
            print(f"Error al leer el archivo Excel: {e}")
            return None

    def listar_hojas_excel(self, contenido: bytes) -> list:
        """Lista los nombres de las hojas en el archivo Excel.

        Args:
            contenido (bytes): Contenido del archivo Excel.

        Returns:
            list: Nombres de las hojas del archivo Excel o None si ocurre un error.
        """
        try:
            datos_excel = pd.read_excel(io.BytesIO(contenido), sheet_name=None, engine='openpyxl')
            return list(datos_excel.keys())
        except Exception as e:
            print(f"Error al listar las hojas del archivo Excel: {e}")
            return None

    def obtener_y_listar_hojas(self, url_pagina: str, texto_enlace: str) -> list:
        """Obtiene la URL del archivo Excel, lo descarga y lista las hojas.

        Args:
            url_pagina (str): URL de la página que contiene el enlace.
            texto_enlace (str): Texto del enlace que contiene la URL del archivo Excel.

        Returns:
            list: Nombres de las hojas del archivo Excel o None si ocurre un error.
        """
        url_excel = self.obtener_url_excel(url_pagina, texto_enlace)
        if url_excel:
            contenido_excel = self.descargar_archivo(url_excel)
            if contenido_excel:
                return self.listar_hojas_excel(contenido_excel)
        return None

    def obtener_y_leer_hoja(self, url_pagina: str, texto_enlace: str, indice_hoja: int) -> pd.DataFrame:
        """Obtiene la URL del archivo Excel, lo descarga y lee una hoja específica por índice.

        Args:
            url_pagina (str): URL de la página que contiene el enlace.
            texto_enlace (str): Texto del enlace que contiene la URL del archivo Excel.
            indice_hoja (int): Índice de la hoja a leer.

        Returns:
            pd.DataFrame: Datos de la hoja especificada o None si ocurre un error.
        """
        url_excel = self.obtener_url_excel(url_pagina, texto_enlace)
        if url_excel:
            contenido_excel = self.descargar_archivo(url_excel)
            if contenido_excel:
                # Lee el archivo Excel y devuelve la hoja especificada por índice
                return pd.read_excel(io.BytesIO(contenido_excel), sheet_name=indice_hoja, engine='openpyxl')
        return None