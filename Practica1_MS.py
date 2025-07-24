
nombre = input("\nIntroduce tu nombre:").strip().title()
print(f"\nBienvenid@ al juego {nombre}, ¡Empezamos!")


def cargar_preguntas():
    return [
        {
            "pregunta": "¿Qué tipo de lenguaje es Python?",
            "opciones": ["A. Compilado", "B. Interpretado", "C. Ensamblador", "D. Binario"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cómo se escribe un comentario de una sola línea en Python?",
            "opciones": ["A. // comentario", "B. <!-- comentario -->", "C. # comentario", "D. /* comentario */"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál es la función para mostrar datos por pantalla?",
            "opciones": ["A. display()", "B. write()", "C. show()", "D. print()"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Qué tipo de dato se obtiene con input()?",
            "opciones": ["A. Entero", "B. Booleano", "C. Cadena (string)", "D. Flotante"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Cuál de las siguientes es una estructura de control condicional?",
            "opciones": ["A. for", "B. def", "C. if", "D. while"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué operador se usa para comparar igualdad?",
            "opciones": ["A. =", "B. ==", "C. !=", "D. <>",],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál de estas estructuras es una lista en Python?",
            "opciones": ["A. {1, 2, 3}", "B. (1, 2, 3)", "C. [1, 2, 3]", "D. <1, 2, 3>"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué palabra clave se usa para definir una función?",
            "opciones": ["A. function", "B. define", "C. func", "D. def"],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "¿Qué imprime el código: print(2 + 3 * 4)?",
            "opciones": ["A. 20", "B. 14", "C. 24", "D. 18"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Qué significa len('Python')?",
            "opciones": ["A. Número de líneas de código", "B. Longitud de la palabra 'Python'", "C. Último carácter", "D. Tamaño en bytes"],
            "respuesta_correcta": "B"
        }
    ]


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


def empezar_cuestionario():
    preguntas = cargar_preguntas()
    aciertos = 0

    for i, pregunta in enumerate(preguntas, 1):
        mostrar_pregunta(pregunta, i)
        respuesta = obtener_respuesta()
        if corregir_respuesta(respuesta, pregunta["respuesta_correcta"]):
            print("Correcto!\n")
            aciertos += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {pregunta['respuesta_correcta']}\n")

    mostrar_resultados(aciertos, len(preguntas))
    input("\nPresiona cualquier tecla para volver al menú...")

def obtener_respuesta():
    respuesta = input("Tu respuesta (A/B/C/D): ").upper()
    while respuesta not in ['A', 'B', 'C', 'D']:
        respuesta = input("Por favor, introduce una opción válida (A/B/C/D): ").upper()
    return respuesta


def mostrar_menu():
    while True:
        print("\n### MENÚ ###")
        print("1 - Empezar cuestionario")
        print("2 - Ranking (opcional)")
        print("3 - Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            empezar_cuestionario()
        elif opcion == "2":
            print("Ranking aún no implementado.")
        elif opcion == "3":
            print("Gracias por jugar con nosotros. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

mostrar_menu()
