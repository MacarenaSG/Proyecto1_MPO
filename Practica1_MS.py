
import json #importar las preguntas generadas en el archivo .json
import time #importar el tiempo en las preguntas.

nombre = input("\nIntroduce tu nombre:").strip().title()
print(f"\nBienvenid@ al juego de Python {nombre}, ¡Empezamos!")

def elegir_nivel():
    print("\nElige un nivel de juego:")
    print("1-Fácil")
    print("2-Medio")


    opciones = {"1": "fácil", "2": "medio"}
    eleccion = input("Selecciona una opción (1 o 2): ")

    while eleccion not in opciones:
        eleccion = input("Opción incorrecta. Elige 1 o 2: ")

    return opciones[eleccion]


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
    tiempo_limite = 10  # segundos
    print("TIENES 10 SEGUNDOS PARA RESPONDER")
    inicio = time.time()

    while True:
        respuesta = input("Tu respuesta (A/B/C/D): ").strip().upper()
        tiempo_transcurrido = time.time() - inicio

        if tiempo_transcurrido > tiempo_limite:
            print("\n¡Tiempo agotado!")
            return None

        if respuesta in ['A', 'B', 'C', 'D']:
            return respuesta
        else:
            print("Respuesta no válida. Introduzca (A,B,C o D)")


def empezar_cuestionario(dificultad):
    total_preguntas = cargar_preguntas()

    preguntas = [p for p in total_preguntas if p.get("dificultad") == dificultad]

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
        if corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            print("Correcto!\n")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['respuesta_correcta']}\n")

    mostrar_resultados(aciertos, len(preguntas))
    input("\nPresiona cualquier tecla para volver al menú...")

    guardar_resultado(nombre, aciertos, len(preguntas))

def mostrar_ranking():
    print("\n--- RANKING DE RESULTADOS ---")
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

def mostrar_menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - Empezar cuestionario")
        print("2 - Ranking")
        print("3 - Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nivel = elegir_nivel()
            empezar_cuestionario(nivel)
        elif opcion == "2":
            mostrar_ranking()
        elif opcion == "3":
            print("Gracias por jugar con nosotros. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


mostrar_menu()




