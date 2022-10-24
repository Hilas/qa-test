
![](https://talana.app/img/logoTalana.png)  
  
# Prueba teórica  
  
1. **¿Cuál de las siguientes cualidades es MÁS probable que forme parte de la mentalidad de un tester que de la de un desarrollador?**  
 - [ ] a)  ~~Experiencia en la que basar sus esfuerzos.~~  
   - [ ] b)  ~~Capacidad de ver lo que puede estar mal.~~  
   - [x] c)  Buena comunicación con los miembros del equipo.  
   - [x] d)  Atención al detalle.  
  
2. **Defina “Defecto”**  
 - Defecto, es un error en un componente o software al cual puede aplicar un resultado no esperado o que no cumple lo requerido  
  
3. **Defina “Resultado Esperado”**  
 - Resultado esperado, es lo que el cliente espera según los criterios esperados en el requerimiento.    
     
4. **¿Cuál de las siguientes opciones es un objetivo característico de la prueba?**  
 - [x] a) Prevenir defectos.  
   - [x] b) Validar que el plan de proyecto se ejecuta conforme a lo requerido.  
   - [ ] c) ~~Ganar confianza en el equipo de desarrollo~~.  
   - [ ] d) ~~Tomar decisiones con respecto a la entrega del sistema sujeto a prueba.~~  
  
# Prueba técnica  
El sitio web http://automationpractice.com/index.php es un e-commerce para realizar pruebas de automatización.   
Se te ha encargado la tarea de construir un set de pruebas automatizadas para las siguientes funcionalidades recientemente agregadas al sitio de pruebas.  
  
**Carrito de compras**  
Validar la correcta actualización del carrito mientras se van agregando items.  
  
**Flujo Checkout con actualización de dirección**  
Además de validar el correcto flujo, se solicita probar la modificación de la dirección en el paso 3 del checkout.  
  
**Historial de órdenes**  
Al finalizar el checkout, la orden queda registrada en el historial de órdenes asociadas al usuario.  
  
## Criterios de aceptación  
  
### Carrito de compras  
  
  #### Criterio de aceptación 1
 - Dado que el cliente quiere añadir un producto a su carro de compra  
   cuando selecciona el producto y presiona sobre la opción "agregar" si  
   el cliente está con la sesión iniciada, podrá proceder con agregar el producto  
   entonces el producto debe ser añadido al carro de compra.

  #### Criterio de aceptación 2
 - Dado que el cliente quiere añadir un producto a su carro de compra  
   cuando selecciona el producto y presiona sobre la opción "agregar" si  
   el cliente no está logueado tiene que iniciar sesión entonces el  
   producto debe será añadido al carro de compra después de iniciar  
   sesión.

  #### Criterio de aceptación 3
 - Dado que el cliente quiere añadir un producto adicional a su carro de compra  
   cuando selecciona el producto y presiona sobre la opción "agregar" si  
   el producto ya se encuentra en el carro de compra entonces el  
   producto debe aumentar en su cantidad en N.  
  
---   
### Flujo Checkout con actualización de dirección  
  #### Criterio de aceptación 1
 - Dado que el cliente desea poder modificar la dirección  
Cuando se encuentra en el 3er paso del carro de compras  
entonces podrá modificar la dirección sin salir del flujo del carro de compra.  

  #### Criterio de aceptación 2
 - Dado que el cliente desea poder realizar el flujo de compra completo  
Cuando se encuentre en el último paso del carro de compras  
entonces podrá verificar que el proceso está completado, ya que obtiene el código de referencia de la orden.
  
---  
  
### Historial de ordenes  

  #### Criterio de aceptación 1
 - Dado que el cliente desea poder tener una referencia sobre sus compras
cuando la compra se finalize, este entrega un código de referencia de la orden
entonces podrá llegar a la compra desde el historial de compras con el código de referencia de la orden.  
  
## Documentación   
  
En esta prueba automatizada, se utilizó **Python** como lenguaje y **Selenium** como framework de automatización.   
  
<img src="https://img.shields.io/badge/-Python-3776AB?logo=Python&logoColor=white&style=for-the-badge"/>   
<img src="https://img.shields.io/badge/-Selenium-43B02A?logo=Selenium&logoColor=white&style=for-the-badge"/>   
<img src="https://img.shields.io/badge/-Pytest-0A9EDC?logo=Pytest&logoColor=white&style=for-the-badge"/>   
<img src="https://img.shields.io/badge/-Pycharm-000000?logo=pycharm&logoColor=white&style=for-the-badge"/>   
<img src="https://img.shields.io/badge/-Github-181717?logo=Github&logoColor=white&style=for-the-badge"/>   
  
#### Requerimientos:   
- [Python 3.10.8](https://www.python.org/downloads/)  
- Python Package:   
   - [Selenium 4.5.0](https://pypi.org/project/selenium/)  
   - [virtualenv 20.16.5](https://pypi.org/project/virtualenv/)  
   - [pytest 7.1.3](https://pypi.org/project/pytest/)  
  
---  
Las pruebas se separaron por requerimiento y subdividido en criterios de aceptación.   
Para ejecutar las pruebas, simplemente se tiene que levantar el agente de virtualización **virtualenv** entrando a la carpeta `venv/bin`  
y ejecutar la activación del entorno virtual.  
  
 $ pip activateEsto levantará el entorno y mostrará en consola el nombre `(venv)`   
Luego, volver a la raíz del projecto y ejecutar las pruebas necesarias.  
  
### Pruebas a ejecutar  

Para ejecutar las pruebas de aceptación sobre el requerimiento de **carro de compra** se tiene que ejecutar lo siguiente (desde la raiz del projecto): 
##### criterio de aceptación 1
    $ pytest shopping_cart_criteria01.py -sv
##### criterio de aceptación 2
    $ pytest shopping_cart_criteria02.py -sv
##### criterio de aceptación 3
    $ pytest shopping_cart_criteria03.py -sv

___

Para ejecutar las pruebas de aceptación sobre el requerimiento **Flujo Checkout con actualización de dirección**, se tiene que ejecutar lo siguiente (desde la raiz del projecto): 
##### criterio de aceptación 1
    $ pytest checkout_criteria01 -sv
##### criterio de aceptación 2
    $ pytest checkout_criteria02 -sv

___

Para ejecutar las pruebas de aceptación sobre el requerimiento de **historial de ordenes** se tiene que ejecutar lo siguiente (desde la raiz del projecto): 
##### criterio de aceptación 1
    $ pytest history_criteria01.py -sv
```  
project
|
|shopping_cart_criteria01.py  
│shopping_cart_criteria02.py  
|shopping_cart_criteria03.py  
|checkout_criteria01.py
|checkout_criteria02.py 
│order_history_criteria01.py
│  
└── functions  
|  |  functions.py  
```