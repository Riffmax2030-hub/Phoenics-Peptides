import os

products = [
    {
        "id": 1, "code": "tirzepatide", "name": "Tirzepatide", "strength": "10MG", "type": "clear_vial",
        "cap_color": "#0055B8", "cap_rim": "#F59E0B", "powder_color": "#FFFFFF",
        "cas": "2023788-19-2", "mw": "4813.45 g/mol", "purity": "99.4%", "rt": "11.24 min",
        "box_theme": "navy_gold"
    },
    {
        "id": 2, "code": "retatrutide", "name": "Retatrutide", "strength": "10MG", "type": "clear_vial",
        "cap_color": "#7C3AED", "cap_rim": "#A78BFA", "powder_color": "#FFFFFF",
        "cas": "2381089-83-2", "mw": "4731.33 g/mol", "purity": "99.3%", "rt": "12.08 min",
        "box_theme": "purple"
    },
    {
        "id": 3, "code": "semaglutide", "name": "Semaglutide", "strength": "5MG", "type": "clear_vial",
        "cap_color": "#059669", "cap_rim": "#34D399", "powder_color": "#FFFFFF",
        "cas": "910463-68-2", "mw": "4113.58 g/mol", "purity": "99.5%", "rt": "10.82 min",
        "box_theme": "green"
    },
    {
        "id": 4, "code": "cagrilintide", "name": "Cagrilintide", "strength": "5MG", "type": "clear_vial",
        "cap_color": "#BE185D", "cap_rim": "#F472B6", "powder_color": "#FFFFFF",
        "cas": "1415456-99-3", "mw": "4522.06 g/mol", "purity": "99.2%", "rt": "11.55 min",
        "box_theme": "pink"
    },
    {
        "id": 5, "code": "bpc157", "name": "BPC-157", "strength": "5MG", "type": "clear_vial",
        "cap_color": "#0284C7", "cap_rim": "#38BDF8", "powder_color": "#FFFFFF",
        "cas": "137525-51-0", "mw": "1419.53 g/mol", "purity": "99.4%", "rt": "8.45 min",
        "box_theme": "cyan"
    },
    {
        "id": 6, "code": "tb500", "name": "TB-500", "strength": "5MG", "type": "clear_vial",
        "cap_color": "#DC2626", "cap_rim": "#F87171", "powder_color": "#FFFFFF",
        "cas": "77591-33-4", "mw": "4963.50 g/mol", "purity": "99.5%", "rt": "9.12 min",
        "box_theme": "red"
    },
    {
        "id": 7, "code": "ghkcu", "name": "GHK-Cu", "strength": "50MG", "type": "clear_vial",
        "cap_color": "#1D4ED8", "cap_rim": "#60A5FA", "powder_color": "#2563EB", # VIVID ROYAL BLUE POWDER!
        "cas": "49557-75-7", "mw": "403.92 g/mol", "purity": "99.6%", "rt": "6.80 min",
        "box_theme": "blue"
    },
    {
        "id": 8, "code": "cjcipam", "name": "CJC + Ipamorelin", "strength": "10MG DUAL", "type": "clear_vial",
        "cap_color": "#64748B", "cap_rim": "#94A3B8", "powder_color": "#FFFFFF",
        "cas": "Dual Agonist Mix", "mw": "3367 / 711 g/mol", "purity": "99.3%", "rt": "10.15 min",
        "box_theme": "silver"
    },
    {
        "id": 9, "code": "tesamorelin", "name": "Tesamorelin", "strength": "5MG", "type": "clear_vial",
        "cap_color": "#D97706", "cap_rim": "#FCD34D", "powder_color": "#FFFFFF",
        "cas": "218949-48-5", "mw": "5135.80 g/mol", "purity": "99.2%", "rt": "12.30 min",
        "box_theme": "bronze"
    },
    {
        "id": 10, "code": "mk677", "name": "MK-677 Ibutamoren", "strength": "25MG/ML", "type": "amber_dropper",
        "cap_color": "#1E293B", "cap_rim": "#334155", "powder_color": "#F59E0B", # Golden oral solution
        "cas": "159752-10-0", "mw": "624.77 g/mol", "purity": "99.5%", "rt": "14.20 min",
        "box_theme": "amber_dropper"
    },
    {
        "id": 11, "code": "motsc", "name": "MOTS-c", "strength": "10MG", "type": "amber_vial",
        "cap_color": "#B45309", "cap_rim": "#FBBF24", "powder_color": "#FFFFFF",
        "cas": "Mitochondrial 12S", "mw": "2174.60 g/mol", "purity": "99.3%", "rt": "9.90 min",
        "box_theme": "amber_vial"
    },
    {
        "id": 12, "code": "epithalon", "name": "Epithalon", "strength": "10MG", "type": "clear_vial",
        "cap_color": "#E2E8F0", "cap_rim": "#94A3B8", "powder_color": "#FFFFFF",
        "cas": "307297-39-8", "mw": "390.35 g/mol", "purity": "99.4%", "rt": "5.60 min",
        "box_theme": "white"
    },
    {
        "id": 13, "code": "semax", "name": "Semax", "strength": "30MG", "type": "amber_nasal_spray",
        "cap_color": "#F8FAFC", "cap_rim": "#38BDF8", "powder_color": "#FFFFFF",
        "cas": "80714-61-0", "mw": "813.90 g/mol", "purity": "99.5%", "rt": "7.40 min",
        "box_theme": "spray"
    },
    {
        "id": 14, "code": "selank", "name": "Selank", "strength": "10MG", "type": "amber_nasal_spray",
        "cap_color": "#F8FAFC", "cap_rim": "#818CF8", "powder_color": "#FFFFFF",
        "cas": "129954-34-3", "mw": "751.90 g/mol", "purity": "99.6%", "rt": "7.10 min",
        "box_theme": "spray"
    },
    {
        "id": 15, "code": "pt141", "name": "PT-141", "strength": "10MG", "type": "clear_vial",
        "cap_color": "#4C1D95", "cap_rim": "#C4B5FD", "powder_color": "#FFFFFF",
        "cas": "189745-56-8", "mw": "1025.20 g/mol", "purity": "99.4%", "rt": "8.90 min",
        "box_theme": "indigo"
    },
    {
        "id": 16, "code": "library384", "name": "Custom 384-Peptide Library", "strength": "384 PEPTIDES", "type": "microplate_384",
        "cap_color": "#00D2FF", "cap_rim": "#38BDF8", "powder_color": "#FFFFFF",
        "cas": "Multiplex Combinatorial Array", "mw": "Multiple (100% MS Tested)", "purity": "≥95.0% per well", "rt": "Robotic Scan",
        "box_theme": "cryo_crate"
    },
    {
        "id": 17, "code": "bulk10g", "name": "Bulk cGMP Lot (10 Grams)", "strength": "10,000 MG", "type": "bulk_jar",
        "cap_color": "#0F172A", "cap_rim": "#F59E0B", "powder_color": "#FFFFFF",
        "cas": "cGMP Active Lot", "mw": "Preclinical Single Batch", "purity": "≥98.5%", "rt": "Certified Lot",
        "box_theme": "bulk_jar"
    },
    {
        "id": 18, "code": "kinase96", "name": "Kinase Profiling Suite", "strength": "96 TARGETS", "type": "microplate_384",
        "cap_color": "#059669", "cap_rim": "#34D399", "powder_color": "#FFFFFF",
        "cas": "Phosphorylated Targets", "mw": "Kinase Substrates", "purity": "≥95.0%", "rt": "Enzymatic Assay",
        "box_theme": "cryo_crate"
    }
]

def generate_vial_svg(p):
    ptype = p["type"]
    name = p["name"].upper()
    strength = p["strength"]
    cas = p["cas"]
    purity = p["purity"]
    cap = p["cap_color"]
    rim = p["cap_rim"]
    powder = p["powder_color"]
    
    # Check container type
    if ptype == "clear_vial" or ptype == "amber_vial":
        is_amber = ptype == "amber_vial"
        glass_fill = "#78350F" if is_amber else "#F8FAFC"
        glass_stroke = "#D97706" if is_amber else "#CBD5E1"
        glass_opac = "0.75" if is_amber else "0.2"
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" />
      <stop offset="100%" stop-color="#070D14" />
    </linearGradient>
    <linearGradient id="glassGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.4" />
      <stop offset="20%" stop-color="#FFFFFF" stop-opacity="0.1" />
      <stop offset="80%" stop-color="#FFFFFF" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="capGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{cap}" />
      <stop offset="50%" stop-color="{rim}" />
      <stop offset="100%" stop-color="{cap}" />
    </linearGradient>
    <filter id="pedestalGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="15" result="blur" />
    </filter>
  </defs>

  <rect width="400" height="400" fill="url(#bgGrad)" />

  <!-- Biolab Circular Pedestal & Shadow -->
  <ellipse cx="200" cy="355" rx="140" ry="25" fill="#00D2FF" opacity="0.15" filter="url(#pedestalGlow)" />
  <ellipse cx="200" cy="355" rx="110" ry="16" fill="#030712" opacity="0.8" />
  <ellipse cx="200" cy="352" rx="100" ry="12" fill="#0D1B2A" stroke="#00D2FF" stroke-width="1.5" stroke-opacity="0.4" />

  <!-- VIAL BODY -->
  <!-- Glass Vial Outer Shadow -->
  <rect x="140" y="110" width="120" height="230" rx="14" fill="#030712" opacity="0.4" />
  
  <!-- Glass Vial Body -->
  <rect x="140" y="110" width="120" height="230" rx="14" fill="{glass_fill}" fill-opacity="{glass_opac}" stroke="{glass_stroke}" stroke-width="2.5" />
  
  <!-- Lyophilized Powder Cake in bottom -->
  <path d="M 142 285 Q 200 280 258 285 L 258 326 Q 200 340 142 326 Z" fill="{powder}" opacity="0.95" />
  <ellipse cx="200" cy="285" rx="58" ry="8" fill="{powder}" opacity="0.8" />

  <!-- Realistic Lab Bottle Label -->
  <rect x="142" y="150" width="116" height="115" rx="4" fill="#FFFFFF" />
  <rect x="142" y="150" width="116" height="8" rx="2" fill="{cap}" />
  
  <!-- Brand on Label -->
  <text x="200" y="172" font-family="'Montserrat', sans-serif" font-size="10" font-weight="800" letter-spacing="1.5" fill="#0D1B2A" text-anchor="middle">PHOENICS PEPTIDE</text>
  <line x1="155" y1="176" x2="245" y2="176" stroke="#E2E8F0" stroke-width="1" />
  
  <!-- Product Name on Label -->
  <text x="200" y="196" font-family="'Montserrat', sans-serif" font-size="13" font-weight="900" fill="{cap}" text-anchor="middle">{name}</text>
  <text x="200" y="212" font-family="'Space Mono', monospace" font-size="12" font-weight="700" fill="#0D1B2A" text-anchor="middle">{strength}</text>
  
  <!-- Lab Purity & CAS -->
  <rect x="152" y="222" width="96" height="18" rx="9" fill="#F1F5F9" />
  <text x="200" y="234" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">HPLC &ge; {purity}</text>
  <text x="200" y="254" font-family="'Space Mono', monospace" font-size="7" fill="#64748B" text-anchor="middle">CAS: {cas[:16]}</text>
  
  <!-- Barcode on Label -->
  <g transform="translate(160, 258)">
    <rect x="0" y="0" width="2" height="5" fill="#000"/>
    <rect x="4" y="0" width="1" height="5" fill="#000"/>
    <rect x="7" y="0" width="3" height="5" fill="#000"/>
    <rect x="12" y="0" width="1" height="5" fill="#000"/>
    <rect x="15" y="0" width="2" height="5" fill="#000"/>
    <rect x="20" y="0" width="3" height="5" fill="#000"/>
    <rect x="25" y="0" width="1" height="5" fill="#000"/>
    <rect x="28" y="0" width="2" height="5" fill="#000"/>
    <rect x="33" y="0" width="2" height="5" fill="#000"/>
    <rect x="37" y="0" width="3" height="5" fill="#000"/>
    <rect x="43" y="0" width="1" height="5" fill="#000"/>
    <rect x="47" y="0" width="2" height="5" fill="#000"/>
    <rect x="52" y="0" width="2" height="5" fill="#000"/>
    <rect x="56" y="0" width="3" height="5" fill="#000"/>
    <rect x="62" y="0" width="1" height="5" fill="#000"/>
    <rect x="66" y="0" width="2" height="5" fill="#000"/>
    <rect x="71" y="0" width="1" height="5" fill="#000"/>
    <rect x="74" y="0" width="3" height="5" fill="#000"/>
  </g>

  <!-- Glass Vertical Specular Reflection -->
  <rect x="145" y="115" width="15" height="218" rx="6" fill="url(#glassGlow)" />
  <line x1="250" y1="120" x2="250" y2="330" stroke="#FFFFFF" stroke-width="2" stroke-opacity="0.3" />

  <!-- VIAL NECK & CRIMP CAP -->
  <!-- Glass Neck -->
  <rect x="175" y="85" width="50" height="25" fill="{glass_fill}" fill-opacity="{glass_opac}" stroke="{glass_stroke}" stroke-width="2" />
  <!-- Aluminum Crimp Collar -->
  <rect x="168" y="70" width="64" height="18" rx="3" fill="url(#capGrad)" stroke="{rim}" stroke-width="1.5" />
  <!-- Flip-Off Plastic Top Button -->
  <rect x="164" y="52" width="72" height="20" rx="6" fill="{cap}" stroke="{rim}" stroke-width="1.8" />
  <ellipse cx="200" cy="54" rx="32" ry="5" fill="{rim}" opacity="0.6" />
  
  <!-- Security Seal Stamp Badge -->
  <circle cx="280" cy="85" r="22" fill="#0D1B2A" stroke="#F59E0B" stroke-width="2" />
  <text x="280" y="83" font-family="'Montserrat', sans-serif" font-size="7" font-weight="800" fill="#FCD34D" text-anchor="middle">AUTHENTIC</text>
  <text x="280" y="93" font-family="'Montserrat', sans-serif" font-size="6" font-weight="700" fill="#FFFFFF" text-anchor="middle">BATCH CERT</text>
</svg>'''
        return svg

    elif ptype == "amber_dropper":
        # 30ml Dropper Bottle for MK-677
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" /><stop offset="100%" stop-color="#070D14" />
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#78350F" /><stop offset="50%" stop-color="#92400E" /><stop offset="100%" stop-color="#451A03" />
    </linearGradient>
    <linearGradient id="pipetteGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1E293B" /><stop offset="50%" stop-color="#475569" /><stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bgGrad)" />
  <ellipse cx="200" cy="360" rx="120" ry="18" fill="#00D2FF" opacity="0.15" />
  <ellipse cx="200" cy="358" rx="90" ry="12" fill="#0D1B2A" stroke="#00D2FF" stroke-width="1.5" stroke-opacity="0.4" />
  
  <!-- 30ml Amber Glass Body -->
  <rect x="135" y="140" width="130" height="205" rx="18" fill="url(#amberGrad)" stroke="#B45309" stroke-width="2.5" />
  <!-- Liquid Level -->
  <rect x="138" y="180" width="124" height="162" rx="14" fill="#D97706" fill-opacity="0.3" />

  <!-- Label -->
  <rect x="142" y="165" width="116" height="135" rx="4" fill="#FFFFFF" />
  <rect x="142" y="165" width="116" height="8" fill="#D97706" />
  <text x="200" y="186" font-family="'Montserrat', sans-serif" font-size="9" font-weight="800" fill="#0D1B2A" text-anchor="middle">PHOENICS PEPTIDE</text>
  <text x="200" y="208" font-family="'Montserrat', sans-serif" font-size="12" font-weight="900" fill="#D97706" text-anchor="middle">{name}</text>
  <text x="200" y="224" font-family="'Space Mono', monospace" font-size="10" font-weight="700" fill="#0D1B2A" text-anchor="middle">{strength} (30ML)</text>
  <rect x="155" y="234" width="90" height="16" rx="8" fill="#FEF3C7" />
  <text x="200" y="246" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#B45309" text-anchor="middle">ORAL RESEARCH REAGENT</text>
  <text x="200" y="268" font-family="'Space Mono', monospace" font-size="7" fill="#64748B" text-anchor="middle">HPLC &ge; {purity} • CAS: 159752-10-0</text>
  
  <!-- Bottle Shoulder & Neck -->
  <path d="M 135 155 Q 165 140 178 120 L 222 120 Q 235 140 265 155 Z" fill="url(#amberGrad)" stroke="#B45309" stroke-width="2" />
  <rect x="178" y="105" width="44" height="18" fill="url(#amberGrad)" stroke="#B45309" stroke-width="1.5" />
  
  <!-- Dropper Ribbed Collar & Pipette Bulb -->
  <rect x="170" y="85" width="60" height="22" rx="3" fill="url(#pipetteGrad)" stroke="#334155" stroke-width="1.5" />
  <!-- Ribs -->
  <line x1="178" y1="87" x2="178" y2="105" stroke="#64748B" stroke-width="1.5" />
  <line x1="188" y1="87" x2="188" y2="105" stroke="#64748B" stroke-width="1.5" />
  <line x1="200" y1="87" x2="200" y2="105" stroke="#64748B" stroke-width="1.5" />
  <line x1="212" y1="87" x2="212" y2="105" stroke="#64748B" stroke-width="1.5" />
  <line x1="222" y1="87" x2="222" y2="105" stroke="#64748B" stroke-width="1.5" />
  
  <!-- Rubber Squeeze Bulb -->
  <path d="M 182 85 C 182 50, 218 50, 218 85 Z" fill="#0F172A" stroke="#334155" stroke-width="2" />
  
  <!-- Graduated Pipette Indicator Tag -->
  <rect x="275" y="160" width="70" height="35" rx="6" fill="#1E293B" stroke="#00D2FF" stroke-width="1" />
  <text x="310" y="176" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#00D2FF" text-anchor="middle">GRADUATED</text>
  <text x="310" y="188" font-family="'Inter', sans-serif" font-size="7" fill="#CBD5E1" text-anchor="middle">1.0mL PIPETTE</text>
</svg>'''
        return svg

    elif ptype == "amber_nasal_spray":
        # 10ml Metered Spray Atomizer for Semax / Selank
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" /><stop offset="100%" stop-color="#070D14" />
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#78350F" /><stop offset="50%" stop-color="#92400E" /><stop offset="100%" stop-color="#451A03" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bgGrad)" />
  <ellipse cx="200" cy="360" rx="110" ry="16" fill="#00D2FF" opacity="0.15" />
  <ellipse cx="200" cy="358" rx="80" ry="11" fill="#0D1B2A" stroke="#00D2FF" stroke-width="1.5" stroke-opacity="0.4" />
  
  <!-- 10ml Amber Glass Body -->
  <rect x="150" y="160" width="100" height="185" rx="14" fill="url(#amberGrad)" stroke="#B45309" stroke-width="2" />
  
  <!-- Label -->
  <rect x="152" y="180" width="96" height="120" rx="4" fill="#FFFFFF" />
  <rect x="152" y="180" width="96" height="6" fill="#0284C7" />
  <text x="200" y="200" font-family="'Montserrat', sans-serif" font-size="8" font-weight="800" fill="#0D1B2A" text-anchor="middle">PHOENICS PEPTIDE</text>
  <text x="200" y="218" font-family="'Montserrat', sans-serif" font-size="12" font-weight="900" fill="#0284C7" text-anchor="middle">{name}</text>
  <text x="200" y="232" font-family="'Space Mono', monospace" font-size="9" font-weight="700" fill="#0D1B2A" text-anchor="middle">{strength}</text>
  <rect x="160" y="240" width="80" height="14" rx="7" fill="#E0F2FE" />
  <text x="200" y="250" font-family="'Inter', sans-serif" font-size="7.5" font-weight="700" fill="#0369A1" text-anchor="middle">METERED SPRAY 0.1mL</text>
  <text x="200" y="270" font-family="'Space Mono', monospace" font-size="6.5" fill="#64748B" text-anchor="middle">HPLC &ge; {purity}</text>
  
  <!-- Atomizer Pump Collar -->
  <rect x="175" y="130" width="50" height="32" rx="3" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" />
  <!-- Finger Wings -->
  <path d="M 160 138 L 240 138 L 235 146 L 165 146 Z" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1" />
  <!-- Spray Nozzle Stem -->
  <rect x="188" y="70" width="24" height="60" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
  <!-- Nozzle Tip -->
  <rect x="194" y="58" width="12" height="14" rx="2" fill="#0284C7" />
  <!-- Translucent Protective Cap -->
  <path d="M 180 50 L 220 50 L 225 130 L 175 130 Z" fill="#38BDF8" fill-opacity="0.15" stroke="#38BDF8" stroke-width="1" stroke-dasharray="3,3" />
</svg>'''
        return svg

    elif ptype == "microplate_384":
        # 384-Peptide High-Throughput Screening Array Plate
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" /><stop offset="100%" stop-color="#070D14" />
    </linearGradient>
    <linearGradient id="plateGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" /><stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bgGrad)" />
  <ellipse cx="200" cy="340" rx="150" ry="25" fill="#00D2FF" opacity="0.2" />
  
  <!-- SBS Standard Microtiter Plate 3D Perspective -->
  <g transform="translate(45, 100)">
    <!-- Plate Base -->
    <polygon points="0,60 120,0 310,0 190,60" fill="#0F172A" stroke="#00D2FF" stroke-width="2" />
    <polygon points="0,60 190,60 190,180 0,180" fill="#1B263B" stroke="#00D2FF" stroke-width="1.5" />
    <polygon points="190,60 310,0 310,120 190,180" fill="#0D1B2A" stroke="#00D2FF" stroke-width="1.5" />

    <!-- 96/384 Wells Grid Matrix Simulated -->
    <g transform="translate(20, 20) skewX(-45) scale(0.7, 0.5)">
      <!-- Wells array -->
      <circle cx="30" cy="30" r="10" fill="#0284C7" opacity="0.8"/>
      <circle cx="60" cy="30" r="10" fill="#00D2FF" opacity="0.9"/>
      <circle cx="90" cy="30" r="10" fill="#38BDF8" opacity="0.7"/>
      <circle cx="120" cy="30" r="10" fill="#F59E0B" opacity="0.9"/>
      <circle cx="150" cy="30" r="10" fill="#10B981" opacity="0.8"/>
      <circle cx="180" cy="30" r="10" fill="#818CF8" opacity="0.9"/>

      <circle cx="30" cy="60" r="10" fill="#0284C7" opacity="0.8"/>
      <circle cx="60" cy="60" r="10" fill="#00D2FF" opacity="0.9"/>
      <circle cx="90" cy="60" r="10" fill="#38BDF8" opacity="0.7"/>
      <circle cx="120" cy="60" r="10" fill="#F59E0B" opacity="0.9"/>
      <circle cx="150" cy="60" r="10" fill="#10B981" opacity="0.8"/>
      <circle cx="180" cy="60" r="10" fill="#818CF8" opacity="0.9"/>

      <circle cx="30" cy="90" r="10" fill="#0284C7" opacity="0.8"/>
      <circle cx="60" cy="90" r="10" fill="#00D2FF" opacity="0.9"/>
      <circle cx="90" cy="90" r="10" fill="#38BDF8" opacity="0.7"/>
      <circle cx="120" cy="90" r="10" fill="#F59E0B" opacity="0.9"/>
      <circle cx="150" cy="90" r="10" fill="#10B981" opacity="0.8"/>
      <circle cx="180" cy="90" r="10" fill="#818CF8" opacity="0.9"/>
    </g>

    <!-- Barcode & Plate Identifier on Front Edge -->
    <rect x="25" y="100" width="140" height="55" rx="4" fill="#FFFFFF" />
    <text x="95" y="118" font-family="'Montserrat', sans-serif" font-size="9" font-weight="900" fill="#0D1B2A" text-anchor="middle">PHOENICS 384-ARRAY</text>
    <text x="95" y="132" font-family="'Space Mono', monospace" font-size="8" font-weight="700" fill="#0284C7" text-anchor="middle">LOT #PX-384-MASTER</text>
    <rect x="40" y="138" width="110" height="10" fill="#000"/>
  </g>

  <!-- High-Throughput Verification Stamp -->
  <rect x="230" y="40" width="130" height="40" rx="6" fill="#0D1B2A" stroke="#F59E0B" stroke-width="1.5" />
  <text x="295" y="58" font-family="'Montserrat', sans-serif" font-size="9" font-weight="800" fill="#FCD34D" text-anchor="middle">384 PEPTIDE SUITE</text>
  <text x="295" y="70" font-family="'Inter', sans-serif" font-size="8" fill="#CBD5E1" text-anchor="middle">100% ESI-MS VERIFIED</text>
</svg>'''
        return svg

    elif ptype == "bulk_jar":
        # 100ml Wide-Mouth Heavy Amber Storage Jar for 10 Grams
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" /><stop offset="100%" stop-color="#070D14" />
    </linearGradient>
    <linearGradient id="amberJar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#78350F" /><stop offset="50%" stop-color="#92400E" /><stop offset="100%" stop-color="#451A03" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bgGrad)" />
  <ellipse cx="200" cy="355" rx="130" ry="20" fill="#F59E0B" opacity="0.15" />
  
  <!-- 100ml Wide Amber Glass Body -->
  <rect x="120" y="140" width="160" height="200" rx="20" fill="url(#amberJar)" stroke="#B45309" stroke-width="2.5" />
  
  <!-- Heavy Ribbed Black Cap -->
  <rect x="128" y="100" width="144" height="42" rx="4" fill="#0F172A" stroke="#334155" stroke-width="2" />
  <line x1="138" y1="104" x2="138" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="152" y1="104" x2="152" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="168" y1="104" x2="168" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="184" y1="104" x2="184" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="200" y1="104" x2="200" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="216" y1="104" x2="216" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="232" y1="104" x2="232" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="248" y1="104" x2="248" y2="138" stroke="#475569" stroke-width="2" />
  <line x1="262" y1="104" x2="262" y2="138" stroke="#475569" stroke-width="2" />

  <!-- Master Batch Label -->
  <rect x="130" y="170" width="140" height="135" rx="4" fill="#FFFFFF" />
  <rect x="130" y="170" width="140" height="8" fill="#F59E0B" />
  <text x="200" y="194" font-family="'Montserrat', sans-serif" font-size="10" font-weight="900" fill="#0D1B2A" text-anchor="middle">PHOENICS PEPTIDE</text>
  <text x="200" y="214" font-family="'Montserrat', sans-serif" font-size="12" font-weight="900" fill="#0D1B2A" text-anchor="middle">{name}</text>
  <text x="200" y="232" font-family="'Space Mono', monospace" font-size="14" font-weight="700" fill="#D97706" text-anchor="middle">{strength}</text>
  <rect x="145" y="244" width="110" height="18" rx="9" fill="#FEF3C7" />
  <text x="200" y="256" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#B45309" text-anchor="middle">cGMP PHARMA GRADE</text>
  <text x="200" y="278" font-family="'Space Mono', monospace" font-size="7.5" fill="#64748B" text-anchor="middle">PURITY &ge; {purity} • LOT #PP-10G</text>
</svg>'''
        return svg


def generate_coa_svg(p):
    name = p["name"].upper()
    cas = p["cas"]
    mw = p["mw"]
    purity = p["purity"]
    rt = p["rt"]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgCoa" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" /><stop offset="100%" stop-color="#020617" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bgCoa)" />

  <!-- Report White Paper Container -->
  <rect x="25" y="20" width="350" height="360" rx="8" fill="#FFFFFF" />
  <rect x="25" y="20" width="350" height="8" rx="4" fill="#0D1B2A" />

  <!-- Header -->
  <text x="45" y="48" font-family="'Montserrat', sans-serif" font-size="12" font-weight="900" fill="#0D1B2A">PHOENICS PEPTIDE</text>
  <text x="355" y="48" font-family="'Space Mono', monospace" font-size="8" font-weight="700" fill="#64748B" text-anchor="end">ANALYTICAL CERTIFICATE</text>
  <line x1="45" y1="56" x2="355" y2="56" stroke="#E2E8F0" stroke-width="1" />

  <!-- Sample Specs Table -->
  <g font-family="'Inter', sans-serif" font-size="8.5" fill="#334155">
    <text x="45" y="74"><strong>Compound:</strong> {name[:24]}</text>
    <text x="210" y="74"><strong>CAS No:</strong> {cas[:16]}</text>
    <text x="45" y="90"><strong>Mol Weight:</strong> {mw}</text>
    <text x="210" y="90"><strong>Method:</strong> RP-HPLC (C18, 214nm)</text>
    <text x="45" y="106"><strong>Purity Result:</strong> <tspan fill="#059669" font-weight="800">&ge; {purity} (PASSED)</tspan></text>
    <text x="210" y="106"><strong>Retention:</strong> {rt}</text>
  </g>

  <!-- RP-HPLC CHROMATOGRAM GRAPH -->
  <g transform="translate(45, 120)">
    <rect x="0" y="0" width="310" height="150" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1" />
    
    <!-- Grid Lines -->
    <line x1="0" y1="30" x2="310" y2="30" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="0" y1="60" x2="310" y2="60" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="0" y1="90" x2="310" y2="90" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="0" y1="120" x2="310" y2="120" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>

    <line x1="60" y1="0" x2="60" y2="150" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="120" y1="0" x2="120" y2="150" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="180" y1="0" x2="180" y2="150" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="240" y1="0" x2="240" y2="150" stroke="#E2E8F0" stroke-width="1" stroke-dasharray="2,2"/>

    <!-- The Sharp HPLC Analyte Peak Curve (>99% purity) -->
    <path d="M 10 145 L 80 144 L 110 144 L 125 142 L 132 135 L 142 15 L 152 135 L 160 143 L 220 144 L 300 145" fill="none" stroke="#0284C7" stroke-width="2.5" />
    <polygon points="125,142 132,135 142,15 152,135 160,143" fill="#38BDF8" fill-opacity="0.25" />

    <!-- Peak Label -->
    <text x="142" y="10" font-family="'Space Mono', monospace" font-size="8" font-weight="700" fill="#0369A1" text-anchor="middle">RT: {rt} ({purity})</text>
  </g>

  <!-- Electrospray Mass Spec Peak Inset -->
  <g transform="translate(230, 130)">
    <rect x="0" y="0" width="115" height="50" rx="3" fill="#FFFFFF" stroke="#94A3B8" stroke-width="1" />
    <text x="6" y="12" font-family="'Inter', sans-serif" font-size="7" font-weight="700" fill="#475569">ESI-MS [M+H]+</text>
    <path d="M 10 42 L 50 42 L 58 16 L 66 42 L 105 42" fill="none" stroke="#DC2626" stroke-width="1.5" />
    <text x="58" y="12" font-family="'Space Mono', monospace" font-size="6.5" font-weight="700" fill="#DC2626" text-anchor="middle">{mw.split()[0]}</text>
  </g>

  <!-- Official Gold QA Stamp -->
  <circle cx="310" cy="325" r="28" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2" />
  <circle cx="310" cy="325" r="24" fill="none" stroke="#D97706" stroke-width="1" stroke-dasharray="3,2" />
  <text x="310" y="322" font-family="'Montserrat', sans-serif" font-size="8" font-weight="900" fill="#B45309" text-anchor="middle">PHOENICS QA</text>
  <text x="310" y="333" font-family="'Montserrat', sans-serif" font-size="6.5" font-weight="800" fill="#B45309" text-anchor="middle">CERTIFIED</text>

  <!-- Signoff -->
  <text x="45" y="315" font-family="'Inter', sans-serif" font-size="8" color="#64748B"><strong>Analytical Chemist:</strong> Dr. H. Vance, Ph.D.</text>
  <text x="45" y="330" font-family="'Inter', sans-serif" font-size="8" color="#64748B"><strong>Quality Director:</strong> Dr. E. Hayes, Bio-Analytics</text>
  <text x="45" y="348" font-family="'Inter', sans-serif" font-size="7" fill="#94A3B8">In-Vitro Laboratory Reagent Only. Not for Human Diagnostic Use.</text>
</svg>'''
    return svg


def generate_pack_svg(p):
    name = p["name"].upper()
    strength = p["strength"]
    btheme = p["box_theme"]
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bgPack" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0B132B" /><stop offset="100%" stop-color="#070D14" />
    </linearGradient>
    <linearGradient id="boxGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" /><stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
  </defs>
  <rect width="400" height="400" fill="url(#bgPack)" />
  <ellipse cx="200" cy="355" rx="140" ry="22" fill="#00D2FF" opacity="0.15" />
  
  <!-- Bio-Thermal Insulated Multi-Vial Presentation Box -->
  <g transform="translate(60, 90)">
    <!-- Box Shadow & Outer Lid Open Perspective -->
    <polygon points="0,50 140,0 280,50 140,100" fill="#0D1B2A" stroke="#00D2FF" stroke-width="1.5" />
    <polygon points="0,50 140,100 140,210 0,160" fill="url(#boxGrad)" stroke="#00D2FF" stroke-width="1.5" />
    <polygon points="140,100 280,50 280,160 140,210" fill="#0B132B" stroke="#00D2FF" stroke-width="1.5" />

    <!-- Open Lid Flap -->
    <polygon points="0,50 140,0 140,-40 0,10" fill="#1B263B" stroke="#00D2FF" stroke-width="1" />
    
    <!-- Gold Embossed Branding on Inside Box -->
    <text x="65" y="10" font-family="'Montserrat', sans-serif" font-size="9" font-weight="900" fill="#FCD34D" transform="rotate(-15)">PHOENICS PEPTIDE</text>

    <!-- Foam Inserts With Vials Nested -->
    <ellipse cx="60" cy="80" rx="14" ry="7" fill="#0284C7" />
    <ellipse cx="100" cy="72" rx="14" ry="7" fill="#0284C7" />
    <ellipse cx="140" cy="65" rx="14" ry="7" fill="#0284C7" />
    <ellipse cx="180" cy="58" rx="14" ry="7" fill="#0284C7" />
    <ellipse cx="220" cy="50" rx="14" ry="7" fill="#0284C7" />

    <!-- Electronic Digital Cold-Chain Temperature Tag (-20.0°C) -->
    <rect x="160" y="125" width="95" height="50" rx="6" fill="#030712" stroke="#38BDF8" stroke-width="1.5" />
    <rect x="166" y="132" width="83" height="26" rx="3" fill="#0F172A" />
    <text x="208" y="150" font-family="'Space Mono', monospace" font-size="14" font-weight="700" fill="#00D2FF" text-anchor="middle">-20.0&deg;C</text>
    <text x="208" y="168" font-family="'Inter', sans-serif" font-size="7" font-weight="800" fill="#10B981" text-anchor="middle">STABLE &bull; COLD-CHAIN OK</text>

    <!-- Holographic Tamper-Evident Security Seal -->
    <rect x="30" y="135" width="90" height="35" rx="3" fill="#E2E8F0" stroke="#CBD5E1" stroke-width="1" />
    <text x="75" y="150" font-family="'Montserrat', sans-serif" font-size="7" font-weight="900" fill="#0D1B2A" text-anchor="middle">PHOENICS TAMPER SEAL</text>
    <text x="75" y="162" font-family="'Space Mono', monospace" font-size="6.5" fill="#0284C7" text-anchor="middle">#SEC-9840219-PHX</text>
  </g>

  <!-- Box Top Floating Tag -->
  <rect x="120" y="45" width="160" height="26" rx="13" fill="#0D1B2A" stroke="#00D2FF" stroke-width="1" />
  <text x="200" y="62" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#38BDF8" text-anchor="middle">BIO-THERMAL INSULATED KIT</text>
</svg>'''
    return svg

# WRITE ALL ASSETS TO BOTH DIRECTORIES
dirs = [
    r"c:\Users\DATA ENG. OLA\Desktop\Riffmax Technology\riffmax-org-agent\phoenicspeptide\standalone-preview\assets\images\products",
    r"c:\Users\DATA ENG. OLA\Desktop\Riffmax Technology\riffmax-org-agent\phoenicspeptide\phoenics-theme\assets\images\products"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    for p in products:
        code = p["code"]
        # 1. Vial
        vial_path = os.path.join(d, f"{code}-vial.svg")
        with open(vial_path, "w", encoding="utf-8") as f:
            f.write(generate_vial_svg(p))
            
        # 2. CoA
        coa_path = os.path.join(d, f"{code}-coa.svg")
        with open(coa_path, "w", encoding="utf-8") as f:
            f.write(generate_coa_svg(p))
            
        # 3. Packaging
        pack_path = os.path.join(d, f"{code}-pack.svg")
        with open(pack_path, "w", encoding="utf-8") as f:
            f.write(generate_pack_svg(p))

print(f"Successfully generated 54 unique SVG images (3 per product) for {len(products)} products across both directories!")
