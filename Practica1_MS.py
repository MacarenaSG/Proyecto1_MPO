
import json #importar las preguntas generadas en el archivo .json
import time #importar el tiempo en las preguntas.

nombre = input("\nIntroduce tu nombre:").strip().title()
print(f"\nBienvenid@ al juego de Python {nombre}, ¡Empezamos!")

def elegir_nivel():
    print("\nElige un nivel de juego:")
    print("1-Fácil")
    print("2-Medio")


    niveles = {"1": "fácil", "2": "medio"}
    eleccion = input("Selecciona una opción (1 o 2): ")

    while eleccion not in niveles:
        eleccion = input("Opción incorrecta. Elige 1 o 2: ")

    return niveles[eleccion]


def cargar_preguntas():
    with open("preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    return preguntas


def mostrar_pregunta(pregunta, numero):
    print(f"\nPregunta {numero}:")
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)

def corregir_respuesta(respuesta, correcta):
    return respuesta == correcta

def mostrar_resultados(aciertos, total):
    print(f"\n--- RESULTADOS PARA {nombre.upper()} ---")
    print(f"Preguntas totales: {total}")
    print(f"Aciertos: {aciertos}")
    porcentaje = (aciertos / total) * 100
    print(f"Porcentaje: {porcentaje:.2f}%")

    if porcentaje >= 80:
        print("PERFECTO, ¡Buen trabajo!")
    elif porcentaje >= 50:
        print("GENIAL, pero puedes mejorar.")
    else:
        print("Necesitas practicar.")


def guardar_resultado(nombre, aciertos, total):
    porcentaje = (aciertos / total) * 100
    with open("resultados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - Aciertos: {aciertos}/{total} - {porcentaje:.2f}%\n")

def obtener_respuesta():
    tiempo_limite = 10  # segundos para contestar
    inicio = time.time() # guarda el momento en el que empieza a contar el tiempo.
    print("TIENES 10 SEGUNDOS PARA RESPONDER")


    while True:
        respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
        tiempo_transcurrido = time.time() - inicio # calcula cúantos segundos pasaron desde que empezó

        if tiempo_transcurrido > tiempo_limite:
            print("\n¡Tiempo agotado!")
            return None #si el tiempo es mayor al límite, devuelve None (nulo,sin respuesta)

        elif respuesta in ['A', 'B', 'C', 'D']:
            return respuesta
        else:
            print("Respuesta no válida. Introduzca (A,B,C o D)")


def empezar_cuestionario(dificultad):
    total_preguntas = cargar_preguntas()

    preguntas = [p for p in total_preguntas if p.get("dificultad") == dificultad] # list comprehension


    if not preguntas:
        print(f"No hay preguntas disponibles para el nivel '{dificultad}'.")
        return

    aciertos = 0

    for i, pregunta in enumerate(preguntas, 1):
        mostrar_pregunta(pregunta, i)
        respuesta = obtener_respuesta()
        if respuesta is None:
            print("Respuesta no registrada por falta de tiempo.\n")
            continue
        elif corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            print("Correcto!\n")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['respuesta_correcta']}\n")

    mostrar_resultados(aciertos, len(preguntas))
    input("\nPresiona Enter para volver al menú...")

    guardar_resultado(nombre, aciertos, len(preguntas))

def mostrar_ranking():
    print("\n--- RANKING DE RESULTADOS ---")
    #Función Try-except
    try:
        with open("resultados.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print(contenido)
            else:
                print("Aún no hay resultados guardados.")
    except FileNotFoundError: #mesaje si el archivo aun no se ha creado. Se deja para que no de error el programa.
        print("Aún no se ha creado el archivo de resultados.")
    input("\nPresiona Enter para volver al menú...")

def notas_jordi():
    while True:
        print("\n---APARTADOS EXTRAS: Comentarios y dificultades---")
        print("1 - Archivo .json y Guardar los resultados ")
        print("2 - Niveles de dificultad")
        print("3 - Tiempo límite por pregunta")
        print("4 - Ranking")
        print("5 - Volver al Menu Principal")

        opcion = input("Selecciona una opción:")

        if opcion == "1":
            print("\nARCHIVO .JSON Y GUARDAR RESULTAD0S\n")
            print("Para poder realizar el archico .jason y guardar los resultados de los usiarios he utilizado referencias donde explicase varias formas de leer archivos de texto:")
            print("https://www.pythontutorial.net/python-basics/python-read-text-file/")
            print("https://es.stackoverflow.com/questions/182482/leer-un-json-desde-python")
            print("https://www.freecodecamp.org/espanol/news/lectura-y-escritura-de-archivos-en-python-como-crear-leer-y-escribir-archivos/")
            print("Gracias a estos recursos, pude implementar correctamente las funciones cargar_preguntas() y guardar_resultado(), creando así los archivos .json y .txt, de forma clara y eficiente.")
            print("Por otro lado, con ayuda de la IA pude sintetizar más el código, haciéndolo más eficiente.")

        elif opcion == "2":
            print("\nNIVELES DE DIFICULTAD\n")
            print("Elegir entre los distintos niveles de dificultas ha sido lo que más trabajo me ha costado enteder e implementar en este proyecto.")
            print("Para lograr que el usuario pueda seleccionar un nivel (fácil o medio), he tenido que aprender a trabajar con listas de diccionarios.")
            print("Ya que cada pregunta se guardaba como un diccionario con claves como -pregunta-, -opciones- y -dificultad-.")
            print("Al principio utlice un bucle for como este:")
            print("preguntas = []")
            print("for p in total_preguntas:")
            print("if p.get(¨dificultad¨) == dificultad:")
            print("preguntas.append(p)")
            print("Pero investigando aprendí que se podía simplificar usando la función list comprehension.")
            print("Usé las siguientes referencias y la IA para lograr escribir el código de una manera más limpia y sintetizada.")
            print("https://www.pythontutorial.net/python-basics/python-list-comprehensions/")
            print("https://www.geeksforgeeks.org/python/filter-list-of-dictionaries/")

        elif opcion == "3":
            print("\nTIEMPO LÍMITE POR PREGUNTA\n")
            print("En este apartado, he importado el módulo de Python, time.")
            print("En concreto, he usado la función time.time() para registrar el momento en que el usuario empieza a responder.")
            print("Así pude calcular después cuanto tardaba en introducir su respuesta en la consola y con esta herramienta contralar el tiempo.")
            print("Los recursos utilizados fueron los siguientes:")
            print("https://diveintopython.org/learn/date/time")
            print("https://www.geeksforgeeks.org/python/python-time-module")


        elif opcion == "4":
            print("\nRANKING\n")
            print("Para implementar esta parte del programa fue necesario aprender cómo manejar errores si el archivo no existía todavía.")
            print("Aquí es donde entró en juego el uso de la estructura try-except, algo que al principio me resultó difícil de comprender.")
            print("Para ello, consulté las siguientes fuentes:")
            print("https://www.pythontutorial.net/python-basics/python-try-except/")
            print("https://www.delftstack.com/howto/python/python-open-file-exception-handling")
            print("De esta forma entendí que esta estructura sirve para intentar ejecutar un bloque de código y, en caso de que ocurra un error, poder controlarlo y mostrar un mensaje adecuado sin que el programa se bloquee.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

def mostrar_menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - Empezar cuestionario")
        print("2 - Ranking")
        print("3 - Notas para Jordi")
        print("4 - Salir")



        opcion = input("Selecciona una opción:")

        if opcion == "1":
            nivel = elegir_nivel()
            empezar_cuestionario(nivel)
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            notas_jordi()
        elif opcion == "4":
            print("Gracias por jugar con nosotros. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


mostrar_menu()




