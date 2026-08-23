"""Documentos legais em português.

RASCUNHOS. São textos redigidos em linguagem clara e cobrem o que este
produto realmente faz, mas precisam de leitura de um advogado antes de
valerem como contrato, principalmente por causa da venda para fora do
Brasil (GDPR) e do regime de tributação.

Os dados da empresa vivem em `ENTITY`, num lugar só.
"""

ENTITY = {
    # A empresa que vende. O endereço ainda falta: a legislação de consumo
    # exige endereço identificável de quem vende à distância, então enquanto
    # `address` estiver vazio o build omite a linha em vez de inventar uma.
    "name": "MS Filmes Ltda",
    "trade": "Mangue Seco Filmes",
    "id": "48.389.938/0001-71",
    "address": "Rua dos Caciques, 414 · Vila da Saúde · São Paulo · SP",
    "email": "contato@sincou.com.br",
}

UPDATED = "21 de agosto de 2026"

L = {
    # ============================================================ EULA ======
    "eula_title": "Licença de uso do Sincou",
    "eula_desc": "Termos da licença de uso do software Sincou.",
    "eula_h1": "Licença de uso",
    "eula_lede": "Este documento diz o que você pode fazer com o Sincou depois "
                 "de instalar. Ele vale para a versão de teste e para a versão "
                 "licenciada.",
    "eula_body": [
        ("1. O que você recebe", [
            "Ao instalar o Sincou você recebe uma licença de uso pessoal, "
            "permanente e não exclusiva do programa, na versão 1.x. A licença "
            "é sua para usar; o programa em si continua sendo nosso.",
            "A licença <strong>Sincou</strong> vale para um computador do "
            "titular. A licença <strong>Estúdio</strong> cobre até três "
            "estações da mesma empresa. Trocar de máquina é permitido: "
            "desative em uma e ative na outra.",
            "A ativação pede conexão uma única vez, para registrar a "
            "máquina e respeitar o limite contratado. Depois disso o "
            "Sincou trabalha sem internet por até 30 dias seguidos entre "
            "uma conferência e outra, e a conferência acontece sozinha "
            "quando houver conexão.",
        ]),
        ("2. O que você produz com ele", [
            "Tudo o que sai do Sincou é seu: os arquivos XML, os relatórios, "
            "as cópias que o ingest fez. Não reivindicamos nenhum direito "
            "sobre o seu material nem sobre o resultado do seu trabalho.",
            "Você pode usar o Sincou em trabalho comercial sem pagar nada "
            "além da licença.",
        ]),
        ("3. O que a licença não permite", [
            "Revender, alugar, sublicenciar ou distribuir o programa.",
            "Compartilhar a sua chave de licença com pessoas fora do limite "
            "de máquinas contratado.",
            "Remover avisos de autoria ou tentar contornar a ativação.",
            "Fazer engenharia reversa do programa, salvo na medida em que a "
            "lei aplicável garanta esse direito apesar desta restrição.",
        ]),
        ("4. Atualizações", [
            "As atualizações da versão 1.x estão incluídas. Uma futura versão "
            "2.0 poderá ser paga; se isso acontecer, a sua licença 1.x "
            "continua funcionando como sempre funcionou.",
        ]),
        ("5. Programas de terceiros", [
            "O Sincou usa o ffmpeg para ler mídia. O ffmpeg é um programa "
            "livre, de terceiros, distribuído dentro do aplicativo sob a "
            "licença LGPL 2.1, em versão compilada sem os componentes GPL. "
            "O texto da licença e o endereço do código-fonte correspondente "
            "acompanham o aplicativo.",
        ]),
        ("6. Garantia e limites", [
            "O Sincou é entregue como está. Ele foi testado com material real "
            "de produção e mede o próprio resultado, mas nenhum software de "
            "sincronização substitui a conferência de quem edita. "
            "<strong>Confira o resultado antes de comprometer uma "
            "entrega.</strong>",
            "Na máxima extensão permitida pela lei aplicável, nossa "
            "responsabilidade por qualquer reclamação relacionada ao programa "
            "fica limitada ao valor que você pagou pela licença. Isso não "
            "afasta os direitos que a legislação de consumo do seu país "
            "garante e que não podem ser afastados por contrato.",
        ]),
        ("7. Fim da licença", [
            "A licença termina se você descumprir estes termos de forma "
            "relevante e não corrigir depois de avisado. Terminando, você deve "
            "desinstalar o programa. Os arquivos que você já produziu "
            "continuam seus.",
        ]),
        ("8. Lei aplicável", [
            "Esta licença é regida pelas leis da República Federativa do "
            "Brasil. Consumidores fora do Brasil mantêm os direitos "
            "obrigatórios do seu próprio país.",
        ]),
    ],

    # =========================================================== TERMOS =====
    "terms_title": "Termos de uso",
    "terms_desc": "Termos de uso do site e condições de venda do Sincou.",
    "terms_h1": "Termos de uso",
    "terms_lede": "Estes termos valem para este site e para a compra de "
                  "licenças do Sincou. A licença do programa em si está em "
                  "documento próprio.",
    "terms_body": [
        ("1. Este site", [
            "Este site apresenta o Sincou, distribui a versão de teste e vende "
            "licenças. Ao usá-lo, você concorda com estes termos.",
            "Os números de desempenho publicados aqui vêm de medições feitas "
            "com material de produção real e estão descritos junto ao número. "
            "Eles indicam o que o programa fez naquele material, e não uma "
            "garantia de resultado idêntico no seu.",
        ]),
        ("2. Teste antes de comprar", [
            "A versão de teste roda por sete dias com todos os recursos "
            "liberados e sem marca no resultado. Ela existe para que você "
            "verifique o programa no seu próprio material antes de pagar. "
            "Recomendamos usar esse período.",
        ]),
        ("3. Compra e entrega", [
            "A compra é feita por meio do nosso processador de pagamentos. A "
            "chave de licença é enviada por e-mail assim que o pagamento é "
            "confirmado. A entrega é digital e imediata.",
            "Se a chave não chegar em até 24 horas, escreva para {email} com "
            "o comprovante e resolvemos.",
        ]),
        ("4. Preços e impostos", [
            "Os preços aparecem em reais para compras no Brasil e em dólares "
            "para compras internacionais. Impostos aplicáveis podem ser "
            "acrescidos no fechamento, conforme o seu país.",
            "Podemos alterar preços a qualquer momento. A alteração não afeta "
            "compras já realizadas.",
        ]),
        ("5. Suporte", [
            "O suporte é feito por e-mail em {email}, em português e inglês. "
            "A licença Estúdio tem prioridade na fila.",
            "Para relatar um problema técnico, o próprio aplicativo gera um "
            "relatório anônimo em <em>Export &rsaquo; Something went "
            "wrong</em>. Ele leva números e apelidos, e nunca nomes de "
            "arquivo, caminhos ou mídia.",
        ]),
        ("6. Alterações destes termos", [
            "Podemos atualizar estes termos. A data da última atualização fica "
            "no rodapé do documento. Mudanças relevantes valem a partir da "
            "publicação e não retroagem sobre compras já feitas.",
        ]),
    ],

    # ====================================================== PRIVACIDADE =====
    "privacy_title": "Privacidade",
    "privacy_desc": "O que o Sincou coleta e o que ele nunca coleta. "
                    "Processamento local, sem upload de mídia.",
    "privacy_h1": "Privacidade",
    "privacy_lede": "A resposta curta: o seu material nunca sai do seu "
                    "computador. O resto desta página explica o pouco que "
                    "acontece fora dele.",
    "privacy_body": [
        ("O que o aplicativo faz com o seu material", [
            "<strong>Nada sai da sua máquina.</strong> O Sincou lê os arquivos "
            "do seu disco, processa o áudio na sua CPU e escreve o XML de "
            "volta no seu disco. Não há upload, não há conta para criar e não "
            "há nuvem envolvida no processamento.",
            "O aplicativo funciona com a internet desligada. Se você quiser "
            "confirmar, desconecte e rode uma diária inteira.",
            "As preferências que o app guarda (tema, idioma, limiares, última "
            "pasta usada) ficam no seu próprio computador, no armazenamento "
            "padrão do sistema.",
        ]),
        ("O relatório técnico, quando você escolhe enviar", [
            "O menu de exportação tem a opção <em>Something went wrong</em>, "
            "que gera um arquivo para nos ajudar a entender um problema. Esse "
            "arquivo é gerado no seu computador e só chega até nós se você o "
            "enviar.",
            "Ele contém: número de clipes, duração, taxas de quadro, notas de "
            "confiança, mensagens de erro e apelidos no lugar dos nomes "
            "(A1, B2, R1). Ele <strong>não</strong> contém nomes de arquivo, "
            "caminhos, imagem, áudio ou qualquer parte da sua mídia. Existe um "
            "teste automatizado no nosso código que falha se algum nome vazar "
            "para esse relatório.",
        ]),
        ("O que este site coleta", [
            "O site é estático e não usa cookies de rastreamento, nem pixels "
            "de rede social, nem perfis de publicidade.",
            "Nossa hospedagem registra acessos (endereço IP, página, horário) "
            "como qualquer servidor faz, para operação e segurança.",
        ]),
        ("Compra", [
            "Quando você compra, o pagamento é processado por um parceiro "
            "especializado. <strong>Não recebemos nem guardamos o número do "
            "seu cartão.</strong> Recebemos o seu e-mail, para enviar a chave "
            "e o comprovante, e os dados fiscais quando a nota exigir.",
            "Guardamos esses dados pelo prazo que a legislação fiscal exige.",
        ]),
        ("Seus direitos", [
            "Você pode pedir acesso, correção ou exclusão dos seus dados "
            "pessoais, e pedir uma cópia deles em formato legível. Escreva "
            "para {email} e respondemos dentro do prazo legal.",
            "No Brasil, esses direitos vêm da LGPD (Lei 13.709/2018). Na "
            "União Europeia e no Reino Unido, do GDPR. Onde os dois se "
            "aplicarem, vale o que for mais favorável a você.",
        ]),
    ],

    # ======================================================== REEMBOLSO =====
    "refunds_title": "Reembolso",
    "refunds_desc": "Política de reembolso do Sincou: quatorze dias, sem "
                    "necessidade de justificar.",
    "refunds_h1": "Reembolso",
    "refunds_lede": "Teste sete dias antes de pagar. Se mesmo assim a compra "
                    "não servir, devolvemos.",
    "refunds_body": [
        ("Quatorze dias, sem precisar justificar", [
            "Você tem <strong>14 dias corridos</strong> a partir da compra "
            "para pedir o reembolso integral. Não pedimos motivo e não "
            "colocamos condição.",
            "O prazo é maior que os sete dias de arrependimento que o Código "
            "de Defesa do Consumidor garante no Brasil, e acompanha os "
            "quatorze dias do direito europeu. Onde a lei do seu país der "
            "mais, vale a lei.",
        ]),
        ("Como pedir", [
            "Escreva para {email} com o e-mail usado na compra. Não é "
            "necessário preencher formulário nem falar com atendimento por "
            "telefone.",
            "Processamos o pedido em até dois dias úteis. O dinheiro volta "
            "pelo mesmo meio de pagamento; o prazo até aparecer no seu extrato "
            "depende do seu banco ou da operadora do cartão.",
        ]),
        ("O que acontece com a licença", [
            "A chave é desativada quando o reembolso é processado. Os arquivos "
            "que você já produziu com o programa continuam seus, sem nenhuma "
            "restrição.",
        ]),
        ("Por que existe um período de teste", [
            "Porque sincronização por áudio depende do material. O teste de "
            "sete dias existe para você rodar a sua própria diária antes de "
            "decidir, e é a forma mais honesta de saber se o programa serve "
            "para o seu trabalho. Use o teste; o reembolso é a rede embaixo.",
        ]),
    ],
}
