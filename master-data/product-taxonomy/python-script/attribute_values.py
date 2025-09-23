import csv
import json

# Input file
ATTRIBUTE_VALUES_FILE = "attribute_values.json"

OUT_ATTRIBUTE_VAL = "erp_item_attribute_value_all.csv"

# Load JSON
with open(ATTRIBUTE_VALUES_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

attribute_values_list = []

# Parse handle: "attribute_name__value"
for val in data.get("values", []):
    handle = val.get("handle")
    val_id = val.get("id")
    val_name = val.get("name")
    if not handle or "__" not in handle:
        continue
    attr_name, attr_val = handle.split("__", 1)
    # Clean dashes and capitalize
    attr_name = attr_name.replace("-", " ").title()
    attr_val = val_name.replace("-", " ").title()
    attribute_values_list.append((attr_name, attr_val, val_id))

# Deduplicate
unique_attribute_values = list({av for av in attribute_values_list})

# Sort by Attribute Name, then Attribute Value
unique_attribute_values.sort(key=lambda x: (x[0], x[1]))

# Write CSV
with open(OUT_ATTRIBUTE_VAL, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Attribute Name", "Attribute Value", "ID"])
    for av in unique_attribute_values:
        w.writerow(av)

print("✅ Attribute Values CSV generated, sorted by Attribute Name and Value:", OUT_ATTRIBUTE_VAL)
