import csv
import json
from datetime import datetime

# Input full taxonomy.json
TAXONOMY_FILE = "taxonomy.json"

OUT_ITEM_GROUP = "erp_item_group_all.csv"
OUT_ATTRIBUTE = "erp_item_attribute_all.csv"
OUT_ATTRIBUTE_VAL = "erp_item_attribute_value_all.csv"
OUT_TAXONOMY_MAPPING = "erp_taxonomy_mapping.csv"

with open(TAXONOMY_FILE, "r", encoding="utf-8") as f:
    taxonomy = json.load(f)

item_groups = []
attributes = {}
attribute_values_list = []
taxonomy_mappings = []

# For hierarchy: category id -> name
cat_id_map = {}
cat_details = {}  # Store full category details

# Helper to walk categories recursively
def walk_category(cat, parent_name="All Item Groups", parent_id="", level=0):
    cat_name = cat.get("name", "")
    cat_id = cat.get("id", "")
    cat_description = cat.get("description", "")
    cat_tags = cat.get("tags", [])
    
    if not cat_name:
        return
    
    # Store category details
    cat_id_map[cat_id] = cat_name
    cat_details[cat_id] = {
        "name": cat_name,
        "description": cat_description,
        "tags": cat_tags,
        "parent_id": parent_id,
        "level": level
    }
    
    is_group = 1 if cat.get("children") else 0
    
    # Enhanced item group with more fields
    item_groups.append({
        "item_group": cat_name,
        "parent_item_group": parent_name,
        "is_group": is_group,
        "item_group_name": cat_name,
        "description": cat_description,
        "tags": ", ".join(cat_tags) if cat_tags else "",
        "level": level,
        "category_id": cat_id,
        "parent_category_id": parent_id
    })
    
    # Process attributes with enhanced fields
    for attr in cat.get("attributes", []):
        attr_id = attr.get("id", "")
        attr_name = attr.get("name", "")
        attr_description = attr.get("description", "")
        attr_type = attr.get("type", "text")
        attr_required = attr.get("required", False)
        
        if not attr_name:
            continue
            
        # Store attribute details
        attributes[attr_name] = {
            "id": attr_id,
            "description": attr_description,
            "type": attr_type,
            "required": attr_required,
            "category_id": cat_id
        }
        
        # Process attribute values with enhanced fields
        for val in attr.get("values", []):
            val_name = val.get("name", "")
            val_description = val.get("description", "")
            val_id = val.get("id", "")
            
            if val_name:
                attribute_values_list.append({
                    "attribute_name": attr_name,
                    "attribute_value": val_name,
                    "value_description": val_description,
                    "value_id": val_id,
                    "attribute_id": attr_id,
                    "category_id": cat_id
                })
    
    # Taxonomy mapping for ERPNext
    taxonomy_mappings.append({
        "category_id": cat_id,
        "category_name": cat_name,
        "parent_category_id": parent_id,
        "parent_category_name": parent_name,
        "level": level,
        "has_attributes": len(cat.get("attributes", [])) > 0,
        "has_children": len(cat.get("children", [])) > 0,
        "description": cat_description,
        "tags": ", ".join(cat_tags) if cat_tags else ""
    })
    
    # Recurse children
    for child in cat.get("children", []):
        walk_category(child, cat_name, cat_id, level + 1)

# Handle verticals → categories
for vertical in taxonomy.get("verticals", []):
    vertical_name = vertical.get("name", "General")
    vertical_id = vertical.get("id", "")
    
    for cat in vertical.get("categories", []):
        walk_category(cat, vertical_name, vertical_id, 1)

# Also handle top-level attributes outside verticals
top_attrs = taxonomy.get("attributes", {})
if top_attrs and isinstance(top_attrs, dict):
    attr_name = top_attrs.get("name", "")
    if attr_name:
        attributes[attr_name] = {
            "id": top_attrs.get("id", ""),
            "description": top_attrs.get("description", ""),
            "type": top_attrs.get("type", "text"),
            "required": top_attrs.get("required", False),
            "category_id": "top_level"
        }
        
        for val in top_attrs.get("values", []):
            val_name = val.get("name", "")
            if val_name:
                attribute_values_list.append({
                    "attribute_name": attr_name,
                    "attribute_value": val_name,
                    "value_description": val.get("description", ""),
                    "value_id": val.get("id", ""),
                    "attribute_id": top_attrs.get("id", ""),
                    "category_id": "top_level"
                })

# Deduplicate item groups
seen = set()
unique_item_groups = []
for ig in item_groups:
    key = (ig["item_group"], ig["parent_item_group"])
    if key not in seen:
        seen.add(key)
        unique_item_groups.append(ig)

# Generate metadata for the export
metadata = {
    "export_date": datetime.now().isoformat(),
    "total_categories": len(unique_item_groups),
    "total_attributes": len(attributes),
    "total_attribute_values": len(attribute_values_list),
    "source_file": TAXONOMY_FILE
}

# --- Write Enhanced CSVs ---

# Item Groups CSV with descriptions
with open(OUT_ITEM_GROUP, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        "Item Group", "Parent Item Group", "Is Group", "Item Group Name", 
        "Description", "Tags", "Level", "Category ID", "Parent Category ID"
    ])
    
    # Add root item group
    w.writerow(["All Item Groups", "", 1, "All Item Groups", 
                "Root category for all item groups", "", 0, "root", ""])
    
    for ig in unique_item_groups:
        w.writerow([
            ig["item_group"],
            ig["parent_item_group"],
            ig["is_group"],
            ig["item_group_name"],
            ig["description"],
            ig["tags"],
            ig["level"],
            ig["category_id"],
            ig["parent_category_id"]
        ])

# Attributes CSV with enhanced fields
with open(OUT_ATTRIBUTE, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        "Attribute Name", "Attribute ID", "Description", "Attribute Type", 
        "Required", "Numeric Values", "From Range", "To Range", "Increment", "Category ID"
    ])
    
    for attr_name, attr_data in attributes.items():
        # Determine if numeric based on type
        numeric_values = 1 if attr_data["type"] in ["number", "integer", "float"] else 0
        
        w.writerow([
            attr_name,
            attr_data["id"],
            attr_data["description"],
            attr_data["type"],
            "Yes" if attr_data["required"] else "No",
            numeric_values,
            "",  # From Range - could be populated from attribute data if available
            "",  # To Range
            "",  # Increment
            attr_data["category_id"]
        ])

# Attribute Values CSV with descriptions
with open(OUT_ATTRIBUTE_VAL, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        "Attribute Name", "Attribute Value", "Value Description", 
        "Value ID", "Attribute ID", "Category ID"
    ])
    
    # Deduplicate
    seen_vals = set()
    for av in attribute_values_list:
        key = (av["attribute_name"], av["attribute_value"])
        if key not in seen_vals:
            seen_vals.add(key)
            w.writerow([
                av["attribute_name"],
                av["attribute_value"],
                av["value_description"],
                av["value_id"],
                av["attribute_id"],
                av["category_id"]
            ])

# Taxonomy Mapping CSV for reference
with open(OUT_TAXONOMY_MAPPING, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        "Category ID", "Category Name", "Parent Category ID", "Parent Category Name",
        "Level", "Has Attributes", "Has Children", "Description", "Tags"
    ])
    
    for mapping in taxonomy_mappings:
        w.writerow([
            mapping["category_id"],
            mapping["category_name"],
            mapping["parent_category_id"],
            mapping["parent_category_name"],
            mapping["level"],
            "Yes" if mapping["has_attributes"] else "No",
            "Yes" if mapping["has_children"] else "No",
            mapping["description"],
            mapping["tags"]
        ])

# Generate a summary report
print("✅ Enhanced ERPNext CSVs generated with full hierarchy and descriptions:")
print(f"📊 Export Summary:")
print(f"   - Date: {metadata['export_date']}")
print(f"   - Total Categories: {metadata['total_categories']}")
print(f"   - Total Attributes: {metadata['total_attributes']}")
print(f"   - Total Attribute Values: {metadata['total_attribute_values']}")
print()
print("📁 Generated Files:")
print(f"   - {OUT_ITEM_GROUP} (Item groups with descriptions and hierarchy)")
print(f"   - {OUT_ATTRIBUTE} (Attributes with types and requirements)")
print(f"   - {OUT_ATTRIBUTE_VAL} (Attribute values with descriptions)")
print(f"   - {OUT_TAXONOMY_MAPPING} (Taxonomy mapping reference)")
print()
print("🎯 Enhanced Features:")
print("   ✓ Descriptions for categories and attributes")
print("   ✓ Tag support for categorization")
print("   ✓ Hierarchy levels for better organization")
print("   ✓ Attribute types and requirement flags")
print("   ✓ Comprehensive ID mapping for integration")
print("   ✓ Taxonomy mapping reference file")