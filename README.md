# Challenge desarrollo

# Resumen
El objetivo consiste en generar un programa que, a partir de los archivos dados, guarde su contenido en una base de datos y por cada registro guardado, en donde la clasificación sea alta (high), envíe un email al manager del owner pidiendo su OK respecto de la clasificación.

Se espera tener una base de datos con la siguiente información almacenada:

- Nombre de la base de datos
- El email del owner
- El email del manager
- La clasificación de la misma

# Input 

El script <validate.py> necesita que existan 2 archivos: "users.csv" y "bases.json". Con estos archivos, el script validará la clasificación de cada base de datos (dentro de bases.json) y solicitará una ratificación al owner cuando se identifique una clasificación = HIGH. Se proporcionan los archivos antes descritos para observar su estructura.

Ejemplo users.csv:
<img width="335" alt="image" src="https://github.com/user-attachments/assets/e569a82c-dbe3-4e7b-9f51-e65d821d83a7" />

Ejemplo bases.json:
![image](https://github.com/user-attachments/assets/ab962b5f-8549-48b5-b895-cf086dbf77e3)


# Output

El script creará un nuevo archivo de nombre "resultados.csv" el cuál registrará todas las bases de datos procesadas (dentro bases.json) junto con sus respectivos responsables (dentro de users.csv). Es importante mencionar que el output se genera una sola vez y no se re-escribe desde cero, en su lugar, se agrega una nueva línea en cada ejecución.
Adicionalmente, el script imprime en consola la simulación del envío del email para bases que requieran confirmación del owner. 

Ejemplo resultados.csv:
<img width="394" alt="image" src="https://github.com/user-attachments/assets/81d6fa3e-36d1-4b72-898d-346d0b35c4b7" />

Ejemplo simulación email:
 ![image](https://github.com/user-attachments/assets/33e8e1db-5cc6-42b1-972e-768c3cd8ebff)


# Requerimientos

- Python 3.9.6
- Bibliotecas json, cv (declaradas en la sección de imports)
- Colocar los archivos users.csv, bases.json y validate.py en una misma carpeta con permisos de escritura (para crear el archivo resultados.csv)
  
Nota: Al ser un script con python "puro" no se requiere ningún framework para su ejecución.

# Ejecución

Dentro de la terminal o consola de comandos, ejecutar:
python3 validate.py

![image](https://github.com/user-attachments/assets/0645e6da-74f5-4a09-a24c-150cc974de39)



# Consideraciones

1. El script también mandará email a bases de datos sin clasificación registrada. Esto para asegurar que no se pierda ninguna potencial base crítica.
2. El script enviará el email al manager únicamente cuando el estatus del owner (user_state) sea "inactive"
3. El script está diseñado a través de diversas funciones para escalarlo y mantenerlo de manera más controlada.
4. El script no manda un email explícitamente, lo simula con impresión en consola
