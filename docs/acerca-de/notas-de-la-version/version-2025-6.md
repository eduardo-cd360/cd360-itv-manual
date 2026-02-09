---
title: Versión 2025-6
slug: version-2025-6
---

# Notas de publicación - Creativa Digital 360 ITV - Versión 2025-6

[:fontawesome-solid-download: Descarga certificado de software](https://programaitv.com/wp-content/uploads/2026/02/Certificado-Software-2025-6-2.pdf){ .md-button }

## Subtarea
* [ITV-5534](http://jira.creativa3d.com:8080/browse/ITV-5534) - Crear una sección Perfil en Android y en Escritorio.

  Se ha creado una pantalla nueva accesible por todos los usuarios llamada Perfil que se encuentra en el menú Archivo. Desde ahí se pueden editar los datos del usuario así como su contraseña.

  Asimismo, en Android se ha creado una pantalla nativa llamada Perfil Usuario que hace exactamente lo mismo que en la versión de escritorio. En este caso se encuentra en los tres puntos al acceder al usuario (donde está el chat, la utilidad de los neumáticos, etc.).

* [ITV-5613](http://jira.creativa3d.com:8080/browse/ITV-5613) - Actualizar botones del panel de Cualificaciones por Tipo Inspección.
        
## Error
* [ITV-5518](http://jira.creativa3d.com:8080/browse/ITV-5518) - Que el foco pase a la matrícula al dar de alta una inspección.

  Subsanación de un error que hacía que al dar de alta una inspección el foco no se situara en el campo de matrícula.

* [ITV-5563](http://jira.creativa3d.com:8080/browse/ITV-5563) - No aparece la bola del mundo cuando esta buscando inspección.

  Solución de un error que impedía que apareciera el icono de la bola del mundo en la pantalla de alta de inspecciones en algunos casos.

## Mejora
* [ITV-5494](http://jira.creativa3d.com:8080/browse/ITV-5494) - ItvAndroid: realizar en 2º plano la recuperación de la inspección.
<!-- TODO: Que hace esto? -->
  
* [ITV-5502](http://jira.creativa3d.com:8080/browse/ITV-5502) - Factura electrónica (FACe). Evitar líneas con importe 0.

  Solución para que en las facturas electrónicas enviadas a FACe no se incluyan líneas con importe 0 y los programas de las administraciones públicas no den error al procesarlas.

* [ITV-5513](http://jira.creativa3d.com:8080/browse/ITV-5513) - Periódica de histórico que la fecha caducidad no sea obligatoria.

  En la configuración de altas de inspección (Archivo > Opciones > General > Altas de inspección) se ha añadido una nueva opción llamada "Fecha caducidad obligatoria".
  
  Si se desmarca esta opción, al dar de alta una inspección periódica de histórico no será obligatorio rellenar la fecha de caducidad.
  <!-- TODO: Comprobar si es para históricos o para todos los casos -->

* [ITV-5525](http://jira.creativa3d.com:8080/browse/ITV-5525) - Envío SII/Verifactu optimización.

  Se ha optimizado el proceso de envío de facturas al SII y a Verifactu para que sea más rápido y consuma menos recursos.

* [ITV-5573](http://jira.creativa3d.com:8080/browse/ITV-5573) - Exportación A3 no se exporten datos persona en facturas simplificadas cuando esta marcado no imprimir datos de cliente.

  Solución para que en la exportación al software de contabilidad A3 no se incluyan los datos de la persona cuando son facturas simplificadas y está marcada la opción "No imprimir datos de cliente" en la configuración de facturación (Archivo > Opciones > Facturación > Facturación > Otros).

* [ITV-5585](http://jira.creativa3d.com:8080/browse/ITV-5585) - Aviso de si se ha imputado el defecto (5.2 y 5.3) subdefecto 6.3 o 6.5 leve y la inspección es de orden 1.

  Se ha añadido un aviso que aparece al finalizar una inspección cuando se han imputado defectos 5.2 o 5.3 con subdefectos 6.3 o 6.5 (leves) y la inspección es de orden 1 (primera inspección). El aviso recuerda que en estos casos no se debe emitir el informe si no es quitado.

* [ITV-5589](http://jira.creativa3d.com:8080/browse/ITV-5589) - Facturación: Plantillas, añadir la opción de factura completa/simplificada.

  Se ha añadido un nuevo check en las plantillas de facturas (*Facturación > Plantillas*) llamada {FACTURADOCOMPLETOSN} que permite marcar si la factura es completa o simplificada.

  De esta forma, cuando en una factura creada manualmente partiendo de una plantilla, podrá trasladarse esta información a la factura generada.

* [ITV-5645](http://jira.creativa3d.com:8080/browse/ITV-5645) - Consulta DGT:  añadir enlace para poder ver Hoja rosa.

  En los resultados devueltos por la Consulta DGT (Consultas > Consulta DGT) se ha añadido un nuevo enlace que permite abrir la Hoja Rosa del vehículo cuando este la incorpora.

* [ITV-5649](http://jira.creativa3d.com:8080/browse/ITV-5649) - Ajustes tacógrafo

  Con motivo de la entrada en vigor de la nueva normativa sobre tacógrafos, se han realizado los siguientes cambios en el software:

    - Se ha quitado el aviso en pesados
    - Añadida opción certificado
    - Quitar calculo defecto en 2026
    - Quitar observaciones en pesados


* [ITV-5655](http://jira.creativa3d.com:8080/browse/ITV-5655) - Tipo de frenada en Vehículos pesadas en Observaciones.

Incorporación de leyenda en observaciones del informe de inspección del tipo de frenada empleado en las pruebas de vehículos pesados. En caso de dejar sin uso el tipo de frenada, se incluirá la leyenda "Frenada sin extrapolación".

## Tarea
* [ITV-5369](http://jira.creativa3d.com:8080/browse/ITV-5369) - Tabla nueva INSPECCIONESFASES, poner hora en cada fase del mecánico.

Se añade control de tiempos por fases en las inspecciones. Al finalizar cada fase, se registra la hora actual.

* [ITV-5506](http://jira.creativa3d.com:8080/browse/ITV-5506) - Facturación: Cambiar grupo por serie.

Se homogeniza el uso de "serie" en lugar de "grupo" en la facturación. Se reagrupan las opciones disponibles en la configuración de facturación y se actualizan los textos para mayor claridad.

* [ITV-5586](http://jira.creativa3d.com:8080/browse/ITV-5586) - Hacer sincronización con industria para los últimos 6 meses.
    