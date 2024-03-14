Prueba Técnica para Backend Developer en DriveMe Barcelona
==========================================================

Bienvenido/a a la prueba técnica para el puesto de Backend Developer en DriveMe Barcelona. El objetivo de esta prueba es evaluar tus habilidades en la conexión a bases de datos desde distintos lenguajes, integración de APIs, realización de peticiones AJAX, y la aplicación de buenas prácticas de programación.

Tiempo estimado
---------------

30-45 minutos.

Objetivos
---------

*   Demostrar habilidad en la conexión a bases de datos.
*   Integrar APIs externas.
*   Realizar peticiones AJAX.
*   Aplicar buenas prácticas de programación.

Ejercicio Propuesto
-------------------

Deberás completar los archivos `index.php` y `app.py` para cumplir con las siguientes funcionalidades:

1.  Al cargar el archivo `index.php`, debe mostrar en el mapa todos los puntos almacenados en la base de datos. Al hacer clic sobre ellos, se mostrará información específica de cada punto.
2.  Al hacer clic en una parte del mapa sin marcadores, se debe realizar una petición AJAX a `/guardar-clima`, gestionada por Python (Flask) en el archivo `app.py`.
3.  Esta petición debe enviar la latitud y longitud, hacer una consulta a la API de OpenWeatherMap, guardar los datos recibidos en la base de datos y devolver una respuesta.

Puedes ver un ejemplo de la funcionalidad esperada en el siguiente gif:

![Demostración del proyecto](demostration.gif)

Instalación
-----------

### Preparación del entorno

1.  **Entorno virtual de Python:**
    
    *   Crea el entorno virtual: `python3 -m venv venv`
    *   Activa el entorno virtual:
        *   En Windows: `venv\Scripts\activate`
        *   En Linux/Mac: `source venv/bin/activate`
    *   Instala las dependencias: `pip install -r requirements.txt`
2.  **Configuración de la base de datos:**
    
    *   Modifica los datos en `config.ini` con los detalles de tu conexión a MySQL.
3.  **Inicialización de la base de datos:**
    
    *   Ejecuta `init-db.php` para crear la base de datos y la tabla `clima` con todas sus columnas.

### Ejecución

*   Si estás utilizando Flask para el endpoint de la API, debes ejecutar el archivo `app.py` y mantenerlo ejecutándose mientras desees que la ruta `/guardar-clima` esté operativa.

A valorar
-----------

Se tendrá en cuenta cualquier mejora que se considere añadir

¡Mucho éxito!
-------------

Esperamos que disfrutes realizando esta prueba tanto como nosotros al diseñarla. ¡Ánimo y suerte!

* * *

Este es solo un ejemplo y puedes ajustarlo según las necesidades específicas de la prueba o las instrucciones adicionales que desees incluir.