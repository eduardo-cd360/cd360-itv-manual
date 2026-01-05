# Alta de una inspección periódica

El proceso para dar un alta de una inspección de tipo periódica es sencillo. A lo largo de este documento se explicarán los pasos para crear una inspección.

Hay dos opciones para dar de alta una inspección: La opción de menú *`Altas principal`* y la opción de menú *`Altas de inspección`*.

Si se usa la opción "Altas principal", se muestra una pantalla donde unicamente hay que seleccionar el tipo de inspección (1) e introducir la matrícula (2) a dar de alta.

![Pantalla Altas principal](images/altas-principal-pasos-alta.png)

Al pulsar Intro tras la matrícula, se abre la pantalla de Altas de inspección con la matricula cargada.

![Secciones de la pantalla de altas de inspección](images/altas-de-inspeccion-secciones.png)


!!! Note "Pantalla **Altas principal**"

    La pantalla de "**Altas principal**" es una pantalla nueva que simplifica la vista diaría de inspecciones, eliminando todo lo superfluo y usando tipografia más grande. Es una ayuda para los usuarios inexpertos o que prefieren trabajar con una pantalla mas despejada. Puedes usarla o no cuando lo desees.

En esta pantalla, tras la consulta de datos a la base de datos y a la DGT, se muestran los datos relativos a:

1. Matrícula del vehículo
2. Datos del vehículo
3. Datos del cliente titular, cliente a facturar y cliente presencial.
4. Datos adicionales de la inspección. Ultima estáción en donde pasó la inspección, Observaciones sobre el vehículo, sobre la inspección realizada por los inspectores (visible en el informe) o observaciones internas (no visibles en el informe).
5. Datos de la inspección (Año, orden o fase, Fecha de caducidad que le corresponde, datos de la inspección anterior, etc..).
6. Cuenta de cobro o forma de pago.
7. Tarifa aplicada, descuentos y opciones que afectan a facturación.

En caso de que durante el alta se detecte que el vehículo tiene algun dato erroneo, no posea seguro, tenga precinto o se omitan datos o hayan datos incorrectos, se mostrarán mensajes de alerta.

Tras la verificación de los datos en la DGT, si no existen en la base de datos, se cumplimentarán todos de forma automática con los obtenidos durante la consulta.

En caso de estar ya registrados, serán contrastados con los existentes, mostrando las discordancias y ofreciendo la posibilidad de copiarlos en memoria o usarlos en los campos indicados.

Los datos faltantes, se rellenarán acorde a la tarjeta de caracteristicas.

En caso de vehículos pesados, aparecerán campos extra para la introducción de más datos que son necesarios.

!!! Note "La elección del usuario"

    El usuario que da el alta debe revisar la tarjeta tecnica y corroborar que los datos son correctos, actuando de oficio en aquellos casos que una discrepancia sea evidente que no es correcta, en cuyo caso podrá trasladar los valores que ofrece la DGT actualizados.

A continuación se rellenarán los campos relativos al **cliente propietario o titular**, al **cliente presencial** y al **cliente a facturar**.

!!! Note "¿Que tipo de cliente relleno?"

    Creativa maneja tres tipos de clientes:

    **Cliente titular**: El propietario del vehículo, que puede ser una persona o una empresa. Generalmente es suministrado por la consulta a la DGT, pero puede ser distinto por haber habido entre inspección e inspección un cambio de titular por venta u otra operación.

    **Cliente a facturar**: Independientemente del titular del vehículo y por tanto de la inspección, es el cliente a quien va a ir emitida la factura o albarán en caso de seleccionar una cuenta de crédito.

    **Cliente presencial**: Es el usuario que lleva el vehículo a pasar la ITV. No es obligatorio en todas las provincias, pero es necesario para poder identificar ante las autoridades en caso de que lo soliciten. Además, en listados de inspecciones se puede usar para temas de marketing, pago de comisiones, etc..

Por último, podrá **seleccionar la ultima estación** en la que se ha pasado la inspección (si no es puesta por la consulta de la DGT) o agregar una **observación a la matrícula** o una **observación interna de inspección**.

!!! Note "Tipos de Observaciones"

    Observaciones de matrícula: Es una nota que se asocia a la matrícula y es usada (se muestra al usuario) cada vez que la matrícula es utilizada en una nueva inspección.

    Observaciones internas de inspección: So anotaciones que están asociadas solamente a la inspección en la que se crean. Son usadas para transmitir información al inspector en ese inspección desde administración, o bien por el inspector para dejar constancia de algún hecho acaecido durante la inspección. Se emplean también como justificación ante algún procedimiento no habitual o problema.

    Observaciones de inspección: Son las observaciones que agregan los inspectores a las inspecciones como resultado de la comprobación de todos los puntos a inspeccionar. ==Estas observaciones no se añaden o modifican desde administración.==

Por otro lado, en el lado derecho del panel de altas, se habrán rellenados los campos de:

- Datos de la inspección actual
- Datos de la inspección anterior
- Forma de pago ó cuenta de cobro y caja (si se usa)
- Tarifa a cobrar, incluye opciones de pago online, descuentos a aplicar
- Selección de Seguro (es automático, pero se puede seleccionar alternativas cuando no está disponible)

Por ultimo se termina el alta al pulsar **Aceptar**. En caso de haber datos mal puestos, incompletos o no superen alguna validación, se mostrará un aviso por pantalla indicandolo para subsanarlos.