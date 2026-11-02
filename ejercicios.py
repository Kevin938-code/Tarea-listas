# =====================================================================
#  ejercicios.py  —  OPCIÓN 3 DEL MENÚ: "Listar ejercicios"
# ---------------------------------------------------------------------
#  Aquí van TODOS los ejercicios del módulo 📋 Listas de la guía:
#     • 3 ejercicios DESARROLLADOS (taller paso a paso)  -> T1, T2, T3
#     • 5 ejercicios PROPUESTOS (solución oculta)         -> P1 ... P5
#
#  Cada ejercicio es UNA función sin parámetros que:
#     1) imprime su enunciado corto,
#     2) usa datos fijos de prueba (los indicados en cada función),
#     3) muestra el resultado.
#
#  REGLA: en cada ejercicio resuelve con DOS versiones cuando se indique:
#     ✋ MANUAL (bucles, patrones del módulo 0)  y  🐍 PYTHON (built-ins
#     y comprensiones). Imprime ambas para comparar.
#  Cuando termines una función, BORRA la línea "pass".
# =====================================================================


# ============================ DESARROLLADOS ==========================

def ejercicio_t1():
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero
    """
    T1 — CRUD de pasajeros con clase Pasajero + list   (Taller, Medio)
    -----------------------------------------------------------------
    Demuestra (sin menú, con llamadas directas) el CRUD completo usando
    tu clase ListaPasajerosPython:
        añadir 3 pasajeros -> listar -> buscar por cédula -> modificar
        -> eliminar -> listar otra vez -> ordenar por NOMBRE con
        sort(key=lambda p: p.nombre)  (es el reto del taller).
    Importa así:  from lista_python import ListaPasajerosPython
                from pasajero import Pasajero
    """
    lista = ListaPasajerosPython()
    pasajero1 = Pasajero("Ana", "0912345678", 28)
    pasajero2 = Pasajero("Luis", "0987654321", 35)
    pasajero3 = Pasajero("Diana", "0911111111", 22)
    lista.añadir(pasajero1)
    lista.añadir(pasajero2)
    lista.añadir(pasajero3)
    lista.listar()
    lista.buscar("0987654321")
    lista.modificar("0912345678", Pasajero("Ana"))
    lista.eliminar_por_valor("0987654321")
    lista.listar()
    ordenar_por_nombre = sorted(lista.datos, key=lambda p: p.nombre)
    print("Lista ordenada por nombre:")
    for p in ordenar_por_nombre:
        print(p)

def ejercicio_t2():
    """
    T2 — Estadísticas de una lista de notas   (Taller, Medio)
    -----------------------------------------------------------------
    Datos:  nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
            notas   = [ 8,     6,      10,      7,      5  ]
    Muestra: promedio, máxima, mínima, cantidad de aprobados (>= 7)
            y el nombre del mejor estudiante.
    ✋ MANUAL : un solo for con acumulador, campeón y contador.
    🐍 PYTHON : sum, max, min, len, notas.index(max(notas)) y
            aprobados con COMPRENSIÓN: [n for n in notas if n >= 7]
    Salida esperada: Promedio 7.20 · Máx 10 (Diana) · Mín 5 · Aprobados 3 de 5
    """
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]
    #Manual
    suma = 0
    max_nota = notas[0]
    min_nota = notas[0]
    aprobados = 0
    for i in range(len(notas)):
        suma += notas[i]
        if notas[i] > max_nota:
            max_nota = notas[i]
        if notas[i] < min_nota:
                min_nota = notas[i]
        if notas[i] >= 7:
            aprobados += 1
    promedio = suma / len(notas)
    print(f"Promedio {promedio:.2f} · Máx {max_nota} ({nombres[notas.index(max_nota)]}) · Mín {min_nota} · Aprobados {aprobados} de {len(notas)}")
    
    #python
    promedio = sum(notas) / len(notas)
    max_nota = max(notas)
    min_nota = min(notas)
    aprobados = len([n for n in notas if n >= 7])
    print(f"Promedio {promedio:.2f} · Máx {max_nota} ({nombres[notas.index(max_nota)]}) · Mín {min_nota} · Aprobados {aprobados} de {len(notas)}")

def ejercicio_t3():
    """
    T3 — Ordenar una lista (bubble sort)   (Taller, Avanzado)
    -----------------------------------------------------------------
    Datos: [5, 2, 8, 1, 9, 3, 7]
    ✋ MANUAL : burbuja con bandera hubo_swap (sobre una COPIA lista[:]).
    🐍 PYTHON : sorted(lista) y lista.sort(reverse=True).
    Extra    : palabras = ["python", "a", "código", "el"] ordenadas con key=len
    Salida esperada: [1, 2, 3, 5, 7, 8, 9]
    """
    lista = [5, 2, 8, 1, 9, 3, 7]
    #Manual
    n = len(lista)
    for vuelta in range(n - 1):
        for i in range(n - 1 - vuelta):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
    print("Lista ordenada manualmente:", lista)
    
    #Python
    lista_python = [5, 2, 8, 1, 9, 3, 7]
    lista_ordenada = sorted(lista_python)
    print("Lista ordenada con sorted():", lista_ordenada)
    
    #Extra: ordenar palabras por longitud
    palabras = ["python", "a", "código", "el"]
    palabras_ordenadas = sorted(palabras, key=len)
    print("Palabras ordenadas por longitud:", palabras_ordenadas)


# ============================= PROPUESTOS ============================

def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3
    #Manual
    contador = 0
    for x in lista:
        if x == v:
            contador += 1
    print(f"{v} aparece {contador} veces (manual)")
    
    #Python
    contador_python = lista.count(v)
    print(f"{v} aparece {contador_python} veces (Python)")
    
    #Comprensión
    contador_comprension = len([x for x in lista if x == v])
    print(f"{v} aparece {contador_comprension} veces (comprensión)")


def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    lista = [1, 2, 3, 4, 5]
    #Manual
    invertida_manual = []
    for i in range(len(lista) - 1, -1, -1):
        invertida_manual.append(lista[i])
    print("Lista invertida manualmente:", invertida_manual)
    
    #Python
    invertida_python = lista[::-1]
    print("Lista invertida con slicing:", invertida_python)
    
    invertida_reversed = list(reversed(lista))
    print("Lista invertida con reversed():", invertida_reversed)
    
    #Comprensión
    invertida_comprension = [lista[i] for i in range(len(lista) - 1, -1, -1)]
    print("Lista invertida con comprensión:", invertida_comprension)


def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
            NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    nums = [1, 3, 2, 3, 4, 1, 5, 2]
    #Manual
    unicos_manual = []
    for num in nums:
        if num not in unicos_manual:
            unicos_manual.append(num)
    print("Números únicos manualmente:", unicos_manual)
    
    #Python
    unicos_python = list(dict.fromkeys(nums))
    print("Números únicos con dict.fromkeys():", unicos_python)
    
    #Explicación de por qué list(set(nums)) no garantiza el orden
    unicos_set = list(set(nums))
    print("Números únicos con set (no garantiza orden):", unicos_set)


def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    nums = [5, 2, 9, 7, 9, 3, 8]
    #Manual
    mayor = segundo = float('-inf')
    for num in nums:
        if num > mayor:
            segundo = mayor
            mayor = num
        elif mayor > num > segundo:
            segundo = num
    print(f"Mayor {mayor} · Segundo {segundo} (manual)")
    
    #Python
    mayor_python = max(nums)
    segundo_python = sorted(set(nums))[-2]
    print(f"Mayor {mayor_python} · Segundo {segundo_python} (Python)")

def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
            y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    #Manual
    fusionada_manual = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            fusionada_manual.append(a[i])
            i += 1
        else:
            fusionada_manual.append(b[j])
            j += 1
    fusionada_manual.extend(a[i:])
    fusionada_manual.extend(b[j:])
    print("Listas fusionadas manualmente:", fusionada_manual)
    
    #Python
    fusionada_python = sorted(a + b)
    print("Listas fusionadas con sorted():", fusionada_python)


# ============================== CATÁLOGO =============================
#  (código, título, tipo, función)   ->  tipo: "taller" o "propuesto"
#  ✅ Ya está armado: NO lo cambies, úsalo en menu_ejercicios().
EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadísticas de una lista de notas",          "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)",             "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor",              "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista",                          "propuesto", ejercicio_p2),
    ("P3", "Números únicos",                              "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor",                               "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas",               "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    """
    QUÉ HACE : muestra los ejercicios agrupados y ejecuta el que elija
            el usuario, hasta que escriba 0.
    PASOS    :
    1. Con COMPRENSIONES separa el catálogo:
        taller     = [e for e in EJERCICIOS if e[2] == "taller"]
        propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
    2. Muestra:
        --- DESARROLLADOS (taller) ---
            T1. CRUD de pasajeros ...
            --- PROPUESTOS ---
            P1. Contar apariciones ...
            0.  Volver
    3. Lee el código (ej. "t2") y pásalo a mayúsculas con .upper().
    4. Busca la tupla con ese código (otra comprensión o next(...)):
            encontrados = [e for e in EJERCICIOS if e[0] == codigo]
    5. Si existe -> llama a su función:  encontrados[0][3]()
        Si no     -> "Código no válido".
    6. Repite hasta que el usuario escriba "0".
    """
    taller = [e for e in EJERCICIOS if e[2] == "taller"]
    propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
    codigo = ""
    while codigo != "0":
        print("\n--- DESARROLLADOS (taller) ---")
        for e in taller:
            print(f"  {e[0]}. {e[1]}")
        
        print("--- PROPUESTOS ---")
        
        for e in propuestos:
            print(f"  {e[0]}. {e[1]}")
        
        print("  0. Volver")
        
        codigo = input("Elige un ejercicio: ").upper()
        
        if codigo != "0":
            encontrados = [e for e in EJERCICIOS if e[0] == codigo]
            if len(encontrados) > 0:
                encontrados[0][3]()
            else:
                print("Código no válido")