"""Legal documents in English. Same keys as `legal_pt.py`.

DRAFTS. Have a lawyer read them before they stand as contract.
"""

UPDATED = "August 21, 2026"

L = {
    # ============================================================ EULA ======
    "eula_title": "Alinhavo license agreement",
    "eula_desc": "Terms of the Alinhavo software license.",
    "eula_h1": "License agreement",
    "eula_lede": "This document covers what you may do with Alinhavo once it is "
                 "installed. It applies to the trial and to the licensed "
                 "version alike.",
    "eula_body": [
        ("1. What you get", [
            "Installing Alinhavo grants you a personal, perpetual, "
            "non-exclusive license to use the program, version 1.x. The "
            "license is yours to use; the program itself remains ours.",
            "The <strong>Alinhavo</strong> license covers one computer "
            "belonging to the holder. The <strong>Studio</strong> license "
            "covers up to three workstations at the same company. Moving "
            "machines is allowed: deactivate on one and activate on the other.",
            "Activation happens on your computer. Alinhavo works without an "
            "internet connection, and no server exists that could stop "
            "responding and keep you from working.",
        ]),
        ("2. What you produce with it", [
            "Everything Alinhavo outputs is yours: the XML files, the reports, "
            "the copies ingest made. We claim no rights over your footage or "
            "over the results of your work.",
            "You may use Alinhavo on commercial work at no cost beyond the "
            "license.",
        ]),
        ("3. What the license does not allow", [
            "Reselling, renting, sublicensing or distributing the program.",
            "Sharing your license key beyond the machine count you bought.",
            "Removing authorship notices or attempting to bypass activation.",
            "Reverse engineering the program, except to the extent applicable "
            "law grants you that right despite this restriction.",
        ]),
        ("4. Updates", [
            "Updates throughout version 1.x are included. A future 2.0 may be "
            "a paid upgrade; if that happens, your 1.x license keeps working "
            "exactly as it always did.",
        ]),
        ("5. Third-party software", [
            "Alinhavo uses ffmpeg to read media. ffmpeg is free third-party "
            "software and is not distributed inside the application: you "
            "install it separately. It carries its own license.",
        ]),
        ("6. Warranty and limits", [
            "Alinhavo is provided as is. It has been tested against real "
            "production footage and measures its own results, but no sync "
            "software replaces the judgment of the person editing. "
            "<strong>Check the result before committing to a delivery.</strong>",
            "To the maximum extent permitted by applicable law, our liability "
            "for any claim related to the program is limited to what you paid "
            "for the license. This does not remove the consumer rights your "
            "country grants and that cannot be waived by contract.",
        ]),
        ("7. Ending the license", [
            "The license ends if you materially breach these terms and do not "
            "correct it after notice. On termination you must uninstall the "
            "program. The files you already produced remain yours.",
        ]),
        ("8. Governing law", [
            "This license is governed by the laws of the Federative Republic "
            "of Brazil. Consumers outside Brazil keep the mandatory rights of "
            "their own country.",
        ]),
    ],

    # =========================================================== TERMS ======
    "terms_title": "Terms of use",
    "terms_desc": "Terms of use for this site and conditions of sale for "
                  "Alinhavo.",
    "terms_h1": "Terms of use",
    "terms_lede": "These terms cover this website and the purchase of Alinhavo "
                  "licenses. The license for the software itself lives in its "
                  "own document.",
    "terms_body": [
        ("1. This website", [
            "This site presents Alinhavo, distributes the trial, and sells "
            "licenses. By using it, you agree to these terms.",
            "The performance figures published here come from measurements on "
            "real production footage and are described alongside the number. "
            "They report what the program did on that footage, not a guarantee "
            "of identical results on yours.",
        ]),
        ("2. Try before you buy", [
            "The trial runs for seven days with every feature unlocked and no "
            "watermark on the result. It exists so you can verify the program "
            "against your own footage before paying. We recommend using it.",
        ]),
        ("3. Purchase and delivery", [
            "Purchases are handled by our payment processor. The license key "
            "is emailed as soon as payment clears. Delivery is digital and "
            "immediate.",
            "If the key has not arrived within 24 hours, write to {email} with "
            "your receipt and we will sort it out.",
        ]),
        ("4. Prices and taxes", [
            "Prices are shown in Brazilian reais for purchases in Brazil and "
            "in US dollars for international purchases. Applicable taxes may "
            "be added at checkout, depending on your country.",
            "We may change prices at any time. A change never affects "
            "purchases already made.",
        ]),
        ("5. Support", [
            "Support is by email at {email}, in Portuguese and English. Studio "
            "licenses get priority in the queue.",
            "To report a technical problem, the application itself generates "
            "an anonymous report under <em>Export &rsaquo; Something went "
            "wrong</em>. It carries numbers and nicknames, never file names, "
            "paths or media.",
        ]),
        ("6. Changes to these terms", [
            "We may update these terms. The date of the last update sits at "
            "the foot of the document. Material changes apply from publication "
            "and never retroactively to purchases already made.",
        ]),
    ],

    # ========================================================= PRIVACY ======
    "privacy_title": "Privacy",
    "privacy_desc": "What Alinhavo collects and what it never collects. Local "
                    "processing, no footage upload.",
    "privacy_h1": "Privacy",
    "privacy_lede": "The short answer: your footage never leaves your "
                    "computer. The rest of this page explains the little that "
                    "happens outside it.",
    "privacy_body": [
        ("What the application does with your footage", [
            "<strong>Nothing leaves your machine.</strong> Alinhavo reads files "
            "from your disk, processes audio on your CPU, and writes the XML "
            "back to your disk. There is no upload, no account to create, and "
            "no cloud involved in processing.",
            "The application works with the internet switched off. If you want "
            "to confirm, disconnect and run a whole shoot day.",
            "The preferences the app stores (theme, language, thresholds, last "
            "folder used) stay on your own computer, in the system's standard "
            "storage.",
        ]),
        ("The technical report, when you choose to send it", [
            "The export menu has a <em>Something went wrong</em> option that "
            "generates a file to help us understand a problem. That file is "
            "generated on your computer and only reaches us if you send it.",
            "It contains: clip count, durations, frame rates, confidence "
            "scores, error messages, and nicknames in place of names (A1, B2, "
            "R1). It does <strong>not</strong> contain file names, paths, "
            "image, audio, or any part of your footage. An automated test in "
            "our codebase fails if any name leaks into that report.",
        ]),
        ("What this site collects", [
            "The site is static and uses no tracking cookies, no social "
            "network pixels, and no advertising profiles.",
            "Our hosting logs requests (IP address, page, timestamp) as any "
            "server does, for operation and security.",
        ]),
        ("Purchases", [
            "When you buy, payment is processed by a specialized partner. "
            "<strong>We never receive or store your card number.</strong> We "
            "receive your email, to send the key and the receipt, and tax "
            "details when an invoice requires them.",
            "We keep that data for as long as tax law requires.",
        ]),
        ("Your rights", [
            "You may request access to, correction of, or deletion of your "
            "personal data, and ask for a copy in a readable format. Write to "
            "{email} and we will respond within the legal deadline.",
            "In Brazil these rights come from the LGPD (Law 13.709/2018). In "
            "the European Union and the United Kingdom, from the GDPR. Where "
            "both apply, whichever is more favorable to you prevails.",
        ]),
    ],

    # ========================================================= REFUNDS ======
    "refunds_title": "Refunds",
    "refunds_desc": "Alinhavo refund policy: fourteen days, no reason needed.",
    "refunds_h1": "Refunds",
    "refunds_lede": "Try it for seven days before paying. If the purchase "
                    "still doesn't fit, we give the money back.",
    "refunds_body": [
        ("Fourteen days, no reason needed", [
            "You have <strong>14 calendar days</strong> from purchase to "
            "request a full refund. We do not ask why and we attach no "
            "conditions.",
            "That window is longer than the seven-day withdrawal right "
            "Brazilian consumer law guarantees, and matches or exceeds the "
            "European fourteen days. Where your country's law gives more, the "
            "law wins.",
        ]),
        ("How to ask", [
            "Write to {email} from the address you used to buy. There is no "
            "form to fill in and no phone queue to sit through.",
            "We process the request within two business days. The money "
            "returns by the same payment method; how long it takes to appear "
            "on your statement depends on your bank or card issuer.",
        ]),
        ("What happens to the license", [
            "The key is deactivated when the refund is processed. Files you "
            "already produced with the program remain yours, with no "
            "restriction whatsoever.",
        ]),
        ("Why there is a trial period", [
            "Because audio sync depends on the footage. The seven-day trial "
            "exists so you can run your own shoot day before deciding, and "
            "it's the most honest way to find out whether the program suits "
            "your work. Use the trial; the refund is the net underneath.",
        ]),
    ],
}
