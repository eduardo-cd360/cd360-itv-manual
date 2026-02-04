# Menú Archivo

En este menú podrás encontrar las siguientes opciones:

- **Salir:** La forma elegante de salir del programa, además de la X.
- **Estilo:** Opciones para cambiar el aspecto del programa
- **Login:** Opciones para abrir una nueva instancia del programa o cambiar de usuario sin salir (preferimos cerrar y abrir de nuevo el programa para cambiar de usuario).
- **Base Datos:** Opciones de utilidad para los usuarios más expertos. Uso por administradores.
- **Seguridad:** Configuración de perfiles de usuario, usuarios y los permisos relacionados con las distintas partes de la aplicación. Visible solo para administradores
- **Opciones locales:** Opciones de configuración y personalización para el equipo donde se ejecuta el programa. Son opciones para el usuario.
- **Opciones:** Opciones de configuración y personalización general para la estación. Son opciones para el servidor y el comportamiento general de la estación.
- **Diseño informes:** Opciones para retocar algunas plantillas de documentos.
- **Posiciones tarjetas:** Opciones para gestionar la posición de los diferentes campos de las tarjetas de ITV (reformas, duplicados, matriculaciones) antiguas a la hora de imprimirlas. Se trata de una opción local, es decir, afecta solo al equipo en el que se modifican los valores.

## Salir

Cierra la aplicación.
En el caso de que se esté ejecutando algún servicio, mostrará un aviso antes de continuar con el cierre.

!!! note "Nota"
    Los servicios que pueden impedir el cierre de la aplicación son:

    - Control horario
    - Maquinas
    - Panel de avisos

## Estilo

Al seleccionar esta opción del menú Archivo, se muestra una ventana que permite cambiar el aspecto de la aplicación.

![Ventana de selección de estilos visuales mostrando una lista de opciones de estilos disponibles para la aplicación](images/menu-archivo_listado-de-estilos.png)

Seleccionando un estilo cambia el aspecto en general. Los temas son variaciones como cambios de color disponibles solo en algún estilo.

!!! note "Nota"
    En algunos casos es necesario reiniciar la aplicación para que los cambios de tema o estilo surtan efecto.

## Login

Realiza un nuevo inicio de sesión o Login en la aplicación sin cerrar la sesión actual.
Aunque está permitido, es preferible cerrar la aplicación y abrir con nuevo usuario. Manteniendo en todo momento al usuario actual como único usuario.

!!! note "Nota"
    La aplicación al realizar operaciones de alta y cobro, asigna al usuario actual a dichas operaciones. Tener más de un usuario a la vez puede tener consecuencias inesperadas al realizar un arqueo de caja.

## Base Datos (administradores)

Contiene opciones para realizar operaciones de mantenimiento con la base de datos del programa.

- Configurar conexión BD
- Actualizar estructura y datos

### Config. Conexión BD (Configurar conexión a Base de Datos)

Muestra un listado de conexiones con servidores de Creativa Digital 360 ITV.

Desde este menú se puede crear una nueva conexión con el servidor de Creativa, modificar una existente o eliminar conexiones.

El programa de gestión cliente de Creativa necesita de al menos una conexión para funcionar. Esta conexión puede ser a una DEMO, la estación de ITV u otras estaciones de ITV dentro de un grupo o empresa.

Elementos de la pantalla de conexiones

![Pantalla de configuración de conexiones a base de datos](images/archivo-base-datos_pantalla-de-conexiones.png)

- Filtro
- Listado de conexiones
- Botones
  - **Nuevo**: Añade una nueva conexión.
  - **Editar**: Edita una conexión existente del listado.
  - **Borrar**: Elimina una o varias conexiones seleccionadas del listado.
  - **Refrescar**: Actualiza la tabla de conexiones.
  - **Probar**: realiza un test de la conexión con los parámetros guardados.
  - **Local** automático: Estando el equipo dentro de la red local, busca al servidor y crea automáticamente la conexión. Por defecto llama a la conexión Server.

!!! Nota

    El uso de varias conexiones permite conectarse además de la estación, por ejemplo, al entorno de pruebas de Creativa Digital 360 y realizar inspecciones de prueba.

**Añadir una conexión**

Para añadir una nueva conexión pulsa el botón Nuevo. Se abre el formulario que se ve en la imagen siguiente.

![Nueva conexión](images/nueva-conexion.png)

Proporciona los siguientes datos:

- **Nombre de la conexión**: Nombre que se da a la conexión que se está creando.
- **Base de datos**: Tipo de conexión de BB.DD (por defecto Internet Comprimido).
- **URL**: Dirección del servidor de BBDD de la estación de ITV.
- **Token**: Palabra o código para autorizar la conexión. Solicítala si no la conoces.

Una vez creada la conexión, cierra el programa y ábrelo nuevamente para verla en el listado de conexiones.

**Editar conexión**

Selecciona una conexión del listado y pulsa el botón Editar, se mostrará la ventana con la información sobre la conexión seleccionada.
 
![Edición de una conexión](images/edicion-de-una-conexion.png)

A continuación, modifica los datos a tu gusto o según indicaciones y pulsa sobre Aceptar para guardar los cambios.

**Crear conexión de forma automática**

Utiliza el botón llamado Local automático para crear una conexión al servidor de la estación.

Se mostrará una ventana preguntándote si deseas hacerlo.

![Pantalla de adicción de nueva conexión](images/pantalla-de-adiccion-de-nueva-conexion.png) 

Responde Si y espera a que termine.

Si todo ha ido bien, se habrá creado una nueva conexión, pero si por el contrario, no se ha podido localizar al servidor de la ITV, un mensaje alertará de ello.
 
![Mensaje de error en la creación de la conexión de forma automática](images/mensaje-error-conexion-automatica.png)

En este caso, solicita los datos de conexión o pide ayuda.

<!-- TODO: Enlace a casos de uso ==> Añadir conexión a demo creativa para practicar
. -->
### Actualizar estructura y datos (administradores e ingenieros)

En determinadas ocasiones, cuando ha habido una actualización, es necesario usar esta opción para que funciones nuevas estén disponibles (seguir instrucciones de Creativa) o se actualicen las tablas comunes (solo si son mantenidas por creativa digital).

<!-- TODO: Poner opción de menú que lleva al check de tablas comunes -->

!!! Nota

    Se pueden marcar si se actualizan o no las tablas comunes de forma automática configurándolo en Archivo > Opciones > Importar / Exportar. Opción [  ] Actualizar tablas comunes al actualizar estructura.

    Las tablas comunes, si se decide no actualizarlas con creativa, deberán ser mantenidas por la propia estación.

### Seguridad (administradores)

El menú seguridad permite gestionar usuarios, perfiles y permisos que permitiendo dar de alta nuevos usuarios, asignarles perfiles y modificar el acceso a los menús y botones de las diferentes pantallas.

![Opciones de seguridad](images/archivo-seguridad.png)

También contiene otras propiedades extendidas de los usuarios.

!!! Nota

    Ciertos elementos que forman también parte de los usuarios se pueden encontrar en el menú Mantenimiento > Gestión de usuarios > Propiedades de usuario, como firmas electrónicas, permisos para usarlas, etc..

#### Perfiles

Los perfiles son un conjunto de permisos y características que pueden asignarse a un conjunto de usuarios, de forma que todos los usuarios implicados, tengan los mismos permisos.

La modificación de los diferentes permisos de un perfil afectará a cada usuario que pertenezca a él.

![alt text](images/menu-archivo_seguridad-perfiles.png)
 
Cuando se selecciona un perfil, este tiene unas propiedades generales como su código, su nombre y un listado de usuarios que están asignados a este perfil.

Además, dispone de una pestaña de permisos que permiten modificar a que zonas del programa o que acciones puede realizar cualquier usuario que herede de este perfil. 

#### Usuarios

Los usuarios son las cuentas con las que se identifican los trabajadores de la estación en el sistema. Por norma general cada trabajador dispondrá de una cuenta de usuario.

Cada cuenta de usuario tendrá un perfil asignado que asignará los permisos preestablecidos por este como si de una plantilla se tratase.

Además, puede contener otros datos o atributos que son usados en diferentes zonas de la aplicación o mostrarse en documentos.

![alt text](images/menu-archivo_seguridad-usuarios.png)
 
!!! Nota

    Existe una gestión de usuarios para cuestiones de firma, imparcialidad y otras gestiones. Puedes saber más accediendo a Gestión de Usuarios.

#### Permisos

Los permisos son opciones que habilitan o deshabilitan el acceso del usuario a ciertas opciones de menú, ciertas opciones o botones de pantallas o también de ciertas funcionalidades.

Si a un usuario que tiene asignado un cierto perfil, se le modifican los permisos, estos prevalecerán sobre los del perfil.

| Permiso | Descripción |
|---------|-------------|
| Ficha Jform principal | Permisos de acceso a los menús del programa |
| Listado Clientes | Botones disponibles en la pantalla de Clientes |
| Listado Cuentas contables | Botones disponibles en la pantalla la pantalla Cuentas Contables |
| Listado Cuentas de cobros | Botones disponibles en la pantalla de Cuentas de Cobros |
| Listado Expedientes Archivos | Botones disponibles en la pantalla Expedientes Archivos |
| Listado FACTDOCUMENTOS | Botones disponibles en la pantalla de Facturas |
| Listado Inspecciones | Botones disponibles en la pantalla de Inspecciones por fecha |
| Listado Inspecciones Atributos | Botones disponibles en la pantalla de Atributos de una inspección Editada |
| Listado Inspmediciones | Botones disponibles en la pantalla de mediciones de una inspección editada |
| Listado Matriculas | Botones disponibles en la pantalla de Matrículas |
| Listado Prestamos de expedientes | Botones disponibles en la pantalla de Prestamos de expedientes |
| Permisos base | Permisos relacionados con el usuario (generalmente inspector) y acciones disponibles en la Tablet |
| Permisos por fase | Permisos especiales para controlar que fases puede ver o usar un inspector en su tablet. Trabaja con la tabla de Fases de líneas |

#### Otros atributos

Bajo la sección o pestaña de atributos se encuentran otras propiedades del usuario que son empleadas por ejemplo en la impresión del informe o la etiqueta, para que aparezca alguna referencia relacionada con él, o bien para guardar otra información relaciona con el usuario, como por ejemplo la disposición de la pantalla de “panel de control” y los elementos que en ella se encuentran.

### Opciones locales (opciones de usuario)
Esta opción de menú muestra el panel de configuración del programa para el usuario. Estas configuraciones son locales y solo afectan al equipo y a todos los usuarios que lo utilicen en él.

!!! Nota "Tip avanzado"

    Si vas a cambiar de equipo o te van a actualizar o formatear el equipo, pue-des conservar las configuraciones y las personalizaciones de los filtros de las diferentes pantallas guardando los ficheros ConfigurationParameters.xml y ConfigurationLongITVReformas.xml que se encuentran en la carpeta de la aplicación de creativa, situada en *C:\Users\[tu-usuario]\listDatos*. Copiando los archivos en el mismo lugar en el equipo nuevo o restaurado, volverás a tener la misma configuración.

#### Impresión

![Menú impresión](images/menu-archivo_opciones-locales_impresion.png)

Opciones de configuración de impresoras que se utilizarán para cada tipo de documento usado en el programa y los márgenes y números de copias.

**Impresión local/Propiedades impresora**

Para cada tipo de documento se dispone de los siguientes ajustes:

- **Nombre**: Tipo de documento impreso.
- **Margen superior, inferior, izquierdo, derecho**: Ajuste del documento a la hoja contenedora. En el caso de hojas pre-impresas, permite el ajuste del contenido al hueco disponible para que encaje todo. Medidas en centímetros.
- **Impresora**: La impresora por la que será impreso el documento. El listado se ob-tiene del listado de impresoras de Windows. Si no se elige ninguna impresora o la que había elegida no está disponible, el programa imprimirá por la que Windows tenga por defecto en ese momento.
- **Nº Copias**: copias que se imprimirán por cada impresión que se ordene en el programa. Útil por ejemplo en los tickets o facturas o imprimir dos copias del informe que envía el inspector.

**Asignar valores por defecto**: Establece los valores configurados por defecto en las columnas de márgenes para uno o más registros seleccionados.

**Configurar valores defecto**: Permite establecer el valor para cada uno de los cuatro márgenes.

#### Otros

##### Opciones varias

###### Formato de pantalla

Permite seleccionar el tipo de pantalla o dispositivo donde se está ejecutando la aplicación, con el fin de adaptar el tamaño de la letra para que sea más fácil leerlo en pantallas de alta resolución.

###### Desactivar mensajes emergentes

Oculta los mensajes que aparecen cuando sucede algo en el programa. Un error, un archivo recibido al anotar una inspección en la DGT, etc.

##### Tarjeta

Las tarjetas de ITV contienen una serie de logos y textos que pueden configurarse dependiendo de si se han adquirido pre-impresas en su totalidad, solo con la cuadricula o vacías.

- Comunidad autónoma: Texto a rellenar con el nombre de la comunidad.
- Consejeria1, Consejeria2: Campos para escribir el nombre de la consejería completo. Se dejarán vacíos si la ficha o el logo ya los incluye.
- Desactivar logo fichas: En caso de que las fichas ya incluyan el gráfico, logo de la comunidad o elemento gráfico, se desmarca para que no se imprima con el que se ha especificado en la sección Logos y Documentos del menú de Opciones globales.
- Tarjetas con nombres de campos: Se marcará si la tarjeta tiene los nombres de los campos pre-impresos. Estando marcado, no se imprimirán al imprimir los datos de esta y se usarán los que ya vienen impresos.

![Texto imprimible en ficha tarjeta](images/menu-archivo_opciones-locales-tarjeta.png)

##### Homologaciones

Permite establecer una conexión con el sistema de fichas reducidas incorporado en Creativa Digital 360 ITV.

Si está disponible, se rellenará con los datos provistos por Creativa con respecto a la estación.

##### Taxímetros

Opciones relativas a la inspección de taxímetros.

!!! Nota

    Esta opción solo tiene aplicación en la Comunidad Valenciana.


  
#### General

#### Altas inspección

Permite modificar eventos que se producen durante el alta de una inspección.

![Altas de inspección](images/menu-archivo_opciones-locales_general-altas-de-inspeccion.png)

**General**

En cada equipo, se podrán activar o desactivar las siguientes opciones

- **Ver detalle factura:** Al imprimirse la factura (de forma manual o automática), se desglosan los conceptos. Si no se marca, solo incluirá un detalle mínimo.
- **Si la inspección está en vigor cerrar automáticamente:** <!-- TODO: Para que sirve?? -->
- **No presentar pantalla de anulación y otros avisos al empezar la inspección:** No muestra una pantalla de aviso con alternativas para evitar errores que provoquen la sobre-escritura de una inspección.

**Impresión**

- **Imprimir factura al dar de alta:** Marcado siempre emite la factura de forma automática. Si está configurada en Impresión local, se imprime por la impresora, pero si no está configurada saldrá por pantalla.
- **Imprimir expediente al dar de alta:** Imprime de forma automática la solicitud de expediente. Si no se marca, preguntará si se imprime.
- **Imprimir inspección al dar de alta:** En casos concretos es necesario que se imprima el informe vacío al cobrar la inspección.

**Listas cuando hay mas de uno**

- **Presentar CP:** Muestra al introducir el Código postal durante el alta una lista de poblaciones que comparten el mismo. Si no se marca, se elige el primero de la lista, teniendo que corregirlo si es distinto.
- **Presentar titulares:** Sin un NIF los titulares pueden estar repetidos. Marcada esta opción muestra la lista de los coincidentes. (Es una opción que no tiene utilidad en estaciones nuevas porque siempre se recoge el DNI/NIF).
- **Presentar homologaciones:** Si la homologación está compartida con varios modelos / series de coche se muestra la lista para elegir.

**Etiquetas**
- **Mostrar etiquetas en alta:** El listado de etiquetas (ver Uso de etiquetas) se muestra en la pantalla de altas para seleccionar un valor de los disponibles.
- **Etiqueta obligatoria:** La inspección no se puede dar de alta si no se elige una etiqueta de la lista..
- **Mantener valor entre inspecciones:** El valor de la etiqueta seleccionada en la última inspección se mantiene para la siguiente.

!!! Nota
    
    Las dos opciones últimas son usadas generalmente por las ITV's móviles para etiquetar ubicaciones.

**Avisos opcionales**

- **Mensaje aviso si no hay motor**: Muestra una alerta al guardar la inspección porque no se ha puesto un tipo de motor. Esto provocaría un error al aplicar la tarifa si no se corrige.
- **Mensaje aviso en voluntarias**: 
- **Aviso si no hay telf. o email en cliente**: Muestra alerta por haber dejado sin rellenar alguno de los campos indicados. Indica que no se podrá contactar con el cliente de ninguna forma si no se rellena al menos uno de los campos.

- **Dias a fecha caducidad AVISO**: Muestra alerta de que aún faltan más de x días para pasar la ITV nuevamente. Los días se toman de la consulta realizada a la DGT previamente.
- **Numero inspecciones mismo titular AVISO**: Muestra una alerta informando que el cliente ha superado el umbral establecido en cuanto a inspecciones. Un valor **0** desactiva la alerta/aviso.

**Datos opcionales**

- **Presentar fecha nacimiento en cliente**: Habilita el campo de "fecha nacimiento" en la sección de datos de alta del cliente, que en caso de rellenarse se almacena en la ficha del cliente.

Posteriormente puede ser usada la opción para mandar recordatorios de cumpleaños (solo recordatorios enviados desde creativa).
- **Presentar teléfono en cliente**: Muestra el campo de teléfono si no se ha introducido este durante el proceso de rellenado de campos. Evita que se quede vacío por olvido. 
- **Presentar cliente cuando no hay DNI**: Muestra un dialogo para introducir los datos de un nuevo cliente si en el campo DNI/CIF no hay ninguno.

**Caja y cuentas de cobro**

- **Pantalla de Euros al dar de alta:** Después de dar el alta, se muestra la pantalla de cobro, con información sobre el coste y diferentes utilidades, como sacar ticket.
- **Presentar fecha de nacimiento en cliente:** Por defecto en la pantalla de alta no se muestra un campo para la fecha de nacimiento. Si se marca, se muestra el campo. Dicho campo está en la ficha del cliente y tiene utilidad para el envío de recordatorios o para su uso con descuentos.

- **Fecha caducidad obligatoria:** Cuando está marcado, si no se ha introducido la fecha de caducidad, muestra un mensaje alertando de ello.
- **Caja por defecto:** Especifica que caja se asigna al equipo por defecto. Se pueden dar de alta las cajas en Mantenimiento > Auxiliares > Cajas.
- **Ruta cajero automático:** Campo específico para el módulo opcional “Cajero automático”, que funciona con cajeros de la marca CashDro.
- **Fecha estado de alarma COVID19:** Campos específicos durante la etapa de COVID, que permitían establecer los diferentes periodos para realizar cálculos durante el alta.

#### Comunicación

##### Listado vehículos

Configuración de la pantalla que muestra el listado de vehículos pendientes de realizar inspección a los inspectores.

Esta es una captura de la pantalla accesible mediante el menú `*Archivo > Gestión > Listado de vehículos a inspeccionar*` que tienen los equipos de línea o final de línea.

![Pantalla de listado de vehículos a inspeccionar que tienen los inspectores en los equipos de línea o final de línea](images/archivo-opciones-listado_de_vehiculos_a_inspeccionar.png)

En la pantalla de configuración se pueden establecer los siguientes parámetros:

Tamaño de fuente de letra para cada una de las tres vistas disponibles en la pantalla de información.

Si no se especifica nada en el campo, se usará "16" que es el valor por defecto.

![Pantalla de configuración del listado de vehículos](images/menu-archivo-opciones-comunicacion_Listado-de-vehiculos.png)

##### Recordatorios

![alt text](images/menu-archivo-opciones-comunicacion-recordatorios_formulario-principal.png)

Permite configurar los parámetros necesarios para el envío de recordatorios a los clientes de la estación.

**Pestaña General**

Gestión de las plantillas para el envío de recordatorio por SMS, Email y Correo ordinario.

##### SMS

Se debe especificar un texto de hasta 160 caracteres (sin caracteres acentuados ni símbolos). Si se supera este límite, el proveedor de SMS puede cobrar más de un mensaje por cada envío.

!!! Aviso

    Esta plantilla solo funciona con el envío de SMS a través de proveedores específicos. En este momento, Creativa Digital 360 solo soporta el envío de SMS a través de la plataforma propia. Las plantillas son gestionadas por nuestro personal de marketing.

Si se desea, se pueden utilizar los campos de combinación que se muestran al final de la pantalla. Serán sustituidos por los datos reales del cliente en el momento de realizar el envío.

[ ] SMS por Json: Si tienes contratado el envío automático de recordatorios o de encuestas, esta opción habilita el uso de una API REST basada en JSON.

!!! Nota

    La activación de esta opción debe ser realizada por el personal de Creativa Digital 360.

##### Email

Configuración de la plantilla que se utilizará para enviar recordatorios por email a los clientes.

Se rellena el asunto del mensaje y el cuerpo del mismo.

Se puede utilizar el editor visual para crear un mensaje atractivo y profesional.

También se pueden utilizar los campos de combinación que se muestran al final de la pantalla. Serán sustituidos por los datos reales del cliente en el momento de realizar el envío.

##### Correo ordinario

[ ] Impresión en PDF: marcando el check, en vez de imprimirse las cartas de recordatorios, se generara un PDF multi-página con todas las cartas.

!!! Nota "Servicios adicionales de marketing"

    Creativa Digital 360 provee de un servicio complementario e integrado totalmente con el programa, que permite realizar envíos personalizados con seguimiento y ofertas incluidas para atraer al cliente.

    Más información: https://creativadigital360.com 

##### Vídeo público

Es una característica especial de Creativa. Permite reproducir un video con una sobreimpresión de datos útiles para los clientes que están esperando en la sala de espera. Está pensado para ser usado en pantallas grandes o televisores que disponen de entrada HDMI conectados a un equipo donde se ejecuta Creativa Digital 360 ITV. Este equipo está dedicado solo a esta función.

![Configuración de la pantalla de Video público](images/menu-archivo-opciones-comunicacion-video_publico.png)

Los parámetros de configuración son:

- **Ruta del vídeo**: Fichero de video que se reproducirá en bucle.
- **Autologin**: Código de usuario con permisos para acceder a la función de vídeo público y su contraseña. Permitirá que el programa inicie automáticamente la función de vídeo público sin intervención del usuario.
- **[  ] Arrancar automáticamente tiempos de espera**: Si se marca, al iniciar la función de vídeo público, se mostrará la pantalla de vehículos terminados e impresos. Puede mostrarse esta pantalla de forma manual desde el menú `*Consultas > Consulta público Vehículos terminados e impresos*`.
<!-- TODO: Enlazar con menú consultas > Consulta público Vehículos terminados e impresos -->
- **[  ] Arrancar automáticamente vehículos terminados**: Si se marca, al iniciar la función de vídeo público, se iniciará también la lista de vehículos terminados para mostrarlos sobreimpresos en el video.
- **[  ] Efecto rotación**: Permite seleccionar un efecto de giro al texto mostrado en los vídeos.
- **[  ] Transparencia**: El texto mostrado sobre el vídeo no tiene fondo.
- **Duración efectos (sg)**: Tiempo en segundos que dura cada efecto de transición entre textos.
- **Cada cuando mostrar (sg)**: Tiempo en segundos que transcurre entre la aparición de un texto y la siguiente aparición.
- **Tiempo mostrar (sg)**: Durante cuanto tiempo se muestra el tiempo de espera (en segundos).
- **Tiempo espera por inspección (min)**: Tiempo medio de espera para la inspección, que se muestra sobreimpreso en el vídeo.
- **Tamaño fuente tiempo**: Tamaño de la letra del texto que muestra el tiempo en el vídeo.
- **Texto**: Testo personalizable que se muestra sobreimpreso en el vídeo para el tiempo de espera.
- **Tamaño fuente**: Tamaño de la letra del texto que se muestra sobreimpreso en el vídeo para el tiempo de espera.
- **Texto2**: 2ª linea de texto personalizable que se muestra sobreimpreso en el vídeo.
- **Tamaño fuente2**: Tamaño de la letra del 2º texto que se muestra sobreimpreso en el vídeo.
- Calculo tiempos de espera: Permite seleccionar el método para calcular los tiempos de espera que se muestran en el vídeo.
  - **Basado en tiempo medio**: Usa el tiempo medio de inspección configurado en minutos para calcular el tiempo de espera.
  - **Basado en coche que mas tiempo se ha tardado de tipo turismo**: Usa el tiempo que más se ha tardado en inspeccionar un turismo para calcular el tiempo de espera.
  - Basado en el nº de coches pendientes:

##### Cita previa

Configuración de la integración con el sistema de cita previa de Creativa Digital 360.

![Configuración de la cita previa](images/menu-archivo-opciones-comunicacion-cita_previa.png)

Los parámetros de configuración son:

- **[  ] Conexión con cita previa en altas**: Activa o desactiva la integración con el sistema de cita previa.
- Tipo: Selección del tipo de sistema de cita previa a utilizar.
  - **Creativa Digital 360**: Sistema de cita previa proporcionado por Creativa Digital 360.
  - **GestITV 15.1 [1]**: Sistema de cita previa Creativa3D (Anterior a la actual) [1].
  - **GestITV 17.1 [2]**: Sistema de cita previa Digital Servi (Anterior a la actual) [2].
- **URL del servicio**: Dirección del servidor de cita previa.
- **User**: Usuario para la conexión con el servidor de cita previa.
- **Token**: Contraseña o token para la conexión con el servidor de cita previa.
- Prefijo tablas: Prefijo usado en las tablas de cita previa en el servidor. (valido para GestITV 15.1).
- **[  ] Recuperar anticipos**: Si se marca, al dar de alta una inspección y comprobar que tiene cita, se recuperan los anticipos realizados en la cita previa y se aplican a la inspección, realizando el apunte correspondiente.
- **Caja debe**: Cuenta contable que se usará para registrar los anticipos recuperados de la cita previa.
- **Banco cita previa**: Cuenta contable que se usará para registrar los anticipos recuperados de la cita previa.
<!-- TODO: Especificar correctamente esto de Caja Debe y Banco cita previa -->

#### Facturación

##### Factura

##### Facturación

#### Maquinas

### Opciones (opciones globales)
Estas opciones afectan al comportamiento general de la estación y a todos los equipos que se conectan al servidor.

#### Opciones globales

![Menú opciones globales](images/menu-archivo_opciones-globales.png)

Permite configurar las opciones generales de la estación de ITV.
Las opciones se encuentran agrupadas en diferentes secciones o pestañas.

##### Logos y documentos

Configuración de los logos y documentos que se usan en los documentos impresos.

![Logos y documentos](images/menu-archivo_opciones-globales_logos_y_documentos.png)

- **Logotipo**: Logo que se imprimirá en la cabecera del informe de inspección.
- **Logotipo factura**: Logo que se imprimirá en la cabecera de la factura.
- **Logotipo etiqueta**: Logo que se imprimirá en la etiqueta que irá pegada en la tarjeta de ITV.
- **ENAC**: Logo que se imprimirá en el informe de inspección si la estación está acreditada por ENAC y el tipo de inspección lo requiere.
- **Región**: Logo que se imprimirá en la cabecera del informe de inspección correspondiente a la comunidad autónoma donde se encuentra la estación.
- **Region2**: Logo que se imprimirá en la tarjeta de ITV correspondiente a la comunidad autónoma donde se encuentra la estación.
- **Region3**: Logo que se imprimirá en la factura correspondiente a la comunidad autónoma donde se encuentra la estación.
- <!-- TODO: Ver para que es realmente y si hay que ponerlo o no -->
- **Sello**: Logo correspondiente al sello oficial de la estación de ITV.

Utiliza los botones de la derecha [+] y [-] para seleccionar las imágenes que se usarán en cada caso.

##### Certificado expedientes documentación

Configuración del certificado digital que se usará para firmar los documentos electrónicos generados o adjuntados por la estación de ITV.

!!! Nota

    Si la estación firma digitalmente los documentos tras su escaneo no es necesario configurar este certificado digital.

![Certificado digital documentos](images/menu-archivo_opciones-globales_certificado_digital_documentos.png)

- **Certificado documentación expedientes**: Selección del certificado digital instalado en el equipo que se usará para firmar los documentos electrónicos generados por la estación de ITV.

Utiliza los botones de la derecha [+] y [-] para seleccionar el certificado digital que se usará.

##### Correo y SMS

Configuración de los parámetros necesarios para el envío de correos electrónicos y SMS desde la estación de ITV.
![Correo y SMS](images/menu-archivo_opciones-globales_correo_y_sms.png)

###### Correo electrónico

Se pueden dar de alta múltiples cuentas de correo electrónico para el envío de correos desde la estación de ITV.

La primera cuenta de correo electrónico que se dé de alta será la cuenta por defecto y se usará para el envío de correos electrónicos desde la estación de ITV de forma automática (recordatorios, encuestas, etc.).

En cada cuenta de correo electrónico se deben especificar los siguientes parámetros:

- **Nombre de la cuenta**: Nombre descriptivo de la cuenta de correo electrónico.
- **Dirección de correo**: Dirección de correo electrónico completa (usuario@dominio).
- **Servidor SMTP**: Dirección del servidor SMTP que se usará para el envío de correos electrónicos.
- **Puerto**: Puerto del servidor SMTP. Por defecto 25, 465 o 587.
- **Usuario**: Usuario para la autenticación en el servidor SMTP.
- **Contraseña**: Contraseña para la autenticación en el servidor SMTP.
- **Usar SSL**: Indica si se debe usar una conexión segura SSL/TLS para la conexión con el servidor SMTP.

**Plantilla**: Permite seleccionar una plantilla de correo electrónico por defecto que se usará para el envío de correos desde cualquiera de las cuentas.

!!! Nota

    La plantilla se puede crear o modificar desde la pantalla de edición de correo electrónico. Creando el diseño y guardando como plantilla usando los botones disponibles. La extensión de las plantillas es *.gtc*.

###### SMS

Configuración de los parámetros necesarios para el envío de SMS desde la estación de ITV.

- **Cliente SMS**: Selección del proveedor de servicios de SMS que se usará para el envío de SMS desde la estación de ITV. Actualmente solo está disponible el proveedor propio de Creativa Digital 360 ITV.
- **Url**: Dirección del servicio web del proveedor de servicios de SMS. Suministrado por creativa Digital 360 ITV.
- **Numero de serie**: Sin uso
- **Usuario**: Usuario para la autenticación en el servicio web del proveedor de servicios de SMS.
- **Clave**: Contraseña para la autenticación en el servicio web del proveedor de servicios de SMS.
- **SMS Remitente**: Texto que aparecerá como remitente del SMS enviado.

##### DGT y Certificados
Configuración de los servicios de conexión con la DGT, la compra de Tasas y los certificados digitales usados para la comunicación segura con la DGT.

![DGT y certificados](images/menu-archivo_opciones-globales_dgt_y_certificados.png)

###### DGT

- **Usa DGT**: Activa o desactiva la conexión con los servicios de la DGT. Activado se realizan las consultas de la matricula durante el alta, consulta de vehículos por matricula o bastidor y se los envíos de inspecciones a la DGT.
- **Subida DGT automática**: Si está activado, al finalizar una inspección que deba enviarse a la DGT, se envía automáticamente sin intervención del usuario.
- **Consulta 24 horas**: Activa el servicio de consulta ATEX24. Este servicio de la DGT restringe las consultas de vehículos a que estén anotados como mínimo 24 horas antes de la consulta. Será obligatorio para todas las estaciones a partir de cierta fecha que aun no se ha publicado.
- **Certificado DGT**: Selección del certificado digital que se usará para la comunicación segura con los servicios de la DGT. Utiliza los botones de la derecha [+] y [-] para seleccionar el certificado digital que se usará.
- **Url servicio DGT**: Dirección del servicio web de la DGT para la comunicación con los servicios de la DGT. Estos valores son suministrados por la DGT y pueden variar en función del entorno (producción, pruebas, etc.). No deben modificarse sin consultar previamente con Creativa Digital 360 ITV.
  - URL Consulta
  - URL Consulta ATEX24
  - URL Anotación inspección
  - URL Reformas
  - URL borrado inspección
- Correo incidencias: Dirección de correo electrónico donde se enviarán las notificaciones de incidencias en la comunicación con la DGT. (actualmente no usado al bloquear el servicio por este medio la DGT).

###### Compra tasas DGT
Creativa Digital 360 ITV dispone de un sistema integrado para la compra de tasas de la DGT desde el propio programa de gestión. La compra se realiza de forma automática y segura a través de los servicios web de la DGT.

Si se produce un error durante la compra, se paraliza el proceso hasta que se solucione. Esto se deberá realizar en el menú de `Gestión > DGT > DGT compras`.


