## Project Overview

The project, titled "Webbutvecklare Distans Gänget - Sentiment Tracker," is focused on performing sentiment analysis on a Discord group used by students of the EC Fullstack .NET webbutvecklare program. The analysis will help gain insights into the overall sentiment, emotions, and perspectives within the group, which could be instrumental in decision-making or for deriving insights into the group dynamics.

## Tools and Methodology

The tools used for this project include the DiscordChatExporter and a custom Python program called `parser.py` for data parsing and cleaning.

DiscordChatExporter is an open-source tool, which was utilized to extract message history from various Discord channels. It supports the extraction of direct messages, group messages, server channels, and more.

After exporting the message histories of the Discord channels, the `parser.py` program was employed to parse the data. This Python program reads the exported HTML, parses relevant information such as timestamps and message content, and organizes the data by date. The processed data is then written to a JSON file, ready for further analysis.

# Progress Journal

## Initial Steps

The project started with obtaining the necessary tokens and information according to the guidelines provided by DiscordChatExporter.

## Data Collection

Data extraction was carried out using DiscordChatExporter from different Discord channels. These included specific channels dedicated to different courses (e.g., "html-css", "javascript-frontend", "c-sharp", "datalagring", "asp-net") and several general discussion channels (e.g., "allmänt-skolan", "orelaterat-till-plugget"). The extraction did not include voice channels.

## Data Parsing

With the data extracted in HTML format, the next step was to parse and clean this data. The Python program `parser.py` was developed to handle this task. It uses the BeautifulSoup library for HTML parsing and structures the parsed data in a JSON format. This step also involves anonymization of data to ensure privacy.

Please refer to `parser.py` for the detailed code.

### Data Cleaning

Following data extraction and parsing, an essential intermediate step was the data cleaning process. The goal of this phase was to ensure that the parsed data is in a suitable format for analysis by the OpenAI API and to comply with its token limits.

To achieve this, a Python script was used to read each JSON file containing the parsed chat data and perform necessary cleaning tasks. This script first eliminates objects that do not contain a message or where the message is null. This simplifies the data structure and avoids unnecessary complexity during the analysis phase as well as cost.

One important aspect to note is the API's token limit. The OpenAI API restricts the size of the text that can be analyzed at one time to 4096 tokens. As such, to ensure compatibility with this limit, the script checks the size of the cleaned data. If the size exceeds this limit, the script splits the data into chunks of an appropriate size, each of which is saved in a separate JSON file. These smaller files are then ready for analysis by the OpenAI API.

This data cleaning process helps to create a streamlined and efficient pipeline for analyzing the chat data, facilitating the extraction of meaningful insights.

The code for the data cleaning process is outlined in `cleaner.py`.

## Data Analysis

For the analysis of the collected and parsed Discord data, a Python script named `interpreter.py` was developed. This script connects to the OpenAI API and uses the GPT-4 model to perform sentiment analysis on the given text data.

The script takes a JSON file containing the parsed text data as input and sends it to the OpenAI API with a specific prompt. The prompt is designed to instruct the model to return a detailed sentiment analysis in a structured JSON format. This includes the levels of frustration and happiness, emoji representation, discussion themes, and the model's confidence in its analysis.

A notable aspect of the script is the usage of the "temperature" parameter in the API request. Setting this parameter to 0 minimizes the degree of randomness in the model's responses, ensuring more consistent and deterministic output.

The resulting analysis is then saved to a file, `output/sum_analysis.json`, for further use.

Refer to `interpreter.py` for the detailed code.
