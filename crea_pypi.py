contenido_pypirc = """
[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcCJDNkMDJlNzkzLWVkNTMtNDkzNy05MmZkLWMxOGMxMjA1MTgzOQACKlszLCJkNTVmZTYyYS0zODIxLTRjMjUtOTYyNC02ZmU4ZjAyYTE2YjAiXQAABiAMoGIhaR6Y6pu5dM980kn2aCffFc3cCfqllJE3bLtTGg
"""

import os
ruta_archivo = os.path.expanduser("~/.pypirc")

with open(ruta_archivo, "w") as archivo:
    archivo.write(contenido_pypirc)

print(f"Archivo .pypirc creado en {ruta_archivo}")
