import json
import os
import logging


def attribute_type(attribute_data):
    data_type = str(type(attribute_data))
    if "str" in data_type:
        return "STRING" 
    elif "dict" in data_type:
        return "ENUM" 
    elif "list" in data_type:
        return "ARRAY" 
    return "INTEGER"



def json_reader(json_file_path, file_index):
    json_reader_logger = logging.getLogger("JSON_reader")
    logging.basicConfig(level=logging.INFO)
    try:
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)
            # json_data = {}
            message_attributes = json_data['message'] if json_data.keys().__contains__('message') else None
            error_message = "This data file has no 'message' attribute."
            if not message_attributes:
                raise AttributeError(error_message)
        message_attribute_keys = message_attributes.keys()
        required_schema_dict = {}
        for key in message_attribute_keys:
            attr_type = attribute_type(message_attributes[key])
            required_schema_dict[key] = {
                "type": attr_type,
                "tag": "",
                "description": "",
                "required": False
            }
        required_json_schema = json.dumps(required_schema_dict)
        schema_file_path = os.path.join(os.path.dirname(__file__), f"../schema/schema_{file_index}.json")
        with open(schema_file_path, "w")as schema_file:
            schema_file.write(required_json_schema)
            json_reader_logger.info("Operation fiinished successfully")
    except Exception as json_reader_exception:
        json_reader_logger.error(f"{json_reader_exception}")

