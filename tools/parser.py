import argparse
from bs4 import BeautifulSoup
import json
import os
from collections import defaultdict

def parse_chatlog(html):
    soup = BeautifulSoup(html, 'html.parser')

    messages_by_date = defaultdict(list)

    for message_group in soup.find_all('div', {'class': 'chatlog__message-group'}):
        message_data = {}

        message_container = message_group.find('div', {'class': 'chatlog__message-container'})
        
        # Extract the timestamp
        timestamp = message_container.find('span', {'class': 'chatlog__timestamp'}).text.strip()
        message_data['timestamp'] = timestamp

        # Extract the date from the timestamp
        date = timestamp.split()[0]

        # Extract the message content
        content = message_container.find('div', {'class': 'chatlog__content chatlog__markdown'})
        if content:
            message_data['message'] = content.text.strip()

        messages_by_date[date].append(message_data)

    return messages_by_date

def main():
    parser = argparse.ArgumentParser(description='Parse chatlog data from HTML file.')
    parser.add_argument('html_file', help='Path to the HTML file containing chatlog data.')

    args = parser.parse_args()

    with open(args.html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    parsed_messages = parse_chatlog(html)

    # Use the original filename but without the extension
    base_filename = os.path.splitext(os.path.basename(args.html_file))[0]
    output_dir = os.path.join('output', base_filename)

    # Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for date, messages in parsed_messages.items():
        # Use the date as the filename
        output_filename = f'{date.replace("/", "-")}.json'  # Replace "/" with "-" to avoid issues with file paths
        json_messages = json.dumps(messages, indent=4)

        # Save the messages for this date to a file
        with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as f:
            f.write(json_messages)

    print(f'Successfully saved the parsed messages to {output_dir}/!')

if __name__ == "__main__":
    main()