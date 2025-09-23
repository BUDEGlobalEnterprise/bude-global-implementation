# bonus_erpnext_config_generator.py
import json
import csv
from datetime import datetime

def generate_erpnext_import_config():
    """Generate configuration files for ERPNext import"""
    
    config = {
        "import_settings": {
            "date_format": "YYYY-MM-DD",
            "ignore_encoding_errors": True,
            "submit_after_import": False,
            "mute_emails": True
        },
        "field_mapping": {
            "item_group": {
                "required": ["Item Group", "Parent Item Group", "Is Group"],
                "optional": ["Description", "Tags", "Level"]
            },
            "item_attribute": {
                "required": ["Attribute Name"],
                "optional": ["Description", "Attribute Type", "Required"]
            }
        },
        "validation_rules": {
            "is_group": "0 or 1",
            "level": "integer >= 0",
            "required": "Yes or No"
        }
    }
    
    with open("erpnext_import_config.json", "w") as f:
        json.dump(config, f, indent=2)
    
    # Generate import template
    template = {
        "doctype": "Data Import",
        "import_type": "Insert New Records",
        "reference_doctype": "Item Group",
        "import_file": "erp_item_group_all.csv"
    }
    
    with open("import_template.json", "w") as f:
        json.dump(template, f, indent=2)
    
    print("✅ ERPNext import configuration generated!")
    print("   - erpnext_import_config.json")
    print("   - import_template.json")

def generate_sample_erpnext_records():
    """Generate sample ERPNext item records based on taxonomy"""
    
    sample_items = []
    categories_with_attrs = []
    
    # Read the taxonomy mapping to find categories with attributes
    try:
        with open("erp_taxonomy_mapping.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Has Attributes"] == "Yes":
                    categories_with_attrs.append(row["Category Name"])
    except FileNotFoundError:
        print("⚠️  Taxonomy mapping file not found. Run the main script first.")
        return
    
    # Generate sample items for top categories
    for category in categories_with_attrs[:5]:  # Limit to 5 for sample
        sample_items.append({
            "item_code": f"Sample_{category.replace(' ', '_').upper()}",
            "item_name": f"Sample {category} Product",
            "item_group": category,
            "description": f"Sample product from {category} category",
            "is_stock_item": 1,
            "stock_uom": "Nos",
            "standard_rate": 100.0
        })
    
    with open("sample_erpnext_items.csv", "w", newline="", encoding="utf-8") as f:
        if sample_items:
            writer = csv.DictWriter(f, fieldnames=sample_items[0].keys())
            writer.writeheader()
            writer.writerows(sample_items)
            
            print("✅ Sample ERPNext items generated!")
            print("   - sample_erpnext_items.csv")
        else:
            print("⚠️  No categories with attributes found for sample generation.")

if __name__ == "__main__":
    generate_erpnext_import_config()
    generate_sample_erpnext_records()