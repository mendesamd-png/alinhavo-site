"""Texto das páginas internas em português (tutorial, PluralEyes, novidades)."""

P = {
    # ================================================== COMO FUNCIONA =======
    "howto_title": "Como funciona o Sincou",
    "howto_desc": "Passo a passo do Sincou: copiar os cartões com verificação, "
                  "sincronizar a diária pelo som e exportar a timeline para "
                  "Premiere, DaVinci Resolve ou Final Cut.",
    "howto_eyebrow": "Passo a passo",
    "howto_h1": "Do cartão no leitor até o corte",
    "howto_lede": "Duas metades do mesmo dia. A primeira tira a mídia do "
                  "cartão com prova de que chegou inteira. A segunda alinha "
                  "tudo pelo som e entrega a timeline montada. Você pode usar "
                  "só uma delas.",
    "howto_toc": "Nesta página",

    "howto_part1_kicker": "Parte 1",
    "howto_part1_h2": "Do cartão para o storage",
    "howto_part1_lede": "A aba Ingest existe porque o momento em que a diária "
                        "só tem uma cópia é o momento em que ela pode "
                        "desaparecer. Quatro passos, e o cartão sai do leitor "
                        "com o trabalho conferido.",
    "howto_ing_steps": [
        ("Escolha o destino e nomeie o job",
         "Aponte o volume onde o material vai morar e escreva o nome do job. "
         "Enquanto você digita, o Sincou mostra o caminho real que vai nascer "
         "no disco, já com a data na frente. O que aparece na tela é "
         "literalmente a pasta que vai existir."),
        ("Solte os cartões",
         "Arraste um cartão, vários, ou pastas já copiadas. O Sincou lê a "
         "árvore inteira, soma o volume e compara com o espaço livre do "
         "destino antes de escrever qualquer coisa."),
        ("Copie com verificação",
         "Cada arquivo é copiado e depois lido de volta do destino para ser "
         "comparado com a origem. É o passo que separa uma cópia de um "
         "backup: cartão com defeito devolve o tamanho certo com os bytes "
         "errados, e só a leitura de volta revela isso."),
        ("Leia o relatório",
         "Cada linha traz um símbolo e um estado. O rodapé resume arquivos, "
         "copiados, já existentes, problemas e volume. Quando algo falha, o "
         "motivo aparece na linha do arquivo, em português, e o motivo "
         "dominante sobe para o topo."),
    ],
    "howto_ing_shot": "A aba Ingest com o destino, o job e o caminho real "
                      "aparecendo em tempo real.",
    "howto_ing_tip_h": "Sobre mover em vez de copiar",
    "howto_ing_tip_p": "O Sincou copia, sempre. Mover apaga a origem antes de "
                       "você ter conferido o destino, e a única hora em que "
                       "isso importa é a hora em que dá errado. Formate o "
                       "cartão você mesmo, depois de ver o relatório.",

    "howto_part2_kicker": "Parte 2",
    "howto_part2_h2": "Do storage para a timeline",
    "howto_part2_lede": "Aqui o som faz o trabalho. Você entrega o material "
                        "bruto e recebe uma timeline com cada câmera na sua "
                        "faixa, o áudio embaixo e o que ficou de fora "
                        "separado.",
    "howto_sync_steps": [
        ("Organize o bruto em pastas por fonte",
         "Uma pasta por câmera, uma por gravador. O Sincou usa a pasta para "
         "saber que aqueles arquivos vieram do mesmo equipamento, e isso "
         "melhora tanto o agrupamento quanto a leitura da timeline. Se o "
         "material já veio do Ingest, a estrutura já está pronta."),
        ("Solte tudo de uma vez",
         "Arraste a pasta da diária inteira. O Sincou faz um reconhecimento "
         "rápido, sem decodificar áudio, e já desenha o material na timeline "
         "com a forma de onda de cada clipe. O resumo no topo diz quantos "
         "clipes, quantas câmeras e quantos gravadores entraram."),
        ("Confira a contagem antes de sincronizar",
         "É o momento barato de perceber que um cartão ficou de fora. Se o "
         "número de câmeras estiver errado, corrija agora: adicionar material "
         "depois significa rodar o sync de novo."),
        ("Aperte Sync",
         "O motor compara as formas de onda de todos os pares plausíveis, "
         "escolhe o melhor alinhamento de cada par e resolve o conjunto "
         "inteiro de uma vez. Ao terminar, os clipes deslizam para a posição "
         "e um som confirma o fim."),
        ("Leia a timeline",
         "Cada linha é uma fonte. As câmeras ficam em cima, os gravadores "
         "embaixo. A distância horizontal entre os blocos é o tempo real "
         "entre as gravações, então o espaço vazio também é informação."),
        ("Ouça antes de exportar",
         "Clique em qualquer ponto e dê play. O Sincou mixa em tempo real "
         "todos os clipes sob o cursor. Alinhado soa como uma fonte só; fora "
         "de sync produz eco. É a conferência mais rápida que existe, e ela "
         "acontece antes de o material chegar no editor."),
        ("Exporte para o seu editor",
         "Escolha o destino no menu Export. Cada opção já traz a instrução de "
         "importação que aquele programa espera, porque cada um deles importa "
         "de um jeito."),
    ],
    "howto_sync_shot1": "O material carregado antes do Sync: cada fonte na sua "
                        "linha, na ordem de gravação.",
    "howto_sync_shot2": "Depois do Sync: os grupos alinhados, o clipe amarelo "
                        "pedindo revisão e o laranja fora do sync.",

    "howto_read_h2": "O que a tela está dizendo",
    "howto_read_lede": "Três coisas carregam informação: as cores, os números "
                       "do rodapé e a posição horizontal.",
    "howto_colors_h": "As cores",
    "howto_colors": [
        ("Roxo, rosa, azul, ciano",
         "Uma cor por fonte. São as câmeras e os gravadores, e a cor se "
         "mantém a mesma do início ao fim da diária."),
        ("Amarelo",
         "Sincronizou, mas com confiança abaixo do limiar de travamento. O "
         "alinhamento provavelmente está certo; vale conferir com o player."),
        ("Laranja",
         "Ficou fora do sync. Nenhuma sobreposição de áudio confiável com o "
         "resto do material. Vai para o fim da timeline, separado."),
    ],
    "howto_numbers_h": "Os números do rodapé",
    "howto_numbers": [
        ("files", "Quantos clipes entraram no total."),
        ("locked", "Alinhados com confiança acima do limiar. Pode confiar."),
        ("review", "Alinhados, mas abaixo do limiar. Confira estes."),
        ("out of sync", "Sem par confiável. Ficaram no fim, em laranja."),
        ("groups", "Blocos de gravação encontrados. Costuma bater com o "
                   "número de tomadas do dia."),
        ("sync time", "Quanto tempo o motor levou."),
    ],
    "howto_thresholds_h": "Se a triagem estiver conservadora demais",
    "howto_thresholds_p": "A engrenagem no topo abre dois limiares. "
                          "<strong>Sync threshold</strong> é o mínimo para o "
                          "Sincou aceitar um alinhamento. <strong>Lock "
                          "threshold</strong> é o mínimo para ele parar de "
                          "pedir revisão. Material com muito ruído de set ou "
                          "sobreposição curta pede um limiar mais baixo; "
                          "material limpo suporta um limiar mais alto.",

    "howto_out_h2": "Quando algo fica de fora",
    "howto_out_lede": "Um clipe em laranja quase sempre tem uma destas causas.",
    "howto_out": [
        ("Não há sobreposição real",
         "O clipe foi gravado quando mais nada estava rodando. Nesse caso o "
         "laranja está certo: não existe com o que sincronizar."),
        ("A sobreposição é curta demais",
         "Poucos segundos em comum produzem correlação que parece boa e não é. "
         "O Sincou pesa a evidência pelo tamanho da sobreposição justamente "
         "para não cair nisso."),
        ("O áudio não tem eventos",
         "Um trecho de silêncio, de vento ou de tom contínuo não dá ao motor "
         "nada para comparar. O alinhamento usa os instantes dos ataques "
         "sonoros, e onde não há ataque não há âncora."),
        ("A câmera gravou sem áudio",
         "Sem faixa de áudio não há sincronização por som. O timecode ainda "
         "pode posicionar o clipe, se existir."),
    ],

    "howto_export_h2": "Como cada editor importa",
    "howto_export": [
        ("Adobe Premiere Pro",
         "Exporte <strong>XML do FCP7</strong> e abra o arquivo pelo Premiere "
         "(File &rsaquo; Open). Ele converte num projeto com as sequências "
         "montadas, a mídia online e o áudio linkado ao vídeo. As pastas do "
         "material bruto viram bins."),
        ("DaVinci Resolve",
         "Exporte <strong>XML do FCP7</strong> e use File &rsaquo; Import "
         "&rsaquo; Timeline. A mídia linka sozinha. Como alternativa, o Sincou "
         "instala um script em Workspace &rsaquo; Scripts que sincroniza o bin "
         "aberto e monta as timelines sem sair do Resolve."),
        ("Final Cut Pro",
         "Exporte <strong>FCPXML</strong> e importe pelo Final Cut. O arquivo "
         "leva as faixas e os offsets do sync."),
        ("Multicam nativo",
         "Ligue <strong>Matching timecode</strong> no menu de exportação. O "
         "Sincou escreve o mesmo timecode para todas as câmeras no XML, e a "
         "função de multicam do seu editor agrupa sozinha. Seus arquivos "
         "originais não são tocados."),
    ],

    "howto_faq_h2": "Dúvidas do caminho",
    "howto_faq": [
        ("Posso rodar só o Ingest, sem sincronizar?",
         "Pode. As duas abas são independentes. Muita gente usa o Ingest na "
         "volta da diária e o Sync só no dia seguinte, já com o material no "
         "storage."),
        ("Posso sincronizar material que não passou pelo Ingest?",
         "Pode. O Sync lê qualquer pasta. O Ingest existe para o caminho do "
         "cartão, e não é pré-requisito."),
        ("O Sincou altera meus arquivos?",
         "Não. Ele lê a mídia e escreve um XML separado. Nem a opção de "
         "igualar timecode toca nos arquivos: o timecode novo vive dentro do "
         "XML."),
        ("Quantas câmeras cabem?",
         "Não há limite fixo. O custo cresce com o número de pares "
         "plausíveis, e uma diária de duas câmeras com dois gravadores e mais "
         "de duzentos clipes roda de uma vez num MacBook."),
        ("E se eu tiver um gravador de várias faixas?",
         "Cada arquivo vira uma fonte. Se o gravador escreve um arquivo por "
         "canal, coloque-os na mesma pasta: o Sincou os trata como o mesmo "
         "equipamento e não tenta sincronizar um contra o outro."),
    ],
    "howto_cta_h": "Pronto para experimentar no seu material?",
    "howto_cta_p": "Sete dias com tudo liberado, sem cadastro.",

    # ================================================ ALTERNATIVA PE ========
    "pe_title": "Alternativa ao PluralEyes para Mac",
    "pe_desc": "O PluralEyes saiu de cena. O Sincou sincroniza a diária pelo "
               "áudio, roda nativo em Apple Silicon e exporta para Premiere, "
               "DaVinci Resolve e Final Cut.",
    "pe_page_eyebrow": "Migração",
    "pe_page_h1": "Uma alternativa ao PluralEyes, feita para os Macs de hoje",
    "pe_page_lede": "Por quase quinze anos, sincronizar multicam por áudio "
                    "queria dizer PluralEyes. O hábito que ele criou continua "
                    "certo: o som que todas as câmeras captaram é a evidência "
                    "mais confiável que existe numa diária. O Sincou parte "
                    "desse mesmo princípio e resolve as partes que "
                    "envelheceram.",

    "pe_why_h2": "O que o PluralEyes acertou, e continua valendo",
    "pe_why": [
        ("O áudio é a fonte da verdade",
         "Claquete falha, timecode livre corre, jam sync se perde. O som que "
         "duas câmeras gravaram do mesmo evento é o mesmo som, e a diferença "
         "entre eles é exatamente o offset. Esse princípio não envelheceu."),
        ("Um botão, a diária inteira",
         "A interface certa para essa tarefa é quase nenhuma interface: "
         "material dentro, timeline fora. O Sincou mantém isso."),
        ("Entregar para o NLE em XML",
         "Trocar timeline por arquivo funciona melhor que plugin instalado "
         "dentro do editor, porque sobrevive à atualização do editor."),
    ],

    "pe_diff_h2": "O que muda no Sincou",
    "pe_diff": [
        ("Nativo em Apple Silicon",
         "O processamento roda direto no seu Mac, sem camada de tradução. "
         "Nada é enviado para nenhum servidor."),
        ("A confiança fica visível",
         "Cada alinhamento carrega uma nota. O Sincou separa o que travou, o "
         "que merece uma conferida e o que ficou de fora, em vez de entregar "
         "tudo com a mesma cara. Um sync errado descoberto na sala de exibição "
         "custa muito mais caro do que um clipe marcado em amarelo."),
        ("Conferência de ouvido embutida",
         "Um player que mixa em tempo real os clipes sob o cursor. Alinhado "
         "soa como uma fonte só."),
        ("O ingest no mesmo aplicativo",
         "Cópia verificada dos cartões, organizada por data, job e câmera. O "
         "programa que sincroniza é o mesmo que sabe de onde o material veio."),
        ("Licença única",
         "Compra uma vez, ativação local, sem assinatura e sem servidor "
         "decidindo se hoje você pode trabalhar."),
    ],

    "pe_move_h2": "Como migrar",
    "pe_move": [
        ("Mantenha suas pastas como estão",
         "Uma pasta por câmera, uma por gravador. É a mesma organização que o "
         "PluralEyes pedia, e o Sincou lê exatamente isso."),
        ("Solte a diária e aperte Sync",
         "Não há projeto para criar nem configuração para acertar antes. Os "
         "limiares têm padrões que funcionam, e ficam a um clique se você "
         "quiser mexer."),
        ("Exporte no formato que você já usava",
         "XML do FCP7 para Premiere e DaVinci Resolve, FCPXML para Final Cut. "
         "São os mesmos formatos que você importava antes."),
    ],
    "pe_page_cta_h": "Traga a próxima diária",
    "pe_page_cta_p": "Sete dias com tudo liberado. Se o fluxo antigo era "
                     "familiar, este vai parecer o mesmo lugar, mais rápido.",

    # ====================================================== NOVIDADES =======
    "wn_title": "Novidades do Sincou",
    "wn_desc": "O que mudou em cada versão do Sincou.",
    "wn_eyebrow": "Registro",
    "wn_h1": "Novidades",
    "wn_lede": "Cada versão e o que ela trouxe. As correções que valem nota "
               "estão aqui também.",
    "wn_releases": [
        ("1.0", "21 de agosto de 2026", "Primeira versão pública", [
            "Sincronização por áudio em dois estágios: envelope de ataques "
            "sonoros para achar o alinhamento e refino por correlação de fase "
            "para chegar ao milissegundo.",
            "Triagem em três estados (travado, revisar, fora do sync), "
            "marcada na timeline e levada para dentro do XML.",
            "Leitura de timecode SMPTE, incluindo drop-frame, usada como "
            "conferência do resultado do áudio.",
            "Detecção de deriva de clock entre equipamentos.",
            "Ingest com cópia verificada, organização por data, job e câmera, "
            "e conferência de espaço antes de escrever o primeiro byte.",
            "Player que mixa em tempo real os clipes sob o cursor.",
            "Exportação para XML do FCP7 (Premiere e DaVinci Resolve), "
            "FCPXML (Final Cut), CSV e JSON.",
            "Script para o DaVinci Resolve, instalado em Workspace &rsaquo; "
            "Scripts, que sincroniza o bin aberto sem sair do programa.",
            "Opção de igualar timecode entre câmeras para usar o multicam "
            "nativo do editor, sem tocar nos arquivos originais.",
            "Interface em português e inglês, com tema claro e escuro.",
        ]),
    ],
    "wn_next_h": "No caminho",
    "wn_next": [
        "Versão para Windows.",
        "Correção de deriva de clock, além da detecção que já existe.",
        "Nome de projeto configurável para os arquivos exportados.",
    ],
    "wn_note": "Datas de itens futuros não são promessa de entrega.",
}
