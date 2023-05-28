import argparse
import openai
import json
import os
import re
from dotenv import load_dotenv
from glob import glob
from pathlib import Path

def analyze_text(text, api_key, prompt, max_retries=1):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        temperature=0,
    )

    # Remove newlines in the result
    result = response['choices'][0]['message']['content'].strip().replace('\n', '')
    # Use regex to extract the JSON part of the result
    match = re.search(r'\{.*\}', result)
    if match:
        json_result = match.group()
        return json_result
    else:
        print(f"No JSON found in the output: {result}")
        if max_retries > 0:
            print(f"Retrying... Remaining retries: {max_retries - 1}")
            return analyze_text(text, api_key, prompt, max_retries - 1)
        else:
            print("Maximum retry limit reached. Returning None.")
            return None

def main():
    parser = argparse.ArgumentParser(description='Analyze text with GPT-4.')
    parser.add_argument('json_dir', help='Path to the directory containing JSON files with text data.')

    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')

    prompt = """
    Analyze the provided text and provide a sentiment analysis. Output should ONLY be a JSON structure containing the following: 

    Frustration level: 0 to 100.
    Happiness level: 0 to 100.
    Emoji representation: Unicode only, example "U+1F60A".
    Summary: Summary of the days discussion (max 100 chars).
    Confidence in analysis: 0 to 100.

    No other output is allowed.
    """

    json_files = glob(os.path.join(args.json_dir, '*.json'))

    # Get the second and subsequent parts of the path, replacing '/' with '_'
    output_filename = "_".join(Path(args.json_dir).parts[1:]) + '.json'

    # Make sure output directory exists
    os.makedirs('output', exist_ok=True)

    results_list = []

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        text = ' '.join([message['message'] for message in data])
        result = analyze_text(text, api_key, prompt)
        if result is not None:
            # Retrieve the filename excluding the path and .json
            date = os.path.basename(json_file).replace('.json', '')
            print("Debug: Date: ", date)
            # Parse result into JSON object
            result_json = json.loads(result.encode('utf-8'))

            analysis_result = {
                'date': date,
                'num_messages': len(data),
                'frustration': result_json.get('Frustration level', None),
                'happiness': result_json.get('Happiness level', None),
                'emoji': result_json.get('Emoji representation', None),
                'summary': result_json.get('Summary', None),
                'confidence': result_json.get('Confidence in analysis', None)
            }

            results_list.append(analysis_result)

    with open(os.path.join('output', output_filename), 'w', encoding='utf-8') as f:  
        json.dump(results_list, f, ensure_ascii=False, indent=4)

    print(f'Successfully saved the analysis results to output/{output_filename}!')

if __name__ == "__main__":
    main()