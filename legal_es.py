# -*- coding: utf-8 -*-
"""Documentos legales en español.

BORRADORES. Son textos redactados en lenguaje claro y cubren lo que este
producto realmente hace, pero necesitan la lectura de un abogado antes de
valer como contrato, sobre todo por la venta fuera de Brasil (GDPR) y por
el régimen tributario.

Los datos de la empresa viven en `legal_pt.ENTITY`, en un solo lugar: una
razón social traducida sería una razón social distinta.
"""

UPDATED = "21 de agosto de 2026"

L = {
    # ============================================================ EULA ======
    "eula_title": "Licencia de uso de Sincou",
    "eula_desc": "Términos de la licencia de uso del software Sincou.",
    "eula_h1": "Licencia de uso",
    "eula_lede": "Este documento dice qué puedes hacer con Sincou después de "
                 "instalarlo. Vale para la versión de prueba y para la "
                 "versión con licencia.",
    "eula_body": [
        ("1. Qué recibes", [
            "Al instalar Sincou recibes una licencia de uso personal, "
            "permanente y no exclusiva del programa, en la versión 1.x. La "
            "licencia es tuya para usarla; el programa en sí sigue siendo "
            "nuestro.",
            "La licencia <strong>Sincou</strong> vale para un ordenador del "
            "titular. La licencia <strong>Estudio</strong> cubre hasta tres "
            "estaciones de la misma empresa. Cambiar de máquina está "
            "permitido: desactiva en una y activa en la otra.",
            "La activación pide conexión una sola vez, y solo para registrar la "
            "máquina y respetar el límite contratado. Después Sincou "
            "funciona sin internet, sin plazo: la clave está firmada y se "
            "verifica en tu propio ordenador.",
        ]),
        ("2. Qué produces con él", [
            "Todo lo que sale de Sincou es tuyo: los archivos XML, los "
            "informes, las copias que hizo la ingesta. No reivindicamos "
            "ningún derecho sobre tu material ni sobre el resultado de tu "
            "trabajo.",
            "Puedes usar Sincou en trabajo comercial sin pagar nada más allá "
            "de la licencia.",
        ]),
        ("3. Qué no permite la licencia", [
            "Revender, alquilar, sublicenciar o distribuir el programa.",
            "Compartir tu clave de licencia con personas fuera del límite de "
            "máquinas contratado.",
            "Quitar avisos de autoría o intentar sortear la activación.",
            "Hacer ingeniería inversa del programa, salvo en la medida en que "
            "la ley aplicable garantice ese derecho pese a esta restricción.",
        ]),
        ("4. Actualizaciones", [
            "Las actualizaciones de la versión 1.x están incluidas. Una "
            "futura versión 2.0 podrá ser de pago; si eso ocurre, tu licencia "
            "1.x sigue funcionando como siempre funcionó.",
        ]),
        ("5. Programas de terceros", [
            "Sincou usa ffmpeg para leer material. ffmpeg es un programa "
            "libre, de terceros, distribuido dentro de la aplicación bajo la "
            "licencia LGPL 2.1, en una versión compilada sin los componentes "
            "GPL. El texto de la licencia y la dirección del código fuente "
            "correspondiente acompañan a la aplicación.",
        ]),
        ("6. Garantía y límites", [
            "Sincou se entrega tal cual. Ha sido probado con material real de "
            "producción y mide su propio resultado, pero ningún software de "
            "sincronización sustituye la comprobación de quien edita. "
            "<strong>Verifica el resultado antes de comprometer una "
            "entrega.</strong>",
            "En la máxima extensión permitida por la ley aplicable, nuestra "
            "responsabilidad por cualquier reclamación relacionada con el "
            "programa queda limitada al importe que pagaste por la licencia. "
            "Esto no afecta los derechos que la legislación de consumo de tu "
            "país garantice y que no puedan renunciarse por contrato.",
        ]),
        ("7. Fin de la licencia", [
            "La licencia termina si incumples estos términos de forma "
            "relevante y no lo corriges tras el aviso. Al terminar, debes "
            "desinstalar el programa. Los archivos que ya produjiste siguen "
            "siendo tuyos.",
        ]),
        ("8. Ley aplicable", [
            "Esta licencia se rige por las leyes de la República Federativa "
            "de Brasil. Los consumidores fuera de Brasil conservan los "
            "derechos obligatorios de su propio país.",
        ]),
    ],

    # =========================================================== TÉRMINOS ===
    "terms_title": "Términos de uso",
    "terms_desc": "Términos de uso del sitio y condiciones de venta de Sincou.",
    "terms_h1": "Términos de uso",
    "terms_lede": "Estos términos valen para este sitio y para la compra de "
                  "licencias de Sincou. La licencia del programa en sí está "
                  "en un documento aparte.",
    "terms_body": [
        ("1. Este sitio", [
            "Este sitio presenta Sincou, distribuye la versión de prueba y "
            "vende licencias. Al usarlo, aceptas estos términos.",
            "Las cifras de rendimiento publicadas aquí vienen de mediciones "
            "hechas con material de producción real y están descritas junto "
            "al número. Indican lo que el programa hizo con ese material, y "
            "no una garantía de resultado idéntico con el tuyo.",
        ]),
        ("2. Prueba antes de comprar", [
            "La versión de prueba corre durante siete días con todas las "
            "funciones desbloqueadas y sin marca en el resultado. Existe para "
            "que verifiques el programa con tu propio material antes de "
            "pagar. Recomendamos usar ese periodo.",
        ]),
        ("3. Compra y entrega", [
            "La compra se hace a través de nuestro procesador de pagos. La "
            "clave de licencia se envía por correo en cuanto se confirma el "
            "pago. La entrega es digital e inmediata.",
            "Si la clave no llega en un plazo de 24 horas, escribe a {email} "
            "con el comprobante y lo resolvemos.",
        ]),
        ("4. Precios e impuestos", [
            "Los precios aparecen en reales para compras en Brasil y en "
            "dólares para compras internacionales. Los impuestos aplicables "
            "pueden añadirse al finalizar, según tu país.",
            "Podemos cambiar los precios en cualquier momento. El cambio no "
            "afecta a las compras ya realizadas.",
        ]),
        ("5. Soporte", [
            "El soporte se hace por correo en {email}, en español, portugués "
            "e inglés. La licencia Estudio tiene prioridad en la cola.",
            "Para reportar un problema técnico, la propia aplicación genera "
            "un informe anónimo en <em>Export &rsaquo; Something went "
            "wrong</em>. Lleva números y apodos, y nunca nombres de archivo, "
            "rutas ni material.",
        ]),
        ("6. Cambios en estos términos", [
            "Podemos actualizar estos términos. La fecha de la última "
            "actualización queda al pie del documento. Los cambios relevantes "
            "valen a partir de su publicación y no retroactúan sobre compras "
            "ya hechas.",
        ]),
    ],

    # ====================================================== PRIVACIDAD ======
    "privacy_title": "Privacidad",
    "privacy_desc": "Qué recoge Sincou y qué no recoge nunca. Procesamiento "
                    "local, sin subir material.",
    "privacy_h1": "Privacidad",
    "privacy_lede": "La respuesta corta: tu material nunca sale de tu "
                    "ordenador. El resto de esta página explica lo poco que "
                    "ocurre fuera de él.",
    "privacy_body": [
        ("Qué hace la aplicación con tu material", [
            "<strong>Nada sale de tu máquina.</strong> Sincou lee los "
            "archivos de tu disco, procesa el audio en tu CPU y escribe el "
            "XML de vuelta en tu disco. No hay subida, no hay cuenta que "
            "crear y no hay nube involucrada en el procesamiento.",
            "La aplicación funciona con internet apagado. Si quieres "
            "confirmarlo, desconéctate y corre una jornada entera.",
            "Las preferencias que la app guarda (tema, idioma, umbrales, "
            "última carpeta usada) quedan en tu propio ordenador, en el "
            "almacenamiento estándar del sistema.",
        ]),
        ("El informe técnico, cuando eliges enviarlo", [
            "El menú de exportación tiene la opción <em>Something went "
            "wrong</em>, que genera un archivo para ayudarnos a entender un "
            "problema. Ese archivo se genera en tu ordenador y solo llega "
            "hasta nosotros si tú lo envías.",
            "Contiene: número de clips, duración, tasas de fotogramas, notas "
            "de confianza, mensajes de error y apodos en lugar de los nombres "
            "(A1, B2, R1). <strong>No</strong> contiene nombres de archivo, "
            "rutas, imagen, audio ni ninguna parte de tu material. Existe una "
            "prueba automatizada en nuestro código que falla si algún nombre "
            "se filtra a ese informe.",
        ]),
        ("Qué recoge este sitio", [
            "El sitio es estático y no usa cookies de rastreo, ni píxeles de "
            "redes sociales, ni perfiles publicitarios.",
            "Nuestro alojamiento registra accesos (dirección IP, página, "
            "hora) como hace cualquier servidor, para operación y seguridad.",
        ]),
        ("Compra", [
            "Cuando compras, el pago lo procesa un socio especializado. "
            "<strong>No recibimos ni guardamos el número de tu "
            "tarjeta.</strong> Recibimos tu correo, para enviarte la clave y "
            "el comprobante, y los datos fiscales cuando la factura los "
            "exija.",
            "Guardamos esos datos durante el plazo que exige la legislación "
            "fiscal.",
        ]),
        ("Tus derechos", [
            "Puedes pedir acceso, corrección o eliminación de tus datos "
            "personales, y pedir una copia de ellos en formato legible. "
            "Escribe a {email} y respondemos dentro del plazo legal.",
            "En Brasil, esos derechos vienen de la LGPD (Ley 13.709/2018). En "
            "la Unión Europea y en el Reino Unido, del GDPR. Donde ambos se "
            "apliquen, vale lo que te sea más favorable.",
        ]),
    ],

    # ======================================================== REEMBOLSOS ====
    "refunds_title": "Reembolsos",
    "refunds_desc": "Política de reembolso de Sincou: catorce días, sin "
                    "necesidad de justificar.",
    "refunds_h1": "Reembolsos",
    "refunds_lede": "Prueba siete días antes de pagar. Si aun así la compra "
                    "no te sirve, te devolvemos el dinero.",
    "refunds_body": [
        ("Catorce días, sin tener que justificar", [
            "Tienes <strong>14 días corridos</strong> desde la compra para "
            "pedir el reembolso íntegro. No pedimos motivo y no ponemos "
            "condiciones.",
            "El plazo es mayor que los siete días de arrepentimiento que "
            "garantiza el Código de Defensa del Consumidor en Brasil, y "
            "acompaña los catorce días del derecho europeo. Donde la ley de "
            "tu país dé más, vale la ley.",
        ]),
        ("Cómo pedirlo", [
            "Escribe a {email} con el correo usado en la compra. No hace "
            "falta rellenar formularios ni hablar con atención telefónica.",
            "Procesamos la solicitud en hasta dos días hábiles. El dinero "
            "vuelve por el mismo medio de pago; el plazo hasta que aparezca "
            "en tu extracto depende de tu banco o de la operadora de la "
            "tarjeta.",
        ]),
        ("Qué pasa con la licencia", [
            "La clave se desactiva cuando se procesa el reembolso. Los "
            "archivos que ya produjiste con el programa siguen siendo tuyos, "
            "sin ninguna restricción.",
        ]),
        ("Por qué existe un periodo de prueba", [
            "Porque la sincronización por audio depende del material. La "
            "prueba de siete días existe para que corras tu propia jornada "
            "antes de decidir, y es la forma más honesta de saber si el "
            "programa sirve para tu trabajo. Usa la prueba; el reembolso es "
            "la red de abajo.",
        ]),
    ],
}
