
import json

nombre = input("\nIntroduce tu nombre:").strip().title()
print(f"\nBienvenid@ al juego {nombre}, ¡Empezamos!")


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

    guardar_resultado(nombre, aciertos, len(preguntas))

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


def guardar_resultado(nombre, aciertos, total):
    porcentaje = (aciertos / total) * 100
    with open("resultados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - Aciertos: {aciertos}/{total} - {porcentaje:.2f}%\n")

mostrar_menu()



