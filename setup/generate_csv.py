import csv

products = [
    # --- HIGH DEMAND METABOLIC & GLP-1 / INCRETIN REAGENTS (US & CANADA #1) ---
    {
        "sku": "PP-TIRZ",
        "name": "Tirzepatide (Dual GIP / GLP-1 Receptor Agonist)",
        "cat": "Metabolic & Incretin Research",
        "tags": "Tirzepatide, GIP, GLP-1, dual agonist, metabolic, glucose homeostasis, weight research",
        "reg_price": 140.00,
        "sale_price": 112.00,
        "short_desc": "Highest analytical grade Tirzepatide dual GIP/GLP-1 agonist lyophilized sequence. #1 cited incretin mimetic research compound in North America. Purity: ≥99.4% (HPLC/MS).",
        "desc": "<h3>Product Specification</h3><p><strong>Tirzepatide</strong> is a synthetic 39-amino-acid linear peptide engineered with C20 fatty diacid moiety that binds selectively to both human GIP and GLP-1 receptors.</p><ul><li><strong>CAS Number:</strong> 2023788-19-2</li><li><strong>Molecular Formula:</strong> C225H348N48O68</li><li><strong>Molecular Weight:</strong> 4813.45 g/mol</li><li><strong>Purity:</strong> ≥99.4% via Reverse-Phase HPLC</li><li><strong>Physical Appearance:</strong> Sterile white lyophilized powder</li><li><strong>Storage:</strong> -20°C non-frost-free</li></ul>",
        "sizes": "5mg, 10mg, 15mg, 30mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-RETA",
        "name": "Retatrutide (Triple GGG: GLP-1 / GIP / GCGR Agonist)",
        "cat": "Metabolic & Incretin Research",
        "tags": "Retatrutide, triple agonist, GGG, GLP-1, GIP, Glucagon, adipocyte lipolysis, thermogenesis",
        "reg_price": 175.00,
        "sale_price": 139.00,
        "short_desc": "Breakthrough triple-agonist peptide targeting GLP-1, GIP, and Glucagon receptors simultaneously. Leading next-generation metabolic research compound in the US and Canada. Purity: ≥99.3%.",
        "desc": "<h3>Product Specification</h3><p><strong>Retatrutide</strong> is a single-peptide triple hormone receptor agonist designed to stimulate energy expenditure and potent lipid clearance.</p><ul><li><strong>CAS Number:</strong> 2381089-83-2</li><li><strong>Molecular Formula:</strong> C221H342N46O68</li><li><strong>Molecular Weight:</strong> 4731.33 g/mol</li><li><strong>Purity:</strong> ≥99.3% HPLC</li></ul>",
        "sizes": "5mg, 10mg, 15mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-SEMA",
        "name": "Semaglutide (Selective GLP-1 Receptor Agonist)",
        "cat": "Metabolic & Incretin Research",
        "tags": "Semaglutide, GLP-1, incretin, insulin secretion, appetite pathways, satiety",
        "reg_price": 115.00,
        "sale_price": 89.00,
        "short_desc": "High-purity GLP-1 receptor agonist peptide functionalized with diacid spacer and albumin-binding C18 chain. Benchmark standard for metabolic signaling. Purity: ≥99.5%.",
        "desc": "<h3>Product Specification</h3><p><strong>Semaglutide</strong> is a modified GLP-1 analog with Aib at position 8 and Arg at position 34.</p><ul><li><strong>CAS Number:</strong> 910463-68-2</li><li><strong>Molecular Formula:</strong> C187H291N45O59</li><li><strong>Molecular Weight:</strong> 4113.58 g/mol</li><li><strong>Purity:</strong> ≥99.5%</li></ul>",
        "sizes": "2mg, 5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-CAGRI",
        "name": "Cagrilintide (Long-Acting Amylin Analog)",
        "cat": "Metabolic & Incretin Research",
        "tags": "Cagrilintide, amylin, calcitonin receptor, dual synergy, satiety research",
        "reg_price": 130.00,
        "sale_price": 99.00,
        "short_desc": "Acylated dual amylin and calcitonin receptor agonist. Extensively investigated in combination with GLP-1 analogs for non-leptin satiety neuro-signaling. Purity: ≥99.2%.",
        "desc": "<h3>Product Specification</h3><p><strong>Cagrilintide</strong> is a synthetic peptide analog of human amylin with extended plasma half-life.</p><ul><li><strong>CAS Number:</strong> 1415456-99-3</li><li><strong>Molecular Formula:</strong> C203H311N53O62S</li><li><strong>Molecular Weight:</strong> 4522.06 g/mol</li><li><strong>Purity:</strong> ≥99.2%</li></ul>",
        "sizes": "5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off)"
    },

    # --- CELLULAR REPAIR & REGENERATION (US/CANADA BESTSELLERS) ---
    {
        "sku": "PP-BPC157",
        "name": "BPC-157 (Body Protection Compound Pentadecapeptide)",
        "cat": "Healing & Tissue Recovery",
        "tags": "BPC-157, pentadecapeptide, gastric peptide, angiogenesis, tendon healing, ligament repair",
        "reg_price": 52.00,
        "sale_price": 39.00,
        "short_desc": "Ultra-pure lyophilized BPC-157. The benchmark sequence for cellular recovery, VEGF angiogenesis signaling, and extracellular matrix remodeling. Purity: ≥99.4%.",
        "desc": "<h3>Product Specification</h3><p><strong>BPC-157</strong> is a 15-amino acid sequence derived from human gastric juice protein.</p><ul><li><strong>CAS Number:</strong> 137525-51-0</li><li><strong>Molecular Weight:</strong> 1419.5 g/mol</li><li><strong>Purity:</strong> ≥99.4%</li></ul>",
        "sizes": "5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-TB500",
        "name": "TB-500 (Thymosin Beta-4 Active Fragment)",
        "cat": "Healing & Tissue Recovery",
        "tags": "TB-500, Thymosin Beta-4, actin sequestering, cellular migration, cardiac tissue",
        "reg_price": 58.00,
        "sale_price": 44.00,
        "short_desc": "Synthetic bioactive fragment of Thymosin Beta-4 (Ac-LKKTETQ). Primary research reagent for actin filament polymerization assays. Purity: ≥99.5%.",
        "desc": "<h3>Product Specification</h3><p><strong>TB-500</strong> corresponds to amino acids 17-23 of human Thymosin Beta-4.</p><ul><li><strong>CAS Number:</strong> 77591-33-4</li><li><strong>Molecular Weight:</strong> 4963.5 g/mol</li><li><strong>Purity:</strong> ≥99.5%</li></ul>",
        "sizes": "5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-GHKCU",
        "name": "GHK-Cu (Copper Tripeptide-1 Blue Powder)",
        "cat": "Healing & Tissue Recovery",
        "tags": "GHK-Cu, copper peptide, collagen synthesis, fibroblast, dermal remodeling",
        "reg_price": 42.00,
        "sale_price": 32.00,
        "short_desc": "High-affinity Glycyl-L-Histidyl-L-Lysine chelated with Cu2+ ion. Induces collagen, elastin, and glycosaminoglycan synthesis in fibroblast cultures. Purity: ≥99.6%.",
        "desc": "<h3>Product Specification</h3><p><strong>GHK-Cu</strong> is a bioactive copper complex widely used in dermatological and wound healing investigations.</p><ul><li><strong>CAS Number:</strong> 49557-75-7</li><li><strong>Purity:</strong> ≥99.6%</li></ul>",
        "sizes": "50mg, 100mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off)"
    },

    # --- SOMATOTROPIC & GROWTH HORMONE RECEPTOR AGONISTS ---
    {
        "sku": "PP-CJCIPAM",
        "name": "CJC-1295 + Ipamorelin Synergistic Blend (5mg + 5mg)",
        "cat": "Growth Hormone Secretagogues",
        "tags": "CJC-1295, Ipamorelin, dual synergy, GHRH, GHRP, pulsatile release",
        "reg_price": 85.00,
        "sale_price": 64.00,
        "short_desc": "Co-lyophilized synergistic research blend containing 5mg CJC-1295 (No DAC) + 5mg Ipamorelin. Dual pituitary receptor activation without prolactin/cortisol rise. Purity: ≥99.3%.",
        "desc": "<h3>Product Specification</h3><p>Combines a selective GHRH analog with a selective ghrelin/GHS-R agonist.</p><ul><li><strong>Ratio:</strong> 5mg Mod GRF 1-29 / 5mg Ipamorelin</li><li><strong>Purity:</strong> ≥99.3%</li></ul>",
        "sizes": "10mg Total (5mg/5mg)",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-TESA",
        "name": "Tesamorelin Trans-3-Hexenoyl GHRH",
        "cat": "Growth Hormone Secretagogues",
        "tags": "Tesamorelin, visceral fat, lipodystrophy, GHRH, metabolic composition",
        "reg_price": 78.00,
        "sale_price": 59.00,
        "short_desc": "Stabilized GHRH derivative with trans-3-hexenoic acid moiety. Benchmark peptide for investigations into visceral adipocyte reduction. Purity: ≥99.2%.",
        "desc": "<h3>Product Specification</h3><p><strong>Tesamorelin</strong> is a synthetic peptide analog of growth hormone-releasing factor.</p><ul><li><strong>CAS Number:</strong> 218949-48-5</li><li><strong>Purity:</strong> ≥99.2%</li></ul>",
        "sizes": "2mg, 5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off)"
    },
    {
        "sku": "PP-MK677",
        "name": "MK-677 (Ibutamoren Mesylate)",
        "cat": "Growth Hormone Secretagogues",
        "tags": "MK-677, Ibutamoren, non-peptide secretagogue, IGF-1, ghrelin mimetic",
        "reg_price": 65.00,
        "sale_price": 49.00,
        "short_desc": "Potent orally bioavailable non-peptide ghrelin receptor agonist. Sustained induction of serum GH and IGF-1 secretion in vitro. Purity: ≥99.5%.",
        "desc": "<h3>Product Specification</h3><p><strong>MK-677</strong> stimulates pituitary secretagogue receptor-1a.</p><ul><li><strong>CAS Number:</strong> 159752-10-0</li><li><strong>Purity:</strong> ≥99.5%</li></ul>",
        "sizes": "30ml Solution (25mg/ml), 60 Capsules (15mg)",
        "packs": "1 Unit, 3 Units (10% Off), 5 Units (15% Off)"
    },

    # --- MITOCHONDRIAL, LONGEVITY & NOOTROPIC PEPTIDES ---
    {
        "sku": "PP-MOTSC",
        "name": "MOTS-c (Mitochondrial-Derived Peptide)",
        "cat": "Longevity & Mitochondrial",
        "tags": "MOTS-c, mitochondrial peptide, metabolic flexibility, AMPK activation, endurance",
        "reg_price": 75.00,
        "sale_price": 56.00,
        "short_desc": "16-amino acid peptide encoded in mitochondrial 12S rRNA. Activates AMPK pathway, enhances insulin sensitivity, and promotes cellular longevity. Purity: ≥99.3%.",
        "desc": "<h3>Product Specification</h3><p><strong>MOTS-c</strong> targets the folate-methionine cycle to stimulate metabolic reprogramming.</p><ul><li><strong>Sequence:</strong> Met-Arg-Trp-Gln-Glu-Met-Gly-Tyr-Ile-Phe-Tyr-Pro-Arg-Lys-Leu-Arg</li><li><strong>Purity:</strong> ≥99.3%</li></ul>",
        "sizes": "5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off)"
    },
    {
        "sku": "PP-EPITH",
        "name": "Epithalon (Epitalon Pineal Tetra-peptide)",
        "cat": "Longevity & Mitochondrial",
        "tags": "Epithalon, Epitalon, telomerase, pineal, anti-senescence, biological clock",
        "reg_price": 60.00,
        "sale_price": 45.00,
        "short_desc": "Synthetic pineal-derived peptide (Ala-Glu-Asp-Gly). Heavily cited for induction of telomerase activity and restoration of circadian melatonin rhythms. Purity: ≥99.4%.",
        "desc": "<h3>Product Specification</h3><p><strong>Epithalon</strong> stimulates elongation of chromosomal telomeres in human somatic cell assays.</p><ul><li><strong>CAS Number:</strong> 307297-39-8</li><li><strong>Purity:</strong> ≥99.4%</li></ul>",
        "sizes": "10mg, 20mg, 50mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },
    {
        "sku": "PP-SEMAX",
        "name": "Semax Synthetic ACTH (4-10) Fragment",
        "cat": "Neuroscience & Nootropic",
        "tags": "Semax, ACTH fragment, BDNF, TrkB receptor, nootropic, neuroprotection",
        "reg_price": 55.00,
        "sale_price": 42.00,
        "short_desc": "Heptapeptide analog of ACTH(4-10) with C-terminal Pro-Gly-Pro. Stimulates rapid BDNF and NGF expression in hippocampal and cortical neurons. Purity: ≥99.5%.",
        "desc": "<h3>Product Specification</h3><p><strong>Semax</strong> is an advanced neuroactive peptide studied for ischemic stroke and cognitive support.</p><ul><li><strong>CAS Number:</strong> 80714-61-0</li><li><strong>Purity:</strong> ≥99.5%</li></ul>",
        "sizes": "30mg, 60mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off)"
    },
    {
        "sku": "PP-SELANK",
        "name": "Selank Heptapeptide Anxiolytic Ligand",
        "cat": "Neuroscience & Nootropic",
        "tags": "Selank, Tuftsin derivative, GABAergic, anxiolytic, nootropic, immune modulation",
        "reg_price": 45.00,
        "sale_price": 34.00,
        "short_desc": "Synthetic Tuftsin hexapeptide derivative. Modulates enkephalin degradation enzymes and GABAergic neurotransmission without sedative side effects. Purity: ≥99.6%.",
        "desc": "<h3>Product Specification</h3><p><strong>Selank</strong> exhibits potent neuroprotective and immunomodulatory properties.</p><ul><li><strong>CAS Number:</strong> 129954-34-3</li><li><strong>Purity:</strong> ≥99.6%</li></ul>",
        "sizes": "5mg, 10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off)"
    },
    {
        "sku": "PP-PT141",
        "name": "PT-141 (Bremelanotide Acetate)",
        "cat": "Receptor & Neuroendocrine",
        "tags": "PT-141, Bremelanotide, MC3R, MC4R, melanocortin agonist, central libido",
        "reg_price": 62.00,
        "sale_price": 47.00,
        "short_desc": "Cyclic heptapeptide melanocortin MC3-R/MC4-R agonist. Acts centrally upon hypothalamic neural receptors. Purity: ≥99.4% (HPLC/MS).",
        "desc": "<h3>Product Specification</h3><p><strong>PT-141</strong> is an active cyclic analog of alpha-MSH devoid of peripheral vascular tanning effects.</p><ul><li><strong>CAS Number:</strong> 189745-56-8</li><li><strong>Purity:</strong> ≥99.4%</li></ul>",
        "sizes": "10mg",
        "packs": "1 Vial, 3 Vials (10% Off), 5 Vials (15% Off), 10 Vials Kit (25% Off)"
    },

    # --- HIGH-TICKET INSTITUTIONAL & ACADEMIC PRODUCTS ($5,000 - $23,500+) ---
    {
        "sku": "PP-LIB-384",
        "name": "Custom Peptide Scanning & Epitope Mapping Library (384 Peptides, 96-Well Format)",
        "cat": "Institutional & Custom Synthesis",
        "tags": "peptide library, high throughput screening, epitope mapping, 384 peptides, pharma discovery, custom synthesis",
        "reg_price": 27500.00,
        "sale_price": 23450.00,
        "short_desc": "High-throughput academic & pharmaceutical peptide library. 384 distinct synthetic peptides arrayed in 96-well microtiter plates. Tailored overlapping sequences, alanine-scanning, or random combinatorial arrays for receptor profiling. Purity: ≥95.0% verified per well.",
        "desc": "<h3>Institutional Master Specification</h3><p>Designed for major university laboratories, pharmaceutical drug development, and high-throughput antibody epitope mapping. Synthesized via robotic multiplexed solid-phase synthesizers.</p><ul><li><strong>Format:</strong> 4x 96-Well Microtiter Plates (Dry Lyophilized 1mg to 5mg/well)</li><li><strong>Scale:</strong> 384 Distinct Defined Sequences (up to 20 amino acids each)</li><li><strong>Quality Control:</strong> 100% Electrospray MS Mass Validation & RP-HPLC Profile</li><li><strong>Documentation:</strong> Comprehensive 2D Plate Map, Sequence Manifest CSV, and Certificate of Analysis Package</li><li><strong>Fulfillment:</strong> Shipped in Insulated Dry-Ice Freight Container</li></ul><p><em>Notice: Academic Purchase Orders (Net 30) and Institutional Wire Transfers Accepted. Contact our synthesis director for sequence uploads.</em></p>",
        "sizes": "384-Peptide Array (1mg/well), 384-Peptide Array (5mg/well)",
        "packs": "Complete Library Master Set"
    },
    {
        "sku": "PP-BULK-10G",
        "name": "Bulk cGMP-Grade Peptide Synthesis Lot (10 Grams Lyophilized Lot)",
        "cat": "Institutional & Custom Synthesis",
        "tags": "bulk synthesis, 10 grams, cGMP grade, API reference, institutional procurement",
        "reg_price": 18500.00,
        "sale_price": 14900.00,
        "short_desc": "Large-scale bulk synthesis lot (10,000 mg) of selected catalog or custom research peptide sequence. Manufactured under stringent cleanroom protocols with complete batch validation documentation for preclinical pharmaceutical assays.",
        "desc": "<h3>Institutional Bulk Reagent Specification</h3><p>Provides research institutes and clinical trial sponsors with single-lot consistency across large preclinical cohorts.</p><ul><li><strong>Quantity:</strong> 10.0 Grams (10,000 mg) Lyophilized Cake</li><li><strong>Purity:</strong> ≥98.5% (Analytical RP-HPLC)</li><li><strong>Residual Solvent & TFA:</strong> &lt;1.0% with optional acetate salt conversion</li><li><strong>Endotoxin Level:</strong> &lt;5.0 EU/mg guaranteed</li></ul>",
        "sizes": "10 Grams (10,000mg)",
        "packs": "Single Certified Master Lot"
    },
    {
        "sku": "PP-EPITOPE-KIT",
        "name": "Kinase Profiling & Phosphorylation Target Master Suite (96 Peptides)",
        "cat": "Institutional & Custom Synthesis",
        "tags": "kinase profiling, phosphorylation, 96 peptides, screening kit, enzymatic assays",
        "reg_price": 11800.00,
        "sale_price": 9450.00,
        "short_desc": "High-density kinase substrate screening suite. 96 synthetic peptide sequences containing phosphorylated and non-phosphorylated tyrosine/serine/threonine motifs for high-throughput enzymatic kinetic assays.",
        "desc": "<h3>Institutional Suite Specification</h3><p>Enables systematic mapping of kinase inhibitor selectivity and catalytic binding affinities across 96 defined peptide targets.</p><ul><li><strong>Format:</strong> 96-Well Microplate Array</li><li><strong>Purity:</strong> ≥95%</li></ul>",
        "sizes": "96-Peptide Suite",
        "packs": "1 Complete Assay Suite"
    }
]

headers = [
    "ID", "Type", "SKU", "Name", "Published", "Is featured?", "Visibility in catalog",
    "Short description", "Description", "Date sale price starts", "Date sale price ends",
    "Tax status", "Tax class", "In stock?", "Stock", "Backorders allowed?", "Sold individually?",
    "Weight (lbs)", "Length (in)", "Width (in)", "Height (in)", "Allow customer reviews?",
    "Purchase note", "Sale price", "Regular price", "Categories", "Tags", "Shipping class",
    "Images", "Download limit", "Download expiry days", "Parent", "Grouped products",
    "Upsells", "Cross-sells", "External URL", "Button text", "Position",
    "Attribute 1 name", "Attribute 1 value(s)", "Attribute 1 visible", "Attribute 1 global",
    "Attribute 2 name", "Attribute 2 value(s)", "Attribute 2 visible", "Attribute 2 global"
]

csv_file = r"c:\Users\DATA ENG. OLA\Desktop\Riffmax Technology\riffmax-org-agent\phoenicspeptide\setup\products.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    
    for idx, p in enumerate(products, start=1):
        row = [
            idx,                        # ID
            "variable",                 # Type
            p["sku"],                   # SKU
            p["name"],                  # Name
            1,                          # Published
            1 if idx <= 6 or p["reg_price"] > 10000 else 0, # Is featured?
            "visible",                  # Visibility in catalog
            p["short_desc"],            # Short description
            p["desc"],                  # Description
            "",                         # Date sale price starts
            "",                         # Date sale price ends
            "taxable",                  # Tax status
            "",                         # Tax class
            1,                          # In stock?
            95,                         # Stock
            0,                          # Backorders allowed?
            0,                          # Sold individually?
            0.25 if p["reg_price"] < 5000 else 5.0, # Weight
            3.0, 1.5, 1.5,
            1,                          # Allow customer reviews?
            "Research order confirmed. Analytical HPLC/MS batch report and cold-chain tracking dispatched.",
            f"{p['sale_price']:.2f}",   # Sale price (DISCOUNTED ON ALL PRODUCTS)
            f"{p['reg_price']:.2f}",    # Regular price (STRIKETHROUGH)
            p["cat"],                   # Categories
            p["tags"],                  # Tags
            "cold-chain-freight",       # Shipping class
            "https://phoenicspeptide.com/wp-content/uploads/peptides/vial-sterile.jpg",
            "", "", "", "", "", "", "", "", 0,
            "Size / Scale",             # Attribute 1 name
            p["sizes"],                 # Attribute 1 value(s)
            1, 1,
            "Package Configuration",    # Attribute 2 name
            p["packs"],                 # Attribute 2 value(s)
            1, 1
        ]
        writer.writerow(row)

print(f"Generated {len(products)} products with discounts into {csv_file}")
