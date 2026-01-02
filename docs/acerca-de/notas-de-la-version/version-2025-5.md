# Versión 2025-5

Fecha de publicación: 01/11/2025

En esta nueva actualización se incluyen entre otras correcciones y mejoras las siguientes funcionalidades:


## Tareas

- Incorporación del sistema Veri*factu.
 
- Incorporación de ATEX24. Sistema nuevo y obligatorio de la DGT que tiene una demora en la consulta de vehículos de 24 horas. Pasadas 24 horas aparecerán las anotaciones realizadas el día anterior. Siempre con 24 horas. Activación necesaria de la estación mediante escrito a la DGT.
 
- Cambio de conexión http por https desde clientes cumpliendo con ENS.

- Uso de contraseñas más seguras y bloqueo de usuario si se intenta acceder más de 5 veces con una contraseña errónea, cumpliendo con ENS.

- Ampliación del nº de documentos disponibles para la tableta de firma, así como mejoras en la interfaz de diseño de estos documentos.

- Los métodos para controlar la proporcionalidad son ahora personalizables.

- Se han añadido avisos para alertar al inspector cuando los defectos marcados deban de comprobarse mediante alguna medida. En este caso el mensaje será no bloqueante y del tipo "[defecto] Datos no introducidos".

- OBFCM. Se añade al registro de OBFCM el campo OVC-HEV para el tipo de vehículo enchufable que es en base a la circular informativa C07.2025.2 de AECA ITV.

## Subtareas

- [ITV-5308] – Al iniciar la aplicación, si la conexión está configurada con el puerto 8080 (http) se cambia automáticamente al 8443 (https). Así se cumple con el ENS usando conexiones seguras.

- [ITV-5439] – Realizar cambios en el sistema de contraseñas de inicio de sesión de usuario.

- Se implementa la caducidad de la contraseña. Ahora es cada 6 meses. El usuario debe cambiarla a su caducidad y no puede ser igual a la anterior.

- Se implementa el bloqueo de cuenta de usuario por intentos excesivos de autenticación. Si el usuario intenta entrar más de 5 veces con una contraseña errónea, se bloquea su cuenta por 60 min. Será necesario desbloquearla por una persona con rol de Administrador tener acceso inmediato. Se recomienda un cambio de contraseña en ese caso.

![Mensaje-de-bloqueo-de-cuenta](images/version-2025-5_mensaje-de-bloqueo-de-cuenta.png)

El administrador del sistema debe acceder a la opción de menú de _Archivo > Seguridad_, elegir al usuario bloqueado y pulsar sobre el botón de desbloqueo. Si no se conoce el acceso mediante Administrador, solicitarnoslo por soporte en soporte.creativadigital360.com

[ITV-5480] – Mostrar fecha de último acceso en caso de login exitoso.

Se han creado dos mensajes para que salga el momento en la última vez que hiciste inicio de sesión tanto en el móvil como en la tablet.

En el escritorio sale arriba de la ventana principal

![Mensaje último acceso](images/version-2025-5_mensaje-ultimo-acceso.png)

En la tablet al momento de conectar.

![Mensaje en tablet](images/version-2025-5_mensaje-en-tablet.png)


## Corrección de errores
[ITV-5328] – Selección parcial de ingenieros en pantalla de turnos y de expedientes.

Se ha solucionado la incidencia relacionada con el listado de ingenieros que aparece al seleccionar un ingeniero en la pantalla de turno o en la de expediente, que a veces salía incompleta.

[ITV-5333] – Módulo control horario: Error en control horario, marcaje salida erróneo.

Solucionada incidencia en marcajes de salida realizados de forma automática.

[ITV-5344] – Al consultar una inspección que no es del día, se establecen los pesos con lo que se hicieron la prueba de frenos.

[ITV-5345] – Mejorar el orden de tabulación de las facturas.

Se han actualizado la disposición de campos de la pantalla de edición de factura (se necesitan permisos para editar facturas) y se han reordenado el pase entre campo y campo (tabulación) al introducir datos.

[ITV-5346] – En albaranes es difícil pulsar en cliente y no funciona bien la lupa del cliente.

Se ha reparado el funcionamiento de los botones y los campos relacionados con el cliente y la búsqueda de clientes en la pantalla de edición de albaranes.

[ITV-5348] – Error en alta de inspecciones con tipos inspección deshabilitado.

[ITV-5355] – Listado de tarjetas de inspección por matrícula.

[ITV-5360] – Impresión o envío de facturas por Email. Error no procesado cuando no hay factura por que es 0€.

[ITV-5373] – Prueba de frenos en vehículos pesados históricos.

[ITV-5410] – No hay aviso cuando no ponen la mom en categoría L.

[ITV-5420] – Tablet: en algunos moviles no se puede pulsar el 1º check de los avisos.

[ITV-5423] – DGT, problemas con las Ñ en el bastidor.

[ITV-5444] – Botón de pestaña de clientes > CRM > Documentos se oculta.

## Mejoras de la aplicación
[ITV-3713] – Agregar regla «inspección en vigor» en la creación de una tarifa.

[ITV-4729] – Generalización de Documentos de firma tableta.

[ITV-4922] – Fichas tecnicas, poder imprimir la copia que quieren.

[ITV-4974] – Previas a la matriculación de vehículos ya matriculados,consultar DGT por bastidor para comprobar si ya existe.

[ITV-5227] – Crear nueva opción en Informes opciones. «No firmar informe automaticamente».

[ITV-5319] – Cuando es Previa Matriculación no debe aparece la matrícula en Ver/Crear Tarjeta.

[ITV-5321] – Poner para que se pueda elegir entre el tipo CORE o B2B en la exportación al SEPA.

[ITV-5325] – Configuración de columnas por nombre, para evitar desconfiguraciones cuando se añaden campos a los listados principales.

[ITV-5329] – Añadir las columnas DIAS, CONTADOSN y DOMICILIACIÓNSN al listado de Formas de pago.

[ITV-5330] – En la ventana de Altas Principal añadir indicativo de que se puede ver información adicional en ciertas columnas.

[ITV-5331] – Añadir campos de cuenta de cobro y cliente a facturar en recordatorios.

[ITV-5334] – Actualizar version android 14.

[ITV-5335] – Agrupación de botones inferiores por pestañas.

[ITV-5338] – Mejorar panel gráfico de la Lista de Vehículos a Inspeccionar.

[ITV-5343] – Tabla Mantenimiento/Auxiliares/Campos de Reforma: Al modificar un registro, el tipo de dato que admite el campo debe ser un desplegable con los tipos disponibles.

[ITV-5349] – Evitar usar tipos inspección desactivadas en expedientes.

[ITV-5350] – tablet: Menú perfil-poder deshabilitarlo por permisos.

[ITV-5351] – Después de hacer el envío parcial, que se refleje en el siguiente mecánico las fotos obligatorias hechas.

[ITV-5352] – En tickets solo mostrar cuentas de cobros activas.

[ITV-5353] – Añadir filtro por línea en Estadísticas ENAC.

[ITV-5362] – Base imponible en listado resumen económico de inspecciones.

[ITV-5364] – Proporcionalidad empiece a contar a partir de x inspecciones del cliente, configurable.

[ITV-5374] – Mejoras en informe inspección Comunidad de Madrid.

[ITV-5376] – Hacer un aviso para que la MMA no pueda ser menor que la MOM. Tanto en la parte de mecánicos como en las altas de inspección.

[ITV-5379] – Aviso cuando existan ciertos defectos y no tenga medida correspondiente.

[ITV-5381] – Añadir combox de tipos en campos de ficha técnica.

[ITV-5382] – Añadir botón asociar expediente en JPlugInTarjetas que esta JT2RTARJETAINSPECCION.

[ITV-5383] – Envío DGT de duplicados , que la Fecha Inicio sea la fecha de firma.

[ITV-5390] – factura electrónica, totalOutstandingAmount no lleva suplidos.

[ITV-5391] – Mostrar tabla «Comunicación histórico» para usuarios que no tengan el menú opciones.

[ITV-5392] – DGT: aviso motor bicombustible en altas.

[ITV-5393] – Madrid: En periódicas, histórico , el botón Ficha técnica se envíe a industria.

[ITV-5398] – Añadir al panel de control la media diaria.

[ITV-5399] – que la proporcionalidad tenga en cuenta el cliente presentador y facturar.

[ITV-5402] – Crear nuevos tipos de combustible BiFuel.

[ITV-5403] – Crear búsqueda de clientes por número de teléfono.

[ITV-5406] – itvAndroid, Aviso método de frenado extrapolación + elevación cuando sea mayor la carga aplicada (+500 kg) a la báscula.

[ITV-5412] – Facturación: listado formas pago, quitar las formas de pago NO CONTADO, y sumar bien los albaranes.

[ITV-5417] – Consulta DGT ATEX24.

[ITV-5424] – Altas inspección: no haga falta activar cálculo si estas en el mismo día.

[ITV-5425] – Poner la cuenta de gastos de descuadre de caja por canales.

[ITV-5426] – MEJORAS alcance 4.15.

[ITV-5428] – Cambiar colores de las cita previa en el alta de inspección (configurables).

[ITV-5433] – VERIFACTU: Cambiar Formato Facturas.

[ITV-5434] – Nuevo avisos equipos: 2 gases (analizador), 2 frenado, 2 holguras, 2 opacímetro, 2 ruidos.

[ITV-5437] – Corregir NullPointer cuando no existen los directorios ES_IN, ES_OUT de máquinas.

[ITV-5438] – L2 con contraseña CU es cuadriciclo para las pruebas.

[ITV-5443] – Crear nuevas pestañas en Impresión Servidor.

[ITV-5445] – Mensaje confirmación al cambiar la forma de pago después de un de alta inspección.

[ITV-5449] – Modificación botones ventanas tickets, inspecciones, expedientes, clientes, logos y documentos generales.

[ITV-5458] – Añadir IP de seguridad para SMS automáticos.

[ITV-5461] – Sincronizar clientes relacionados con usuarios para imparcialidad.

[ITV-5469] – Extrapolación por Fbrake: Se han añadido los semirremolques de 4 ejes.

[ITV-5470] – Ciclomotores 0300 en la opción de elegir freno hidraulicos DEBE salir seleccionado los tubos rígidos.

[ITV-5481] – Crear columna de correo y teléfono en la tabla de usuarios.

## Nueva función

[ITV-5327] – Seguridad de usuarios cambiar color si no está activo.

[ITV-5361] – Al eliminar el expediente, eliminar la asociación con la tarjeta.

[ITV-5435] – Aviso de FBRAKE.

[ITV-5451] – Añadir png a botones faltantes.

## Tarea

[ITV-4411] – Botón asociar expediente en Ficha tarjeta.

[ITV-4653] – Panel de control: añadir filtro para inspecciones [mañana/tarde/todo el día].

[ITV-4716] – Tarifas: añadir filtro clasificación utilidad.

[ITV-4960] – Cambiar los avisos de altas de inspección para que se agrupen en una sola tabla.

[ITV-5010] – En ficha técnica poder visualizar la ficha técnica entera.

[ITV-5118] – Crear plantillas de operaciones con caja.

[ITV-5292] – Declaración responsable VERIFACTU.

[ITV-5324] – Añadir botón «Ver factura» para albaranes en listado de facturas.

[ITV-5332] – Mejora en las lecturas en COCs.

[ITV-5365] – quitar check de factura completa cuando es cliente de a crédito.

[ITV-5378] – Avisos alineación , distancias en función de defectos.

[ITV-5396] – Actualización «Acerca de…» a la nueva marca.

[ITV-5418] – Tu app se ve afectada por los requisitos de tamaño de página de 16 kB de Google Play.

[ITV-5440] – Si el cliente titular y representante son exactamente la misma persona, solo aparecerá uno de los dos.

[ITV-5442] – Realizar correcciones con la solicitud de las no periódicas.

[ITV-5482] – OBFCM, Se añade HÍBRIDO ENCHUFABLE, OVC-HEV.