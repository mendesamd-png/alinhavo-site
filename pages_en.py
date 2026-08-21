"""Inner page copy in English. Same keys as `pages_pt.py`."""

P = {
    # =================================================== HOW IT WORKS =======
    "howto_title": "How Alinhavo works",
    "howto_desc": "A walkthrough of Alinhavo: copy cards with verification, sync "
                  "the shoot day by sound, and export the timeline to Premiere, "
                  "DaVinci Resolve or Final Cut.",
    "howto_eyebrow": "Walkthrough",
    "howto_h1": "From the card in the reader to the cut",
    "howto_lede": "Two halves of the same day. The first gets footage off the "
                  "card with proof it arrived whole. The second aligns "
                  "everything by sound and hands you a finished timeline. You "
                  "can use just one of them.",
    "howto_toc": "On this page",

    "howto_part1_kicker": "Part 1",
    "howto_part1_h2": "From card to storage",
    "howto_part1_lede": "The Ingest tab exists because the moment a shoot day "
                        "has only one copy is the moment it can disappear. "
                        "Four steps, and the card leaves the reader with the "
                        "work verified.",
    "howto_ing_steps": [
        ("Pick the destination and name the job",
         "Point at the volume where the footage will live and type the job "
         "name. As you type, Alinhavo shows the real path that will exist on "
         "disk, with the date already in front. What appears on screen is "
         "literally the folder that gets created."),
        ("Drop the cards",
         "Drag in one card, several, or folders you already copied. Alinhavo "
         "reads the whole tree, adds up the volume, and compares it against "
         "the free space on the destination before writing anything."),
        ("Copy with verification",
         "Every file is copied and then read back from the destination to be "
         "compared with the source. This is the step that separates a copy "
         "from a backup: a failing card returns the right size with the wrong "
         "bytes, and only reading back reveals it."),
        ("Read the report",
         "Every line carries a symbol and a state. The footer sums up files, "
         "copied, already there, problems and volume. When something fails, "
         "the reason appears on that file's own line, in plain words, and the "
         "dominant reason rises to the top."),
    ],
    "howto_ing_shot": "The Ingest tab with the destination, the job, and the "
                      "real path appearing in real time.",
    "howto_ing_tip_h": "About moving instead of copying",
    "howto_ing_tip_p": "Alinhavo copies, always. Moving erases the source before "
                       "you have verified the destination, and the one time "
                       "that matters is the time it goes wrong. Format the "
                       "card yourself, after you have seen the report.",

    "howto_part2_kicker": "Part 2",
    "howto_part2_h2": "From storage to timeline",
    "howto_part2_lede": "Here the sound does the work. You hand over raw "
                        "footage and get back a timeline with each camera on "
                        "its own track, audio underneath, and whatever fell "
                        "outside kept separate.",
    "howto_sync_steps": [
        ("Organize the raw footage in folders by source",
         "One folder per camera, one per recorder. Alinhavo uses the folder to "
         "know those files came from the same piece of gear, and that improves "
         "both the grouping and how the timeline reads. If the footage came "
         "through Ingest, the structure is already there."),
        ("Drop it all at once",
         "Drag in the whole shoot day. Alinhavo does a quick pass without "
         "decoding audio and draws the footage on the timeline right away, "
         "waveform included. The summary up top says how many clips, cameras "
         "and recorders came in."),
        ("Check the count before syncing",
         "This is the cheap moment to notice a card got left out. If the "
         "camera count is wrong, fix it now: adding footage later means "
         "running the sync again."),
        ("Press Sync",
         "The engine compares waveforms across every plausible pair, picks the "
         "best alignment for each, and resolves the whole set at once. When it "
         "finishes, the clips slide into position and a chime confirms the end."),
        ("Read the timeline",
         "Each row is a source. Cameras sit on top, recorders underneath. The "
         "horizontal distance between blocks is the real time between "
         "recordings, so empty space carries information too."),
        ("Listen before you export",
         "Click anywhere and hit play. Alinhavo mixes every clip under the "
         "cursor in real time. Aligned sounds like a single source; out of "
         "sync produces echo. It's the fastest check there is, and it happens "
         "before the footage reaches your editor."),
        ("Export to your editor",
         "Pick the destination in the Export menu. Each option carries the "
         "import instruction that program expects, because each of them "
         "imports differently."),
    ],
    "howto_sync_shot1": "Footage loaded before Sync: each source on its own "
                        "row, in recording order.",
    "howto_sync_shot2": "After Sync: groups aligned, the yellow clip asking "
                        "for review and the orange one out of sync.",

    "howto_read_h2": "What the screen is telling you",
    "howto_read_lede": "Three things carry information: the colors, the "
                       "numbers in the footer, and horizontal position.",
    "howto_colors_h": "The colors",
    "howto_colors": [
        ("Purple, pink, blue, cyan",
         "One color per source. These are the cameras and recorders, and the "
         "color stays the same from the first clip of the day to the last."),
        ("Yellow",
         "Synced, but with confidence below the lock threshold. The alignment "
         "is probably right; it's worth a check with the player."),
        ("Orange",
         "Fell out of sync. No trustworthy audio overlap with the rest of the "
         "footage. It goes to the end of the timeline, kept separate."),
    ],
    "howto_numbers_h": "The footer numbers",
    "howto_numbers": [
        ("files", "How many clips came in altogether."),
        ("locked", "Aligned above the confidence threshold. You can trust these."),
        ("review", "Aligned, but below the threshold. Check these."),
        ("out of sync", "No trustworthy pair. They sit at the end, in orange."),
        ("groups", "Recording blocks found. Usually matches the number of "
                   "takes in the day."),
        ("sync time", "How long the engine took."),
    ],
    "howto_thresholds_h": "If triage feels too conservative",
    "howto_thresholds_p": "The gear icon up top opens two thresholds. "
                          "<strong>Sync threshold</strong> is the minimum for "
                          "Alinhavo to accept an alignment at all. <strong>Lock "
                          "threshold</strong> is the minimum for it to stop "
                          "asking for review. Footage with heavy set noise or "
                          "short overlap wants a lower threshold; clean "
                          "footage takes a higher one.",

    "howto_out_h2": "When something falls outside",
    "howto_out_lede": "An orange clip almost always has one of these causes.",
    "howto_out": [
        ("There is no real overlap",
         "The clip was recorded while nothing else was rolling. Here the "
         "orange is correct: there is nothing to sync it against."),
        ("The overlap is too short",
         "A few seconds in common produce correlation that looks good and "
         "isn't. Alinhavo weighs the evidence by how much overlap it had, "
         "precisely to avoid falling for that."),
        ("The audio has no events",
         "A stretch of silence, wind, or continuous tone gives the engine "
         "nothing to compare. Alignment uses the instants where sound attacks, "
         "and where there is no attack there is no anchor."),
        ("The camera recorded without audio",
         "No audio track means no syncing by sound. Timecode can still place "
         "the clip, if it exists."),
    ],

    "howto_export_h2": "How each editor imports",
    "howto_export": [
        ("Adobe Premiere Pro",
         "Export <strong>FCP7 XML</strong> and open the file from Premiere "
         "(File &rsaquo; Open). It converts into a project with the sequences "
         "built, media online, and audio linked to video. Your raw folders "
         "become bins."),
        ("DaVinci Resolve",
         "Export <strong>FCP7 XML</strong> and use File &rsaquo; Import "
         "&rsaquo; Timeline. Media links itself. As an alternative, Alinhavo "
         "installs a script under Workspace &rsaquo; Scripts that syncs the "
         "open bin and builds the timelines without leaving Resolve."),
        ("Final Cut Pro",
         "Export <strong>FCPXML</strong> and import it from Final Cut. The "
         "file carries the tracks and the sync offsets."),
        ("Native multicam",
         "Turn on <strong>Matching timecode</strong> in the export menu. "
         "Alinhavo writes the same timecode across every camera in the XML, and "
         "your editor's multicam feature groups them on its own. Your original "
         "files are never touched."),
    ],

    "howto_faq_h2": "Questions along the way",
    "howto_faq": [
        ("Can I run only Ingest, without syncing?",
         "Yes. The two tabs are independent. Plenty of people run Ingest when "
         "they get back from the shoot and Sync the next day, with the footage "
         "already on storage."),
        ("Can I sync footage that never went through Ingest?",
         "Yes. Sync reads any folder. Ingest exists for the path off the card, "
         "and is not a prerequisite."),
        ("Does Alinhavo change my files?",
         "No. It reads the media and writes a separate XML. Even the matching "
         "timecode option leaves files alone: the new timecode lives inside "
         "the XML."),
        ("How many cameras fit?",
         "There is no fixed limit. Cost grows with the number of plausible "
         "pairs, and a two-camera day with two recorders and more than two "
         "hundred clips runs in one pass on a MacBook."),
        ("What about a multitrack recorder?",
         "Each file becomes a source. If your recorder writes one file per "
         "channel, put them in the same folder: Alinhavo treats them as the same "
         "piece of gear and won't try to sync one against the other."),
    ],
    "howto_cta_h": "Ready to try it on your own footage?",
    "howto_cta_p": "Seven days fully unlocked, no sign-up.",

    # ============================================= PLURALEYES ALTERNATIVE ===
    "pe_title": "PluralEyes alternative for Mac",
    "pe_desc": "PluralEyes is gone. Alinhavo syncs your shoot day by audio, runs "
               "native on Apple Silicon, and exports to Premiere, DaVinci "
               "Resolve and Final Cut.",
    "pe_page_eyebrow": "Migration",
    "pe_page_h1": "A PluralEyes alternative, built for today's Macs",
    "pe_page_lede": "For nearly fifteen years, syncing multicam by audio meant "
                    "PluralEyes. The habit it created still holds: the sound "
                    "every camera captured is the most reliable evidence a "
                    "shoot day has. Alinhavo starts from that same principle and "
                    "fixes the parts that aged.",

    "pe_why_h2": "What PluralEyes got right, and still holds",
    "pe_why": [
        ("Audio is the source of truth",
         "Slates get missed, free-run timecode drifts, jam sync gets lost. The "
         "sound two cameras recorded of the same event is the same sound, and "
         "the difference between them is exactly the offset. That principle "
         "has not aged."),
        ("One button, the whole day",
         "The right interface for this task is almost no interface: footage "
         "in, timeline out. Alinhavo keeps that."),
        ("Hand off to the NLE as XML",
         "Trading timelines as files works better than a plugin installed "
         "inside the editor, because it survives the editor's updates."),
    ],

    "pe_diff_h2": "What changes in Alinhavo",
    "pe_diff": [
        ("Native on Apple Silicon",
         "Processing runs directly on your Mac, with no translation layer. "
         "Nothing is sent to any server."),
        ("Confidence you can see",
         "Every alignment carries a score. Alinhavo separates what locked, what "
         "deserves a look, and what fell outside, instead of handing "
         "everything back looking identical. A bad sync discovered in the "
         "screening room costs far more than a clip flagged in yellow."),
        ("Checking by ear, built in",
         "A player that mixes the clips under the cursor in real time. Aligned "
         "sounds like a single source."),
        ("Ingest in the same application",
         "Verified card copy, organized by date, job and camera. The program "
         "that syncs is the same one that knows where the footage came from."),
        ("One license",
         "Buy once, activate locally, no subscription and no server deciding "
         "whether you get to work today."),
    ],

    "pe_move_h2": "How to move over",
    "pe_move": [
        ("Keep your folders as they are",
         "One folder per camera, one per recorder. It's the same organization "
         "PluralEyes asked for, and exactly what Alinhavo reads."),
        ("Drop the day and press Sync",
         "There is no project to create and no configuration to get right "
         "first. The thresholds ship with defaults that work, and sit one "
         "click away if you want to change them."),
        ("Export in the format you already used",
         "FCP7 XML for Premiere and DaVinci Resolve, FCPXML for Final Cut. "
         "The same formats you were importing before."),
    ],
    "pe_page_cta_h": "Bring your next shoot day",
    "pe_page_cta_p": "Seven days fully unlocked. If the old flow felt "
                     "familiar, this will feel like the same place, faster.",

    # ======================================================== WHAT'S NEW ====
    "wn_title": "What's new in Alinhavo",
    "wn_desc": "What changed in each version of Alinhavo.",
    "wn_eyebrow": "Changelog",
    "wn_h1": "What's new",
    "wn_lede": "Each version and what it brought. Fixes worth noting are here "
               "too.",
    "wn_releases": [
        ("1.0", "August 21, 2026", "First public release", [
            "Two-stage audio sync: an onset envelope to find the alignment and "
            "phase-correlation refinement to land on the millisecond.",
            "Three-state triage (locked, review, out of sync), marked on the "
            "timeline and carried into the XML.",
            "SMPTE timecode reading, drop-frame included, used to cross-check "
            "the audio result.",
            "Clock drift detection between devices.",
            "Ingest with verified copy, organization by date, job and camera, "
            "and a space check before the first byte is written.",
            "A player that mixes the clips under the cursor in real time.",
            "Export to FCP7 XML (Premiere and DaVinci Resolve), FCPXML (Final "
            "Cut), CSV and JSON.",
            "A DaVinci Resolve script, installed under Workspace &rsaquo; "
            "Scripts, that syncs the open bin without leaving the program.",
            "An option to match timecode across cameras so the editor's native "
            "multicam can group them, without touching the original files.",
            "Interface in Portuguese and English, with light and dark themes.",
        ]),
    ],
    "wn_next_h": "On the way",
    "wn_next": [
        "Windows version.",
        "Drift correction, on top of the detection that already exists.",
        "Configurable project name for exported files.",
    ],
    "wn_note": "Dates for future items are not a delivery promise.",
}
