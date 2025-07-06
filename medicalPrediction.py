import re

class medicalPrediction:
    def __init__(self, name ,req):
        self.name = name
        self.req = req

    def medSpecialty (self):
        ophthalmology_keywords = [
            "عين", "eye",
            "عيوني", "my eye",
            "الرؤية", "vision",
            "نظر", "sight",
            "نظري", "my vision",
            "ضعف نظر", "poor vision",
            "قصر نظر", "nearsightedness",
            "طول نظر", "farsightedness",
            "عدسات", "lenses",
            "نظارة", "glasses",
            "احمرار العين", "eye redness",
            "التهاب العين", "eye infection",
            "حساسية العين", "eye allergy",
            "حول", "strabismus",
            "جفاف العين", "dry eyes",
            "شبكية", "retina",
            "قرنية", "cornea",
            "العمى", "blindness",
            "فحص نظر", "eye exam",
            "ضغط العين", "eye pressure",
            "كهرباء العين", "eye twitching",
            "نزيف العين", "eye bleeding",
            "نقطة سوداء", "floaters",
            "تشويش", "blurred vision",
            "ظلام", "darkness",
            "إبصار", "seeing",
            "عمى الألوان", "color blindness",
            "تنظيف عدسات", "cleaning lenses"
        ]

        internal_medicine_keywords = [
            "معدة", "stomach",
            "قولون", "colon",
            "كبد", "liver",
            "سكري", "diabetes",
            "ضغط", "blood pressure",
            "دم", "blood",
            "تنفس", "breathing",
            "رئة", "lung",
            "كحة", "cough",
            "حرقة", "heartburn",
            "غثيان", "nausea",
            "قيء", "vomiting",
            "دوخة", "dizziness",
            "صداع", "headache",
            "حساسية", "allergy",
            "تعب", "fatigue",
            "أرق", "insomnia",
            "خمول", "lethargy",
            "غدة", "gland",
            "قلب", "heart",
            "نبض", "pulse",
            "خفقان", "palpitations",
            "حموضة", "acidity",
            "التهاب مزمن", "chronic inflammation",
            "إمساك", "constipation",
            "إسهال", "diarrhea",
            "شهية", "appetite",
            "أمعاء", "intestine",
            "التهاب كبدي", "hepatitis",
            "البلع", "swallowing",
            "فحص دم", "blood test",
            "سعال", "coughing",
            "بول", "urine",
            "انتفاخ", "bloating",
            "حمى", "fever"
        ]

        dentistry_keywords = [
            "اسنان", "teeth",
            "ضرس", "molar",
            "ألم ضرس", "toothache",
            "خلع", "extraction",
            "تسوس", "cavity",
            "تجميل الأسنان", "cosmetic dentistry",
            "ابتسامة", "smile",
            "تلبيسة", "crown",
            "تنظيف", "cleaning",
            "تبييض", "whitening",
            "تقويم", "braces",
            "لثة", "gum",
            "نزيف لثة", "bleeding gums",
            "خراج", "abscess",
            "رائحة الفم", "bad breath",
            "تركيبة", "denture",
            "زرع أسنان", "dental implant",
            "حشوة", "filling",
            "كسر سن", "tooth fracture",
            "طقم أسنان", "dentures",
            "برد الأسنان", "filing teeth",
            "قاطع", "incisor",
            "ناب", "canine",
            "أضراس العقل", "wisdom teeth",
            "نخر", "decay",
            "ألم فم", "mouth pain",
            "فك", "jaw",
            "عصب", "nerve",
            "صبغة سن", "tooth stain",
            "حساسية سن", "tooth sensitivity",
            "رعشة بالأسنان", "teeth shivering"
        ]

        if self.req.strip().lower() in ophthalmology_keywords :
            return f"Hello {self.name} , you must go to the Ophthalmologist"

        elif self.req.strip().lower() in internal_medicine_keywords :
            return f"Hello {self.name} , you must go to the Internist"

        elif self.req.strip().lower() in dentistry_keywords :
            return f"Hello {self.name} , you must go to the Dentist"

        else :
            return f"sorry {self.name} i dont know"




