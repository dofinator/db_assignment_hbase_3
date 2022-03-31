#from lxml import etree as ET
import xml.etree.cElementTree as ET
import happybase

def run():
    foods = get_foods()
    connection = happybase.Connection()

def get_foods():
    root = get_root('Food_Display_Table.xml')
    foods = []
    for elem in (root):
        
        wanted_dict = {
            "Food_Code": None,
            "Display_Name": None,
            "Portion_Default": None,
            "Portion_Amount": None,
            "Portion_Display_Name": None,
            "Factor": None,
            "Increment": None,
            "Multiplier": None,
            "Grains": None,
            "Whole_Grains": None,
            "Vegetables": None,
            "Orange_Vegetables": None,
            "Drkgreen_Vegetables": None,
            "Starchy_vegetables": None,
            "Other_Vegetables": None,
            "Fruits": None,
            "Milk": None,
            "Meats": None,
            "Soy": None,
            "Drybeans_Peas": None,
            "Oils": None,
            "Solid_Fats": None,
            "Added_Sugars": None,
            "Alcohol": None,
            "Calories": None,
            "Saturated_Fats": None
        }
        wanted_dict = generic_extracting(elem,wanted_dict)
        foods.append(wanted_dict)
    return foods


def generic_extracting(etree, dict_extract):
    for wanted_tags in dict_extract.keys():  
        try:            
            generic_find = etree.find('.//{*}'+ wanted_tags)
        except AttributeError:
            continue
        if generic_find is not None:    
            text = generic_find.text
            dict_extract[wanted_tags] = text

    return dict_extract

def get_root(doc):
    try:
        tree = ET.parse(doc)
        return tree.getroot()
    except ET.XMLSyntaxError:
        return None
   