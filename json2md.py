import json
import sys

convert_data = {
        "Event" : "Event \n",
        "orgc_id" : "Event ID",
        "ShadowAttribute" : "Shadow Attribute",
        "id" : "ID",
        "threat_level_id" : "Threat level ID",
        "uuid" : "uuid",
        "Orgc" : "Organisation (Orgc)",
        "timestamp" : "Timestamp",
        "Org" : "Organisation (Org)",
        "RelatedEvent" : "Related Events",
        "sharing_group_id" : "Sharing group ID",
        "date" : "Date",
        "info" : "Informations",
        "locked" : "Locked",
        "publish_timestamp" : "Publish Timestamp",
        "event_id" : "Event ID",
        "to_ids" : "To IDs",
        "value" : "Value",
        "deleted" : "Deleted",
        "SharingGroup" : "Sharing Group",
        "distribution" : "Distribution",
        "category" : "Category",
        "colour" : "Colour",
        "exportable" : "Exportable"
        }

def add_tab(tab_count, string):
    ret = ""
    i = 0
    while (i < tab_count):
        ret += "#"
        i += 1
    return ret + " " + string

def get_name(string):
    if string in convert_data:
        return convert_data[string]
    else:
        return string

def convert(array, tab_count):
    text_to_convert = array.keys()[0]
    text_converted = ""
    current_tab = tab_count
    for key in array:
        # The dict element contains another dict
        if (isinstance(array[key], list)) or (isinstance(array[key], dict)):
            text_converted += add_tab(current_tab, get_name(key)) + "\n" + convert_list(array[key], current_tab+4)
        else:
            text_converted += convert_generic(array, key, current_tab) + "\n"
    return text_converted

def convert_list(list_to_convert, tab_count):
    ret = ""
    #ret = add_tab(tab_count, "")
    for i, val in enumerate(list_to_convert):
        #ret += add_tab(tab_count, "")
        if (isinstance(val, list)) or (isinstance(val, dict)):
            #for i, subval in enumerate(val):
           # ret += add_tab(tab_count, "")
           #     ret += subval + " : " + str(val[subval]) + "\n"
            ret += convert(val, tab_count)
            #ret += convert_list(val, tab_count+1)
        else:
            ret += add_tab(tab_count, "")
            ret += get_name(val) + " : " + str(list_to_convert[val]) + "\n"
    return ret

def convert_generic(array, name, tab_count):
    converted_text = ""
    converted_text = add_tab(tab_count, "")
    converted_text += get_name(name) + " : " + str(array[name])
    return converted_text

def convert_title(dic):
    name = convert_data["".join(dic)].translate(None, ' \n')
    converted_text = "# " + name + "\n"
    converted_text += convert(dic[name], 2)
    return converted_text

if (len(sys.argv) == 2):
    with open(sys.argv[1]) as json_file:
        json_data = json.load(json_file)
        converted_text = convert_title(json_data)
        print (converted_text)
else:
    print("Usage: json2md file.json")
