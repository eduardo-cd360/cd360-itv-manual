# FACTURAS

En este documento:

### La pantalla de facturas

Desde el menú Facturación > Facturas, se puede ver el listado de facturas emitidas por el programa, tanto generadas de forma automática a clientes de contado y a clientes con cuentas de crédito como las que se generan de forma manual.

Como en todas las pantallas de la aplicación, entre todos los datos que se muestran en el listado de facturas, está el Identificador o el Grupo, que pueden estar ocultos. Mediante estos dos campos es fácil localizar y visualizar por separado las facturas normales de las de clientes de crédito. Están diferenciadas por el grupo, que en el caso de las mensuales suele ser “m”, las rectificativas “r”, etc. En cualquier caso, se encuentran definidos en la

Para mostrar campos ocultos en los listados de creativa, se puede utilizar el clic derecho del ratón sobre cualquier dato de la tabla. Se mostrará entre otras opciones el menú Campos. Mediante este menú, puedes activar cualquiera de los campos que están ocultos u ocultar los que se muestran actualmente.

Para localizar las facturas mensuales o de cualquier otro tipo, se puede utilizar el filtro rápido o mostrar el campo Grupo, para poder filtrar por tipo de factura.

![Imagen 1](./images/image_1.png)

Las tareas que se pueden realizar con las facturas están repartidas en pestañas según su funcionalidad.

Pestaña Principal

![Imagen 2](./images/image_2.png)

Nuevo: Crea una nueva factura que hay que rellenar de forma manual.

Editar: Modifica una factura

Borrar: Borra una factura o un conjunto de facturas.

Refrescar: Actualiza la tabla de facturas. Es posible que desde otro equipo se hayan creado nuevas y es recomendable que antes de realizar operaciones se trabaje con la vista actualizada.

Cobrar factura: Genera un movimiento de caja y deja la factura como cobrada.

Marcar cobrada / no cobrada: Cuando son facturas de crédito (diferentes de contado o tarjeta de crédito) las da por cobradas o por no cobradas. Se utiliza con las cuentas de crédito.

Rectificar: Seleccionando una factura cobrada previamente, pulsando este botón se genera una factura negativa o rectificativa por el valor total de la factura seleccionada. En caso de querer una rectificación parcial, habrá que eliminar los conceptos que no se rectifican y corregir el importe abonado en observaciones a cuenta.

Pestaña Informes

![Imagen 3](./images/image_3.png)

Imp. Factura: Imprime la factura o facturas seleccionadas por la impresora configurada en el programa (facturas). Si se selecciona más de una factura, se muestra dialogo para indicar nº de copias de cada una, y a continuación manda una tras otra las facturas a imprimir.

Vista previa: Muestra la factura seleccionada en PDF. Si se elige más de una factura para previsualizar, se mostrará la primera de todas.

Recibí: Muestra un documento recibí en formato pdf con los datos del cliente y el importe entregado de la factura.

Suma: Seleccionando dos o más facturas, muestra una ventana con la suma de los diferentes conceptos de estas.

Huecos: Permite comprobar la existencia de huecos en la numeración de las facturas emitidas así como la existencia de facturas desordenadas.

Enviar Email: Envía la factura o facturas seleccionadas por email. Usa la cuenta de correo electrónico asociada al cliente de la factura. Si se seleccionan varias facturas, solo se podrán modificar opciones comunes. Debe estar configurado el correo electrónico en el programa.

Listado: Se imprime por pantalla en formato listado el contenido de la tabla mostrado en pantalla.

Exportar

![Imagen 4](./images/image_4.png)

Estas opciones permiten generar listados para diferentes programas de contabilidad.

Contaplus: Genera dos archivos para ser importados con Contaplus

Golden: Genera un fichero Excel compatible con Golden Soft

Excel: Genera un fichero Excel compatible con Aire ERP

Existen multitud de programas en el mercado que puede importar alguno de estos ficheros.

Para facilitar la gestión de las facturas, se utilizan códigos de color.

Texto rojo	Las facturas no están marcadas como cobradas

Texto negro	Las facturas están cobradas

Fondo amarillo	Las facturas han sido exportadas a contabilidad.

### Crear nueva factura

Durante el alta de inspecciones, se generan facturas de forma automática, pero en algunas ocasiones es necesario generar una factura manual, ya sea para facturar algo que no es una inspección, o para crear una factura personalizada.

La creación de una factura de forma manual se realiza desde la pantalla Facturación/Facturas. Una factura recién creada está sin cobrar y habrá que utilizar posteriormente el botón “Cobrar factura” o bien se pueden añadir de forma manual entregas a cuenta, hasta cubrir el total de la factura.

Mediante este método de entregas a cuenta, es el único método por el que se pueden hacer cobros parciales con métodos de pago distintos.

Para realizar una factura de forma manual se pulsa sobre el botón “Nuevo+”. Se muestra la pantalla formulario para rellenar con los datos de la factura.

![Imagen 5](./images/image_5.png)

Se cumplimentarán los siguientes campos:

Año: Año de la factura. Por defecto sale el actual.

Grupo: Es la serie. Por defecto se muestra “1”, pero se puede poner la serie adecuada (“m” o “r”).

Cód. Factura: Es el nº que se asigna a la factura. Dejar en blanco por defecto, se cumplimenta solo.

Fecha Factura: La fecha de la factura. Por defecto se muestra la actual.

Cliente: Cliente al que se factura.

Colaborador: Es otro cliente que actúa como colaborador / representante / conseguidor.

Forma de pago: Elegir una forma de la lista

Estado: el estado en el que se encuentra la factura (no cobrada, cobrada, enviada, etc..)

Plantilla: Elegir una plantilla si se desea agregar líneas preconfiguradas, o si es una plantilla completa, además de las líneas se añaden el resto de campos.

Descripción: Agregar un texto que describa el contenido de la factura

Añadir documento, Año, Grupo, Número: Permite importar el contenido de otra factura o albarán como nuevas líneas en la actual.

Caja Fecha, Caja Euros, Fecha cobro: Para dejarla como cobrada, pulsar el botón (+), y agregar una o más líneas de Entrega a Cuenta.

### Rectificar una factura

### Cobrar una factura

### Duplicar una factura

### Eliminar facturas

### Facturación mensual