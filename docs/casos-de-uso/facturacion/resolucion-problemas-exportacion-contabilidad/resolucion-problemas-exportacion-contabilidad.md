## Resolución de problemas con exportación a contabilidad

Es poco común que durante la exportación a contabilidad para los diferentes programas que soporta CREATIVA3D, se produzcan fallos o falte información.

En la mayoría de los casos, se ha omitido algún paso o algún dato que es necesario para que todo funcione adecuadamente.

En este documento se tratarán los posibles problemas que se pueden dar a la hora de generar los ficheros de exportación.

Exportación a A3

Al generar el fichero suenlace.dat, faltan clientes o facturas

Exportación CONTAPLUS

Se crean cuentas contables en CONTAPLUS aunque ya estén creadas

### Exportación A3

#### Al generar el fichero suenlace.dat, faltan clientes o facturas

Siempre que se realiza exportación de contabilidad, el software busca los datos relativos a la cuenta de cobro relacionada con el cliente facturado, y entre ellos la cuenta contable. Si no la encuentra, ese cliente y su facturación no serán exportados.

La solución consiste en editar las cuentas de cobro afectadas y cumplimentar el campo “cuenta contable” con la que tengan asignada.

Ahora se detecta esta irregularidad y se muestra aviso para que sean corregidas antes de la exportación. Versión correctora: 2021-2

### Exportación contaplus

#### Se crean cuentas contables en CONTAPLUS aunque ya estén creadas

Si una cuenta de cobro carece de cuenta contable asignada, quiere decir que aún no la tiene en CONTAPLUS, por lo que se genera un fichero adicional con las cuentas contables, que es importado en CONTAPLUS para crear dichos clientes.

Si ya tiene una cuenta de cobro asignado en CONTAPLUS, hay que editar la tabla de cuentas de cobro, y colocar la cuenta contable correspondiente o asignada al cliente en CONTAPLUS.