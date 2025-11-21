import sys

# Recibe argumentos desde la linea de comando. Escribe el mensaje
# en la salida estándar.

nombre_usuario = sys.argv[1] if len(sys.argv) > 1 else 'usuario desconocido'

# Usa el argumento proporcionado o el valor predeterminado en el mensaje.
print(f'Hola, {nombre_usuario}. ¿Cómo estás?')