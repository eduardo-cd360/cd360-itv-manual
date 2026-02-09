# Menú Mantenimiento

Desde este menú se accede a las tablas de datos principales del programa, ya sea para crear, mantener o eliminar los datos relacionados.

Las opciones de menú disponibles son:

- **Clientes**. Tabla con todos los clientes de la aplicación. Pueden ser del tipo titular, presencial o de facturación.
- **Matrículas**. Tabla con todos los registros de vehículos (matrículas) que han sido dados de alta en algún momento.
- **Tarifas**. Tabla de tarifas a aplicar durante un alta de una inspección.
- **Maestras**. Conjunto de tablas principales de la aplicación.
- **Auxiliares**. COnjunto de tablas auxilires con datos menos relevantes.
- **Gestión de usuarios**. Acceso a otros datos adicionales de usuario del programa que no están contemplados en el menú de seguridad. Gestión de firmas de usuarios entre otros.
- **Reconocer matrícula**. Opción no utilizada.
- **Equipos y líneas**. Tablas de configuración de la estación en cuanto a las Lineas, fases y equipos asociados a cada una de ellas.
- **Taxis**. Opciones relativas a la inspección de taxis. Operativa unicamente para Valencia. Resto de comunidades, solamente es administrativa.
- **Gestión regalos-puntos**. Opción obsoleta.
- Prestamos de expedientes. Relación de expedientes prestados a otras estaciones.
- **Expedientes solicitados**. Relación de expedientes solicitados a otras estaciones.
- **Maquinas**. Tabla de configuración de las maquinas (equipos de pruebas de línea) de cada línea la estación.

!!! Alert "Aviso"

    Según la configuración de perfil y permisos de cada usuario, pueden mostrarse todos los menús o ver un listado parcial solamente.


## Clientes

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/guia-de-inicio/interfaz-de-usuario/images/menu-mantenimiento-clientes_tabla-de-clientes.png -->
![tabla de clientes](images/menu-mantenimiento-clientes_tabla-de-clientes.png)

Tabla de gestión de clientes.

Para mostrar los clientes disponibles, se debe establecer el filtrado previo por alguno de los campos disponibles.
Una vez obtenido el listado, se puede utilizar el filtro dinámico bien por todos los campos o por campo o bien el avanzado, para selecciones múltiples dentro de la misma columna.

Las operaciones que pueden realizarse son:

- **Nuevo**: Crear un nuevo cliente. Esta operación se realiza de forma automática du-rante el alta de una inspección.
- **Editar**: Carga la ficha del cliente para modificar la información existente.
- **Borrar**: Borra el registro o registros seleccionados. Solo será borrado si no tiene in-formación relacionada como matriculas o inspecciones.
- **Refrescar**: Actualiza la información de la tabla.
- **Cambio CP**: Modifica el Código postal del cliente en su ficha y en todos los registros relacionados.
- **Cambio DNI**: Modifica el DNI del cliente en su ficha y en todos los registros rela-cionados.
- **Cambiar ID**: Modifica el nº de cliente en su ficha y en todos los registros relaciona-dos.
- **Mover datos a otro cliente [administradores]**: Asigna todos los registros relacio-nados con su ficha a la ficha de otro cliente. Permite corregir situaciones con clien-tes duplicados.
- **Canjear Puntos**: Realiza la operación de canje usando la tarjeta de puntos asignada.
- **Documento RGPD**: Imprime el documento RGPD que firma el cliente la primera vez que es dado de alta.
- **Listado**: Genera una impresión por pantalla del contenido de la tabla. Está forma-teado en A4 para su impresión en papel.
- **Generador Consultas [administradores]**: Utilidad avanzada para mostrar informa-ción mediante consultas SQL.

## Matrículas

Tabla de gestión de matrículas, en donde se pueden realizar operaciones de mantenimiento relacionadas con estas.

Cada registro de matrícula contiene toda la información relativa a las características del vehículo.

Un cambio de estas características durante una inspección, altera la información que con-tiene su registro en esta tabla, para que en la siguiente inspección y sucesivas se utilicen los datos actualizados.

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/guia-de-inicio/interfaz-de-usuario/images/menu-mantenimiento-matriculas_tabla%20de%20matriculas.png -->
![Tabla de vehiculos dados de alta en inspecciones](images/menu-mantenimiento-matriculas_tabla%20de%20matriculas.png)

Las operaciones permitidas en esta pantalla son:

- **Nuevo**: Crea un nuevo registro de matrícula. Este proceso se realiza de forma au-tomática desde el alta de una inspección
- **Editar**: Permite editar los datos relativos a la matrícula seleccionada.
- **Borrar**: Borra el registro o registros seleccionados, siempre y cuando no tengan in-formación asociada.
- **Refrescar**: Actualiza la información de la tabla.
- **Avisos**: Asocia un texto a la matrícula. Cuando se realiza un alta de inspección y se introduce una matrícula con avisos, una alerta es mostrada con este aviso.
- **Listado**: Vista por pantalla con formato A4 para impresión en papel.
- **Generador Consultas [administradores]**: Utilidad avanzada para mostrar informa-ción mediante consultas SQL.

## Tarifas

Listado de tarifas de aplicación en la ITV.

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/guia-de-inicio/interfaz-de-usuario/images/menu-mantenimiento-tarifas_lista-de-tarifas.png -->
![Listado de tarifas](images/menu-mantenimiento-tarifas_lista-de-tarifas.png)

Listado de tarifas

Se pueden dar de alta nuevas tarifas, modificar las existentes o eliminarlas.

Las tarifas están compuestas por una parte relativa a los precios de cada uno de los con-ceptos de una inspección como prueba de seguridad, gases, ruidos, etc.. y los diferentes impuestos y tasas, y por otra parte una serie de reglas que permiten ajustar la tarifa a los tipos de inspección y características del vehículo.

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/guia-de-inicio/interfaz-de-usuario/images/menu-mantenimiento-tarifas_formato-tarifas.png -->
![alt text](images/menu-mantenimiento-tarifas_formato-tarifas.png)
 
Las tarifas pueden ser activadas o desactivadas, según la conveniencia de la estación o bien eliminadas si no son empleadas en ninguna inspección.
