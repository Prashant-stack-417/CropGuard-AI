"""
42-class crop disease catalogue for Indian agriculture.
Crops: Rice(5), Wheat(5), Tomato(10), Potato(3), Cotton(6), Maize(5), Sugarcane(8)
"""

DISEASE_CATALOGUE: dict[str, dict] = {

    # ─────────────────── RICE (5) ───────────────────

    "rice_bacterial_blight": {
        "name": "Rice Bacterial Blight",
        "crop": "Rice",
        "description": "Bacterial blight (Xanthomonas oryzae pv. oryzae) is one of the most destructive rice diseases, causing water-soaked lesions that turn yellow-white and progress from leaf tips and margins inward.",
        "symptoms": [
            "Water-soaked to yellowish stripes on leaf margins",
            "Lesions enlarge turning white to yellow",
            "Wilting and drying of infected tissues",
            "Kresek phase: complete wilting of young plants",
            "Milky or yellow bacterial ooze from cut tissue",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy infected plant debris",
                "Spray 1% Bordeaux mixture (10 g copper sulphate + 10 g lime per litre)",
                "Apply neem cake @ 250 kg/acre as soil amendment",
            ],
            "chemical": [
                "Copper oxychloride 50% WP @ 3 g/litre — spray at 15-day intervals",
                "Streptocycline 90% SP @ 0.5 g + Copper oxychloride 50% WP @ 3 g per litre",
                "Kasugamycin 3% SL @ 2 ml/litre at early infection stage",
            ],
            "dosage_per_acre": "200–250 litres spray solution per acre",
            "indian_brands": ["Blitox (Bayer)", "Kasu-B (Dhanuka)", "Plantomycin (Aries)"],
        },
        "prevention": [
            "Use certified disease-free seeds",
            "Grow resistant varieties: IR-64, Pusa Basmati-1, ADT-43",
            "Avoid excess nitrogen fertilisation",
            "Maintain proper field drainage",
            "Follow crop rotation with non-host crops",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "rice_brown_spot": {
        "name": "Rice Brown Spot",
        "crop": "Rice",
        "description": "Caused by Bipolaris oryzae, brown spot produces circular to oval brown lesions on leaves, sheaths and grains. It is favoured by nutrient-deficient soils and humid conditions.",
        "symptoms": [
            "Small, circular to oval brown spots with yellow halo on leaves",
            "Lesion centres may be grey or whitish",
            "Heavy infection causes leaf drying",
            "Dark brown discolouration on glumes (grain discolouration)",
            "Seedling blight in nursery",
        ],
        "treatment": {
            "organic": [
                "Seed treatment with Pseudomonas fluorescens @ 10 g/kg seed",
                "Spray 2% neem oil with 0.1% Teepol (spreader)",
                "Foliar spray of 2% potassium silicate to strengthen cell walls",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre — 2–3 sprays at 10-day intervals",
                "Tricyclazole 75% WP @ 0.6 g/litre",
                "Propiconazole 25% EC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Tilt (Syngenta)", "Beam (Dow)"],
        },
        "prevention": [
            "Apply balanced NPK fertilisers, especially potassium and silicon",
            "Use healthy certified seeds",
            "Maintain optimum plant spacing for airflow",
            "Drain water periodically to reduce humidity",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "rice_leaf_smut": {
        "name": "Rice Leaf Smut",
        "crop": "Rice",
        "description": "Caused by Entyloma oryzae, leaf smut produces small, angular, black powdery spots on both surfaces of rice leaves. The disease is relatively mild but can reduce photosynthetic area.",
        "symptoms": [
            "Small angular black spots scattered on leaf surface",
            "Black powdery spore masses visible on spots",
            "Spots surrounded by yellow margin",
            "Mild chlorosis of heavily infected leaves",
        ],
        "treatment": {
            "organic": [
                "Remove and burn infected leaves",
                "Spray 1% Bordeaux mixture",
            ],
            "chemical": [
                "Thiram 75% WP seed treatment @ 3 g/kg seed",
                "Mancozeb 75% WP @ 2 g/litre foliar spray",
            ],
            "dosage_per_acre": "150–200 litres spray solution per acre",
            "indian_brands": ["Captaf (Aries)", "Dithane M-45 (UPL)"],
        },
        "prevention": [
            "Use disease-free seed",
            "Avoid waterlogging in field",
            "Apply recommended doses of fertilisers",
        ],
        "severity": "low",
        "is_healthy": False,
    },

    "rice_neck_blast": {
        "name": "Rice Neck Blast",
        "crop": "Rice",
        "description": "Caused by Magnaporthe oryzae, neck blast attacks the panicle neck node causing it to turn brown and break, leading to partial or complete loss of grain fill (whiteheads).",
        "symptoms": [
            "Brown to black lesion at panicle neck node",
            "Neck breaks easily at infection point",
            "Partial or total whitehead symptom",
            "Grain sterility in affected panicles",
            "Spindle-shaped eye spots on leaves (leaf blast)",
        ],
        "treatment": {
            "organic": [
                "Silicon-rich soil amendment (silica @ 200 kg/acre) to strengthen stems",
                "Seed treatment with Trichoderma viride @ 4 g/kg",
                "Spray 5% fermented butter milk solution at booting stage",
            ],
            "chemical": [
                "Tricyclazole 75% WP @ 0.6 g/litre — spray at booting and heading",
                "Isoprothiolane 40% EC @ 1.5 ml/litre",
                "Azoxystrobin 23% SC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Beam (Dow)", "Fuji-One (Nippon Soda)", "Amistar (Syngenta)"],
        },
        "prevention": [
            "Grow blast-resistant varieties: Improved Samba Mahsuri, ADT-36, CR Dhan 310",
            "Avoid excess nitrogen — split nitrogen application",
            "Maintain field water level to reduce humidity",
            "Early morning dew removal by rope dragging",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "rice_sheath_blight": {
        "name": "Rice Sheath Blight",
        "crop": "Rice",
        "description": "Caused by Rhizoctonia solani, sheath blight is one of the most widespread rice diseases, producing oval to irregular lesions on leaf sheaths with white centres and brown borders.",
        "symptoms": [
            "Oval to irregular greenish-grey watersoaked lesions on sheath",
            "Lesions enlarge with white/grey centre and brown border",
            "Lesions coalesce causing sheath blight",
            "Leaves turn yellow, then brown and die",
            "Sclerotia (brown seed-like structures) on infected tissue",
        ],
        "treatment": {
            "organic": [
                "Apply Pseudomonas fluorescens @ 2.5 kg/acre as soil drench",
                "Trichoderma harzianum application in nursery soil",
                "Avoid dense planting",
            ],
            "chemical": [
                "Hexaconazole 5% EC @ 2 ml/litre",
                "Validamycin 3% L @ 2.5 ml/litre",
                "Propiconazole 25% EC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Contaf (Bayer)", "Sheathmar (Rallis)", "Tilt (Syngenta)"],
        },
        "prevention": [
            "Reduce plant density — avoid transplanting more than 2 seedlings/hill",
            "Drain water at tillering stage to harden plants",
            "Avoid excess nitrogen, especially urea",
            "Remove and destroy crop debris after harvest",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    # ─────────────────── WHEAT (5) ───────────────────

    "wheat_brown_rust": {
        "name": "Wheat Brown Rust",
        "crop": "Wheat",
        "description": "Caused by Puccinia triticina, brown rust (leaf rust) is the most common rust disease of wheat, producing small orange-brown pustules predominantly on the upper leaf surface.",
        "symptoms": [
            "Small, round to oval orange-brown uredia pustules on upper leaf",
            "Chlorotic halo around pustules",
            "Scattered arrangement unlike stem rust",
            "Telia (black pustules) in late season",
            "High infection reduces grain weight",
        ],
        "treatment": {
            "organic": [
                "Garlic extract spray (500 g garlic in 10 litres water) — weekly",
                "Neem oil 2% with spreader",
            ],
            "chemical": [
                "Propiconazole 25% EC @ 1 ml/litre",
                "Tebuconazole 25.9% EC @ 1.5 ml/litre",
                "Mancozeb 75% WP @ 2.5 g/litre as preventive",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Tilt (Syngenta)", "Folicur (Bayer)", "Dithane M-45 (UPL)"],
        },
        "prevention": [
            "Grow resistant varieties: PBW-343, GW-322, HD-2781",
            "Timely sowing (mid-November) to escape peak rust period",
            "Avoid excess nitrogen",
            "Monitor crop regularly from tillering stage",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "wheat_healthy": {
        "name": "Wheat Healthy",
        "crop": "Wheat",
        "description": "The crop is healthy with no signs of disease. Leaves are green, firm and upright with no lesions, pustules or discolouration.",
        "symptoms": [],
        "treatment": {
            "organic": [],
            "chemical": [],
            "dosage_per_acre": None,
            "indian_brands": [],
        },
        "prevention": [
            "Continue balanced fertilisation (NPK as per soil test)",
            "Maintain proper irrigation at critical stages",
            "Scout field regularly for early disease signs",
            "Keep field free of weeds",
        ],
        "severity": "none",
        "is_healthy": True,
    },

    "wheat_loose_smut": {
        "name": "Wheat Loose Smut",
        "crop": "Wheat",
        "description": "Caused by Ustilago tritici, loose smut replaces the grain with a mass of dark olive-brown teliospores. Infection is systemic — the fungus colonises the embryo of seed and erupts at heading.",
        "symptoms": [
            "Entire ear replaced by black smutted mass at heading",
            "Smut spores blown away leaving bare rachis",
            "Infected plants head earlier than healthy plants",
            "Grain formation completely absent",
        ],
        "treatment": {
            "organic": [
                "Hot water seed treatment: soak seed in water at 52°C for 10 minutes",
                "Solar heat treatment: wet seed spread in thin layer under sun",
            ],
            "chemical": [
                "Carboxin 37.5% + Thiram 37.5% WS (Vitavax Power) @ 2.5 g/kg seed",
                "Tebuconazole 2% DS @ 1.5 g/kg seed",
                "Triadimefon 25% WP @ 1 g/kg seed",
            ],
            "dosage_per_acre": "Seed treatment only",
            "indian_brands": ["Vitavax Power (Chemtura)", "Raxil (Bayer)", "Baytan (Bayer)"],
        },
        "prevention": [
            "Use certified disease-free treated seed every season",
            "Grow resistant varieties: Raj-4120, NW-1014",
            "Rogue infected plants before spore dispersal",
            "Avoid saving seed from infected fields",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "wheat_stem_rust": {
        "name": "Wheat Stem Rust",
        "crop": "Wheat",
        "description": "Caused by Puccinia graminis f. sp. tritici, stem rust produces brick-red to dark brown elongated pustules on stems, leaf sheaths and both leaf surfaces. Virulent race Ug99 is a global concern.",
        "symptoms": [
            "Elongated brick-red to brown uredial pustules on stems and sheaths",
            "Pustules rupture epidermis leaving ragged edges",
            "Stems weaken causing lodging",
            "Black teliospores in later season",
            "Severe infection during grain fill causes shrivelled grain",
        ],
        "treatment": {
            "organic": [
                "Early scouting and removal of heavily infected plants",
                "Apply wood ash to soil to improve potassium levels",
            ],
            "chemical": [
                "Propiconazole 25% EC @ 1 ml/litre",
                "Hexaconazole 5% EC @ 2 ml/litre",
                "Tebuconazole 25.9% EC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Tilt (Syngenta)", "Contaf (Bayer)", "Folicur (Bayer)"],
        },
        "prevention": [
            "Grow resistant varieties: HD-2967, K-9107, WH-1142",
            "Early sowing to avoid peak rust temperatures (15–25°C)",
            "Avoid dense sowing",
            "Eradicate alternate host Berberis spp. near fields",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "wheat_yellow_rust": {
        "name": "Wheat Yellow Rust",
        "crop": "Wheat",
        "description": "Also called stripe rust, caused by Puccinia striiformis, this disease produces yellow-orange uredial pustules arranged in stripes along leaf veins. It thrives in cooler, humid conditions.",
        "symptoms": [
            "Yellow to orange pustules arranged in stripes along leaf veins",
            "Chlorotic streaks between pustules",
            "Leaves dry and shred under heavy infection",
            "Pustules appear on glumes and awns at advanced stages",
        ],
        "treatment": {
            "organic": [
                "Spray 2% potassium bicarbonate solution to raise leaf pH",
                "Neem oil 2% + 0.1% spreader weekly",
            ],
            "chemical": [
                "Propiconazole 25% EC @ 1 ml/litre",
                "Trifloxystrobin 25% + Tebuconazole 50% WG @ 0.5 g/litre",
                "Mancozeb 75% WP @ 2.5 g/litre preventive spray",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Tilt (Syngenta)", "Nativo (Bayer)", "Dithane M-45 (UPL)"],
        },
        "prevention": [
            "Grow resistant varieties: PBW-621, HD-3086, HI-8498",
            "Avoid very early sowing",
            "Closely monitor crop at tillering and jointing",
            "Reduce relative humidity by proper spacing",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    # ─────────────────── TOMATO (10) ───────────────────

    "tomato_bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "crop": "Tomato",
        "description": "Caused by Xanthomonas vesicatoria, bacterial spot produces small water-soaked lesions on leaves, stems and fruit that turn dark brown and are surrounded by yellow halos.",
        "symptoms": [
            "Small, water-soaked circular spots on leaves",
            "Spots turn dark brown with yellow halo",
            "Spots with irregular margins on fruit",
            "Raised, scab-like lesions on green fruit",
            "Defoliation under heavy infection",
        ],
        "treatment": {
            "organic": [
                "Spray copper sulphate 1% (Bordeaux mixture) every 7–10 days",
                "Garlic-chilli extract spray (500 g garlic + 250 g chilli per 10 litres)",
            ],
            "chemical": [
                "Copper oxychloride 50% WP @ 3 g/litre",
                "Streptocycline 90% SP @ 0.5 g/litre + Copper oxychloride",
                "Kasugamycin 3% SL @ 2 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Blitox (Bayer)", "Kocide (Dow)", "Kasu-B (Dhanuka)"],
        },
        "prevention": [
            "Use disease-free certified transplants",
            "Avoid overhead irrigation",
            "Remove and destroy infected plant debris",
            "Practice 2-year crop rotation",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_early_blight": {
        "name": "Tomato Early Blight",
        "crop": "Tomato",
        "description": "Caused by Alternaria solani, early blight produces characteristic concentric ring (target-board) lesions on older leaves, stems and fruit. It thrives in warm, humid conditions.",
        "symptoms": [
            "Dark brown spots with concentric rings (target pattern) on old leaves",
            "Yellow halo surrounds lesions",
            "Defoliation from bottom upwards",
            "Dark, sunken lesions at stem end of fruit",
            "Collar rot at soil line of seedlings",
        ],
        "treatment": {
            "organic": [
                "Remove infected lower leaves immediately",
                "Spray 1% Bordeaux mixture",
                "Neem oil 3% + 0.1% wetting agent weekly",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Chlorothalonil 75% WP @ 2 g/litre",
                "Azoxystrobin 23% SC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Kavach (Syngenta)", "Amistar (Syngenta)"],
        },
        "prevention": [
            "Plant resistant varieties: Arka Rakshak, Pusa Ruby",
            "Mulch to prevent soil splash",
            "Use drip irrigation instead of overhead",
            "Maintain proper plant spacing",
            "Apply balanced calcium nutrition",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_healthy": {
        "name": "Tomato Healthy",
        "crop": "Tomato",
        "description": "The crop is healthy with no visible signs of disease. Leaves are dark green, firm and free of lesions, spots or discolouration.",
        "symptoms": [],
        "treatment": {
            "organic": [],
            "chemical": [],
            "dosage_per_acre": None,
            "indian_brands": [],
        },
        "prevention": [
            "Continue regular monitoring for early pest/disease signs",
            "Maintain drip irrigation schedule",
            "Apply balanced fertilisation based on crop stage",
            "Scout for whitefly, thrips, mites weekly",
        ],
        "severity": "none",
        "is_healthy": True,
    },

    "tomato_late_blight": {
        "name": "Tomato Late Blight",
        "crop": "Tomato",
        "description": "Caused by Phytophthora infestans, late blight is a devastating disease that can destroy entire fields within days under cool, moist conditions. Water-soaked lesions rapidly turn brown-black.",
        "symptoms": [
            "Large water-soaked, irregular dark green-brown lesions on leaves",
            "White sporulation (fuzzy growth) on underside of lesions",
            "Rapid browning and death of affected tissue",
            "Dark brown to black greasy lesions on fruit",
            "Entire plant can collapse within 2–3 days",
        ],
        "treatment": {
            "organic": [
                "Spray 1% Bordeaux mixture as preventive",
                "Remove and destroy infected plant material immediately",
                "Spray potassium bicarbonate 5 g/litre",
            ],
            "chemical": [
                "Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/litre",
                "Cymoxanil 8% + Mancozeb 64% WP @ 3 g/litre",
                "Propamocarb 72.2% SL @ 2.5 ml/litre",
            ],
            "dosage_per_acre": "200–250 litres spray solution per acre",
            "indian_brands": ["Ridomil Gold (Syngenta)", "Curzate (DuPont)", "Previcur (Bayer)"],
        },
        "prevention": [
            "Avoid late planting during monsoon/cool humid period",
            "Ensure good air circulation with proper staking",
            "Avoid overhead irrigation",
            "Scout daily when weather is cool and wet",
            "Use resistant varieties where available",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "tomato_leaf_mold": {
        "name": "Tomato Leaf Mold",
        "crop": "Tomato",
        "description": "Caused by Passalora fulva (syn. Cladosporium fulvum), leaf mold primarily affects greenhouse tomatoes. Pale yellow patches appear on upper leaf surface with olive-green to brown mold beneath.",
        "symptoms": [
            "Pale yellow-green patches on upper leaf surface",
            "Olive-green to brown velvety mold on lower leaf surface",
            "Leaves curl upward and wither",
            "Fruit infection rare but results in leathery black lesions",
        ],
        "treatment": {
            "organic": [
                "Improve ventilation to reduce humidity below 85%",
                "Remove and destroy infected leaves",
                "Spray 2% baking soda (sodium bicarbonate) solution",
            ],
            "chemical": [
                "Chlorothalonil 75% WP @ 2 g/litre",
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Myclobutanil 10% WP @ 1 g/litre",
            ],
            "dosage_per_acre": "150–200 litres spray solution per acre",
            "indian_brands": ["Kavach (Syngenta)", "Dithane M-45 (UPL)", "Index (Aries)"],
        },
        "prevention": [
            "Grow resistant varieties",
            "Maintain greenhouse humidity below 85%",
            "Space plants adequately for airflow",
            "Avoid wetting leaves during irrigation",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "crop": "Tomato",
        "description": "Tomato Mosaic Virus (ToMV) causes mottled light and dark green patterns on leaves, leaf distortion and stunting. It spreads through contact with contaminated tools, hands and infected plant material.",
        "symptoms": [
            "Mosaic (mottled light-dark green) pattern on leaves",
            "Leaf curling and distortion",
            "Plant stunting",
            "Reduced fruit set and deformed fruit",
            "Internal browning of fruit in some strains",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy infected plants",
                "Spray neem oil 5% to control aphid vectors",
                "Wash tools with soap water between plants",
            ],
            "chemical": [
                "No curative chemical available for viruses",
                "Control aphid vectors: Imidacloprid 17.8% SL @ 0.5 ml/litre",
                "Thiamethoxam 25% WG @ 0.4 g/litre for vector control",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Confidor (Bayer)", "Actara (Syngenta)"],
        },
        "prevention": [
            "Use ToMV-resistant varieties: Pusa Hybrid-4, Arka Rakshak",
            "Disinfect tools with 10% bleach or 70% alcohol",
            "Wash hands before handling plants",
            "Control aphids and thrips with systemic insecticides",
            "Remove rogues immediately",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_septoria_leaf_spot": {
        "name": "Tomato Septoria Leaf Spot",
        "crop": "Tomato",
        "description": "Caused by Septoria lycopersici, septoria leaf spot produces numerous small circular spots with white centres and dark borders, mainly on lower leaves. Severe infection causes defoliation.",
        "symptoms": [
            "Numerous small, circular spots (3–6 mm) with light grey/white centres",
            "Dark brown margins around spots",
            "Tiny black dots (pycnidia) visible in lesion centres",
            "Progressive defoliation from lower leaves upward",
            "No fruit infection",
        ],
        "treatment": {
            "organic": [
                "Remove infected lower leaves promptly",
                "Spray copper-based fungicide (Bordeaux mixture 1%)",
                "Mulch soil to prevent spore splash",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Chlorothalonil 75% WP @ 2 g/litre",
                "Copper oxychloride 50% WP @ 3 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Kavach (Syngenta)", "Blitox (Bayer)"],
        },
        "prevention": [
            "Use certified disease-free seed",
            "Apply mulch to reduce soil splash",
            "Stake plants for good air circulation",
            "Avoid working in wet fields",
            "Crop rotation with non-solanaceous crops",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_spider_mites": {
        "name": "Tomato Spider Mites",
        "crop": "Tomato",
        "description": "Two-spotted spider mite (Tetranychus urticae) causes stippling, bronzing and webbing on tomato leaves. Severe infestations lead to leaf scorch and significant yield loss in dry conditions.",
        "symptoms": [
            "Fine stippling (tiny white/yellow dots) on upper leaf surface",
            "Bronzing or silvering of affected leaves",
            "Fine webbing on undersides of leaves",
            "Tiny red-brown mites visible with hand lens",
            "Leaf drop under severe infestation",
        ],
        "treatment": {
            "organic": [
                "Spray neem oil 3% + 0.1% spreader every 5–7 days",
                "Spray soap solution (5 g soap per litre) under leaf surface",
                "Release predatory mites: Phytoseiulus persimilis",
            ],
            "chemical": [
                "Abamectin 1.9% EC @ 0.5 ml/litre",
                "Hexythiazox 5.45% EC @ 1 ml/litre",
                "Spiromesifen 22.9% SC @ 1 ml/litre",
                "Fenazaquin 10% EC @ 2 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Vertimec (Syngenta)", "Nissoran (Bayer)", "Oberon (Bayer)", "Magister (Aries)"],
        },
        "prevention": [
            "Avoid excess nitrogen that promotes soft growth",
            "Maintain adequate soil moisture with irrigation",
            "Avoid broad-spectrum insecticide overuse (kills predators)",
            "Remove heavily infested leaves and destroy",
            "Monitor undersides of leaves regularly",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_target_spot": {
        "name": "Tomato Target Spot",
        "crop": "Tomato",
        "description": "Caused by Corynespora cassiicola, target spot produces concentric ring lesions similar to early blight but also affects fruit heavily. It is increasingly common in warm, humid regions of India.",
        "symptoms": [
            "Circular spots with concentric rings on leaves",
            "Small, dark brown spots on young fruit enlarging to sunken lesions",
            "Lesions may coalesce causing large necrotic areas",
            "Affected fruit may have water-soaked appearance",
        ],
        "treatment": {
            "organic": [
                "Remove infected leaves and destroy",
                "Spray Bordeaux mixture 1%",
            ],
            "chemical": [
                "Azoxystrobin 23% SC @ 1 ml/litre",
                "Difenoconazole 25% EC @ 0.5 ml/litre",
                "Fluopyram 17.35% + Tebuconazole 17.35% SC @ 0.5 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Amistar (Syngenta)", "Score (Syngenta)", "Luna Experience (Bayer)"],
        },
        "prevention": [
            "Ensure good canopy management",
            "Avoid high humidity by proper spacing",
            "Rotate with non-host crops",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "tomato_yellow_leaf_curl": {
        "name": "Tomato Yellow Leaf Curl Virus",
        "crop": "Tomato",
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV), transmitted by whitefly Bemisia tabaci, causes severe stunting, leaf curling and yellowing. It is one of the most economically destructive tomato diseases in India.",
        "symptoms": [
            "Upward curling and yellowing of leaflets",
            "Leaves crinkle and become thickened",
            "Severe stunting of the entire plant",
            "Marked reduction in fruit set",
            "Abundant whiteflies on leaf undersides",
        ],
        "treatment": {
            "organic": [
                "No cure — remove and destroy infected plants early",
                "Yellow sticky traps @ 10 traps/acre to monitor whiteflies",
                "Spray neem oil 3% to repel whitefly",
            ],
            "chemical": [
                "Imidacloprid 70% WS seed treatment @ 5 g/kg seed",
                "Thiamethoxam 25% WG @ 0.3 g/litre foliar spray",
                "Spirotetramat 11.01% + Imidacloprid 11.01% SC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Gaucho (Bayer)", "Actara (Syngenta)", "Movento Combi (Bayer)"],
        },
        "prevention": [
            "Grow TYLCV-resistant varieties: CARI Tomato-1, Arka Rakshak, NS-585",
            "Cover nursery with 40-mesh nylon insect-proof net",
            "Reflective mulch to repel whiteflies",
            "Rogue infected plants immediately",
            "Control whitefly with systemic insecticides",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    # ─────────────────── POTATO (3) ───────────────────

    "potato_early_blight": {
        "name": "Potato Early Blight",
        "crop": "Potato",
        "description": "Caused by Alternaria solani, early blight produces dark brown concentric ring lesions on older leaves and can cause severe defoliation and reduced tuber yield.",
        "symptoms": [
            "Dark brown to black spots with concentric rings on older leaves",
            "Yellow halo around lesions",
            "Progressive defoliation from base upward",
            "Dark, sunken lesions with concentric rings on tubers",
            "Collar rot at soil line",
        ],
        "treatment": {
            "organic": [
                "Remove infected lower leaves",
                "Spray 1% Bordeaux mixture at 10-day intervals",
                "Neem oil 3% spray",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Chlorothalonil 75% WP @ 2 g/litre",
                "Difenoconazole 25% EC @ 0.5 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Kavach (Syngenta)", "Score (Syngenta)"],
        },
        "prevention": [
            "Use certified disease-free seed tubers",
            "Use resistant varieties: Kufri Bahar, Kufri Jyoti",
            "Maintain soil fertility and balanced nutrition",
            "Avoid overhead irrigation",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "potato_healthy": {
        "name": "Potato Healthy",
        "crop": "Potato",
        "description": "The crop is healthy with no signs of disease. Foliage is green and vigorous with no lesions, wilting or discolouration.",
        "symptoms": [],
        "treatment": {
            "organic": [],
            "chemical": [],
            "dosage_per_acre": None,
            "indian_brands": [],
        },
        "prevention": [
            "Keep monitoring for late blight especially during cool, moist weather",
            "Maintain earthing-up schedule",
            "Scout for aphids and whiteflies weekly",
        ],
        "severity": "none",
        "is_healthy": True,
    },

    "potato_late_blight": {
        "name": "Potato Late Blight",
        "crop": "Potato",
        "description": "Caused by Phytophthora infestans, potato late blight is the most destructive potato disease, capable of destroying entire fields within days. It caused the Irish famine of 1845.",
        "symptoms": [
            "Dark, water-soaked lesions on leaves and stems",
            "White, sporulating growth on leaf undersides",
            "Lesions turn brown-black and dry under hot weather",
            "Brown to purple firm lesions on tubers extending into flesh",
            "Entire plant collapse within a week in wet conditions",
        ],
        "treatment": {
            "organic": [
                "Spray 1% Bordeaux mixture as prophylactic in cool weather",
                "Remove and destroy infected haulm immediately",
            ],
            "chemical": [
                "Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/litre",
                "Cymoxanil 8% + Mancozeb 64% WP @ 3 g/litre",
                "Fenamidone 10% + Mancozeb 50% WG @ 3 g/litre",
            ],
            "dosage_per_acre": "200–250 litres spray solution per acre",
            "indian_brands": ["Ridomil Gold (Syngenta)", "Curzate M (DuPont)", "Sectin (Bayer)"],
        },
        "prevention": [
            "Use certified disease-free seed tubers from cold storage",
            "Grow tolerant varieties: Kufri Girdhari, Kufri Frysona",
            "Avoid late planting in plains",
            "Ensure good drainage in the field",
            "Spray protectant fungicide before onset of cool, wet periods",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    # ─────────────────── COTTON (6) ───────────────────

    "cotton_bacterial_blight": {
        "name": "Cotton Bacterial Blight",
        "crop": "Cotton",
        "description": "Caused by Xanthomonas axonopodis pv. malvacearum, bacterial blight produces angular water-soaked lesions on leaves, stem cankers and systemic blackarm on bolls and stems.",
        "symptoms": [
            "Angular water-soaked spots on leaves limited by veins",
            "Spots turn dark brown to black with yellow halo",
            "Vein blackening and blighting",
            "Blackarm — dark sunken cankers on stems and petioles",
            "Dark, water-soaked lesions on bolls",
        ],
        "treatment": {
            "organic": [
                "Seed treatment with streptomycin @ 0.25 g + water",
                "Spray 1% Bordeaux mixture at 15-day intervals",
            ],
            "chemical": [
                "Streptocycline 90% SP @ 0.5 g + Copper oxychloride @ 3 g/litre",
                "Copper hydroxide 77% WP @ 3 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Plantomycin (Aries)", "Kocide (Dow)"],
        },
        "prevention": [
            "Use disease-free, acid-delinted certified seed",
            "Grow resistant varieties: NH-615, G.Cot-Hy-8",
            "Avoid field entry when plants are wet",
            "Crop rotation with sorghum or soybean",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "cotton_curl_virus": {
        "name": "Cotton Leaf Curl Virus",
        "crop": "Cotton",
        "description": "Cotton Leaf Curl Disease (CLCuD) is caused by a begomovirus complex transmitted by whitefly Bemisia tabaci. It is a serious threat to cotton production in Punjab, Haryana and Rajasthan.",
        "symptoms": [
            "Upward curling of leaves",
            "Leaf veins thicken and turn dark — vein swelling",
            "Leaf enations (cup-shaped outgrowths) on underside",
            "Stunted plants with reduced boll setting",
            "Abundant whiteflies on undersides",
        ],
        "treatment": {
            "organic": [
                "No cure for viral infection",
                "Remove infected plants immediately",
                "Yellow sticky traps @ 12/acre for whitefly monitoring",
            ],
            "chemical": [
                "Imidacloprid 70% WS seed treatment @ 5 g/kg seed",
                "Thiamethoxam 25% WG @ 0.5 g/litre foliar spray",
                "Diafenthiuron 50% WP @ 1.5 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Gaucho (Bayer)", "Actara (Syngenta)", "Polo (Syngenta)"],
        },
        "prevention": [
            "Grow tolerant Bt cotton varieties: Bollgard-II + CLCuD tolerance",
            "Control whitefly from seedling stage",
            "Rogue infected plants before virus spreads",
            "Spray systemic insecticides at 15-day intervals",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "cotton_fusarium_wilt": {
        "name": "Cotton Fusarium Wilt",
        "crop": "Cotton",
        "description": "Caused by Fusarium oxysporum f. sp. vasinfectum, fusarium wilt invades the vascular system causing yellowing, wilting and death of cotton plants. It persists in soil for many years.",
        "symptoms": [
            "Yellowing starting from lower leaves",
            "Wilting of entire plant or single branches",
            "Brown discolouration of vascular tissue when stem cut",
            "Stunted growth and premature boll opening",
            "Taproot and lateral roots show brown rot",
        ],
        "treatment": {
            "organic": [
                "Seed treatment with Trichoderma viride @ 4 g/kg seed",
                "Soil drenching with T. viride @ 2.5 kg/acre in 200 litres",
                "Apply neem cake @ 250 kg/acre to suppress pathogen",
            ],
            "chemical": [
                "Carbendazim 50% WP seed treatment @ 2 g/kg",
                "Thiophanate methyl 70% WP @ 1 g/litre soil drench",
            ],
            "dosage_per_acre": "200–250 litres soil drench per acre",
            "indian_brands": ["Bavistin (BASF)", "Roko (Rallis)"],
        },
        "prevention": [
            "Grow resistant varieties: Suraj, G.Cot-Hy-4",
            "Avoid planting in fields with known wilt history",
            "Deep summer ploughing to expose and kill fungus",
            "Maintain soil pH 6.5–7.0",
            "Crop rotation with cereals",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "cotton_grey_mildew": {
        "name": "Cotton Grey Mildew",
        "crop": "Cotton",
        "description": "Caused by Ramularia areola, grey mildew produces angular pale-green spots on leaves that develop greyish white mold on the lower surface. It is rampant in rainy seasons.",
        "symptoms": [
            "Angular pale-green to yellow spots on upper leaf surface",
            "Greyish-white powdery growth on underside of spots",
            "Spots turn reddish-brown to grey",
            "Defoliation under heavy infection",
            "Reduction in boll size",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy infected leaves",
                "Spray copper-based fungicide preventively",
            ],
            "chemical": [
                "Carbendazim 50% WP @ 1 g/litre",
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Thiophanate methyl 70% WP @ 1.5 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Bavistin (BASF)", "Dithane M-45 (UPL)", "Roko (Rallis)"],
        },
        "prevention": [
            "Proper spacing for air circulation",
            "Timely defoliation sprays before harvest",
            "Balance nitrogen fertilisation",
        ],
        "severity": "low",
        "is_healthy": False,
    },

    "cotton_healthy": {
        "name": "Cotton Healthy",
        "crop": "Cotton",
        "description": "The crop is healthy with no visible disease. Plants show normal dark-green foliage, good branching and boll development.",
        "symptoms": [],
        "treatment": {
            "organic": [],
            "chemical": [],
            "dosage_per_acre": None,
            "indian_brands": [],
        },
        "prevention": [
            "Monitor regularly for bollworm, whitefly and mites",
            "Apply scheduled fertiliser doses",
            "Maintain drip/furrow irrigation schedule",
        ],
        "severity": "none",
        "is_healthy": True,
    },

    "cotton_leaf_spot": {
        "name": "Cotton Leaf Spot",
        "crop": "Cotton",
        "description": "Caused by Cercospora gossypina, Alternaria spp. and other fungi, leaf spot diseases produce various-sized brown spots on cotton leaves causing premature defoliation and reduced yield.",
        "symptoms": [
            "Brown to reddish-brown spots of varying sizes on leaves",
            "Concentric rings may be visible in some spots",
            "Spots may coalesce to form large necrotic patches",
            "Premature leaf drop",
            "Reduced boll retention",
        ],
        "treatment": {
            "organic": [
                "Spray 1% Bordeaux mixture",
                "Neem oil 2% + 0.1% spreader spray",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Copper oxychloride 50% WP @ 3 g/litre",
                "Propiconazole 25% EC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Blitox (Bayer)", "Tilt (Syngenta)"],
        },
        "prevention": [
            "Balanced fertilisation avoiding excess nitrogen",
            "Regular field scouting from 40 DAS",
            "Remove and compost fallen leaves",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    # ─────────────────── MAIZE (5) ───────────────────

    "maize_cercospora_leaf_spot": {
        "name": "Maize Grey Leaf Spot (Cercospora)",
        "crop": "Maize",
        "description": "Caused by Cercospora zeae-maydis and C. zeina, grey leaf spot produces rectangular lesions limited by leaf veins that turn tan to grey under humid conditions.",
        "symptoms": [
            "Rectangular lesions limited by leaf veins — light brown initially",
            "Lesions turn grey to tan with distinct margins",
            "Lesions run parallel to leaf veins",
            "Severe infection causes leaf blight and lodging",
            "Disease progresses from lower leaves upward",
        ],
        "treatment": {
            "organic": [
                "Remove lower infected leaves",
                "Spray neem oil 2% + 0.1% spreader",
            ],
            "chemical": [
                "Propiconazole 25% EC @ 1 ml/litre",
                "Azoxystrobin 23% SC @ 1 ml/litre",
                "Mancozeb 75% WP @ 2.5 g/litre preventive",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Tilt (Syngenta)", "Amistar (Syngenta)", "Dithane M-45 (UPL)"],
        },
        "prevention": [
            "Grow resistant hybrids: DKC 9144, Pioneer P3396",
            "Crop rotation with soybean or wheat",
            "Avoid excess plant density",
            "Minimum tillage to reduce debris breakdown time",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "maize_common_rust": {
        "name": "Maize Common Rust",
        "crop": "Maize",
        "description": "Caused by Puccinia sorghi, common rust produces cinnamon-brown uredial pustules scattered on both leaf surfaces. It is most severe in cool, humid areas.",
        "symptoms": [
            "Scattered cinnamon to brick-red uredial pustules on both leaf surfaces",
            "Pustules oval to elongated",
            "Yellow chlorotic patches around pustule clusters",
            "Black teliospores develop late season",
            "Severe infection causes premature drying",
        ],
        "treatment": {
            "organic": [
                "Remove heavily infected leaves",
                "Spray neem oil 3% weekly",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Propiconazole 25% EC @ 1 ml/litre",
                "Tebuconazole 25.9% EC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Tilt (Syngenta)", "Folicur (Bayer)"],
        },
        "prevention": [
            "Plant rust-resistant hybrids",
            "Early sowing to avoid humid, cool conditions",
            "Balanced potassium application",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "maize_healthy": {
        "name": "Maize Healthy",
        "crop": "Maize",
        "description": "The crop is healthy with dark green, upright leaves and no signs of disease.",
        "symptoms": [],
        "treatment": {
            "organic": [],
            "chemical": [],
            "dosage_per_acre": None,
            "indian_brands": [],
        },
        "prevention": [
            "Scout regularly for fall armyworm, shoot fly and rust",
            "Apply recommended NPK doses at sowing and topdressing",
            "Maintain adequate soil moisture at tasselling",
        ],
        "severity": "none",
        "is_healthy": True,
    },

    "maize_northern_leaf_blight": {
        "name": "Maize Northern Leaf Blight",
        "crop": "Maize",
        "description": "Caused by Setosphaeria turcica (anamorph: Exserohilum turcicum), Northern Leaf Blight produces long, cigar-shaped grey-green to tan lesions that can cause significant yield loss.",
        "symptoms": [
            "Elliptical/cigar-shaped lesions 5–15 cm long on leaves",
            "Lesions grey-green initially, turning tan/grey with age",
            "Dark sporulation visible in lesion centre under humidity",
            "Disease progresses from lower leaves upward",
            "Multiple lesions coalesce causing blighting",
        ],
        "treatment": {
            "organic": [
                "Remove infected lower leaves early",
                "Spray Bordeaux mixture 1%",
            ],
            "chemical": [
                "Propiconazole 25% EC @ 1 ml/litre",
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Azoxystrobin + Cyproconazole SC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Tilt (Syngenta)", "Dithane M-45 (UPL)", "Amistar Top (Syngenta)"],
        },
        "prevention": [
            "Grow resistant hybrids: DHM-117, HQPM-7",
            "Crop rotation with legumes or wheat",
            "Deep ploughing to bury infected debris",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "maize_southern_leaf_blight": {
        "name": "Maize Southern Leaf Blight",
        "crop": "Maize",
        "description": "Caused by Cochliobolus heterostrophus (Bipolaris maydis), southern leaf blight produces elongated lesions restricted between leaf veins, more common in warm humid lowland areas.",
        "symptoms": [
            "Tan to brown rectangular lesions between veins",
            "Lesions have distinctive tan colour with brown borders",
            "Entire leaf can be killed under heavy infection",
            "Dark sporulation on lesion surface in humidity",
        ],
        "treatment": {
            "organic": [
                "Rotate with non-host crops",
                "Remove and destroy crop debris",
            ],
            "chemical": [
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Propiconazole 25% EC @ 1 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Dithane M-45 (UPL)", "Tilt (Syngenta)"],
        },
        "prevention": [
            "Use resistant hybrids",
            "Ensure proper drainage in the field",
            "Avoid late sowing in humid areas",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    # ─────────────────── SUGARCANE (8) ───────────────────

    "sugarcane_bacterial_blight": {
        "name": "Sugarcane Bacterial Blight",
        "crop": "Sugarcane",
        "description": "Caused by Xanthomonas albilineans, leaf scald/bacterial blight produces creamy to white stripes along leaves, pencil-line symptoms and scalding. It is transmitted through contaminated cutting knives.",
        "symptoms": [
            "One or more cream-white pencil-line stripes along leaf length",
            "Leaf scalding — rapid drying of leaves",
            "Chlorotic and necrotic streaks on leaves",
            "Ratoon stunting in severe cases",
            "Internal discolouration (red) in vascular bundles",
        ],
        "treatment": {
            "organic": [
                "Hot water treatment of setts @ 50°C for 2–3 hours",
                "Disinfect cutting knives with 1% mercuric chloride / bleach",
            ],
            "chemical": [
                "No effective curative chemical treatment",
                "Preventive copper spray: Copper oxychloride 3 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Blitox (Bayer)"],
        },
        "prevention": [
            "Use disease-free seed material from approved nurseries",
            "Hot water treatment of setts before planting",
            "Use separate planting knives per row to avoid spread",
            "Grow tolerant varieties: Co-86032, CoH-92",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "sugarcane_grassy_shoot": {
        "name": "Sugarcane Grassy Shoot Disease",
        "crop": "Sugarcane",
        "description": "Grassy Shoot Disease is caused by a phytoplasma transmitted by leafhopper Pyrilla perpusilla. It results in profuse tillering, producing grassy appearance and severely reduced yield.",
        "symptoms": [
            "Profuse tillering with numerous thin, weak tillers",
            "White to pale-yellow discolouration of young leaves",
            "Tillers fail to produce normal canes",
            "Entire clump appears bushy and grass-like",
            "Severely affected plants produce no economic yield",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy affected stools immediately",
                "Biocontrol of leafhoppers using entomopathogenic fungi",
            ],
            "chemical": [
                "No chemical cure for phytoplasma",
                "Control leafhopper vector: Imidacloprid 200 SL @ 0.5 ml/litre",
                "Thiamethoxam 25% WG @ 0.3 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Confidor (Bayer)", "Actara (Syngenta)"],
        },
        "prevention": [
            "Use disease-free seed from certified nurseries",
            "Sett treatment with hot water @ 52°C for 30 minutes",
            "Grow tolerant varieties: Co-7704, CoLk-8001",
            "Control leafhopper population regularly",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "sugarcane_healthy": {
        "name": "Sugarcane Healthy",
        "crop": "Sugarcane",
        "description": "The crop is healthy with dark green, erect leaves and no signs of disease.",
        "symptoms": [],
        "treatment": {
            "organic": [],
            "chemical": [],
            "dosage_per_acre": None,
            "indian_brands": [],
        },
        "prevention": [
            "Scout regularly for top shoot borer, red rot and smut",
            "Apply scheduled fertiliser doses",
            "Maintain irrigation schedule during dry periods",
        ],
        "severity": "none",
        "is_healthy": True,
    },

    "sugarcane_mosaic": {
        "name": "Sugarcane Mosaic Virus",
        "crop": "Sugarcane",
        "description": "Caused by Sugarcane Mosaic Virus (SCMV, a potyvirus), mosaic disease produces light and dark green mosaic pattern on leaves. It is transmitted by aphid species.",
        "symptoms": [
            "Light and dark green mosaic/mottling pattern on leaves",
            "Leaf edges may show yellowing",
            "Plant stunting in severe cases",
            "Pale coloured streaks on young leaves",
        ],
        "treatment": {
            "organic": [
                "Remove infected plants",
                "Control aphid vectors with neem oil 3%",
            ],
            "chemical": [
                "No curative treatment for virus",
                "Aphid control: Thiamethoxam 25% WG @ 0.3 g/litre",
                "Imidacloprid 17.8% SL @ 0.5 ml/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Actara (Syngenta)", "Confidor (Bayer)"],
        },
        "prevention": [
            "Use virus-free seed material",
            "Grow resistant varieties: Co-7717, CoLk-94184",
            "Control aphid population from early growth stages",
            "Rogue infected plants",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "sugarcane_pokkah_boeng": {
        "name": "Sugarcane Pokkah Boeng",
        "crop": "Sugarcane",
        "description": "Caused by Fusarium moniliforme (F. verticillioides), Pokkah Boeng (Indonesian for 'malformed top') causes irregular chlorosis, leaf twisting and knife-cut symptoms in young spindle leaves.",
        "symptoms": [
            "Irregular chlorotic patches on young leaves",
            "Leaf twisting and puckering",
            "Knife-cut symptoms on young spindle leaves",
            "Rotting and death of growing point in severe cases",
            "Red discolouration of stem tissue (top rot)",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy severely infected tops",
                "Apply Trichoderma-based bioagents in soil",
            ],
            "chemical": [
                "Carbendazim 50% WP @ 1 g/litre spray",
                "Propiconazole 25% EC @ 1 ml/litre foliar spray",
                "Pour carbendazim solution in leaf whorl @ 0.1%",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Bavistin (BASF)", "Tilt (Syngenta)"],
        },
        "prevention": [
            "Avoid waterlogging in field",
            "Balanced fertilisation, especially potassium",
            "Use tolerant varieties: Co-86032, CoSe-96268",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "sugarcane_red_rot": {
        "name": "Sugarcane Red Rot",
        "crop": "Sugarcane",
        "description": "Caused by Colletotrichum falcatum, red rot is the most important disease of sugarcane. It causes reddening of internal stalk tissue with alcohol-like smell and can destroy entire fields.",
        "symptoms": [
            "Red discolouration of internal stalk tissue with white patches",
            "Alcohol-like (fermented) smell from cut cane",
            "Third and fourth leaves from top show yellowing then drying",
            "Leaf drooping and shredding",
            "Moist rot of stalk leading to plant death",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy infected stools",
                "Sett treatment with Trichoderma viride @ 4 g/kg",
                "Hot water treatment of setts @ 54°C for 30 minutes",
            ],
            "chemical": [
                "Carbendazim 50% WP sett treatment @ 0.1% solution (2 g/litre) — 10-minute soak",
                "Propiconazole 25% EC @ 1 ml/litre foliar spray",
            ],
            "dosage_per_acre": "Sett soaking + 200 litres foliar spray per acre",
            "indian_brands": ["Bavistin (BASF)", "Tilt (Syngenta)"],
        },
        "prevention": [
            "Use red-rot-resistant varieties: CoLk-94184, Co-7527, CoH-119",
            "Hot water treatment of seed setts",
            "Drain excess water promptly",
            "Avoid ratoon crop in confirmed red-rot-positive fields",
            "Don't transport infected material",
        ],
        "severity": "high",
        "is_healthy": False,
    },

    "sugarcane_rust": {
        "name": "Sugarcane Rust",
        "crop": "Sugarcane",
        "description": "Caused by Puccinia melanocephala (common rust) or P. kuehnii (orange rust), sugarcane rust produces orange-brown pustules on leaves. It reduces photosynthetic area and cane yield.",
        "symptoms": [
            "Small, orange to brown elongated pustules on leaf surface",
            "Yellow halo around pustules",
            "Lesions coalesce causing leaf drying in severe cases",
            "Spots visible on both surfaces but more common on underside",
        ],
        "treatment": {
            "organic": [
                "Remove severely infected leaves",
                "Spray neem oil 3% + 0.1% spreader weekly",
            ],
            "chemical": [
                "Propiconazole 25% EC @ 1 ml/litre",
                "Mancozeb 75% WP @ 2.5 g/litre",
                "Trifloxystrobin 25% + Tebuconazole 50% WG @ 0.5 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Tilt (Syngenta)", "Dithane M-45 (UPL)", "Nativo (Bayer)"],
        },
        "prevention": [
            "Grow resistant varieties: Co-86032, CoS-767",
            "Avoid late planting during rust-prone season",
            "Proper spacing for air movement",
        ],
        "severity": "medium",
        "is_healthy": False,
    },

    "sugarcane_yellow_leaf": {
        "name": "Sugarcane Yellow Leaf Disease",
        "crop": "Sugarcane",
        "description": "Caused by Sugarcane Yellow Leaf Virus (SCYLV, a polerovirus) transmitted by aphid Melanaphis sacchari, yellow leaf disease causes yellowing of midrib and leaf blade with significant yield reduction.",
        "symptoms": [
            "Bright yellow colouration of leaf midrib (undersurface) — key symptom",
            "Yellow colour extends to leaf surface",
            "Reduced plant vigour and stalk length",
            "High sucrose loss in affected canes",
            "Yellowing starts from top leaves and progresses downward",
        ],
        "treatment": {
            "organic": [
                "Remove and destroy infected plants",
                "Control aphid vector with neem oil 3%",
            ],
            "chemical": [
                "No curative treatment for virus",
                "Aphid control: Imidacloprid 17.8% SL @ 0.5 ml/litre",
                "Thiamethoxam 25% WG @ 0.3 g/litre",
            ],
            "dosage_per_acre": "200 litres spray solution per acre",
            "indian_brands": ["Confidor (Bayer)", "Actara (Syngenta)"],
        },
        "prevention": [
            "Use SCYLV-free seed from certified nurseries",
            "Grow less-susceptible varieties: CoLk-94184, CoJ-64",
            "Control aphid vectors from crop establishment",
        ],
        "severity": "medium",
        "is_healthy": False,
    },
}


def get_all_diseases() -> list[dict]:
    return [
        {
            "key": key,
            "name": data["name"],
            "crop": data["crop"],
            "severity": data["severity"],
            "is_healthy": data["is_healthy"],
        }
        for key, data in DISEASE_CATALOGUE.items()
    ]


def get_disease(key: str) -> dict | None:
    data = DISEASE_CATALOGUE.get(key)
    if data is None:
        return None
    return {"key": key, **data}


def get_crops() -> list[str]:
    return sorted({d["crop"] for d in DISEASE_CATALOGUE.values()})


def get_class_keys() -> list[str]:
    return list(DISEASE_CATALOGUE.keys())
