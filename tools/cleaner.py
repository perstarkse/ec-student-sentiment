import json
import os
import argparse

def split_file(file_name, data):
    # Limit of characters for each file
    size_limit = 3500 * 4

    chunks = []
    chunk = []
    size = 0

    for obj in data:
        obj_str = json.dumps(obj)
        obj_size = len(obj_str)

        if size + obj_size > size_limit:
            # Start a new chunk
            chunks.append(chunk)
            chunk = [obj]
            size = obj_size
        else:
            # Add the object to the current chunk
            chunk.append(obj)
            size += obj_size

    # Add the last chunk
    chunks.append(chunk)

    num_chunks = len(chunks)

    # Check the number of chunks
    if num_chunks == 1:
        # Save the single chunk to the file
        with open(f'{file_name}.json', 'w', encoding='utf8') as file:
            json.dump(chunks[0], file, ensure_ascii=False)
    elif num_chunks == 2:
        # Save two chunks to separate files
        for i, chunk in enumerate(chunks):
            with open(f'{file_name}-{i+1}.json', 'w', encoding='utf8') as file:
                json.dump(chunk, file, ensure_ascii=False)
    else:
        # Save three equally sized chunks to separate files
        chunk_size = num_chunks // 3

        for i in range(3):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size

            chunk = chunks[start_index:end_index]

            with open(f'{file_name}-{i+1}.json', 'w', encoding='utf8') as file:
                json.dump(chunk, file, ensure_ascii=False)

    # Remove the original file
    os.remove(file_name)

def process_file(file_path):
    # Read JSON data from file
    with open(file_path, 'r', encoding='utf8') as file:
        data = json.load(file)
    
    # Remove objects without a message
    data = [obj for obj in data if 'message' in obj and obj['message']]
    
    # Split file if necessary
    if len(json.dumps(data)) > 3500 * 4:
        # Remove the .json extension to split the file
        file_name = os.path.splitext(file_path)[0]
        split_file(file_name, data)
    else:
        # Save cleaned data back to the file
        with open(file_path, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a JSON file.')
    parser.add_argument('path', metavar='P', type=str, nargs='+', help='the path to the JSON file')

    args = parser.parse_args()

    # Process all json files in the provided directory
    for file_name in os.listdir(args.path[0]):
        if file_name.endswith('.json'):
            process_file(os.path.join(args.path[0], file_name))
