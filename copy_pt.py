"""Todo o texto do site em português.

Uma chave por string. O inglês vive em `copy_en.py` com as MESMAS chaves;
`build.py` falha se uma faltar de um lado, para nenhuma página sair meio
traduzida sem ninguém perceber.

As URLs ficam sem acento e sem cedilha de propósito: caminho de URL com
caractere fora do ASCII vira percent-encoding no navegador e fica ilegível
quando alguém cola o link.
"""

VERSION = "1.0"
UPDATED = "21 de agosto de 2026"

T = {
    # ------------------------------------------------------- navegação -----
    "lang_other": "EN",
    "lang_switch_aria": "Ver este site em inglês",
    "theme_aria": "Alternar tema claro e escuro",
    "nav_howto": "Como funciona",
    "nav_pluraleyes": "Vem do PluralEyes",
    "nav_whatsnew": "Novidades",
    "nav_price": "Preço",
    "nav_download": "Baixar",
    "nav_eula": "Licença de uso",
    "nav_terms": "Termos",
    "nav_privacy": "Privacidade",
    "nav_refunds": "Reembolso",
    "url_howto": "/como-funciona/",
    "url_pluraleyes": "/alternativa-pluraleyes/",
    "url_whatsnew": "/novidades/",
    "url_eula": "/licenca-de-uso/",
    "url_terms": "/termos/",
    "url_privacy": "/privacidade/",
    "url_refunds": "/reembolso/",
    "email": "contato@alinhavo.app",

    # ---------------------------------------------------------- rodapé -----
    "foot_tagline": "Sincroniza a diária pelo som, organiza os cartões e "
                    "entrega a timeline pronta para o seu editor.",
    "foot_product": "Produto",
    "foot_legal": "Legal",
    "foot_contact": "Contato",
    "foot_req": "macOS 12 Monterey ou superior · Apple Silicon e Intel · "
                "versão para Windows em desenvolvimento",
    "made_in": "Feito no Brasil",

    # =========================================================== HOME =======
    "home_title": "Alinhavo",
    "home_tagline": "sincroniza a diária pelo som",
    "home_desc": "Sincronize a diária inteira pelo som e importe no Premiere, "
                 "DaVinci Resolve ou Final Cut com a timeline pronta. Para "
                 "macOS, licença única.",
    "hero_h1_a": "Toda a diária,",
    "hero_h1_b": "sincronizada pelo som.",
    "hero_lede": "Solte as pastas das câmeras e dos gravadores, aperte Sync e "
                 "importe o XML no Premiere ou no DaVinci Resolve. O material "
                 "chega organizado, cada câmera na sua faixa, pronto para "
                 "cortar.",
    "hero_cta": "Baixar para Mac",
    "hero_cta2": "Ver o passo a passo",
    "hero_note": "macOS 12+ · Apple Silicon e Intel",
    "stage_clips": "242 clipes",
    "stage_srcs": "2 câmeras · 2 gravadores",
    "stage_dur": "7,6 h de material",
    "stage_replay": "Sincronizar de novo",
    "stage_alt": "Clipes de duas câmeras e dois gravadores deslizando das "
                 "posições brutas para as posições sincronizadas",

    "stat1_v": "242", "stat1_k": "clipes numa diária real",
    "stat2_v": "100%", "stat2_k": "linkados no Premiere e no Resolve",
    "stat3_v": "&le; &frac12;",
    "stat3_k": "quadro de desvio, medido pela API do Resolve",
    "stat4_v": "0,5 ms", "stat4_k": "precisão do motor em material controlado",

    "flow_eyebrow": "O fluxo",
    "flow_h2": "Três passos entre o cartão e o corte",
    "flow_lede": "O caminho que um assistente faria à mão, feito por uma "
                 "máquina que mantém a mesma atenção no clipe 1 e no clipe 242.",
    "flow1_h": "Solte o material",
    "flow1_p": "Pastas inteiras, taxas de quadro misturadas, câmeras e "
               "gravadores juntos. O Alinhavo lê os metadados na hora e desenha "
               "a timeline antes de analisar.",
    "flow2_h": "Aperte Sync",
    "flow2_p": "O motor compara as formas de onda e alinha cada clipe com "
               "precisão de milissegundo. Cada par recebe uma nota de "
               "confiança, e a triagem separa o que está travado, o que merece "
               "revisão e o que ficou de fora.",
    "flow3_h": "Exporte o XML",
    "flow3_p": "Uma timeline com uma faixa por câmera, áudio embaixo e as "
               "pastas do bruto viradas em bins. Abre no seu editor com a "
               "mídia online.",
    "flow_more": "Ver o passo a passo completo",

    "pe_eyebrow": "Continuidade",
    "pe_h2": "Você já conhece este fluxo",
    "pe_lede": "O PluralEyes ensinou uma geração de editores a confiar no som "
               "para sincronizar. O Alinhavo segue esse caminho e roda nativo "
               "nos Macs de hoje.",
    "pe_same_h": "O que continua igual",
    "pe_same": ["Solte a diária inteira e deixe o áudio resolver o alinhamento",
                "Uma timeline por bloco de gravação, cada ângulo na sua faixa",
                "XML que abre direto no Premiere e no DaVinci Resolve"],
    "pe_new_h": "O que o Alinhavo traz",
    "pe_new": ["Nativo em Apple Silicon, com o áudio processado no seu Mac",
               "Backup verificado dos cartões dentro do mesmo aplicativo",
               "Player para conferir o sync de ouvido antes de exportar",
               "Licença única, comprada uma vez"],
    "pe_more": "Ler a página completa",

    "feat_eyebrow": "Dentro do app",
    "feat_h2": "Uma janela para o dia inteiro",
    "feat_lede": "O que costuma exigir três programas diferentes acontece em "
                 "um lugar só.",
    "feats": [
        ("Taxas mistas", "23,976 e 59,94 no mesmo projeto",
         "Cada arquivo entra no XML na taxa em que foi gravado, que é "
         "justamente o que mantém a mídia online quando o projeto tem câmeras "
         "diferentes."),
        ("Revisão", "Ouça antes de exportar",
         "Clique em qualquer ponto da timeline e dê play: o Alinhavo mixa as "
         "câmeras sob o cursor em tempo real. Alinhado soa junto, e o ouvido "
         "confirma o sync antes de o material chegar no NLE."),
        ("Triagem", "Três estados, uma cor cada",
         "Travado, revisar e fora do sync, marcados na timeline e no XML. "
         "Você olha direto para os poucos clipes que pedem atenção."),
        ("DaVinci Resolve", "Script nativo incluído",
         "Um comando em Workspace &rsaquo; Scripts sincroniza o bin aberto e "
         "monta as timelines por dentro do Resolve, com os clipes linkados ao "
         "Media Pool e a triagem pintada."),
        ("Timecode", "Igualar TC para multicam",
         "Na exportação, o Alinhavo escreve o mesmo timecode para todas as "
         "câmeras e o multicam nativo do seu editor agrupa sozinho. Seus "
         "arquivos permanecem intactos."),
        ("Privacidade", "Tudo acontece no seu Mac",
         "O material é lido do disco, processado na sua CPU e devolvido em "
         "XML. O relatório de suporte, quando você escolhe enviar, leva "
         "apenas números e apelidos."),
    ],

    "ing_eyebrow": "Passo zero",
    "ing_h2": "O cartão chega inteiro, e você tem prova disso",
    "ing_lede": "Antes de sincronizar existe o momento mais frágil da diária: "
                "a mídia mora num cartão só. O Alinhavo copia, confere byte a "
                "byte e registra o que aconteceu com cada arquivo.",
    "ing_items": [
        ("Verificação byte a byte",
         "Cada arquivo é lido de volta do destino e comparado com a origem. "
         "Cartão com defeito devolve o tamanho certo e os bytes errados, e a "
         "leitura de volta é o que revela isso enquanto o cartão ainda está "
         "no leitor."),
        ("Espaço conferido antes do primeiro byte",
         "O Alinhavo soma o volume a copiar e compara com o disco antes de "
         "começar. Descobrir disco cheio no arquivo 15 de 63 é o pior momento "
         "possível, então a conta vem primeiro."),
        ("Estrutura montada no ato",
         "Escolha data, job e câmera, e o caminho real aparece na tela "
         "enquanto você digita. O que você vê é literalmente a pasta que vai "
         "nascer no storage."),
        ("Erro em português, na linha do arquivo",
         "Disco cheio, permissão negada, cartão com defeito. O log diz o "
         "motivo no arquivo em que ele aconteceu e resume o motivo dominante "
         "no topo, então você sabe o que consertar antes de tentar de novo."),
    ],
    "ing_log": "Log da cópia",
    "ing_copied": "copiado e verificado",
    "ing_there": "já estava lá",
    "ing_nospace": "sem espaço no destino",
    "ing_foot": "63 arquivos · 61 copiados · 1 já estava lá · 1 problema · 248 GB",

    "exp_eyebrow": "Exportação",
    "exp_h2": "Chega pronto no seu editor",
    "exports": [
        ("Adobe Premiere Pro", "XML do FCP7",
         "Abra o arquivo no Premiere: a mídia linka sozinha e as pastas do "
         "bruto viram bins organizados."),
        ("DaVinci Resolve", "XML do FCP7 · ou script nativo",
         "File &rsaquo; Import &rsaquo; Timeline e a mídia linka sozinha, do "
         "mesmo jeito. O script incluído faz o caminho inteiro de dentro do "
         "Resolve."),
        ("Final Cut Pro", "FCPXML",
         "Arquivo no formato nativo do Final Cut, com as faixas e os offsets "
         "do sync."),
        ("Planilha e dados", "CSV · JSON",
         "Offsets, confiança e triagem de cada clipe, para conferir a olho ou "
         "alimentar seu próprio script."),
    ],

    "price_eyebrow": "Licença",
    "price_h2": "Compra uma vez, é seu",
    "price_lede": "Comece pelos sete dias com tudo liberado. Quando eles "
                  "acabam o Alinhavo continua seu, sincronizando projetos de "
                  "até 10 clipes, sem prazo para expirar. A licença tira o "
                  "teto e é comprada uma vez só.",
    "plan1_name": "Grátis",
    "plan1_price": "R$ 0",
    "plan1_unit": "· para sempre",
    "plan1_items": ["7 dias com tudo liberado, sem limite",
                    "Depois disso, até 10 clipes por vez, sem prazo",
                    "XML limpo, pronto para produção",
                    "Baixe e abra, sem cadastro"],
    "plan1_cta": "Baixar para Mac",
    "plan2_name": "Pro",
    "plan2_price": "R$ 249",
    "plan2_unit": "· uma vez",
    "plan2_items": ["Uma licença para o seu Mac",
                    "Sync, ingest, player e todos os exports",
                    "Script do DaVinci Resolve incluído",
                    "Atualizações da versão 1.x"],
    "plan2_cta": "Comprar",
    "plan3_name": "Estúdio",
    "plan3_price": "R$ 599",
    "plan3_unit": "· uma vez",
    "plan3_items": ["Até três estações",
                    "Nota fiscal em nome da empresa",
                    "Suporte por e-mail com prioridade"],
    "plan3_cta": "Falar com a gente",
    "price_intl": "Fora do Brasil: US$ 49 e US$ 119, com o mesmo conteúdo.",
    "soon_h": "Versão para Windows em desenvolvimento.",
    "soon_p": "O motor já roda multiplataforma. A versão empacotada para "
              "Windows entra em seguida.",

    "faq_eyebrow": "Perguntas",
    "faq_h2": "Antes de baixar",
    "faq": [
        ("Preciso de claquete ou de timecode casado?",
         "O Alinhavo trabalha com o som que as câmeras e o gravador captaram do "
         "mesmo evento, então basta que cada arquivo tenha áudio. Quando há "
         "timecode, ele entra como conferência e avisa se discordar do áudio."),
        ("E se o áudio da câmera for ruim?",
         "É o caso comum, e o motor foi feito para ele. A comparação usa os "
         "instantes dos ataques sonoros, que são iguais em qualquer microfone "
         "da sala, independentes de ganho, distância e resposta de frequência. "
         "Depois disso um segundo estágio refina o alinhamento com precisão de "
         "amostra."),
        ("Funciona com taxas de quadro diferentes?",
         "Sim. A diária usada na validação tinha 23,976 e 59,94 no mesmo "
         "projeto, com áudio a 48 kHz. O XML declara cada arquivo na taxa "
         "dele, que é o que garante o link dentro do NLE."),
        ("O que acontece com o que fica fora do sync?",
         "Vai para o fim da timeline, marcado em cor, separado do material que "
         "fechou. O Alinhavo prefere apontar o clipe duvidoso a entregar um "
         "alinhamento que você descobriria errado na sala de exibição."),
        ("Quantos clipes ele aguenta de uma vez?",
         "A validação mais pesada até agora foi uma diária de 242 clipes, 7,6 "
         "horas de material, duas câmeras e dois gravadores, processada de uma "
         "vez num MacBook."),
        ("Preciso instalar mais alguma coisa?",
         "O ffmpeg, que faz a leitura de mídia e costuma já estar na máquina "
         "de quem edita. Um comando instala: <span class=\"mono\">brew install "
         "ffmpeg</span>."),
        ("O que acontece quando os 7 dias acabam?",
         "O Alinhavo continua funcionando. Ele passa para o modo gratuito, que "
         "sincroniza projetos de até 10 clipes por vez, sem prazo e sem marca "
         "no XML. Diárias maiores pedem a licença, e ela é comprada uma vez."),
        ("A licença expira ou vira assinatura?",
         "Nem uma coisa nem outra. Você compra uma vez e ela é sua, com as "
         "atualizações da versão 1.x incluídas. A ativação acontece no seu "
         "computador e o app abre offline: não existe servidor que possa "
         "deixar de responder e impedir o seu trabalho."),
        ("Posso instalar em mais de um computador?",
         "A licença Alinhavo vale para um Mac, e a Estúdio para três. "
         "Trocar de máquina é livre: você libera a vaga dentro do próprio app "
         "e ativa no outro computador. Reinstalar o sistema no mesmo Mac não "
         "consome uma vaga nova."),
        ("Tem versão para Windows?",
         "Em desenvolvimento. O motor já é multiplataforma, e a versão "
         "empacotada para Windows entra em seguida."),
        ("Meu material sobe para algum servidor?",
         "O processamento é inteiramente local: o app lê os arquivos do seu "
         "disco e escreve o XML de volta nele. Tudo acontece dentro da sua "
         "máquina, offline."),
    ],

    "close_h2": "A próxima diária pode começar já montada.",
    "close_lede": "Baixe, solte as pastas e veja o material se encaixar.",
    "close_note": "7 dias com tudo liberado · macOS 12+",
}
