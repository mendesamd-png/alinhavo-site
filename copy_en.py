"""All site copy in English. Same keys as `copy_pt.py`."""

VERSION = "1.0"
UPDATED = "August 21, 2026"

T = {
    # ----------------------------------------------------- navigation ------
    "lang_other": "PT",
    "lang_switch_aria": "View this site in Portuguese",
    "theme_aria": "Switch between light and dark",
    "nav_howto": "How it works",
    "nav_pluraleyes": "From PluralEyes",
    "nav_whatsnew": "What's new",
    "nav_price": "Pricing",
    "nav_download": "Download",
    "nav_eula": "License",
    "nav_terms": "Terms",
    "nav_privacy": "Privacy",
    "nav_refunds": "Refunds",
    "url_howto": "/how-it-works/",
    "url_pluraleyes": "/pluraleyes-alternative/",
    "url_whatsnew": "/whats-new/",
    "url_eula": "/license/",
    "url_terms": "/terms/",
    "url_privacy": "/privacy/",
    "url_refunds": "/refunds/",
    "email": "contato@sincro.app",

    # --------------------------------------------------------- footer ------
    "foot_tagline": "Syncs the whole shoot day by sound, organizes your cards "
                    "and hands your editor a finished timeline.",
    "foot_product": "Product",
    "foot_legal": "Legal",
    "foot_contact": "Contact",
    "foot_req": "macOS 12 Monterey or later · Apple Silicon and Intel · "
                "Windows version in development",
    "made_in": "Made in Brazil",

    # =========================================================== HOME =======
    "home_title": "Sincro",
    "home_desc": "Sync a whole shoot day by sound and import into Premiere, "
                 "DaVinci Resolve or Final Cut with the timeline already "
                 "built. For macOS, one-time license.",
    "hero_h1_a": "The whole shoot day,",
    "hero_h1_b": "synced by sound.",
    "hero_lede": "Drop the camera and recorder folders, press Sync, and import "
                 "the XML into Premiere or DaVinci Resolve. Your footage "
                 "arrives organized, each camera on its own track, ready to cut.",
    "hero_cta": "Download for Mac",
    "hero_cta2": "See how it works",
    "hero_note": "macOS 12+ · Apple Silicon and Intel",
    "stage_clips": "242 clips",
    "stage_srcs": "2 cameras · 2 recorders",
    "stage_dur": "7.6 h of footage",
    "stage_replay": "Sync again",
    "stage_alt": "Clips from two cameras and two recorders sliding from their "
                 "raw positions into their synced positions",

    "stat1_v": "242", "stat1_k": "clips in a real shoot day",
    "stat2_v": "100%", "stat2_k": "linked in Premiere and Resolve",
    "stat3_v": "&le; &frac12;", "stat3_k": "frame of drift, measured through the Resolve API",
    "stat4_v": "0.5 ms", "stat4_k": "engine accuracy on controlled footage",

    "flow_eyebrow": "The flow",
    "flow_h2": "Three steps from card to cut",
    "flow_lede": "The path an assistant would take by hand, done by a machine "
                 "that pays the same attention to clip 1 and clip 242.",
    "flow1_h": "Drop the footage",
    "flow1_p": "Whole folders, mixed frame rates, cameras and recorders "
               "together. Sincro reads the metadata right away and draws the "
               "timeline before analyzing anything.",
    "flow2_h": "Press Sync",
    "flow2_p": "The engine compares waveforms and aligns every clip to the "
               "millisecond. Each pair gets a confidence score, and triage "
               "separates what is locked, what deserves a look, and what fell "
               "outside.",
    "flow3_h": "Export the XML",
    "flow3_p": "A timeline with one track per camera, audio underneath, and "
               "your raw folders turned into bins. Opens in your editor with "
               "media online.",
    "flow_more": "See the full walkthrough",

    "pe_eyebrow": "Continuity",
    "pe_h2": "You already know this flow",
    "pe_lede": "PluralEyes taught a generation of editors to trust sound for "
               "syncing. Sincro follows that path and runs native on today's "
               "Macs.",
    "pe_same_h": "What stays the same",
    "pe_same": ["Drop the whole day and let the audio resolve the alignment",
                "One timeline per recording block, every angle on its own track",
                "XML that opens straight into Premiere and DaVinci Resolve"],
    "pe_new_h": "What Sincro adds",
    "pe_new": ["Native on Apple Silicon, with audio processed on your own Mac",
               "Verified card backup inside the same application",
               "A player to check the sync by ear before exporting",
               "One license, bought once"],
    "pe_more": "Read the full page",

    "feat_eyebrow": "Inside the app",
    "feat_h2": "One window for the whole day",
    "feat_lede": "What usually takes three separate programs happens in one "
                 "place.",
    "feats": [
        ("Mixed rates", "23.976 and 59.94 in the same project",
         "Every file enters the XML at the rate it was shot, which is exactly "
         "what keeps media online when a project mixes cameras."),
        ("Review", "Listen before you export",
         "Click anywhere on the timeline and hit play: Sincro mixes the "
         "cameras under the cursor in real time. Aligned sounds like one "
         "source, and your ear confirms the sync before the footage ever "
         "reaches the NLE."),
        ("Triage", "Three states, one color each",
         "Locked, review and out of sync, marked on the timeline and inside "
         "the XML. You look straight at the few clips that need attention."),
        ("DaVinci Resolve", "Native script included",
         "One command under Workspace &rsaquo; Scripts syncs the open bin and "
         "builds the timelines from inside Resolve, with clips linked to the "
         "Media Pool and triage already colored."),
        ("Timecode", "Matching TC for multicam",
         "On export, Sincro writes the same timecode across every camera and "
         "your editor's native multicam groups them on its own. Your files "
         "stay untouched."),
        ("Privacy", "Everything happens on your Mac",
         "Footage is read from disk, processed on your CPU and handed back as "
         "XML. The support report, when you choose to send one, carries only "
         "numbers and nicknames."),
    ],

    "ing_eyebrow": "Step zero",
    "ing_h2": "The card arrives whole, and you have proof",
    "ing_lede": "Before any syncing comes the most fragile moment of the day: "
                "the footage lives on a single card. Sincro copies it, checks "
                "it byte for byte, and records what happened to every file.",
    "ing_items": [
        ("Byte-for-byte verification",
         "Every file is read back from the destination and compared against "
         "the source. A failing card returns the right size with the wrong "
         "bytes, and reading back is what reveals that while the card is still "
         "in the reader."),
        ("Space checked before the first byte",
         "Sincro adds up what it is about to copy and compares it against the "
         "disk before starting. Finding out the drive is full on file 15 of 63 "
         "is the worst possible moment, so the math comes first."),
        ("Structure built as you type",
         "Pick the date, the job and the camera, and the real path appears on "
         "screen while you type. What you see is literally the folder that "
         "will exist on the drive."),
        ("Errors in plain words, on the file's own line",
         "Disk full, permission denied, failing card. The log states the "
         "reason on the line of the file it happened to, and lifts the "
         "dominant reason to the top, so you know what to fix before trying "
         "again."),
    ],
    "ing_log": "Copy log",
    "ing_copied": "copied and verified",
    "ing_there": "already there",
    "ing_nospace": "no space on destination",
    "ing_foot": "63 files · 61 copied · 1 already there · 1 problem · 248 GB",

    "exp_eyebrow": "Export",
    "exp_h2": "It arrives ready in your editor",
    "exports": [
        ("Adobe Premiere Pro", "FCP7 XML",
         "Open the file in Premiere: media links itself and your raw folders "
         "become organized bins."),
        ("DaVinci Resolve", "FCP7 XML · or native script",
         "File &rsaquo; Import &rsaquo; Timeline and media links itself, the "
         "same way. The included script does the whole path from inside "
         "Resolve."),
        ("Final Cut Pro", "FCPXML",
         "A file in Final Cut's own format, carrying the tracks and the sync "
         "offsets."),
        ("Spreadsheet and data", "CSV · JSON",
         "Offsets, confidence and triage for every clip, to check by eye or "
         "feed your own script."),
    ],

    "price_eyebrow": "License",
    "price_h2": "Buy once, it's yours",
    "price_lede": "A perpetual license with local activation. You install once "
                  "and the app opens every time, online or not.",
    "plan1_name": "Trial",
    "plan1_price": "Free",
    "plan1_unit": "· 7 days",
    "plan1_items": ["Every feature unlocked",
                    "Clean XML, production ready",
                    "Download and open, the trial starts itself"],
    "plan1_cta": "Download for Mac",
    "plan2_name": "Sincro",
    "plan2_price": "$69",
    "plan2_unit": "· one time",
    "plan2_items": ["One license, two computers of your own",
                    "Sync, ingest, player and every export",
                    "DaVinci Resolve script included",
                    "Updates throughout version 1.x"],
    "plan2_cta": "Buy",
    "plan3_name": "Studio",
    "plan3_price": "$179",
    "plan3_unit": "· one time",
    "plan3_items": ["Up to five workstations",
                    "Company invoice",
                    "Priority email support"],
    "plan3_cta": "Get in touch",
    "price_intl": "In Brazil: R$ 349 and R$ 899, with the same contents.",
    "soon_h": "Windows version in development.",
    "soon_p": "The engine already runs cross-platform. The packaged Windows "
              "version comes next.",

    "faq_eyebrow": "Questions",
    "faq_h2": "Before you download",
    "faq": [
        ("Do I need a slate or jam-synced timecode?",
         "Sincro works with the sound your cameras and recorder captured from "
         "the same event, so all it needs is audio on every file. When "
         "timecode exists, it comes in as a cross-check and warns you if it "
         "disagrees with the audio."),
        ("What if the camera audio is bad?",
         "That's the common case, and the engine was built for it. The "
         "comparison uses the instants where sound attacks, which are the same "
         "in any microphone in the room, independent of gain, distance and "
         "frequency response. A second stage then refines the alignment to "
         "sample accuracy."),
        ("Does it work with different frame rates?",
         "Yes. The shoot day used for validation had 23.976 and 59.94 in the "
         "same project, with 48 kHz audio. The XML declares each file at its "
         "own rate, which is what guarantees the link inside the NLE."),
        ("What happens to footage that falls out of sync?",
         "It goes to the end of the timeline, marked in color, separate from "
         "the material that locked. Sincro would rather point at a doubtful "
         "clip than hand you an alignment you'd discover was wrong in the "
         "screening room."),
        ("How many clips can it handle at once?",
         "The heaviest validation so far was a shoot day of 242 clips, 7.6 "
         "hours of footage, two cameras and two recorders, processed in one "
         "pass on a MacBook."),
        ("Do I need to install anything else?",
         "ffmpeg, which handles media reading and is usually already on an "
         "editor's machine. One command installs it: <span class=\"mono\">brew "
         "install ffmpeg</span>."),
        ("Is there a Windows version?",
         "In development. The engine is already cross-platform, and the "
         "packaged Windows version comes next."),
        ("Does my footage go to a server?",
         "Processing is entirely local: the app reads files from your disk and "
         "writes the XML back to it. Everything happens inside your own "
         "machine, offline."),
    ],

    "close_h2": "Your next shoot day can start already assembled.",
    "close_lede": "Download it, drop the folders, and watch the footage fall "
                  "into place.",
    "close_note": "7 days fully unlocked · macOS 12+",
}
