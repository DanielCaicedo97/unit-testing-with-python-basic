# Aprendiendo Unit Test con Python 🧪🐍

Este proyecto tiene como objetivo enseñar y practicar pruebas unitarias en Python utilizando herramientas comunes como `unittest`, `ipdb` para depuración interactiva y `pycodestyle` para revisión de estilo de código.

---

## 🛠️ Requisitos Previos

Antes de ejecutar las pruebas o desarrollar en este repositorio, es recomendable crear un entorno virtual (virtual environment) e instalar las dependencias necesarias.

### 1. Crear un entorno virtual

```bash
python -m venv venv
```
2. Activar el entorno virtual
- En Windows:

```bash
venv\Scripts\activate
```
- En macOS/Linux:
```bash
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```
🧰 Herramientas utilizadas
- **unittest**: Framework de pruebas unitarias incluido en la biblioteca estándar de Python.  
  [Documentación oficial de unittest](https://docs.python.org/3/library/unittest.html)

- **ipdb**: Depurador interactivo que permite pausar la ejecución y explorar el estado del programa.

- **pycodestyle**: Herramienta para verificar que el código cumpla con la guía de estilo PEP8.

- **idna**: Soporte para nombres de dominio internacionalizados (Unicode).

- **requests**: Biblioteca para realizar peticiones HTTP de forma sencilla.

- **Faker**: Generador de datos falsos útiles para pruebas (nombres, correos, direcciones, etc.).

- **coverage**: Herramienta para medir la cobertura del código durante la ejecución de pruebas.

### para inicializar las pruebas se llama el modulo de unittest y la carpeta test 
``` bash
python -m unittest discover -v -s test
```

# Fundamentos Testing Python 

Probar software no solo es una tarea técnica, es un proceso crítico que puede marcar la diferencia entre el éxito o el fracaso de un proyecto. Un pequeño error no detectado puede causar grandes problemas, como lo demuestra el caso del cohete de la Agencia Espacial Europea en 1996. Afortunadamente, en el desarrollo de software contamos con herramientas como Python y sus módulos para asegurar la calidad del código antes de que llegue a los usuarios.

## ¿Qué tipos de pruebas son necesarias para asegurar la calidad del software?
 - Pruebas unitarias: Se encargan de validar que cada componente pequeño del código funcione correctamente de manera aislada.
 - Pruebas de integración: Verifican que los distintos componentes trabajen bien en conjunto, evitando problemas en la interacción de partes.
 - Pruebas funcionales: Validan que el sistema en su totalidad funcione como se espera según los requisitos.
 - Pruebas de rendimiento: Aseguran que el software sea rápido y eficiente, evaluando su comportamiento bajo diferentes condiciones de carga.
 - Pruebas de aceptación: Determinan si el software cumple con las expectativas del usuario final.

## ¿Qué herramientas de testing ofrece Python?
- UnitTest: Permite crear pruebas unitarias de manera sencilla, asegurando que todas las partes del código realicen su función correctamente.
- PyTest: Facilita la creación de pruebas con una configuración avanzada para cubrir diferentes escenarios.
- DocTest: Integra pruebas directamente en los comentarios de las funciones, permitiendo validar el código mientras se mantiene la documentación.

## ¿Cómo garantizar que todas las líneas de código están siendo probadas?
Es crucial identificar las líneas de código que no están cubiertas por pruebas. Para esto, existe Coverage, una herramienta que genera un reporte en HTML mostrando qué partes del código no han sido validadas, lo que permite agregar pruebas adicionales donde sea necesario.

## ¿Por qué es importante el testing en software?
El testing asegura que el software sea funcional, rápido y confiable, pero más allá de eso, puede evitar costosos errores, pérdidas financieras y en casos extremos, salvar vidas. Al probar el software antes de que llegue a producción, los desarrolladores tienen la ventaja de corregir fallos antes de que impacten a los usuarios.

## Pruebas Automatizadas y Unitarias con Python: Ahorra Tiempo y Evita Errores

Las pruebas en el desarrollo de software son esenciales para garantizar la calidad y estabilidad del código antes de lanzarlo a producción. Tanto las pruebas manuales como las automatizadas juegan un rol fundamental para detectar errores. Usar Python para automatizar estas pruebas no solo ahorra tiempo, sino que también asegura que los errores críticos se detecten antes, evitando posibles pérdidas económicas y de confianza de los usuarios.

### ¿Qué son las pruebas manuales y cómo funcionan?
Las pruebas manuales consisten en validar el funcionamiento de un cambio en el código mediante la interacción directa con la aplicación. Esto se hace, por ejemplo, al modificar una línea de código, ejecutar la aplicación y verificar si el cambio funciona correctamente. Es similar al trabajo de un mecánico que ajusta un auto y luego lo prueba encendiéndolo cada vez.

### ¿Cómo funcionan las pruebas unitarias?
Las pruebas unitarias permiten validar que pequeñas piezas de código, como funciones individuales, trabajan correctamente. En el ejemplo de un mecánico, esto sería como revisar solo un neumático: inflarlo, verificar que no tenga fugas y confirmar que esté en buen estado. En Python, estas pruebas se automatizan utilizando la palabra clave assert, que compara los resultados esperados con los reales.

### ¿Qué son las pruebas de integración?
Las pruebas de integración verifican que diferentes componentes de la aplicación funcionen en conjunto sin problemas. En el caso del mecánico, sería comprobar que el neumático instalado en el coche funcione bien con el resto de las piezas del vehículo. En desarrollo de software, esto se traduce a verificar, por ejemplo, que el proceso de inicio de sesión funcione correctamente, desde la entrada del usuario hasta la confirmación del acceso.

### ¿Cómo Python nos ayuda a automatizar pruebas?
Python ofrece herramientas para automatizar las pruebas, permitiendo ejecutar muchas validaciones rápidamente sin intervención manual. A través de pruebas automatizadas, podemos detectar errores que de otro modo podrían pasar desapercibidos y llegar a producción, como un fallo en el cálculo de una orden de compra. Esto es crítico para evitar situaciones como la que enfrentó CrowdStrike, donde un error no detectado en una actualización paralizó aeropuertos.

``` python
def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total


def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook", "price": 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products) == 12


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
```

## Estructura de Proyectos de Testing con Unit Test en Python

La creación de funciones y pruebas para el código que se va a producción es clave para validar resultados correctamente. En Python, el uso de Unit Testing simplifica este proceso, permitiendo automatizar pruebas y hacerlas más legibles y eficientes, además de integrarse fácilmente con sistemas de Continuous Integration.

### ¿Cómo mejorar la legibilidad de las pruebas con Unit Testing?
Python incluye Unit Testing de forma nativa, proporcionando clases reutilizables para ejecutar pruebas de manera automática o manual. Esta herramienta no solo permite mejorar la legibilidad, sino también identificar y solucionar errores rápidamente, sin necesidad de depender de print para verificar si las pruebas se están ejecutando.

### ¿Cómo estructurar un proyecto de testing en Python?
Separación de código y pruebas: Coloca el código fuente en una carpeta src y las pruebas en una carpeta test.
Entorno virtual: Crea un entorno virtual para aislar dependencias del proyecto. Esto se hace con `python -m venv`, lo que genera una carpeta con binarios y librerías solo para el proyecto.
Uso de gitignore: Añade un archivo`.gitignore` para evitar que el entorno virtual y otros archivos no deseados se suban al repositorio.
## ¿Cómo escribir y ejecutar pruebas con Unit Test?
Para escribir pruebas, sigue estas buenas prácticas:

Crea un archivo de pruebas, como `test_calculator.py`, y empieza importando Unit Test.
Define clases que hereden de unittest.TestCase.
Escribe métodos de prueba que validen funciones específicas usando assertEqual para verificar resultados.
Ejemplo básico de prueba:
``` python
import unittest
from src.calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
```
Ejecuta las pruebas con `python -m unittest discover` para que Unit Testing encuentre y ejecute las pruebas automáticamente.

### ¿Qué hacer cuando una prueba falla?
Si una prueba falla, Unittest lo indica con una “F”, mostrando el error detallado, lo que facilita la depuración. Puedes forzar un fallo, por ejemplo, esperando que la `suma de 2 + 3 sea 6 en lugar de 5`, para ver cómo se comporta.

# Conceptos Básicos de Unittest

## Pruebas Unitarias con Python: Métodos Setup y Teardown
Las pruebas unitarias en Python son esenciales para asegurar el correcto funcionamiento del código. Utilizando la clase TestCase de la biblioteca UnitTest, podemos estructurar pruebas de manera eficiente y limpiar recursos una vez que se han ejecutado. Además, permite automatizar la validación de resultados y la captura de errores. Vamos a profundizar en cómo implementar estas pruebas y algunos métodos clave que facilitan este proceso.

 ### ¿Cómo configurar las pruebas en Python con TestCase?
El método `setUp()` nos permite configurar elementos antes de que cada prueba se ejecute. Imagina que tienes cinco pruebas que requieren la misma preparación: en lugar de repetir la configuración, puedes ejecutarla una sola vez aquí. Esto ahorra tiempo y esfuerzo al evitar la duplicación de código.

Por ejemplo:

Puedes utilizar `setUp()` para crear una base común de datos, abrir archivos, o preparar datos de entrada.
Luego, cada prueba reutiliza esta configuración, asegurando que el entorno siempre esté listo para las pruebas.
### ¿Cómo limpiar después de una prueba?
El método `tearDown()` sirve para limpiar los recursos utilizados en la prueba. Supongamos que has creado cientos de archivos para una prueba, este método permite eliminarlos automáticamente después de que la prueba finaliza, asegurando que el sistema no quede lleno de datos innecesarios.

Algunos ejemplos de cuándo usarlo:

- Eliminar archivos temporales creados durante las pruebas.
- Cerrar conexiones a bases de datos o liberar recursos del sistema.

### ¿Cómo ejecutar pruebas y capturar errores?
La clase `TestCase` no solo organiza las pruebas, también proporciona un método automático para ejecutar cada una de ellas. El método `runTest()` gestiona la ejecución de las pruebas, captura los errores y valida que todo funcione correctamente. Este proceso automatiza la validación de resultados esperados y la identificación de fallos.

Por ejemplo:

- Si tienes una lista de pruebas, este método las ejecutará una por una, asegurando que todas se validen correctamente.
-Además, capturará las excepciones que se lancen durante la ejecución.
### ¿Cómo validar excepciones en las pruebas unitarias?
Una situación común en las pruebas de una calculadora es manejar la división por cero. La mejor práctica es lanzar una excepción para evitar errores. Python permite validar que la excepción se ha lanzado correctamente en las pruebas.

Pasos clave:

- Crear una prueba donde `b = 0`.
- Utilizar `assertRaises()` para verificar que se ha lanzado la excepción ValueError.


## ¿Por qué validar excepciones en pruebas unitarias?

Detección temprana de errores: Identifica fallos en la lógica de tu código antes de que causen problemas en producción.
Código más robusto: Hace que tu código sea más resistente a errores inesperados.
Documentación implícita: Indica las condiciones de error y los tipos de errores posibles.
Facilita la depuración: Aísla la causa de los errores de manera más efectiva.
Mejora la calidad del código: Contribuye a un código más limpio y confiable.

## Formato de Nombres para Pruebas Unitarias en Python

Nombrar pruebas correctamente es clave para el éxito en equipo, facilitando la comprensión del código y la colaboración efectiva. Aunque no es obligatorio, tener un formato claro para las pruebas es muy beneficioso.

 ### ¿Cómo definir el formato de los nombres de las pruebas?
Todos los tests deben agruparse en clases, cada una relacionada con una clase de tu proyecto. Por ejemplo, si tienes una clase llamada BankAccount, la clase de prueba debería llamarse BankAccountTest.
Cada prueba debe comenzar con test_, para que las herramientas de testing la identifiquen fácilmente.

El siguiente elemento en el nombre debe ser el método que estás probando. Si es un método deposit, el nombre sería test_deposit_.

### ¿Cómo estructurar el escenario de la prueba?
Después del método, añade el escenario. Esto se refiere a los valores o parámetros que usas en la prueba. Por ejemplo, en el caso de un valor positivo en un depósito, el escenario sería positive_amount.

### ¿Cómo describir el resultado esperado?
Para finalizar el nombre, indica el resultado esperado. Si el depósito incrementa el saldo, añade algo como increase_balance. Así, un nombre de prueba completo sería: test_deposit_positive_amount_increase_balance.

### ¿Por qué es útil este formato?
Permite a cualquier miembro del equipo entender el propósito de la prueba sin revisar el código completo.
Facilita el mantenimiento del código y el soporte, ya que con solo leer el nombre, se entiende el objetivo de la prueba.

### ¿Qué reto se propone para mejorar las pruebas actuales?
Refactoriza las pruebas que has creado, probando diferentes escenarios y resultados posibles.
Imagina nuevas circunstancias para probar el código.
Compara tus resultados con el proyecto refactorizado que estará disponible en la sección de recursos, y comparte tus ideas.

Estructura sugerida:

`test_MétodoProbado_escenario_ResultadoEsperado`

Método probado: deposit
escenario: positive amount
resultado esperado: increase balance
test_deposit_positive_amount_increase_balance

# Técnicas Avanzadas en pruebas unitarias

## Pruebas de APIs en Python con Mocking(imitar ) y UnitTest
La simulación de servicios externos es crucial en proyectos de software para garantizar que las pruebas no dependan de APIs externas. Para lograrlo, utilizamos los Mocks, que permiten evitar las llamadas reales a servicios y, en cambio, retornan respuestas controladas en nuestras pruebas. En este caso, aprenderemos a mockear una API de geolocalización y a realizar pruebas efectivas.

### ¿Qué es un Mock y cómo nos ayuda?
Un Mock es una herramienta que nos permite simular comportamientos de funciones o servicios externos. En lugar de ejecutar una llamada real a una API, podemos definir una respuesta predefinida, lo que permite:

Evitar depender de servicios externos en pruebas.
Acelerar la ejecución de las pruebas.
Controlar los resultados esperados.
### ¿Cómo integramos una API externa en Python?
Primero, se configura una función que recibe la IP del cliente y devuelve la ubicación mediante una API de terceros. Para hacer esto:

Se instala la librería requests con 

``` bash
pip install requests
```
Se crea un archivo api_client.py donde conectamos con la API utilizando requests.get.
Al recibir la respuesta, se convierte el resultado a JSON para obtener la información de país, ciudad y región.

### ¿Cómo probamos sin hacer llamadas reales?
El problema principal de las pruebas de integraciones con APIs es que pueden demorar, ya que las respuestas dependen de factores externos. Para evitar esto, se usan Mocks. A través del decorador @patch de unittest.mock, podemos interceptar la llamada a la API y retornar datos predefinidos.

Pasos a seguir:

Decorar la función de prueba con @patch.
Simular el valor retornado usando mock.return_value para definir qué debe devolver la llamada a la API.
Definir tanto el código de estado como el contenido del JSON que esperamos recibir.
### ¿Cómo validar que nuestra simulación funciona correctamente?
Además de simular respuestas, debemos asegurarnos de que las pruebas validen correctamente los llamados. Se puede usar assertCalledOnceWith para garantizar que la URL y los parámetros pasados son los correctos.


## simulación de Side Effect Con Mock en Pruebas Unitarias
Mock nos permite simular comportamientos variables, una herramienta útil cuando queremos probar cómo reacciona nuestro código ante diferentes escenarios sin modificar el entorno real. Uno de los usos más poderosos es el “side effect”, que nos ayuda a hacer que un método falle en un caso y funcione en otro. Esto es clave para manejar errores temporales, como en el caso de una API de pagos que rechaza una tarjeta incorrecta, pero acepta una correcta en un segundo intento.

### ¿Cómo se define un “side effect” en Mock?
El “side effect” en Mock nos permite modificar el comportamiento de un método en distintas llamadas. Se define como una lista de comportamientos, donde cada elemento de la lista corresponde al resultado de una llamada específica. Esto permite:

Simular fallos de manera controlada, como lanzar excepciones específicas en las pruebas.
Probar el código bajo diferentes condiciones sin interactuar con los servicios externos.

### ¿Cómo se maneja un error y una respuesta exitosa en pruebas unitarias?
En una prueba unitaria con Mock, podemos definir comportamientos variables. Por ejemplo, para simular una excepción, usamos la estructura side_effect, donde la primera llamada lanza un error y la segunda retorna una respuesta exitosa. Esto permite cubrir ambos casos sin necesidad de realizar un request real.

Definimos el primer comportamiento con una excepción.
Luego, para el segundo comportamiento, usamos Mock para devolver un objeto con los valores que esperamos, simulando una respuesta exitosa.
### ¿Qué métodos auxiliares facilita Mock?
Mock facilita métodos como raiseException, que lanza una excepción específica, y mock, que permite crear objetos personalizados. Estos objetos pueden tener parámetros configurables como status_code y devolver datos específicos al llamar métodos como JSON. Este tipo de pruebas es crucial para validar la resiliencia del software ante errores temporales.

### ¿Cómo integrar validaciones adicionales en las pruebas?
Para reforzar las pruebas, puedes agregar validaciones adicionales, como simular el envío de una IP inválida. En este caso, si la IP es incorrecta, se debe lanzar un error, mientras que si es válida, debe retornar los datos de geolocalización. Esto se implementa agregando más casos en la lista de side effects, cubriendo así todas las situaciones posibles.


## Simulación de horarios para pruebas unitarias en python

En esta lección, hemos aprendido a modificar el comportamiento de objetos y funciones dentro de nuestras pruebas en Python, utilizando técnicas como el patch para simular situaciones específicas, como el control del horario de retiro en una cuenta bancaria. Esta habilidad es crucial cuando necesitamos validar restricciones temporales o cualquier otra lógica de negocio que dependa de factores externos, como el tiempo.

### ¿Cómo podemos restringir el horario de retiros en una cuenta bancaria?
Para implementar la restricción de horario, se utilizó la clase datetime para obtener la hora actual. Definimos que los retiros solo pueden realizarse durante el horario de oficina: entre las 8 AM y las 5 PM. Cualquier intento fuera de este horario lanzará una excepción personalizada llamada WithdrawalError.

Se implementó la lógica en el método de retiro de la clase BankAccount.
La restricción se basa en comparar la hora actual obtenida con datetime.now().hour.
Si la hora es menor que las 8 AM o mayor que las 5 PM, se lanza la excepción.

### ¿Cómo podemos probar la funcionalidad de manera efectiva?
Las pruebas unitarias permiten simular diferentes horas del día para validar que las restricciones funcionen correctamente. Para lograrlo, usamos el decorador patch del módulo unittest.mock, el cual modifica temporalmente el comportamiento de la función datetime.now().

Con patch, podemos definir un valor de retorno específico para now(), como las 7 AM o las 10 AM.
De esta forma, se puede validar que la excepción se lance correctamente si el retiro ocurre fuera del horario permitido.
En caso de que el retiro sea dentro del horario, la prueba verificará que el saldo de la cuenta se actualice correctamente.

### ¿Cómo corregimos errores en la lógica de negocio?
Durante la implementación, encontramos un error en la condición lógica del horario. Inicialmente, se utilizó un operador and incorrecto para verificar si la hora estaba dentro del rango permitido. Este error se corrigió cambiando la condición a un or, asegurando que la lógica prohibiera retiros antes de las 8 AM y después de las 5 PM.

# Exploración de Herramientas y Métodos Complementarios

## Parametrizacion de pruebas Con SubTest en unitTest

El uso de SubTest en UnitTest te permite optimizar tus pruebas evitando la duplicación de código. Imagina que necesitas probar un método con varios valores diferentes. Sin SubTest, tendrías que crear varias pruebas casi idénticas, lo que resulta ineficiente. SubTest permite parametrizar pruebas, lo que significa que puedes ejecutar la misma prueba con diferentes valores sin repetir el código.

### ¿Cómo evitar la duplicación de pruebas con SubTest?
Al utilizar SubTest, puedes definir todos los valores que deseas probar en una lista o diccionario. Luego, iteras sobre estos valores mediante un bucle for, ejecutando la misma prueba con cada conjunto de parámetros. Así, si es necesario modificar la prueba, solo tienes que hacer cambios en un único lugar.

### ¿Cómo implementar SubTest en un caso práctico?
Para ilustrarlo, se puede crear una prueba llamada test_deposit_various_values. En lugar de duplicar la prueba con diferentes valores de depósito, utilizas un diccionario que contiene los valores a probar y el resultado esperado. Después, recorres estos valores con SubTest usando la estructura with self.subTest(case=case) y ejecutas la prueba para cada valor del diccionario. Esto asegura que cada prueba sea independiente y evita sumar valores a la cuenta de manera incorrecta.

### ¿Cómo gestionar errores con SubTest?
SubTest también es útil para identificar errores específicos. Si una prueba falla con un conjunto particular de parámetros, SubTest te permite ver fácilmente qué valores causaron el fallo. Esto facilita mucho la corrección de errores, ya que puedes aislar rápidamente los casos problemáticos y corregirlos de manera eficiente.

## Pruebas de Código con Doctest en Python

El uso de Doctest es una herramienta poderosa que te permite escribir pruebas directamente en la documentación del código, lo que facilita que otros desarrolladores comprendan y verifiquen los resultados esperados. Además de los Unit Tests tradicionales, Doctest permite que tus comentarios sean interactivos, ofreciendo ejemplos funcionales que se ejecutan dentro del código de Python. Veamos cómo puedes utilizarlo de manera eficiente.

### ¿Qué es Doctest y cómo se usa?
Doctest es una librería que está incluida en Python y que permite crear pruebas en los comentarios del código. Esto lo hace práctico ya que puedes escribir pruebas de manera muy similar a una sesión interactiva de Python. Solo debes añadir los ejemplos dentro de los comentarios y ejecutarlos con el comando python -m doctest.

### ¿Cómo se estructuran las pruebas en Doctest?
Para escribir una prueba, simplemente crea un comentario que simule una sesión interactiva. Estas sesiones se caracterizan por comenzar con >>>. Por ejemplo, si tienes una función de suma en tu clase Calculator, podrías escribir lo siguiente:
```
>>> sum(5, 7)
12
```
Esto se ejecutará como si estuvieras en el shell de Python, y esperará que la salida sea 12. Si el resultado no coincide con lo esperado, Doctest te notificará el error.

### ¿Qué hacer si hay un error en la prueba?
Si Doctest encuentra un error, revisa el mensaje de error y ajusta el código o la prueba según sea necesario. Por ejemplo, si ejecutas una prueba y esperabas 12 pero el resultado fue 11, Doctest te informará de la discrepancia. Solucionas el error, corriges el comentario, y ejecutas nuevamente.

### ¿Cómo manejar excepciones en Doctest?
Doctest también te permite probar excepciones. Si tienes una función que lanza un ValueError al intentar dividir por cero, puedes capturar este comportamiento en el comentario:
```
>>> divide(10, 0)
Traceback (most recent call last):
  ...
ValueError: División por 0 no permitida
```
Este tipo de pruebas asegura que las excepciones se manejen correctamente y ayuda a otros desarrolladores a entender los casos de error.

### ¿Por qué es importante documentar con Doctest?
La documentación clara es clave en cualquier proyecto de software, y Doctest facilita agregar ejemplos en el código que no solo explican cómo usar las funciones, sino que además se prueban automáticamente. Esto garantiza que la documentación esté siempre alineada con el comportamiento real del código.

### ¿Qué reto implica utilizar Doctest?
El reto de este enfoque es agregar suficiente documentación con ejemplos ejecutables que cubran todos los casos, incluyendo los casos de borde, como divisiones por cero o parámetros inválidos. Este proceso no solo mejora la calidad del código, sino también la de la documentación, haciéndola más útil para todo el equipo.


## Generación de Datos de Prueba con la Librería Faker
Generar datos de prueba puede ser una tarea tediosa, pero con la librería Faker, este proceso se simplifica enormemente. Faker nos permite crear datos aleatorios como nombres, correos electrónicos y otros atributos de manera eficiente para validar la compatibilidad de nuestro código con diversas entradas. A continuación, exploramos cómo aprovechar Faker en pruebas automatizadas y cómo integrar la librería en nuestro proyecto.

### ¿Cómo instalar Faker y qué ventajas ofrece?
Para empezar a utilizar Faker, simplemente debemos instalarla a través de la terminal con el comando:
```
pip install Faker
```
En Windows
```
pip freeze | findstr Faker
```
Una vez instalada, podemos importarla en nuestro proyecto e instanciar un generador de datos aleatorios. Faker nos ofrece una gran variedad de métodos predefinidos para generar nombres, correos, cuentas bancarias, entre otros. La ventaja clave es que nos permite automatizar la generación de múltiples entradas en cada ejecución de nuestras pruebas.

### ¿Cómo integramos Faker en nuestro proyecto?
Una vez que hemos instalado Faker, es esencial agregar la librería a nuestro archivo requirements.txt. Esto asegura que todas las dependencias se mantengan actualizadas y permite su instalación en futuros entornos. También es importante definir una versión fija para evitar problemas con actualizaciones inesperadas que puedan romper nuestro código.

### ¿Cómo crear una clase User con Faker?
Al integrar Faker, podemos crear pruebas más realistas. Por ejemplo, al generar datos para un usuario con múltiples cuentas bancarias, podemos usar Faker para generar atributos como el nombre, correo electrónico y balances de cuentas de forma dinámica. A continuación, se muestra un ejemplo de cómo podemos definir una clase User y generar múltiples cuentas con balances aleatorios:

Se crea una clase User que requiere un nombre, correo electrónico y una lista de cuentas bancarias.
Faker se utiliza para generar estos valores automáticamente en cada prueba.
Se pueden generar múltiples cuentas para un mismo usuario, iterando sobre un ciclo for para generar diferentes balances y archivos de log.
### ¿Cómo se estructuran las pruebas con Faker?
En nuestras pruebas unitarias, podemos instanciar Faker en el método setUp para reutilizarla en todas las pruebas. Esto nos permite generar nombres y correos electrónicos dinámicos en cada ejecución. A continuación, se presentan los pasos clave para estructurar las pruebas:

Instanciamos Faker en el método setUp.
Definimos pruebas para la creación de usuarios con múltiples cuentas.
Utilizamos Faker para generar atributos aleatorios como balances y nombres de archivo.
Validamos que los valores generados sean correctos utilizando assertEqual para verificar la integridad de los datos.
### ¿Qué otras configuraciones y opciones ofrece Faker?
Faker ofrece una amplia gama de configuraciones. Por ejemplo, podemos definir el idioma de los datos generados. Esto es útil si necesitamos que nuestros datos de prueba estén en español o en otro idioma. También es posible generar datos más complejos como nombres de archivos, países o incluso valores numéricos aleatorios con rangos definidos.

### ¿Cómo limpiar el entorno de pruebas?
Al generar archivos temporales durante las pruebas, es importante asegurarse de limpiar el entorno una vez que finalicen. Esto se puede hacer implementando un método tearDown que borre los archivos generados durante la ejecución de las pruebas, garantizando que el entorno de pruebas se mantenga limpio.

# Mejora y Automatizacion de Pruebas 

## Cobertura de Código en Python con Coverage: Instalación y Uso

En los proyectos grandes de software, resulta difícil identificar qué partes del código están correctamente probadas y cuáles no lo están. Por ello, es esencial usar herramientas como Coverage, que nos permite analizar qué porciones de nuestro código han sido ejecutadas durante las pruebas y cuáles no. Esto facilita la detección de áreas que necesitan cobertura adicional.

### ¿Qué es Coverage y cómo funciona?
Coverage es una herramienta que se ejecuta junto a las pruebas y captura un reporte sobre qué partes del código han sido probadas. Una vez finalizado el proceso, genera un informe detallado que indica qué porcentaje del código está cubierto. De esta manera, puedes identificar qué secciones de código necesitan nuevas pruebas.

### ¿Cómo instalar y utilizar Coverage?
Para instalar Coverage en un proyecto Python, sigue los siguientes pasos:

Abre la terminal e instala la herramienta con 
```
pip install coverage.
```
Después, usa 
linux y mac 
```
pip freeze | grep coverage
```
windows
```
pip freeze | findstr coverage
```
para agregar la librería a tu archivo de requirements.
Una vez instalada, ejecuta el comando 
```
coverage run -m unittest discover -s tests, 
```
que corre las pruebas en la carpeta tests.

### ¿Cómo generar el reporte de cobertura?
Para generar el informe de cobertura de código:

Usa el comando coverage report para obtener un resumen de las pruebas.
Si quieres un reporte visual más detallado, ejecuta coverage html. Esto creará una carpeta con archivos HTML que podrás abrir en el navegador.
### ¿Cómo mejorar el reporte excluyendo archivos de prueba?
Para evitar que los archivos de prueba aparezcan en el reporte, agrega el parámetro --source=src al comando coverage run. Esto asegura que solo se evalúe el código fuente de la aplicación y no las pruebas en sí mismas.

### ¿Cómo detectar y corregir código sin pruebas?
Coverage permite identificar líneas específicas que no han sido probadas. Usando el reporte HTML, puedes hacer clic en los archivos para ver las líneas de código no ejecutadas. Un ejemplo sería la detección de un método que no maneja una división por cero. Al agregar un test para esta excepción, puedes aumentar la cobertura total del proyecto.

### ¿Cómo validar un porcentaje mínimo de cobertura?
En proyectos con equipos grandes, es recomendable establecer un porcentaje mínimo de cobertura, como un 80%, para garantizar la calidad del código. Esto se puede configurar en la documentación de Coverage.

## Integración Continua con GitHub Actions para Pruebas Automatizadas
Integrar una suite de pruebas en un sistema de Continuous Integration (CI) es clave para automatizar el proceso de verificación de cambios en el código. En este caso, usaremos GitHub Actions para correr nuestras pruebas de manera automática cada vez que haya un cambio en el repositorio, asegurándonos de que el código esté siempre funcionando correctamente.

## ¿Cómo configurar tu primera GitHub Action?
Primero, accede a la pestaña de “Actions” dentro de tu repositorio en GitHub. Ahí encontrarás un Marketplace con varias opciones. Busca “Python” y selecciona la Action “Python Application”. Esta configuración correrá pruebas automáticamente cada vez que haya un push o un pull request hacia la rama “Main”.

## ¿Qué pasos incluye el workflow de pruebas?
Clonación del repositorio: El workflow comienza clonando tu código, similar a un git clone.
Configuración de Python: Utiliza la versión 3.10 de Python, asegurando compatibilidad con el código del proyecto.
Instalación de dependencias: Ejecuta las instalaciones de las librerías listadas en el archivo requirements.txt, por ejemplo, Faker y Coverage.
Modificación del comando de pruebas: En lugar de utilizar un test genérico, el comando se cambia a `python -m unittest discover test` , adaptado a las pruebas unitarias del proyecto.
## ¿Cómo verificar si el workflow fue exitoso?
Una vez configurado el archivo y hecho el commit, puedes ver el progreso de la ejecución en la pestaña de “Actions”. Si todo salió bien, aparecerá un checkmark verde indicando que las pruebas pasaron exitosamente.

## ¿Cómo mejorar la cobertura de pruebas en tu pipeline?
El reto adicional consiste en ejecutar las pruebas con diferentes versiones de Python utilizando Matrix en GitHub Actions. Esto te permitirá probar tu código en varios entornos, asegurando mayor robustez y evitando problemas de compatibilidad.