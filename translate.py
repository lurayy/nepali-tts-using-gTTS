from translator import sanscript
from translator.sanscript import transliterate

to_script = sanscript.ITRANS
nepali_text = "नेपाली टेक्स्ट"
roman_text = transliterate(nepali_text, sanscript.DEVANAGARI, to_script)
