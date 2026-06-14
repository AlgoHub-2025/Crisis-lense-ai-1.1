# utils/location_extractor.py

import re


class LocationExtractor:

    def __init__(self):

        # Comprehensive Pakistan location database organized by province
        # Each entry: (canonical_name, province, [aliases/alternate_spellings])
        self.location_db = [
            # ══════════════════════════════════════════════
            # KHYBER PAKHTUNKHWA (KPK)
            # ══════════════════════════════════════════════
            ("Peshawar", "KPK", ["peshawar", "peshawer"]),
            ("Swat", "KPK", ["swat", "mingora", "matta", "bahrain swat", "kalam"]),
            ("Chitral", "KPK", ["chitral", "chitral town"]),
            ("Dir", "KPK", ["dir", "upper dir", "lower dir", "dir upper", "dir lower"]),
            ("Mardan", "KPK", ["mardan"]),
            ("Mansehra", "KPK", ["mansehra", "balakot", "shinkiari"]),
            ("Abbottabad", "KPK", ["abbottabad", "abbotabad", "abottabad"]),
            ("Kohistan", "KPK", ["kohistan", "upper kohistan", "lower kohistan", "dasu"]),
            ("Dera Ismail Khan", "KPK", ["dera ismail khan", "d.i. khan", "d.i khan", "di khan", "dik"]),
            ("Nowshera", "KPK", ["nowshera", "noshera", "nowshara"]),
            ("Charsadda", "KPK", ["charsadda", "charsada"]),
            ("Swabi", "KPK", ["swabi"]),
            ("Kohat", "KPK", ["kohat"]),
            ("Bannu", "KPK", ["bannu", "banu"]),
            ("Tank", "KPK", ["tank"]),
            ("Shangla", "KPK", ["shangla", "besham"]),
            ("Buner", "KPK", ["buner", "bunair"]),
            ("Battagram", "KPK", ["battagram", "batagram"]),
            ("Haripur", "KPK", ["haripur", "haripure"]),
            ("Hangu", "KPK", ["hangu"]),
            ("Lakki Marwat", "KPK", ["lakki marwat", "lakki"]),
            ("Karak", "KPK", ["karak"]),
            ("Torghar", "KPK", ["torghar", "tor ghar"]),
            ("Malakand", "KPK", ["malakand"]),

            # ══════════════════════════════════════════════
            # PUNJAB
            # ══════════════════════════════════════════════
            ("Lahore", "Punjab", ["lahore"]),
            ("Rawalpindi", "Punjab", ["rawalpindi", "pindi", "rawalpindi cantonment"]),
            ("Multan", "Punjab", ["multan"]),
            ("Faisalabad", "Punjab", ["faisalabad", "fsd"]),
            ("Sialkot", "Punjab", ["sialkot"]),
            ("Gujranwala", "Punjab", ["gujranwala"]),
            ("Gujrat", "Punjab", ["gujrat"]),
            ("Sargodha", "Punjab", ["sargodha"]),
            ("Bahawalpur", "Punjab", ["bahawalpur"]),
            ("Rahim Yar Khan", "Punjab", ["rahim yar khan", "rahimyar khan", "ryk"]),
            ("DG Khan", "Punjab", ["dg khan", "dera ghazi khan", "d.g. khan", "d.g khan"]),
            ("Muzaffargarh", "Punjab", ["muzaffargarh", "muzafargarh"]),
            ("Rajanpur", "Punjab", ["rajanpur"]),
            ("Jhang", "Punjab", ["jhang"]),
            ("Toba Tek Singh", "Punjab", ["toba tek singh", "toba"]),
            ("Sahiwal", "Punjab", ["sahiwal"]),
            ("Okara", "Punjab", ["okara"]),
            ("Kasur", "Punjab", ["kasur"]),
            ("Sheikhupura", "Punjab", ["sheikhupura"]),
            ("Hafizabad", "Punjab", ["hafizabad"]),
            ("Mandi Bahauddin", "Punjab", ["mandi bahauddin"]),
            ("Jhelum", "Punjab", ["jhelum"]),
            ("Chakwal", "Punjab", ["chakwal"]),
            ("Attock", "Punjab", ["attock"]),
            ("Mianwali", "Punjab", ["mianwali"]),
            ("Khushab", "Punjab", ["khushab"]),
            ("Bhakkar", "Punjab", ["bhakkar"]),
            ("Layyah", "Punjab", ["layyah"]),
            ("Vehari", "Punjab", ["vehari"]),
            ("Lodhran", "Punjab", ["lodhran"]),
            ("Pakpattan", "Punjab", ["pakpattan"]),
            ("Narowal", "Punjab", ["narowal"]),
            ("Chiniot", "Punjab", ["chiniot"]),
            ("Nankana Sahib", "Punjab", ["nankana sahib", "nankana"]),

            # ══════════════════════════════════════════════
            # SINDH
            # ══════════════════════════════════════════════
            ("Karachi", "Sindh", ["karachi", "khi"]),
            ("Hyderabad", "Sindh", ["hyderabad sindh", "hyderabad"]),
            ("Sukkur", "Sindh", ["sukkur", "sukkar"]),
            ("Larkana", "Sindh", ["larkana"]),
            ("Nawabshah", "Sindh", ["nawabshah", "shaheed benazirabad"]),
            ("Mirpur Khas", "Sindh", ["mirpur khas", "mirpurkhas"]),
            ("Thatta", "Sindh", ["thatta"]),
            ("Badin", "Sindh", ["badin"]),
            ("Jacobabad", "Sindh", ["jacobabad"]),
            ("Shikarpur", "Sindh", ["shikarpur"]),
            ("Dadu", "Sindh", ["dadu", "johi"]),
            ("Khairpur", "Sindh", ["khairpur"]),
            ("Sanghar", "Sindh", ["sanghar"]),
            ("Umerkot", "Sindh", ["umerkot", "umarkot"]),
            ("Tharparkar", "Sindh", ["tharparkar", "thar", "mithi"]),
            ("Ghotki", "Sindh", ["ghotki"]),
            ("Kashmore", "Sindh", ["kashmore", "kandhkot"]),
            ("Jamshoro", "Sindh", ["jamshoro"]),
            ("Matiari", "Sindh", ["matiari"]),
            ("Tando Allahyar", "Sindh", ["tando allahyar"]),
            ("Tando Muhammad Khan", "Sindh", ["tando muhammad khan", "tando m khan"]),
            ("Sujawal", "Sindh", ["sujawal"]),

            # ══════════════════════════════════════════════
            # BALOCHISTAN
            # ══════════════════════════════════════════════
            ("Quetta", "Balochistan", ["quetta"]),
            ("Gwadar", "Balochistan", ["gwadar", "gawadar"]),
            ("Turbat", "Balochistan", ["turbat", "kech"]),
            ("Khuzdar", "Balochistan", ["khuzdar"]),
            ("Lasbela", "Balochistan", ["lasbela", "hub", "uthal"]),
            ("Kalat", "Balochistan", ["kalat"]),
            ("Zhob", "Balochistan", ["zhob"]),
            ("Loralai", "Balochistan", ["loralai"]),
            ("Sibi", "Balochistan", ["sibi"]),
            ("Pishin", "Balochistan", ["pishin"]),
            ("Chagai", "Balochistan", ["chagai"]),
            ("Nushki", "Balochistan", ["nushki"]),
            ("Panjgur", "Balochistan", ["panjgur"]),
            ("Awaran", "Balochistan", ["awaran"]),
            ("Barkhan", "Balochistan", ["barkhan"]),
            ("Dera Bugti", "Balochistan", ["dera bugti", "sui"]),
            ("Nasirabad", "Balochistan", ["nasirabad", "dera murad jamali"]),
            ("Jaffarabad", "Balochistan", ["jaffarabad"]),
            ("Jhal Magsi", "Balochistan", ["jhal magsi"]),
            ("Mastung", "Balochistan", ["mastung"]),
            ("Ziarat", "Balochistan", ["ziarat"]),
            ("Harnai", "Balochistan", ["harnai"]),
            ("Musakhel", "Balochistan", ["musakhel", "musa khel"]),
            ("Sherani", "Balochistan", ["sherani"]),
            ("Washuk", "Balochistan", ["washuk"]),

            # ══════════════════════════════════════════════
            # GILGIT-BALTISTAN
            # ══════════════════════════════════════════════
            ("Gilgit", "Gilgit-Baltistan", ["gilgit"]),
            ("Skardu", "Gilgit-Baltistan", ["skardu"]),
            ("Hunza", "Gilgit-Baltistan", ["hunza", "karimabad", "attabad"]),
            ("Nagar", "Gilgit-Baltistan", ["nagar"]),
            ("Ghanche", "Gilgit-Baltistan", ["ghanche", "khaplu"]),
            ("Diamer", "Gilgit-Baltistan", ["diamer", "chilas"]),
            ("Astore", "Gilgit-Baltistan", ["astore"]),
            ("Ghizer", "Gilgit-Baltistan", ["ghizer", "gahkuch"]),
            ("Shigar", "Gilgit-Baltistan", ["shigar"]),

            # ══════════════════════════════════════════════
            # AZAD JAMMU & KASHMIR (AJK)
            # ══════════════════════════════════════════════
            ("Muzaffarabad", "AJK", ["muzaffarabad"]),
            ("Mirpur", "AJK", ["mirpur ajk", "mirpur"]),
            ("Bagh", "AJK", ["bagh"]),
            ("Kotli", "AJK", ["kotli"]),
            ("Rawalakot", "AJK", ["rawalakot", "poonch"]),
            ("Bhimber", "AJK", ["bhimber"]),
            ("Neelum", "AJK", ["neelum", "neelam", "athmuqam"]),
            ("Haveli", "AJK", ["haveli"]),
            ("Sudhanoti", "AJK", ["sudhanoti"]),
            ("Hattian", "AJK", ["hattian"]),

            # ══════════════════════════════════════════════
            # ISLAMABAD CAPITAL TERRITORY
            # ══════════════════════════════════════════════
            ("Islamabad", "Islamabad", ["islamabad", "isb"]),

            # ══════════════════════════════════════════════
            # COMMON LANDMARKS / RIVERS / AREAS
            # ══════════════════════════════════════════════
            ("Indus River", "Sindh", ["indus river", "river indus", "indus"]),
            ("Swat River", "KPK", ["swat river", "river swat"]),
            ("Chenab River", "Punjab", ["chenab river", "river chenab", "chenab"]),
            ("Jhelum River", "Punjab", ["jhelum river", "river jhelum"]),
            ("Kabul River", "KPK", ["kabul river", "river kabul"]),
            ("Ravi River", "Punjab", ["ravi river", "river ravi", "ravi"]),
            ("Sutlej River", "Punjab", ["sutlej river", "river sutlej", "sutlej"]),
            ("Tarbela", "KPK", ["tarbela", "tarbela dam"]),
            ("Mangla", "AJK", ["mangla", "mangla dam"]),
            ("Sukkur Barrage", "Sindh", ["sukkur barrage"]),
            ("Taunsa Barrage", "Punjab", ["taunsa barrage", "taunsa"]),
            ("Guddu Barrage", "Sindh", ["guddu barrage", "guddu"]),

            # ══════════════════════════════════════════════
            # PROVINCE-LEVEL FALLBACK
            # ══════════════════════════════════════════════
            ("KPK", "KPK", ["khyber pakhtunkhwa", "kpk", "k.p.k", "nwfp"]),
            ("Punjab", "Punjab", ["punjab"]),
            ("Sindh", "Sindh", ["sindh"]),
            ("Balochistan", "Balochistan", ["balochistan", "baluchistan"]),
            ("AJK", "AJK", ["azad kashmir", "ajk", "azad jammu"]),
        ]

        # Build a fast lookup: lowercase alias -> (canonical_name, province)
        # Sort by alias length DESC so longer/more-specific names match first
        self.lookup = []
        for canonical, province, aliases in self.location_db:
            for alias in aliases:
                self.lookup.append((alias.lower(), canonical, province))
        self.lookup.sort(key=lambda x: len(x[0]), reverse=True)

    def extract(self, text):
        """Extract the most specific location mentioned in the text."""

        if not text:
            return "Unknown"

        text_lower = text.lower()

        # Try matching the longest (most specific) alias first
        for alias, canonical, province in self.lookup:
            if alias in text_lower:
                return canonical

        return "Unknown"

    def extract_with_province(self, text):
        """Extract location AND province from text."""

        if not text:
            return "Unknown", "Unknown"

        text_lower = text.lower()

        for alias, canonical, province in self.lookup:
            if alias in text_lower:
                return canonical, province

        return "Unknown", "Unknown"


# Global Object
extractor = LocationExtractor()


def extract_location(text):
    return extractor.extract(text)


def extract_location_with_province(text):
    return extractor.extract_with_province(text)