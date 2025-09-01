# Alcance de segundas inspecciones

Segunda inspección o inspección de 2º orden, es cualquier inspección realizada como motivo de una 1º inspección con resultado desfavorable.

Cuando se da de alta una inspección que es calificada como 2º inspección o 2º fase o de subsanación de defectos, creativa aplica (si existe o está configurado) el **alcance de las segundas inspecciones**.

Este alcance es una relación de defectos que aplicarán a la inspección en base a cada uno de los defectos existentes en la inspección anterior con resultado desfavorable.

Es aplicable tanto para inspecciones de la propia estación como de las que vienen desde otra estación a pasar 2º en la nuestra.

## Como se introducen los defectos de las 2º inspecciones que vienen de fuera

Para introducir defectos en una inspección de 2º orden, duarante el alta de una inspección se debe utilizar el botón [D] que hay a la derecha del campo Nº de informe anterior.

![](images/creativa3d-altas-inspeccion-anterior.png)

En esta pantalla se deberán introducir todos los defectos que haya en el informe que presenta el cliente de la otra estación.

![](images/creativa3d-altas-inspeccion-anterior-defectos.png)

> Las inspecciones de 2º orden de nuestra estación, de forma automática adquieren los defectos de la 1º desfavorable.

El alta de debe de terminar de forma habitual.

## Modificar el alcance a aplicar de los puntos a inspeccionar

Para modificar el alcance que se muestra a los inspectores cuando se realiza una inspección de 2º orden se deben modificar los registros de la tabla "Alcance de segundas inspecciones"

![](images/creativa3d-mantenimiento-maestras-alcance_segundas_inspecciones.png)

En esta tabla hay un conjunto de registros que permiten asignar por cada Grupo de defectos, numero de defecto e incluso número de descripción de defecto, que puntos deben ser comprobados.

![](images/creativa3d-mantenimiento-maestras-alcance_segundas_inspecciones-tabla.png)

En esta tabla se pueden modificar o añadir registros nuevos, en el caso de ser necesarios.

- **Grupo**: Grupo de defecto
- **Número**: Numero de defecto
- **ID Descripción**: Nº de descripción del defecto, en el mismo orden que en el manual de ITV.
- **Puntos a comprobar**: Grupos (G1,G2..) o defectos (3.1,3.2..) que serán añadidos al alcance de la inspección de 2º orden cuando sea marcado este defecto (en el caso de 2º de fuera) o trasladado de una inspección de 1º orden desfavorable de esta estación.

Para modificar un alcance de un defecto en concreto, se selecciona el defecto, (por ejemplo el 4.1) y se pulsa sobre editar (o un doble clic con el ratón) y se escriben los grupos o defectos separados por comas, como se muestra en la imagen.

![](images/creativa3d-mantenimiento-maestras-alcance_segundas_inspecciones-tabla-edicion.png)

> Usar el número o ID de descripción de defecto, aunque es posible, en la práctica no se utiliza porque entonces habría que especificar un alcance por cada una de las descripciones.