from notion_client import Client
import json

file = open("keys.json")
data = json.load(file)
notion_token = data["token"]
notion_database_id = data["database"]
file.close()

# Write to .json
def write_dict_to_file_as_json(content, file_name):
    content_as_json_str = json.dumps(content)

    with open(file_name, 'w') as f:
        f.write(content_as_json_str)

# Read Notion information 
def read_text(client, page_id):
    response = client.blocks.children.list(block_id=page_id)
    return response['results']

# Get data from keys.json file
def safe_get(data, dot_chained_keys):
    keys = dot_chained_keys.split('.')
    for key in keys:
        try:
            if isinstance(data, list):
                data = data[int(key)]
            else:
                data = data[key]
        except (KeyError, TypeError, IndexError):
            return None
    return data

# Generate .json file
def main():
    client = Client(auth=notion_token)
    
    # Getting database
    db_info = client.databases.retrieve(database_id=notion_database_id)

    write_dict_to_file_as_json(db_info, 'db_info.json')
    # Getting pages
    db_rows = client.databases.query(database_id=notion_database_id)

    write_dict_to_file_as_json(db_rows, 'db_rows.json')

    simple_rows = []
    # Cleaning up into a readable .json
    print("Cleaning data...")
    for row in db_rows['results']:
        shot = safe_get(row, 'properties.Scene.title.0.plain_text')
        start = safe_get(row, 'properties.Start.rich_text.0.plain_text')
        end = safe_get(row, 'properties.End.rich_text.0.plain_text')

        simple_rows.append({
            'shot': shot,
            'start': start,
            'end': end
        })
    print("Cleaned!")
    write_dict_to_file_as_json(simple_rows, 'simple_rows.json')
    print("Data retrieved successfully")


if __name__ == '__main__':
    main()

