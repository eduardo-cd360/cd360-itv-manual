## Forma de pago o vencimiento en facturas con texto incorrecto

Todas las facturas en la parte inferior contienen dos leyendas, la forma de pago y el vencimiento.

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/casos-de-uso/facturacion/forma-pago-texto-incorrecto/images/image_1.png -->
![Imagen 1](./images/image_1.png)

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/casos-de-uso/facturacion/forma-pago-texto-incorrecto/images/image_2.png -->
![Imagen 2](./images/image_2.png)

Estas formas de pago están definidas en la tabla de formas de pago, localizable en:

Verificar que en la tabla de formas de pago, que la forma de pago -1, 0 y 2, coinciden con lo que se muestra en esta tabla. De no ser así, en la factura, se mostraría o el texto de “forma pago” o “vencimiento” cuando no deben.

Si se especifica en “Dias” algún número, en la factura saldrá vencimiento al nº de días indicados en el campo.

Si se cambia el texto de la columna “Forma pago”, cuando la inspección se realice por ese método, en la factura saldrá este texto.

El resto de formas de pago, son utilizadas en los albaranes, que se generan cuando se trata de cuentas de cobro, y se especifican en la ficha del cliente, en la forma de pago, de la misma forma que su cuenta bancaria.

<!-- https://github.com/eduardo-cd360/cd360-itv-manual/tree/main/docs/casos-de-uso/facturacion/forma-pago-texto-incorrecto/images/image_3.png -->
![Imagen 3](./images/image_3.png)
