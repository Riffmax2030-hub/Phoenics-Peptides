import csv

code_map = {
    1: "tirzepatide",
    2: "retatrutide",
    3: "semaglutide",
    4: "cagrilintide",
    5: "bpc157",
    6: "tb500",
    7: "ghkcu",
    8: "cjcipam",
    9: "tesamorelin",
    10: "mk677",
    11: "motsc",
    12: "epithalon",
    13: "semax",
    14: "selank",
    15: "pt141",
    16: "library384",
    17: "bulk10g",
    18: "kinase96",
}

csv_path = "setup/products.csv"

rows = []
with open(csv_path, mode="r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    img_col_idx = header.index("Images")
    id_col_idx = header.index("ID")
    
    for row in reader:
        if not row or len(row) <= id_col_idx:
            continue
        try:
            prod_id = int(row[id_col_idx])
            if prod_id in code_map:
                code = code_map[prod_id]
                base = "wp-content/themes/phoenics-theme/assets/images/products"
                row[img_col_idx] = f"{base}/{code}-vial.svg, {base}/{code}-coa.svg, {base}/{code}-pack.svg"
        except ValueError:
            pass
        rows.append(row)

with open(csv_path, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Successfully updated setup/products.csv with 3-image galleries for all 18 products.")
