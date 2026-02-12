---
title: Envío de recordatorios usando filtros (envío parcial)
subtitle:
description: En este caso de uso se muestra el proceso para realizar el envío de recordatorios usando filtros.
icon:
status: draft
---

Contenido:

- [Obtener el listado de recordatorios a enviar](#obtener-el-listado-de-recordatorios-a-enviar)
- [Excluir recordatorios que no cumplen criterios seleccionados](#excluir-recordatorios-que-no-cumplen-criterios-seleccionados)
- [Envío de SMS, cartas y correos](#envío-de-sms-cartas-y-correos)


## Obtener el listado de recordatorios a enviar
Para obtener el listado de recordatorios a enviar, se realiza una consulta de recordatorios `Menú: Consultas > Recordatorios > Recordatorios`.

En el formulario, seleccionar todos los contactos, dejando la opción de descartar recordatorios con inspección pasada recientemente marcada (por defecto).

En el listado, aparecen todos los vehículos a los que hay que notificar su caducidad.

## Excluir recordatorios que no cumplen criterios seleccionados
En el listado de recordatorios, se pueden excluir aquellos que no cumplen los criterios seleccionados, como por ejemplo aquellos que tienen un tipo de inspección que no se desea incluir, o que tienen una cuenta de cobro que no se desea incluir, etc.

Para excluir registros del listado, se pueden usar los filtros de la parte superior del listado, o si son opciones mas avanzadas, se pueden usar los filtros avanzados, que se muestran al pulsar el botón de **Más filtros**.

![Filtros avanzados](images/caso-de-uso-recordatorios-filtros-avanzados.png)

En el ejemplo de la imagen, se han aplicado los siguientes filtros:
- Tipo de inspección: Distinto a Vehículo nuevo UE
- O
- Tipo de inspección: Distinto a Vehículo usado UE

Que excluyen del listado todos los registros (recordatorios a enviar de las matrículas involucradas) que cumplen esas condiciones.

## Envío de SMS, cartas y correos

En este caso, y según lo que tengas contratado con Creativa se realiza un envío de SMS (usando el botón SMS) y/o un envío de Correspondencia (botón Cartas), que es procesado por Creativa directamente.

El botón Email, enviará un Email a cada cliente si dispone de cuenta de email en su ficha del cliente. Se usará la plantilla de email configurada en el programa, sustituyendo las variables por los datos de cada cliente.