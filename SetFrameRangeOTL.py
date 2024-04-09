import hou
import json

node = hou.pwd()

# Get paths
def get_clean_name(input_string, separator):
    parts = input_string.split(separator, 1)
    result = parts[0]
    return result

# Check the name of the Houdini file to match .json data
def check_scene_name(scene_name, json_data):
    for entry in json_data:
        if entry.get('shot') == scene_name:
            print(f"The Houdini scene name '{scene_name}' is present in the JSON dictionary.")
            return entry.get('start'), entry.get('end')

    print(f"The Houdini scene name '{scene_name}' is not found in the JSON dictionary.")
    return None, None

# Get the Start and End values from the .json file        
def get_start_end_values(scene_name, json_data):
    for entry in json_data:
        if entry.get('shot') == scene_name:
            start_value = entry.get('start', None)
            end_value = entry.get('end', None)
            if start_value is not None and end_value is not None:
                print(f"For shot '{scene_name}':")
                print(f"Start Value: {start_value}")
                print(f"End Value: {end_value}")
                start_frame= int(start_value)
                end_frame = int(end_value)
                return start_frame, end_frame
            else:
                print(f"Missing 'start' or 'end' values for shot '{scene_name}' in the JSON dictionary.")
            
    print(f"Shot '{scene_name}' not found in the JSON dictionary.")
    return None, None

# Set Frame Range
def main():
    json_file_path = hou.pwd().parm("path").evalAsString()
    fullname = hou.hipFile.basename()
    separator = "."
    name = get_clean_name(fullname, separator)
    try:
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)
        start_frame, end_frame = get_start_end_values(name, json_data)
        if start_frame is not None and end_frame is not None:
            hou.playbar.setFrameRange(start_frame, end_frame)
    except FileNotFoundError:
        print(f"Error: JSON file not found at '{json_file_path}'.")
