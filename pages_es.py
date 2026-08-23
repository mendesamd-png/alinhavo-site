# -*- coding: utf-8 -*-
"""Texto de las páginas internas en español (tutorial, PluralEyes, novedades)."""

P = {
    # ================================================== CÓMO FUNCIONA =======
    "howto_title": "Cómo funciona Sincou",
    "howto_desc": "Paso a paso de Sincou: copiar las tarjetas con "
                  "verificación, sincronizar la jornada por el sonido y "
                  "exportar la línea de tiempo a Premiere, DaVinci Resolve o "
                  "Final Cut.",
    "howto_eyebrow": "Paso a paso",
    "howto_h1": "De la tarjeta en el lector hasta el corte",
    "howto_lede": "Dos mitades del mismo día. La primera saca el material de "
                  "la tarjeta con prueba de que llegó entero. La segunda "
                  "alinea todo por el sonido y entrega la línea de tiempo "
                  "armada. Puedes usar solo una de ellas.",
    "howto_toc": "En esta página",

    "howto_part1_kicker": "Parte 1",
    "howto_part1_h2": "De la tarjeta al almacenamiento",
    "howto_part1_lede": "La pestaña Ingesta existe porque el momento en que "
                        "la jornada solo tiene una copia es el momento en que "
                        "puede desaparecer. Cuatro pasos, y la tarjeta sale "
                        "del lector con el trabajo verificado.",
    "howto_ing_steps": [
        ("Elige el destino y nombra el trabajo",
         "Apunta al volumen donde va a vivir el material y escribe el nombre "
         "del trabajo. Mientras escribes, Sincou muestra la ruta real que va "
         "a nacer en el disco, ya con la fecha delante. Lo que aparece en "
         "pantalla es literalmente la carpeta que va a existir."),
        ("Suelta las tarjetas",
         "Arrastra una tarjeta, varias, o carpetas ya copiadas. Sincou lee el "
         "árbol entero, suma el volumen y lo compara con el espacio libre del "
         "destino antes de escribir nada."),
        ("Copia con verificación",
         "Cada archivo se copia y después se lee de vuelta desde el destino "
         "para compararlo con el origen. Es el paso que separa una copia de "
         "una copia de seguridad: una tarjeta defectuosa devuelve el tamaño "
         "correcto con los bytes equivocados, y solo la lectura de vuelta lo "
         "revela."),
        ("Lee el informe",
         "Cada línea trae un símbolo y un estado. El pie resume archivos, "
         "copiados, ya existentes, problemas y volumen. Cuando algo falla, el "
         "motivo aparece en la línea del archivo, en tu idioma, y el motivo "
         "dominante sube arriba."),
    ],
    "howto_ing_shot": "La pestaña Ingesta con el destino, el trabajo y la "
                      "ruta real apareciendo en tiempo real.",
    "howto_ing_tip_h": "Sobre mover en vez de copiar",
    "howto_ing_tip_p": "Sincou copia, siempre. Mover borra el origen antes de "
                       "que hayas verificado el destino, y la única hora en "
                       "que eso importa es la hora en que sale mal. Formatea "
                       "la tarjeta tú mismo, después de ver el informe.",

    "howto_part2_kicker": "Parte 2",
    "howto_part2_h2": "Del almacenamiento a la línea de tiempo",
    "howto_part2_lede": "Aquí el sonido hace el trabajo. Entregas el material "
                        "en bruto y recibes una línea de tiempo con cada "
                        "cámara en su pista, el audio abajo y lo que quedó "
                        "fuera separado.",
    "howto_sync_steps": [
        ("Organiza el material en carpetas por fuente",
         "Una carpeta por cámara, una por grabadora. Sincou usa la carpeta "
         "para saber que esos archivos vinieron del mismo equipo, y eso "
         "mejora tanto el agrupamiento como la lectura de la línea de tiempo. "
         "Si el material ya vino de la Ingesta, la estructura ya está lista."),
        ("Suelta todo de una vez",
         "Arrastra la carpeta de la jornada entera. Sincou hace un "
         "reconocimiento rápido, sin decodificar audio, y ya dibuja el "
         "material en la línea de tiempo con la forma de onda de cada clip. "
         "El resumen de arriba dice cuántos clips, cuántas cámaras y cuántas "
         "grabadoras entraron."),
        ("Verifica el conteo antes de sincronizar",
         "Es el momento barato de darte cuenta de que quedó una tarjeta "
         "fuera. Si el número de cámaras está mal, corrígelo ahora: añadir "
         "material después significa correr la sincronía de nuevo."),
        ("Pulsa Sync",
         "El motor compara las formas de onda de todos los pares plausibles, "
         "elige el mejor alineamiento de cada par y resuelve el conjunto "
         "entero de una vez. Al terminar, los clips se deslizan a su posición "
         "y un sonido confirma el final."),
        ("Lee la línea de tiempo",
         "Cada fila es una fuente. Las cámaras quedan arriba, las grabadoras "
         "abajo. La distancia horizontal entre los bloques es el tiempo real "
         "entre las grabaciones, así que el espacio vacío también es "
         "información."),
        ("Escucha antes de exportar",
         "Haz clic en cualquier punto y dale play. Sincou mezcla en tiempo "
         "real todos los clips bajo el cursor. Alineado suena como una sola "
         "fuente; fuera de sincronía produce eco. Es la verificación más "
         "rápida que existe, y ocurre antes de que el material llegue al "
         "editor."),
        ("Exporta a tu editor",
         "Elige el destino en el menú Export. Cada opción ya trae la "
         "instrucción de importación que ese programa espera, porque cada uno "
         "importa de una manera."),
    ],
    "howto_sync_shot1": "El material cargado antes del Sync: cada fuente en "
                        "su fila, en orden de grabación.",
    "howto_sync_shot2": "Después del Sync: los grupos alineados, el clip "
                        "amarillo pidiendo revisión y el naranja fuera de "
                        "sincronía.",

    "howto_read_h2": "Qué te está diciendo la pantalla",
    "howto_read_lede": "Tres cosas llevan información: los colores, los "
                       "números del pie y la posición horizontal.",
    "howto_colors_h": "Los colores",
    "howto_colors": [
        ("Morado, rosa, azul, cian",
         "Un color por fuente. Son las cámaras y las grabadoras, y el color "
         "se mantiene igual de principio a fin de la jornada."),
        ("Amarillo",
         "Sincronizó, pero con confianza por debajo del umbral de bloqueo. El "
         "alineamiento probablemente está bien; vale la pena comprobarlo con "
         "el reproductor."),
        ("Naranja",
         "Quedó fuera de sincronía. Ninguna superposición de audio confiable "
         "con el resto del material. Va al final de la línea de tiempo, "
         "separado."),
    ],
    "howto_numbers_h": "Los números del pie",
    "howto_numbers": [
        ("files", "Cuántos clips entraron en total."),
        ("locked", "Alineados con confianza por encima del umbral. Puedes "
                   "confiar."),
        ("review", "Alineados, pero por debajo del umbral. Comprueba estos."),
        ("out of sync", "Sin par confiable. Quedaron al final, en naranja."),
        ("groups", "Bloques de grabación encontrados. Suele coincidir con el "
                   "número de tomas del día."),
        ("sync time", "Cuánto tardó el motor."),
    ],
    "howto_thresholds_h": "Si la clasificación queda demasiado conservadora",
    "howto_thresholds_p": "El engranaje de arriba abre dos umbrales. "
                          "<strong>Sync threshold</strong> es el mínimo para "
                          "que Sincou acepte un alineamiento. <strong>Lock "
                          "threshold</strong> es el mínimo para que deje de "
                          "pedir revisión. El material con mucho ruido de set "
                          "o con superposición corta pide un umbral más bajo; "
                          "el material limpio soporta uno más alto.",

    "howto_out_h2": "Cuando algo queda fuera",
    "howto_out_lede": "Un clip en naranja casi siempre tiene una de estas "
                      "causas.",
    "howto_out": [
        ("No hay superposición real",
         "El clip se grabó cuando nada más estaba corriendo. En ese caso el "
         "naranja está bien: no existe con qué sincronizarlo."),
        ("La superposición es demasiado corta",
         "Pocos segundos en común producen una correlación que parece buena y "
         "no lo es. Sincou pesa la evidencia por el tamaño de la "
         "superposición justamente para no caer en eso."),
        ("El audio no tiene eventos",
         "Un tramo de silencio, de viento o de tono continuo no le da al "
         "motor nada que comparar. El alineamiento usa los instantes de los "
         "ataques sonoros, y donde no hay ataque no hay ancla."),
        ("La cámara grabó sin audio",
         "Sin pista de audio no hay sincronización por sonido. El timecode "
         "todavía puede posicionar el clip, si existe."),
    ],

    "howto_export_h2": "Cómo importa cada editor",
    "howto_export": [
        ("Adobe Premiere Pro",
         "Exporta <strong>XML de FCP7</strong> y abre el archivo desde "
         "Premiere (File &rsaquo; Open). Lo convierte en un proyecto con las "
         "secuencias armadas, el material en línea y el audio vinculado al "
         "vídeo. Las carpetas del material original se convierten en bins."),
        ("DaVinci Resolve",
         "Exporta <strong>XML de FCP7</strong> y usa File &rsaquo; Import "
         "&rsaquo; Timeline. El material se vincula solo. Como alternativa, "
         "Sincou instala un script en Workspace &rsaquo; Scripts que "
         "sincroniza el bin abierto y arma las líneas de tiempo sin salir de "
         "Resolve."),
        ("Final Cut Pro",
         "Exporta <strong>FCPXML</strong> e impórtalo desde Final Cut. El "
         "archivo lleva las pistas y los offsets de la sincronía."),
        ("Multicámara nativo",
         "Activa <strong>Matching timecode</strong> en el menú de "
         "exportación. Sincou escribe el mismo timecode para todas las "
         "cámaras en el XML, y la función de multicámara de tu editor agrupa "
         "sola. Tus archivos originales no se tocan."),
    ],

    "howto_faq_h2": "Dudas del camino",
    "howto_faq": [
        ("¿Puedo usar solo la Ingesta, sin sincronizar?",
         "Puedes. Las dos pestañas son independientes. Mucha gente usa la "
         "Ingesta al volver de la jornada y el Sync solo al día siguiente, ya "
         "con el material en el almacenamiento."),
        ("¿Puedo sincronizar material que no pasó por la Ingesta?",
         "Puedes. El Sync lee cualquier carpeta. La Ingesta existe para el "
         "camino de la tarjeta, y no es un requisito previo."),
        ("¿Sincou modifica mis archivos?",
         "No. Lee el material y escribe un XML aparte. Ni siquiera la opción "
         "de igualar timecode toca los archivos: el timecode nuevo vive "
         "dentro del XML."),
        ("¿Cuántas cámaras caben?",
         "No hay un límite fijo. El costo crece con el número de pares "
         "plausibles, y una jornada de dos cámaras con dos grabadoras y más "
         "de doscientos clips corre de una vez en un MacBook."),
        ("¿Y si tengo una grabadora de varias pistas?",
         "Cada archivo se vuelve una fuente. Si la grabadora escribe un "
         "archivo por canal, ponlos en la misma carpeta: Sincou los trata "
         "como el mismo equipo y no intenta sincronizar uno contra el otro."),
    ],
    "howto_cta_h": "¿Listo para probarlo con tu material?",
    "howto_cta_p": "Siete días con todo desbloqueado, sin registro.",

    # ================================================ ALTERNATIVA PE ========
    "pe_title": "Alternativa a PluralEyes para Mac",
    "pe_desc": "PluralEyes salió de escena. Sincou sincroniza la jornada por "
               "el audio, corre nativo en Apple Silicon y exporta a Premiere, "
               "DaVinci Resolve y Final Cut.",
    "pe_page_eyebrow": "Migración",
    "pe_page_h1": "Una alternativa a PluralEyes, hecha para los Mac de hoy",
    "pe_page_lede": "Durante casi quince años, sincronizar multicámara por "
                    "audio quería decir PluralEyes. El hábito que creó sigue "
                    "siendo correcto: el sonido que todas las cámaras "
                    "captaron es la evidencia más confiable que existe en una "
                    "jornada. Sincou parte del mismo principio y resuelve las "
                    "partes que envejecieron.",

    "pe_why_h2": "Lo que PluralEyes acertó, y sigue valiendo",
    "pe_why": [
        ("El audio es la fuente de la verdad",
         "La claqueta falla, el timecode libre se corre, el jam sync se "
         "pierde. El sonido que dos cámaras grabaron del mismo evento es el "
         "mismo sonido, y la diferencia entre ellos es exactamente el offset. "
         "Ese principio no envejeció."),
        ("Un botón, la jornada entera",
         "La interfaz correcta para esta tarea es casi ninguna interfaz: "
         "material adentro, línea de tiempo afuera. Sincou lo mantiene."),
        ("Entregar al NLE en XML",
         "Intercambiar la línea de tiempo por archivo funciona mejor que un "
         "plugin instalado dentro del editor, porque sobrevive a la "
         "actualización del editor."),
    ],

    "pe_diff_h2": "Lo que cambia en Sincou",
    "pe_diff": [
        ("Nativo en Apple Silicon",
         "El procesamiento corre directo en tu Mac, sin capa de traducción. "
         "Nada se envía a ningún servidor."),
        ("La confianza queda visible",
         "Cada alineamiento lleva una nota. Sincou separa lo que quedó fijo, "
         "lo que merece una comprobación y lo que quedó fuera, en vez de "
         "entregar todo con la misma cara. Una sincronía equivocada "
         "descubierta en la sala de proyección cuesta mucho más cara que un "
         "clip marcado en amarillo."),
        ("Comprobación de oído incorporada",
         "Un reproductor que mezcla en tiempo real los clips bajo el cursor. "
         "Alineado suena como una sola fuente."),
        ("La ingesta en la misma aplicación",
         "Copia verificada de las tarjetas, organizada por fecha, trabajo y "
         "cámara. El programa que sincroniza es el mismo que sabe de dónde "
         "vino el material."),
        ("Licencia única",
         "Compras una vez, activación local, sin suscripción y sin un "
         "servidor decidiendo si hoy puedes trabajar."),
    ],

    "pe_move_h2": "Cómo migrar",
    "pe_move": [
        ("Deja tus carpetas como están",
         "Una carpeta por cámara, una por grabadora. Es la misma organización "
         "que pedía PluralEyes, y Sincou lee exactamente eso."),
        ("Suelta la jornada y pulsa Sync",
         "No hay proyecto que crear ni configuración que acertar antes. Los "
         "umbrales tienen valores por defecto que funcionan, y quedan a un "
         "clic si quieres tocarlos."),
        ("Exporta en el formato que ya usabas",
         "XML de FCP7 para Premiere y DaVinci Resolve, FCPXML para Final Cut. "
         "Son los mismos formatos que importabas antes."),
    ],
    "pe_page_cta_h": "Trae la próxima jornada",
    "pe_page_cta_p": "Siete días con todo desbloqueado. Si el flujo antiguo te "
                     "resultaba familiar, este va a parecer el mismo lugar, "
                     "más rápido.",

    # ====================================================== NOVEDADES =======
    "wn_title": "Novedades de Sincou",
    "wn_desc": "Qué cambió en cada versión de Sincou.",
    "wn_eyebrow": "Registro",
    "wn_h1": "Novedades",
    "wn_lede": "Cada versión y lo que trajo. Las correcciones que merecen "
               "nota también están aquí.",
    "wn_releases": [
        ("1.0", "21 de agosto de 2026", "Primera versión pública", [
            "Sincronización por audio en dos etapas: envolvente de ataques "
            "sonoros para encontrar el alineamiento y refinamiento por "
            "correlación de fase para llegar al milisegundo.",
            "Clasificación en tres estados (fijo, revisar, fuera de "
            "sincronía), marcada en la línea de tiempo y llevada dentro del "
            "XML.",
            "Lectura de timecode SMPTE, incluido drop-frame, usada como "
            "verificación del resultado del audio.",
            "Detección de deriva de reloj entre equipos.",
            "Ingesta con copia verificada, organización por fecha, trabajo y "
            "cámara, y verificación de espacio antes de escribir el primer "
            "byte.",
            "Reproductor que mezcla en tiempo real los clips bajo el cursor.",
            "Exportación a XML de FCP7 (Premiere y DaVinci Resolve), FCPXML "
            "(Final Cut), CSV y JSON.",
            "Script para DaVinci Resolve, instalado en Workspace &rsaquo; "
            "Scripts, que sincroniza el bin abierto sin salir del programa.",
            "Opción de igualar el timecode entre cámaras para usar el "
            "multicámara nativo del editor, sin tocar los archivos "
            "originales.",
            "Interfaz en español, portugués e inglés, con tema claro y "
            "oscuro.",
        ]),
    ],
    "wn_next_h": "En camino",
    "wn_next": [
        "Versión para Windows.",
        "Corrección de deriva de reloj, además de la detección que ya existe.",
        "Nombre de proyecto configurable para los archivos exportados.",
    ],
    "wn_note": "Las fechas de los elementos futuros no son promesa de entrega.",
}
