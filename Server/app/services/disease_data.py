"""
Indian Crop Disease Knowledge Base
-----------------------------------
Comprehensive disease data for 7 major Indian crops with Indian-market
chemical treatments, organic solutions, dosage per acre, and prevention.
"""

DISEASE_DATABASE = {
    # ═══════════════════════════════════════════════════════════════════
    #   RICE
    # ═══════════════════════════════════════════════════════════════════
    "Rice___Blast": {
        "disease_name": "Rice Blast",
        "crop": "Rice",
        "symptoms": [
            "Diamond-shaped lesions on leaves with grey centers",
            "Brown borders around leaf spots",
            "Neck rot causing panicle breakage",
            "White to grey lesions on nodes",
        ],
        "cause": "Fungus Magnaporthe oryzae, spread by wind-borne spores in humid conditions (25–28°C)",
        "description": "Rice blast is one of the most devastating diseases of rice in India, capable of destroying an entire crop in severe cases. The fungus attacks leaves, nodes, and panicles, reducing grain filling and causing significant yield loss up to 70–80% in susceptible varieties.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Apply neem oil spray (5 ml/litre of water) at 10-day intervals",
            "Use Trichoderma viride bio-fungicide (4 g/litre) as seed treatment and foliar spray",
            "Spray Pseudomonas fluorescens (10 g/litre) at tillering and panicle initiation stages",
            "Maintain proper spacing to allow air circulation",
        ],
        "chemical_treatment": [
            "Tricyclazole 75% WP (Baan/Beam) — 0.6 g/litre foliar spray",
            "Isoprothiolane 40% EC (Fujione) — 1.5 ml/litre",
            "Carbendazim 50% WP (Bavistin) — 1 g/litre as preventive spray",
            "Kasugamycin 3% SL (Kasu-B) — 2 ml/litre at first symptom appearance",
        ],
        "dosage": "Tricyclazole: 300 g/acre in 200 litres of water. Spray at boot-leaf and heading stage. Repeat after 15 days if needed.",
        "prevention": [
            "Use blast-resistant varieties (Pusa Basmati 1509, IR64)",
            "Avoid excess nitrogen fertilisation",
            "Maintain field sanitation — remove crop residues",
            "Ensure proper water management — avoid drought stress",
            "Treat seeds with Carbendazim (2 g/kg seed) before sowing",
        ],
    },
    "Rice___Brown_Spot": {
        "disease_name": "Rice Brown Spot",
        "crop": "Rice",
        "symptoms": [
            "Oval brown spots on leaves with grey centres",
            "Dark brown spots on leaf sheaths and glumes",
            "Poor grain filling with discoloured grains",
            "Seedling blight in nursery beds",
        ],
        "cause": "Fungus Bipolaris oryzae (Cochliobolus miyabeanus), favoured by nutrient-deficient soils and temperatures of 25–30°C",
        "description": "Rice brown spot is associated with mineral-deficient soils, particularly low silicon and potassium. It was the primary cause of the Great Bengal Famine of 1943. The disease causes significant yield reduction through poor grain filling and seed discolouration.",
        "severity": "Medium",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Apply Pseudomonas fluorescens (10 g/litre) as foliar spray",
            "Use Trichoderma harzianum (4 g/kg) as seed treatment",
            "Spray neem kernel extract (5%) at 15-day intervals",
            "Apply Panchagavya (3%) foliar spray for plant immunity",
        ],
        "chemical_treatment": [
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Carbendazim 50% WP (Bavistin) — 1 g/litre",
            "Propiconazole 25% EC (Tilt) — 1 ml/litre",
            "Zineb 75% WP (Indofil Z-78) — 2 g/litre",
        ],
        "dosage": "Mancozeb: 500 g/acre in 200 litres of water. Apply at tillering stage and repeat after 15 days.",
        "prevention": [
            "Apply balanced fertilisation (NPK + micronutrients)",
            "Use certified disease-free seed",
            "Apply silicon-based fertilisers to strengthen plant cells",
            "Avoid prolonged flooding — maintain alternate wetting and drying",
            "Seed treatment with Carbendazim (2 g/kg seed)",
        ],
    },
    "Rice___Leaf_Blight": {
        "disease_name": "Rice Bacterial Leaf Blight",
        "crop": "Rice",
        "symptoms": [
            "Water-soaked lesions starting from leaf tips and margins",
            "Yellowish-white streaks along leaf veins",
            "Leaves dry up and turn greyish-white",
            "Bacterial ooze visible on leaves in early morning",
        ],
        "cause": "Bacterium Xanthomonas oryzae pv. oryzae, spread through rain splash and contaminated irrigation water",
        "description": "Bacterial leaf blight is one of the most serious rice diseases in South and Southeast Asia. It can cause yield losses of 20–50% in severe epidemics. The disease is particularly destructive during the kharif season in flooded paddies.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Spray Pseudomonas fluorescens (10 g/litre) at 10-day intervals",
            "Apply neem oil (5 ml/litre) mixed with copper-based organic formulation",
            "Use Bacillus subtilis-based bio-pesticide (5 g/litre)",
            "Foliar spray of turmeric extract (5%) as a natural bactericide",
        ],
        "chemical_treatment": [
            "Streptomycin sulphate + Tetracycline (Streptocycline) — 0.5 g + Copper oxychloride 2.5 g/litre",
            "Copper hydroxide 77% WP (Kocide) — 2 g/litre",
            "Copper oxychloride 50% WP (Blitox) — 2.5 g/litre",
        ],
        "dosage": "Streptocycline 6 g + Copper oxychloride 500 g per acre in 200 litres of water. Spray at first symptom and repeat after 10 days.",
        "prevention": [
            "Use resistant varieties (Improved Samba Mahsuri, Swarna)",
            "Avoid excess nitrogen — use balanced NPK",
            "Drain excess standing water from fields",
            "Avoid clipping leaves during transplanting",
            "Disinfect tools and avoid working in wet fields",
        ],
    },
    "Rice___Healthy": {
        "disease_name": "Healthy",
        "crop": "Rice",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your rice plant looks healthy! The leaves show normal green coloration with no signs of infection, spots, or lesions. Continue with your current crop management practices to maintain plant health.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": [
            "Continue regular neem oil spray (3 ml/litre) as a preventive measure",
            "Apply Panchagavya (3%) foliar spray once a month for plant vitality",
            "Maintain mulching with organic matter to improve soil health",
        ],
        "chemical_treatment": [
            "No chemical treatment needed",
            "Optional preventive spray of Mancozeb (1.5 g/litre) before monsoon season",
        ],
        "dosage": "No treatment dosage needed. For preventive Mancozeb: 300 g/acre in 200 litres of water.",
        "prevention": [
            "Maintain balanced NPK fertilisation",
            "Ensure proper water management — alternate wetting and drying",
            "Monitor fields regularly for early signs of pest or disease",
            "Rotate crops with pulses to maintain soil health",
        ],
    },

    # ═══════════════════════════════════════════════════════════════════
    #   WHEAT
    # ═══════════════════════════════════════════════════════════════════
    "Wheat___Leaf_Rust": {
        "disease_name": "Wheat Leaf Rust",
        "crop": "Wheat",
        "symptoms": [
            "Small, round, orange-brown pustules on upper leaf surface",
            "Pustules scattered randomly on leaves",
            "Premature leaf drying in severe cases",
            "Reduced ear head size and grain shrivelling",
        ],
        "cause": "Fungus Puccinia triticina, spread by wind-borne uredospores over long distances",
        "description": "Leaf rust (brown rust) is the most common wheat rust in India, appearing annually in the Indo-Gangetic plains. It reduces photosynthetic area leading to 15–30% yield loss. The disease is favour by temperatures of 15–22°C with high humidity.",
        "severity": "Medium",
        "spread_risk": "High",
        "organic_treatment": [
            "Spray neem oil (5 ml/litre) at early pustule stage",
            "Apply Trichoderma viride (4 g/litre) as preventive foliar spray",
            "Use buttermilk spray (10%) as a natural fungicide — traditional remedy",
            "Remove and destroy heavily infected leaves",
        ],
        "chemical_treatment": [
            "Propiconazole 25% EC (Tilt) — 1 ml/litre",
            "Tebuconazole 25.9% EC (Folicur) — 1 ml/litre",
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Triadimefon 25% WP (Bayleton) — 1 g/litre",
        ],
        "dosage": "Propiconazole: 200 ml/acre in 200 litres of water. Spray at flag-leaf stage when first pustules appear. One spray usually sufficient.",
        "prevention": [
            "Grow rust-resistant varieties (HD 3086, DBW 187, PBW 725)",
            "Timely sowing — avoid late planting",
            "Monitor fields from January onwards in North India",
            "Avoid excessive nitrogen — promotes lush growth susceptible to rust",
        ],
    },
    "Wheat___Powdery_Mildew": {
        "disease_name": "Wheat Powdery Mildew",
        "crop": "Wheat",
        "symptoms": [
            "White powdery patches on upper leaf surface",
            "Patches later turn grey-brown with black fruiting bodies",
            "Stunted growth and reduced tillering",
            "Premature leaf senescence",
        ],
        "cause": "Fungus Blumeria graminis f. sp. tritici, spread by wind and favoured by cool humid weather (15–22°C)",
        "description": "Powdery mildew can cause 15–20% yield reduction in wheat. It is common in irrigated wheat in northern India, especially in areas with dense canopy and high humidity. The fungus directly reduces photosynthesis and grain size.",
        "severity": "Medium",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Spray milk solution (1:10 dilution with water) on affected leaves",
            "Apply potassium bicarbonate (3 g/litre) as foliar spray",
            "Use sulphur-based organic formulation (3 g/litre)",
            "Neem oil spray (5 ml/litre) at 10-day intervals",
        ],
        "chemical_treatment": [
            "Karathane 48% EC (Dinocap) — 1 ml/litre",
            "Propiconazole 25% EC (Tilt) — 1 ml/litre",
            "Sulfex (Wettable Sulphur) 80% WP — 3 g/litre",
            "Triadimefon 25% WP (Bayleton) — 1 g/litre",
        ],
        "dosage": "Sulfex: 600 g/acre in 200 litres of water. Apply at first sign of powdery growth. Repeat after 15 days if disease persists.",
        "prevention": [
            "Avoid excess irrigation — allow topsoil to dry between waterings",
            "Ensure proper plant spacing for air circulation",
            "Grow resistant varieties where available",
            "Avoid heavy nitrogen doses in late season",
        ],
    },
    "Wheat___Healthy": {
        "disease_name": "Healthy",
        "crop": "Wheat",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your wheat plant appears healthy with no visible signs of disease. The leaves show normal green colour and there are no lesions, spots, or fungal growth observed.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": [
            "Apply preventive neem oil spray (3 ml/litre) every 2 weeks",
            "Use vermicompost top-dressing for improved soil biology",
        ],
        "chemical_treatment": [
            "No treatment needed",
        ],
        "dosage": "No treatment dosage required.",
        "prevention": [
            "Continue balanced fertilisation",
            "Monitor fields regularly during tillering and heading stages",
            "Maintain proper irrigation scheduling",
        ],
    },

    # ═══════════════════════════════════════════════════════════════════
    #   TOMATO
    # ═══════════════════════════════════════════════════════════════════
    "Tomato___Late_Blight": {
        "disease_name": "Tomato Late Blight",
        "crop": "Tomato",
        "symptoms": [
            "Large, dark brown water-soaked patches on leaves",
            "White fungal growth on underside of leaves in humid conditions",
            "Dark brown lesions on stems",
            "Firm dark spots on green and ripe fruits",
        ],
        "cause": "Oomycete Phytophthora infestans, favoured by cool wet weather (15–20°C with high humidity)",
        "description": "Late blight is the most destructive disease of tomato in India, especially during the rabi season and in hilly regions. It can destroy an entire crop within 7–10 days under favorable conditions. The pathogen also attacks potatoes, making management critical.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Spray Bordeaux mixture (1%) — 10 g copper sulphate + 10 g lime per litre of water",
            "Apply Trichoderma viride (4 g/litre) as preventive spray before monsoon",
            "Use Pseudomonas fluorescens (10 g/litre) foliar spray",
            "Remove and destroy infected plant parts immediately",
        ],
        "chemical_treatment": [
            "Metalaxyl 8% + Mancozeb 64% WP (Ridomil Gold) — 2.5 g/litre",
            "Cymoxanil 8% + Mancozeb 64% WP (Curzate M8) — 3 g/litre",
            "Copper oxychloride 50% WP (Blitox) — 2.5 g/litre",
            "Dimethomorph 50% WP (Acrobat) — 1 g/litre",
        ],
        "dosage": "Ridomil Gold: 500 g/acre in 200 litres of water. Spray at first symptom and repeat every 7–10 days during wet weather. Alternate with contact fungicides.",
        "prevention": [
            "Use disease-free transplants from certified nurseries",
            "Provide staking and proper spacing for air circulation",
            "Avoid overhead irrigation — use drip irrigation",
            "Apply mulch to prevent soil splash",
            "Destroy volunteer plants and crop residues after harvest",
        ],
    },
    "Tomato___Early_Blight": {
        "disease_name": "Tomato Early Blight",
        "crop": "Tomato",
        "symptoms": [
            "Dark brown concentric ring spots (target board pattern) on lower leaves",
            "Yellowing around leaf spots",
            "Leaf drop starting from bottom of plant",
            "Dark sunken spots near fruit stem end",
        ],
        "cause": "Fungus Alternaria solani, favoured by warm humid conditions (24–29°C) and stressed plants",
        "description": "Early blight is common across India wherever tomatoes are grown. It starts on older, lower leaves and progresses upward. Yield losses of 20–40% are common. Stressed plants (drought, nutrient deficiency) are more susceptible.",
        "severity": "Medium",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Spray Trichoderma viride (4 g/litre) starting from transplanting",
            "Apply neem oil (5 ml/litre) every 10 days",
            "Use baking soda spray (5 g/litre) as a foliar treatment",
            "Apply compost tea drench to build soil microbe diversity",
        ],
        "chemical_treatment": [
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Chlorothalonil 75% WP (Kavach) — 2 g/litre",
            "Azoxystrobin 23% SC (Amistar) — 1 ml/litre",
            "Carbendazim 12% + Mancozeb 63% WP (SAAF) — 2 g/litre",
        ],
        "dosage": "Mancozeb: 500 g/acre in 200 litres of water. Start at first symptom and spray every 10–14 days. Rotate fungicide groups to prevent resistance.",
        "prevention": [
            "Use resistant/tolerant varieties (Arka Rakshak, Arka Abhed)",
            "Maintain adequate nutrition — don't stress plants with hunger",
            "Use drip irrigation to avoid wetting foliage",
            "Stake plants and prune lower branches for air flow",
            "Rotate with non-solanaceous crops for 2–3 seasons",
        ],
    },
    "Tomato___Leaf_Curl": {
        "disease_name": "Tomato Leaf Curl Virus",
        "crop": "Tomato",
        "symptoms": [
            "Upward curling and cupping of leaves",
            "Thickened, leathery leaf texture",
            "Stunted plant growth with short internodes",
            "Yellow margins on curled leaves",
            "Flowers drop without fruit set",
        ],
        "cause": "Tomato Leaf Curl Virus (ToLCV), transmitted by whitefly (Bemisia tabaci)",
        "description": "Leaf curl virus is the most economically important tomato disease in India, especially in summer season. Yield losses can reach 80–100% when infection occurs at an early stage. The disease is transmitted by the silverleaf whitefly, which is prevalent across India.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Install yellow sticky traps (12 per acre) to monitor and trap whiteflies",
            "Spray neem oil (5 ml/litre) every 7 days to repel whiteflies",
            "Apply Verticillium lecanii (5 g/litre) — a whitefly bio-control agent",
            "Intercrop with marigold to repel whiteflies",
            "Uproot and destroy infected plants immediately",
        ],
        "chemical_treatment": [
            "Imidacloprid 17.8% SL (Confidor) — 0.3 ml/litre for whitefly control",
            "Thiamethoxam 25% WG (Actara) — 0.3 g/litre",
            "Diafenthiuron 50% WP (Polo) — 1 g/litre",
            "Spiromesifen 22.9% SC (Oberon) — 0.5 ml/litre for nymphal stages",
        ],
        "dosage": "Imidacloprid: 60 ml/acre in 200 litres of water. Spray at seedling stage and repeat every 15 days. Alternate insecticide groups to prevent resistance in whiteflies.",
        "prevention": [
            "Use ToLCV-resistant hybrids (Arka Ananya, TH-1, Lakshmi)",
            "Raise nursery under insect-proof nylon net (40–50 mesh)",
            "Transplant during cooler months when whitefly is less active",
            "Remove weeds around fields — whitefly harbours on alternate hosts",
            "Avoid planting near cotton fields (cotton is a whitefly host)",
        ],
    },
    "Tomato___Septoria_Leaf_Spot": {
        "disease_name": "Tomato Septoria Leaf Spot",
        "crop": "Tomato",
        "symptoms": [
            "Small circular spots (2–3 mm) with dark brown borders and grey centres",
            "Tiny black dots (pycnidia) visible in spot centres",
            "Starts on lower leaves and moves upward",
            "Severe defoliation in advanced stages",
        ],
        "cause": "Fungus Septoria lycopersici, spread by rain splash and overhead irrigation",
        "description": "Septoria leaf spot causes significant early defoliation of tomato plants. While it rarely infects fruit directly, the loss of foliage results in sunscalded fruit and reduced yields of 30–50%. It is common during humid, rainy seasons.",
        "severity": "Medium",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Remove and destroy infected lower leaves",
            "Apply Trichoderma viride (4 g/litre) as preventive spray",
            "Spray copper-based organic fungicide (Bordeaux mixture 1%)",
            "Improve air circulation with proper staking and pruning",
        ],
        "chemical_treatment": [
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Chlorothalonil 75% WP (Kavach) — 2 g/litre",
            "Hexaconazole 5% SC (Contaf) — 1 ml/litre",
            "Azoxystrobin 23% SC (Amistar) — 1 ml/litre",
        ],
        "dosage": "Mancozeb: 500 g/acre in 200 litres. Spray at first symptom, repeat every 10 days. Alternate with systemic fungicide every third application.",
        "prevention": [
            "Avoid overhead irrigation — use drip",
            "Mulch around plants to prevent soil splash",
            "Remove lower leaves that touch the ground",
            "Rotate with non-solanaceous crops for 2 years",
        ],
    },
    "Tomato___Healthy": {
        "disease_name": "Healthy",
        "crop": "Tomato",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your tomato plant looks healthy! The leaves are green with no spots, curling, or unusual markings. Keep up your current management practices.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": ["Continue preventive neem oil spray (3 ml/litre) every 2 weeks"],
        "chemical_treatment": ["No treatment needed"],
        "dosage": "No dosage required.",
        "prevention": [
            "Monitor for whiteflies using yellow sticky traps",
            "Maintain proper staking and air circulation",
            "Use balanced NPK fertilisation",
        ],
    },

    # ═══════════════════════════════════════════════════════════════════
    #   POTATO
    # ═══════════════════════════════════════════════════════════════════
    "Potato___Late_Blight": {
        "disease_name": "Potato Late Blight",
        "crop": "Potato",
        "symptoms": [
            "Dark brown water-soaked patches on leaf margins and tips",
            "White cottony fungal growth on underside of leaves",
            "Rapid browning and collapse of foliage",
            "Brown rotting of tubers from surface inwards",
        ],
        "cause": "Oomycete Phytophthora infestans, favoured by cool wet conditions (12–18°C with high humidity)",
        "description": "Late blight is historically the single most destructive potato disease worldwide. In India, it is severe in the hills (Shimla, Darjeeling) and plains (UP, West Bengal) during foggy winter periods. It can cause 40–80% crop loss within 2 weeks.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Spray Bordeaux mixture (1%) as preventive before rains",
            "Apply Trichoderma viride (4 g/litre) foliar spray",
            "Use Pseudomonas fluorescens (10 g/litre) bio-fungicide",
            "Hill up soil around stems to protect tubers from spore infection",
        ],
        "chemical_treatment": [
            "Metalaxyl 8% + Mancozeb 64% WP (Ridomil Gold) — 2.5 g/litre",
            "Cymoxanil 8% + Mancozeb 64% WP (Curzate M8) — 3 g/litre",
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre (preventive only)",
            "Fenamidone 10% + Mancozeb 50% WG (Sectin) — 3 g/litre",
        ],
        "dosage": "Ridomil Gold: 500 g/acre in 200 litres. Spray at first symptom, repeat every 7 days during wet weather. Alternate systemic and contact fungicides.",
        "prevention": [
            "Use certified disease-free seed tubers",
            "Plant resistant varieties (Kufri Girdhari, Kufri Khyati)",
            "Avoid overhead sprinkler irrigation",
            "Destroy volunteer plants and cull piles",
            "Apply prophylactic fungicide spray before forecasted foggy/rainy weather",
        ],
    },
    "Potato___Early_Blight": {
        "disease_name": "Potato Early Blight",
        "crop": "Potato",
        "symptoms": [
            "Dark brown concentric ring spots on older leaves (target board pattern)",
            "Yellowing around spots",
            "Premature senescence of lower leaves",
            "Small dark sunken lesions on tuber surface",
        ],
        "cause": "Fungus Alternaria solani, favoured by warm days (25–30°C) and cool nights with dew",
        "description": "Early blight is a chronic disease of potato in India, occurring every season. It reduces photosynthetic area leading to 20–30% yield loss. Nutritionally stressed and older plants are most susceptible.",
        "severity": "Medium",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Spray neem oil (5 ml/litre) every 10 days",
            "Apply Trichoderma viride (4 g/litre) foliar application",
            "Remove and destroy heavily infected lower leaves",
            "Maintain soil health with compost and humic acid application",
        ],
        "chemical_treatment": [
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Carbendazim 12% + Mancozeb 63% WP (SAAF) — 2 g/litre",
            "Azoxystrobin 23% SC (Amistar) — 1 ml/litre",
            "Chlorothalonil 75% WP (Kavach) — 2 g/litre",
        ],
        "dosage": "Mancozeb: 500 g/acre in 200 litres. Start at 45 days after planting and repeat every 10–14 days.",
        "prevention": [
            "Use healthy seed tubers from certified sources",
            "Maintain proper nutrition — don't let plants become hungry",
            "Irrigation management — avoid alternate drought and flood",
            "Crop rotation with cereals for 2+ seasons",
        ],
    },
    "Potato___Healthy": {
        "disease_name": "Healthy",
        "crop": "Potato",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your potato plant looks healthy with normal green foliage and no signs of blight, spots, or viral infection.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": ["Continue preventive care with neem oil spray every 2 weeks"],
        "chemical_treatment": ["No treatment needed"],
        "dosage": "No dosage required.",
        "prevention": [
            "Monitor for late blight during foggy/dew periods",
            "Maintain balanced fertilisation",
            "Earth up tubers properly to prevent greening",
        ],
    },

    # ═══════════════════════════════════════════════════════════════════
    #   COTTON
    # ═══════════════════════════════════════════════════════════════════
    "Cotton___Bacterial_Blight": {
        "disease_name": "Cotton Bacterial Blight",
        "crop": "Cotton",
        "symptoms": [
            "Small angular water-soaked spots on leaves (angular leaf spot)",
            "Spots enlarge, turn brown, and may coalesce",
            "Black arm symptoms on stems and branches",
            "Boll rot with brown-black discolouration",
        ],
        "cause": "Bacterium Xanthomonas citri pv. malvacearum, spread by rain splash and contaminated seed",
        "description": "Bacterial blight (angular leaf spot) is one of the oldest known diseases of cotton in India. It is most damaging in Central and South India during monsoon season with warm, humid weather. Severe infections can cause 30–40% yield loss.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Spray Pseudomonas fluorescens (10 g/litre) at 10-day intervals",
            "Apply copper-based organic spray (Bordeaux mixture 1%)",
            "Use neem oil (5 ml/litre) with turmeric extract (2%) as foliar spray",
            "Remove and burn infected plant debris after harvest",
        ],
        "chemical_treatment": [
            "Streptomycin sulphate (Streptocycline) — 0.5 g/litre + Copper oxychloride 2.5 g/litre",
            "Copper hydroxide 77% WP (Kocide) — 2 g/litre",
            "Copper oxychloride 50% WP (Blitox) — 2.5 g/litre",
        ],
        "dosage": "Streptocycline 6 g + Copper oxychloride 500 g per acre in 200 litres. Start at first symptom and repeat after 10 days.",
        "prevention": [
            "Use acid-delinted disease-free seed",
            "Seed treatment with Carboxin (2 g/kg) or Streptocycline (1 g/10 litres water for seed soak)",
            "Grow resistant varieties (Suraj, NH 615)",
            "Avoid working in fields when plants are wet",
            "Crop rotation with cereals for 2+ years",
        ],
    },
    "Cotton___Leaf_Curl": {
        "disease_name": "Cotton Leaf Curl Virus",
        "crop": "Cotton",
        "symptoms": [
            "Upward curling of leaf margins",
            "Thickening and darkening of leaf veins (vein swelling)",
            "Cup-shaped leaves with enation (outgrowths) on underside",
            "Stunted plant growth with reduced boll formation",
        ],
        "cause": "Cotton Leaf Curl Virus (CLCuV), transmitted by whitefly (Bemisia tabaci)",
        "description": "Cotton leaf curl disease is one of the most devastating cotton diseases in northwestern India (Punjab, Haryana, Rajasthan). It caused massive epidemics in the 1990s. Yield losses can reach 50–80% in susceptible varieties.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Install yellow sticky traps (15 per acre) for whitefly management",
            "Spray neem oil (5 ml/litre) every 7 days",
            "Apply Verticillium lecanii (5 g/litre) against whitefly nymphs",
            "Uproot and destroy infected plants early to prevent virus spread",
        ],
        "chemical_treatment": [
            "Imidacloprid 17.8% SL (Confidor) — 0.3 ml/litre",
            "Thiamethoxam 25% WG (Actara) — 0.3 g/litre",
            "Diafenthiuron 50% WP (Polo) — 1 g/litre",
            "Pyriproxyfen 10% EC (Lano) — 1 ml/litre (targets whitefly eggs and nymphs)",
        ],
        "dosage": "Imidacloprid: 60 ml/acre in 200 litres. Start from 15 days after germination, repeat every 15 days. Rotate insecticide groups.",
        "prevention": [
            "Grow CLCuV-tolerant Bt cotton hybrids",
            "Avoid early sowing — plant after first June rains to escape peak whitefly",
            "Avoid planting near old cotton crop residues",
            "Keep borders clean — remove weeds that harbour whiteflies",
        ],
    },
    "Cotton___Healthy": {
        "disease_name": "Healthy",
        "crop": "Cotton",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your cotton plant looks healthy with normal leaf growth and no signs of curling, spots, or bacterial infection.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": ["Continue preventive neem oil spray"],
        "chemical_treatment": ["No treatment needed"],
        "dosage": "No dosage required.",
        "prevention": ["Monitor for whiteflies weekly", "Maintain balanced fertilisation"],
    },

    # ═══════════════════════════════════════════════════════════════════
    #   MAIZE
    # ═══════════════════════════════════════════════════════════════════
    "Maize___Northern_Leaf_Blight": {
        "disease_name": "Maize Northern Leaf Blight",
        "crop": "Maize",
        "symptoms": [
            "Long elliptical greyish-green lesions (5–15 cm) on leaves",
            "Lesions start on lower leaves and progress upwards",
            "Severe blight can kill entire leaves",
            "Reduced ear size and grain filling",
        ],
        "cause": "Fungus Exserohilum turcicum, favoured by moderate temperatures (18–27°C) with high humidity and dew",
        "description": "Northern leaf blight (turcicum blight) is the most important foliar disease of maize in India. It is common in the hilly regions and during the kharif season in the plains. Yield losses of 30–50% can occur when the upper leaves are severely infected before tasseling.",
        "severity": "High",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Apply Trichoderma viride (4 g/litre) as foliar spray at 10-day intervals",
            "Spray neem oil (5 ml/litre) at first symptom",
            "Remove heavily infected lower leaves to slow spread",
            "Use Pseudomonas fluorescens (10 g/litre)",
        ],
        "chemical_treatment": [
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Propiconazole 25% EC (Tilt) — 1 ml/litre",
            "Azoxystrobin 23% SC (Amistar) — 1 ml/litre",
            "Zineb 75% WP (Indofil Z-78) — 2 g/litre",
        ],
        "dosage": "Mancozeb: 500 g/acre in 200 litres. First spray at knee-high stage, repeat at pre-tassel. Apply Propiconazole if severe.",
        "prevention": [
            "Use resistant hybrids (HQPM-1, DHM 117)",
            "Remove and destroy crop residues after harvest",
            "Avoid mono-cropping of maize — rotate with pulses or oilseeds",
            "Maintain balanced NPK with adequate potassium for disease resistance",
        ],
    },
    "Maize___Common_Rust": {
        "disease_name": "Maize Common Rust",
        "crop": "Maize",
        "symptoms": [
            "Small circular to elongated brownish-red pustules on both leaf surfaces",
            "Pustules burst to release powdery brown spores",
            "In severe cases, leaves turn brown and dry up",
        ],
        "cause": "Fungus Puccinia sorghi, spread by wind-borne spores",
        "description": "Common rust is widespread across all maize-growing regions of India. It is usually moderate in severity but can cause 15–25% yield loss when infection occurs early.",
        "severity": "Medium",
        "spread_risk": "High",
        "organic_treatment": [
            "Apply neem oil (5 ml/litre) at early pustule stage",
            "Spray Trichoderma viride (4 g/litre) preventively",
        ],
        "chemical_treatment": [
            "Mancozeb 75% WP (Dithane M-45) — 2.5 g/litre",
            "Propiconazole 25% EC (Tilt) — 1 ml/litre",
            "Hexaconazole 5% SC (Contaf) — 2 ml/litre",
        ],
        "dosage": "Propiconazole: 200 ml/acre in 200 litres. One spray usually sufficient at flag-leaf stage.",
        "prevention": [
            "Grow resistant hybrids",
            "Timely sowing to avoid peak infection period",
            "Remove volunteer maize plants",
        ],
    },
    "Maize___Healthy": {
        "disease_name": "Healthy",
        "crop": "Maize",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your maize plant is healthy with vigorous green leaves and no disease symptoms.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": ["Continue good agronomic practices"],
        "chemical_treatment": ["No treatment needed"],
        "dosage": "No dosage required.",
        "prevention": ["Monitor for fall armyworm and leaf blight during kharif season"],
    },

    # ═══════════════════════════════════════════════════════════════════
    #   SUGARCANE
    # ═══════════════════════════════════════════════════════════════════
    "Sugarcane___Red_Rot": {
        "disease_name": "Sugarcane Red Rot",
        "crop": "Sugarcane",
        "symptoms": [
            "Drying and withering of the 3rd and 4th leaves from top",
            "Internal cane tissue turns red with white patches (brick-red and white cross-section)",
            "Sour alcoholic smell from split cane",
            "Shrinkage and hollowing of internodes",
        ],
        "cause": "Fungus Colletotrichum falcatum, spread through infected setts (seed cane) and soil",
        "description": "Red rot is called the 'cancer of sugarcane' and is the most devastating disease in Indian sugarcane cultivation. It has historically wiped out entire varieties in India (e.g. Co 997). The disease is soil-borne and seed-borne, making management challenging.",
        "severity": "High",
        "spread_risk": "High",
        "organic_treatment": [
            "Treat setts with Trichoderma viride (10 g/litre) for 30 minutes before planting",
            "Apply Pseudomonas fluorescens as soil drench around root zone",
            "Use Bacillus subtilis-based bio-agent at planting",
            "Practice hot water treatment of setts at 52°C for 30 minutes (traditional method)",
        ],
        "chemical_treatment": [
            "Carbendazim 50% WP (Bavistin) — sett treatment (1 g/litre for 30 min dip)",
            "Thiophanate Methyl 70% WP (Topsin-M) — 1 g/litre sett dip",
            "No effective foliar treatment once disease is established",
        ],
        "dosage": "Carbendazim: Prepare 1 g/litre solution. Dip setts for 30 minutes before planting. 200 litres solution per acre of setts.",
        "prevention": [
            "Use red rot-resistant varieties (Co 0238, CoLk 94184)",
            "Always use disease-free seed cane from declared disease-free nurseries",
            "Avoid ratooning of susceptible varieties",
            "Remove and destroy infected stools — do not leave in field",
            "Flood fields for 7 days to kill soil-borne inoculum before planting",
        ],
    },
    "Sugarcane___Smut": {
        "disease_name": "Sugarcane Smut",
        "crop": "Sugarcane",
        "symptoms": [
            "Long black whip-like structure (5–100 cm) emerging from growing point",
            "Whip is initially covered with silvery membrane that ruptures to release black spores",
            "Thin, grass-like tillers with narrow leaves",
            "Excessive tillering from infected stool",
        ],
        "cause": "Fungus Sporisorium scitamineum, spread by wind-borne spores and infected setts",
        "description": "Whip smut is easily recognizable by the black whip emerging from the top of the plant. It is common across India and can cause 30–40% yield loss. Ratooning increases disease severity significantly.",
        "severity": "Medium",
        "spread_risk": "Medium",
        "organic_treatment": [
            "Hot water treatment of setts at 52°C for 30 minutes",
            "Apply Trichoderma viride (10 g/litre) sett treatment",
            "Remove and burn smutted whips before they release spores",
        ],
        "chemical_treatment": [
            "Carbendazim 50% WP (Bavistin) — 1 g/litre sett dip for 30 minutes",
            "Triadimefon 25% WP (Bayleton) — 1 g/litre foliar spray on ratoon cane",
        ],
        "dosage": "Carbendazim: 1 g/litre sett dip for 30 min before planting.",
        "prevention": [
            "Use smut-resistant varieties (CoLk 94184, Co 0238)",
            "Avoid ratooning for more than 2 cycles",
            "Rogue out smutted clumps before whips open",
            "Use only healthy setts from disease-free nurseries",
        ],
    },
    "Sugarcane___Healthy": {
        "disease_name": "Healthy",
        "crop": "Sugarcane",
        "symptoms": [],
        "cause": "No disease detected",
        "description": "Your sugarcane looks healthy with strong cane growth and no visible symptoms of rot, smut, or leaf scald.",
        "severity": "None",
        "spread_risk": "None",
        "organic_treatment": ["Maintain good agronomic practices"],
        "chemical_treatment": ["No treatment needed"],
        "dosage": "No dosage required.",
        "prevention": ["Always use disease-free setts from certified nurseries"],
    },
}


def get_disease_info(class_key: str) -> dict | None:
    """Look up disease by class key (e.g. 'Tomato___Late_Blight')."""
    return DISEASE_DATABASE.get(class_key)


def get_all_diseases() -> list[dict]:
    """Return list of all disease documents."""
    return [
        {**v, "class_key": k}
        for k, v in DISEASE_DATABASE.items()
        if v["disease_name"] != "Healthy"
    ]


def get_diseases_by_crop(crop: str) -> list[dict]:
    """Return diseases for a specific crop."""
    return [
        {**v, "class_key": k}
        for k, v in DISEASE_DATABASE.items()
        if v["crop"].lower() == crop.lower() and v["disease_name"] != "Healthy"
    ]


# Class index mapping — matches training label encoding order
# Update this after training your model
CLASS_INDEX_MAP = {i: key for i, key in enumerate(DISEASE_DATABASE.keys())}
INDEX_CLASS_MAP = {v: k for k, v in CLASS_INDEX_MAP.items()}
