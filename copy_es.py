# -*- coding: utf-8 -*-
"""Todo el texto del sitio en español.

Una clave por cadena. El portugués vive en `copy_pt.py` y el inglés en
`copy_en.py` con las MISMAS claves; `build.py` falla si falta una de
cualquier lado, para que ninguna página salga a medio traducir sin que
nadie se dé cuenta.

Las URL van sin acentos ni eñes a propósito: una ruta con caracteres fuera
del ASCII se convierte en percent-encoding en el navegador y queda
ilegible cuando alguien pega el enlace.

El español es neutro, sin regionalismos: el público va de México a
Argentina y "ordenador" o "computadora" delatan de dónde salió el texto.
"""

VERSION = "1.0"
RELEASE = "3 de septiembre de 2026"
UPDATED = "21 de agosto de 2026"

T = {
    # ------------------------------------------------------ navegación -----
    "lang_other": "PT",
    "lang_switch_aria": "Ver este sitio en portugués",
    "lang_group_aria": "Elige el idioma del sitio",
    "lang_name_pt": "Portugués",
    "lang_name_en": "Inglés",
    "lang_name_es": "Español",
    "theme_aria": "Alternar tema claro y oscuro",
    "nav_howto": "Cómo funciona",
    "nav_pluraleyes": "Vienes de PluralEyes",
    "nav_whatsnew": "Novedades",
    "nav_price": "Precio",
    "nav_download": "Descargar",
    "nav_eula": "Licencia de uso",
    "nav_terms": "Términos",
    "nav_privacy": "Privacidad",
    "nav_refunds": "Reembolsos",
    "url_howto": "/como-funciona/",
    "url_pluraleyes": "/alternativa-pluraleyes/",
    "url_whatsnew": "/novedades/",
    "url_eula": "/licencia-de-uso/",
    "url_terms": "/terminos/",
    "url_privacy": "/privacidad/",
    "url_refunds": "/reembolsos/",
    "email": "contato@sincou.com.br",

    # ------------------------------------------------------------- pie -----
    "foot_tagline": "Sincroniza la jornada por el sonido, organiza las "
                    "tarjetas y entrega la línea de tiempo lista para tu "
                    "editor.",
    "foot_product": "Producto",
    "foot_legal": "Legal",
    "foot_contact": "Contacto",
    "foot_req": "macOS 11 Big Sur o superior · Apple Silicon e Intel · "
                "versión para Windows en desarrollo",
    "made_in": "Hecho en Brasil",

    # =========================================================== HOME =======
    "home_title": "Sincou",
    "home_tagline": "sincroniza la jornada por el sonido",
    "home_desc": "Sincroniza la jornada entera por el sonido e importa en "
                 "Premiere, DaVinci Resolve o Final Cut con la línea de "
                 "tiempo lista. Para macOS, licencia única.",
    "hero_h1_a": "Toda la jornada,",
    "hero_h1_b": "sincronizada por el sonido.",
    "hero_lede": "Suelta las carpetas de las cámaras y las grabadoras, pulsa "
                 "Sync e importa el XML en Premiere o en DaVinci Resolve. El "
                 "material llega organizado, cada cámara en su pista, listo "
                 "para cortar.",
    "hero_cta": "Descargar para Mac",
    "hero_cta2": "Ver el paso a paso",
    "hero_note": "macOS 11+ · Apple Silicon e Intel · nada más que instalar",
    "hero_versao": "Versión {v} · {d}",
    "stage_clips": "242 clips",
    "stage_srcs": "2 cámaras · 2 grabadoras",
    "stage_dur": "7,6 h de material",
    "stage_replay": "Sincronizar otra vez",
    "stage_alt": "Clips de dos cámaras y dos grabadoras deslizándose desde "
                 "las posiciones originales hasta las sincronizadas",

    "stat1_v": "242", "stat1_k": "clips en una jornada real",
    "stat2_v": "100%", "stat2_k": "vinculados en Premiere y en Resolve",
    "stat3_v": "&le; &frac12;",
    "stat3_k": "fotograma de desvío, medido por la API de Resolve",
    "stat4_v": "0,5 ms", "stat4_k": "precisión del motor en material controlado",

    "flow_eyebrow": "El flujo",
    "flow_h2": "Tres pasos entre la tarjeta y el corte",
    "flow_lede": "El camino que haría un asistente a mano, hecho por una "
                 "máquina que mantiene la misma atención en el clip 1 y en "
                 "el clip 242.",
    "flow1_h": "Suelta el material",
    "flow1_p": "Carpetas enteras, tasas de fotogramas mezcladas, cámaras y "
               "grabadoras juntas. Sincou lee los metadatos al instante y "
               "dibuja la línea de tiempo antes de analizar.",
    "flow2_h": "Pulsa Sync",
    "flow2_p": "El motor compara las formas de onda y alinea cada clip con "
               "precisión de milisegundo. Cada par recibe una nota de "
               "confianza, y la clasificación separa lo que quedó fijo, lo "
               "que merece revisión y lo que quedó fuera.",
    "flow3_h": "Exporta el XML",
    "flow3_p": "Una línea de tiempo con una pista por cámara, el audio "
               "abajo y las carpetas del original convertidas en bins. Abre "
               "en tu editor con el material en línea.",
    "flow_more": "Ver el paso a paso completo",

    "pe_eyebrow": "Continuidad",
    "pe_h2": "Ya conoces este flujo",
    "pe_lede": "PluralEyes le enseñó a una generación de editores a confiar "
               "en el sonido para sincronizar. Sincou sigue ese camino y "
               "corre nativo en los Mac de hoy.",
    "pe_same_h": "Lo que sigue igual",
    "pe_same": ["Suelta la jornada entera y deja que el audio resuelva el "
                "alineamiento",
                "Una línea de tiempo por bloque de grabación, cada ángulo en "
                "su pista",
                "XML que abre directo en Premiere y en DaVinci Resolve"],
    "pe_new_h": "Lo que trae Sincou",
    "pe_new": ["Nativo en Apple Silicon, con el audio procesado en tu Mac",
               "Copia verificada de las tarjetas dentro de la misma "
               "aplicación",
               "Reproductor para comprobar la sincronía de oído antes de "
               "exportar",
               "Licencia única, comprada una sola vez"],
    "pe_more": "Leer la página completa",

    "feat_eyebrow": "Dentro de la app",
    "feat_h2": "Una ventana para el día entero",
    "feat_lede": "Lo que suele exigir tres programas distintos ocurre en un "
                 "solo lugar.",
    "feats": [
        ("Tasas mixtas", "23,976 y 59,94 en el mismo proyecto",
         "Cada archivo entra en el XML en la tasa en que fue grabado, que es "
         "justamente lo que mantiene el material en línea cuando el proyecto "
         "tiene cámaras distintas."),
        ("Revisión", "Escucha antes de exportar",
         "Haz clic en cualquier punto de la línea de tiempo y dale play: "
         "Sincou mezcla las cámaras bajo el cursor en tiempo real. Alineado "
         "suena junto, y el oído confirma la sincronía antes de que el "
         "material llegue al NLE."),
        ("Clasificación", "Tres estados, un color cada uno",
         "Fijo, revisar y fuera de sincronía, marcados en la línea de tiempo "
         "y en el XML. Miras directo a los pocos clips que piden atención."),
        ("DaVinci Resolve", "Script nativo incluido",
         "Un comando en Workspace &rsaquo; Scripts sincroniza el bin abierto "
         "y arma las líneas de tiempo por dentro de Resolve, con los clips "
         "vinculados al Media Pool y la clasificación pintada."),
        ("Timecode", "Igualar TC para multicámara",
         "Al exportar, Sincou escribe el mismo timecode para todas las "
         "cámaras y el multicámara nativo de tu editor agrupa solo. Tus "
         "archivos permanecen intactos."),
        ("Privacidad", "Todo ocurre en tu Mac",
         "El material se lee del disco, se procesa en tu CPU y se devuelve "
         "en XML. El informe de soporte, cuando eliges enviarlo, lleva solo "
         "números y apodos."),
    ],

    "ing_eyebrow": "Paso cero",
    "ing_h2": "La tarjeta llega entera, y tienes prueba de ello",
    "ing_lede": "Antes de sincronizar existe el momento más frágil de la "
                "jornada: el material vive en una sola tarjeta. Sincou copia, "
                "verifica byte a byte y registra qué pasó con cada archivo.",
    "ing_items": [
        ("Verificación byte a byte",
         "Cada archivo se lee de vuelta desde el destino y se compara con el "
         "origen. Una tarjeta defectuosa devuelve el tamaño correcto y los "
         "bytes equivocados, y esa lectura de vuelta es lo que lo revela "
         "mientras la tarjeta sigue en el lector."),
        ("Espacio verificado antes del primer byte",
         "Sincou suma el volumen a copiar y lo compara con el disco antes de "
         "empezar. Descubrir el disco lleno en el archivo 15 de 63 es el peor "
         "momento posible, así que la cuenta viene primero."),
        ("Estructura armada al instante",
         "Elige fecha, trabajo y cámara, y la ruta real aparece en pantalla "
         "mientras escribes. Lo que ves es literalmente la carpeta que va a "
         "nacer en el almacenamiento."),
        ("Error en tu idioma, en la línea del archivo",
         "Disco lleno, permiso denegado, tarjeta defectuosa. El registro dice "
         "el motivo en el archivo donde ocurrió y resume el motivo dominante "
         "arriba, así sabes qué arreglar antes de intentarlo de nuevo."),
    ],
    "ing_log": "Registro de la copia",
    "ing_copied": "copiado y verificado",
    "ing_there": "ya estaba ahí",
    "ing_nospace": "sin espacio en el destino",
    "ing_foot": "63 archivos · 61 copiados · 1 ya estaba · 1 problema · 248 GB",

    "exp_eyebrow": "Exportación",
    "exp_h2": "Llega listo a tu editor",
    "exports": [
        ("Adobe Premiere Pro", "XML de FCP7",
         "Abre el archivo en Premiere: el material se vincula solo y las "
         "carpetas del original se convierten en bins organizados."),
        ("DaVinci Resolve", "XML de FCP7 · o script nativo",
         "File &rsaquo; Import &rsaquo; Timeline y el material se vincula "
         "solo, igual. El script incluido hace el camino entero desde dentro "
         "de Resolve."),
        ("Final Cut Pro", "FCPXML",
         "Archivo en el formato nativo de Final Cut, con las pistas y los "
         "offsets de la sincronía."),
        ("Planilla y datos", "CSV · JSON",
         "Offsets, confianza y clasificación de cada clip, para revisar a ojo "
         "o alimentar tu propio script."),
    ],

    "price_eyebrow": "Licencia",
    "price_h2": "Compras una vez, es tuyo",
    "price_lede": "Empieza por los siete días con todo desbloqueado. Cuando "
                  "se acaban, Sincou sigue siendo tuyo, sincronizando "
                  "proyectos de hasta 10 clips, sin fecha de vencimiento. La "
                  "licencia quita el tope y se compra una sola vez.",
    "plan1_name": "Gratis",
    "plan1_price": "US$ 0",
    "plan1_unit": "· para siempre",
    "plan1_items": ["7 días con todo desbloqueado, sin límite",
                    "Después, hasta 10 clips por vez, sin plazo",
                    "XML limpio, listo para producción",
                    "Descarga y abre, sin registro"],
    "plan1_cta": "Descargar para Mac",
    "plan2_name": "Pro",
    "plan2_price": "US$ 49",
    "plan2_unit": "· una vez",
    "plan2_items": ["Una licencia para tu Mac",
                    "Sync, ingesta, reproductor y todas las exportaciones",
                    "Script de DaVinci Resolve incluido",
                    "Actualizaciones de la versión 1.x"],
    "plan2_cta": "Comprar",
    "plan3_name": "Estudio",
    "plan3_price": "US$ 119",
    "plan3_unit": "· una vez",
    "plan3_items": ["Hasta tres estaciones",
                    "Factura a nombre de la empresa",
                    "Soporte por correo con prioridad"],
    "plan3_cta": "Hablar con nosotros",
    "price_intl": "En Brasil: R$ 249 y R$ 599, con el mismo contenido.",
    "soon_h": "Versión para Windows en desarrollo.",
    "soon_p": "El motor ya corre multiplataforma. La versión empaquetada "
              "para Windows entra en seguida.",

    "autor_eyebrow": "Quién lo hizo",
    "autor_h2": "Hecho por alguien que edita todo el día",
    "autor_iniciais": "DM",
    "autor_nome": "Douglas Mendes",
    "autor_cargo": "Director, DoP y editor · autor de Sincou",
    "autor_p": [
        "Sincronizar multicámara a mano siempre fue el peaje antes de que la "
        "edición empezara de verdad. Quise librarme de eso desde temprano, "
        "pero las herramientas automáticas que probé no daban abasto con mis "
        "proyectos: las buenas exigen suscripción, y las que entraban en el "
        "presupuesto se atascaban justo con los archivos grandes.",
        "Así que, a partir de mi propia rutina, creé Sincou y lo probé en "
        "jornadas reales de día entero, con varias cámaras y grabadora. La "
        "sesión más pesada que ha procesado tiene 242 clips y 7,6 horas, y "
        "es la misma que uso para probar cada cambio: si falla ahí, me "
        "entero antes que tú.",
    ],
    "autor_promessa": "Sincou es gratuito durante siete días sin "
                      "restricciones, y siempre gratuito para hasta 10 clips "
                      "por vez. Existe para quitarte de encima la rutina de "
                      "sincronizar a mano y devolver ese tiempo a la parte "
                      "que importa: editar.",
    "faq_eyebrow": "Preguntas",
    "faq_h2": "Antes de descargar",
    "faq": [
        ("¿Necesito claqueta o timecode enlazado?",
         "Sincou trabaja con el sonido que las cámaras y la grabadora "
         "captaron del mismo evento, así que basta con que cada archivo tenga "
         "audio. Cuando hay timecode, entra como verificación y avisa si "
         "discrepa del audio."),
        ("¿Y si el audio de la cámara es malo?",
         "Es el caso común, y el motor se hizo para él. La comparación usa "
         "los instantes de los ataques sonoros, que son iguales en cualquier "
         "micrófono de la sala, independientes de ganancia, distancia y "
         "respuesta de frecuencia. Después, una segunda etapa refina el "
         "alineamiento con precisión de muestra."),
        ("¿Funciona con tasas de fotogramas distintas?",
         "Sí. La jornada usada en la validación tenía 23,976 y 59,94 en el "
         "mismo proyecto, con audio a 48 kHz. El XML declara cada archivo en "
         "su propia tasa, que es lo que garantiza el vínculo dentro del NLE."),
        ("¿Qué pasa con lo que queda fuera de sincronía?",
         "Va al final de la línea de tiempo, marcado en color, separado del "
         "material que cerró. Sincou prefiere señalar el clip dudoso antes "
         "que entregar un alineamiento que descubrirías equivocado en la sala "
         "de proyección."),
        ("¿Cuántos clips aguanta de una vez?",
         "La validación más pesada hasta ahora fue una jornada de 242 clips, "
         "7,6 horas de material, dos cámaras y dos grabadoras, procesada de "
         "una sola vez en un MacBook."),
        ("¿Necesito instalar algo más?",
         "Nada. Sincou ya viene con todo lo que necesita para leer material, "
         "incluido el decodificador. Descarga, arrastra a Aplicaciones y "
         "abre."),
        ("¿Qué pasa cuando se acaban los 7 días?",
         "Sincou sigue funcionando. Pasa al modo gratuito, que sincroniza "
         "proyectos de hasta 10 clips por vez, sin plazo y sin marca en el "
         "XML. Las jornadas más grandes piden la licencia, y se compra una "
         "sola vez."),
        ("¿La licencia vence o se vuelve suscripción?",
         "Ni lo uno ni lo otro. La compras una vez y es tuya, con las "
         "actualizaciones de la versión 1.x incluidas."),
        ("¿Cómo recibo mi clave después de comprar?",
         "Llega a tu correo en segundos, automáticamente, junto con el "
         "recibo. Pégala en la app, pulsa Activar y listo. Si no encuentras "
         "el mensaje, revisa la carpeta de promociones antes de escribirnos."),
        ("Perdí mi clave. ¿Y ahora?",
         "Está en el correo de la compra. Si no encuentras el mensaje, "
         "escribe al soporte desde la dirección con la que compraste y te "
         "lo reenviamos al instante."),
        ("¿Necesito internet para trabajar?",
         "Solo una vez, al activar, y únicamente para contar en cuántas "
         "máquinas está la clave. Después, nunca más: la clave está "
         "firmada y Sincou la verifica dentro de tu propio Mac, sin plazo "
         "y sin servidor. Puedes pasar la jornada entera en modo avión."),
        ("¿Puedo instalarlo en más de un ordenador?",
         "La licencia Sincou vale para un Mac, y la Estudio para tres. "
         "Cambiar de máquina es libre: liberas la plaza dentro de la propia "
         "app, en Licencia > Liberar este Mac, y activas en el otro equipo. "
         "Si el Mac antiguo ya no está contigo, el soporte libera la "
         "plaza. Reinstalar el sistema en el mismo Mac no consume una "
         "plaza nueva."),
        ("¿Hay versión para Windows?",
         "En desarrollo. El motor ya es multiplataforma, y la versión "
         "empaquetada para Windows entra en seguida."),
        ("¿Mi material sube a algún servidor?",
         "El procesamiento es enteramente local: la app lee los archivos de "
         "tu disco y escribe el XML de vuelta en él. Todo ocurre dentro de tu "
         "máquina, sin conexión."),
    ],

    "close_h2": "La próxima jornada puede empezar ya montada.",
    "close_lede": "Descarga, suelta las carpetas y mira cómo el material "
                  "encaja.",
    "close_note": "7 días con todo desbloqueado · macOS 11+",
}
