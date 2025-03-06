from Estructuras.HashTable import HashTable

import time

def limpiar_cache():
    print("[START]Limpiando Cache")
    time.sleep(1.5)
    print("[END]Limpieza de Cache")

def eliminar_tmp():
    print("[START]Eliminar archivos tmp")
    time.sleep(1.5)
    print("[END]Eliminar archivos tmp")

def crear_log_file_tmp():
    print("[START]Crear archivo de logs en tmp")
    time.sleep(1.5)
    print("[END]Crear archivo de logs en tmp")

def ejecutar_ls():
    print("[START]Redireccionar ls a archivo de logs")
    time.sleep(1.5)
    print("[END]Redireccionar ls a archivo de logs")

def ejecutar_grep():
    print("[START]Ejecutar grep sobre directorio tmp")
    time.sleep(1.5)
    print("[END]Ejecutar grep sobre directorio tmp")

def ejecutar_cat():
    print("[START]Ejecutar cat sobre archivo de logs")
    time.sleep(1.5)
    print("[END]Ejecutar cat sobre archivos de logs")

FUNCTION_CATALOG = HashTable()
FUNCTION_CATALOG.insert("A", limpiar_cache)
FUNCTION_CATALOG.insert("B", eliminar_tmp),
FUNCTION_CATALOG.insert("C", crear_log_file_tmp),
FUNCTION_CATALOG.insert("D", ejecutar_ls),
FUNCTION_CATALOG.insert("E", ejecutar_grep),
FUNCTION_CATALOG.insert("F", ejecutar_cat)