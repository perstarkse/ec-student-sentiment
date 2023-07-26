export const textAssets = {
	introduction:
		'The project, titled "Webbutvecklare Distans Gänget - Sentiment Tracker," is focused on performing sentiment analysis on a Discord group used by students of the EC Fullstack .NET webbutvecklare program. The analysis will help gain insights into the overall sentiment, emotions, and perspectives within the group, which could be instrumental in decision-making or for deriving insights into the group dynamics.',
	socials: [
		{ icon: 'github', text: 'Github', link: 'https://github.com/perstarkse' },
		{ icon: 'web', text: 'Personal webpage', link: 'https://perstark.xyz' },
		{ icon: 'linkedin', text: 'LinkedIn', link: 'https://linkedin.com/in/per-stark' },
	],
	purpose:
		'The purpose of this project was to gain insights into the overall sentiment, emotions, and perspectives within the group, which could be helpful in decision-making. A personal note was to investigate and experiment with the usage of the OpenAI API for doing sentiment analysis and psychological analysis. The use of AI in this area has great potential to ease research in the psychology field.',
	limitations:
		'There are several great limitations to the validity of the analysis. 1, The interpretation done by gpt is not controlled in any way. It is taken at face value. One might argue that a qualitative analysis being done by humans also contain great potential for error. 2, The data used for analysis is from a chat group, there is some selection bias regarding who writes in the group or not, and what topics they express. ',
	method:
		'The tools used for this project include the DiscordChatExporter and a custom Python program called parser.py for data parsing and cleaning. DiscordChatExporter is an open-source tool, which was utilized to extract message history from various Discord channels. It supports the extraction of direct messages, group messages, server channels, and more. After exporting the message histories of the Discord channels, the parser.py program was employed to parse the data. This Python program reads the exported HTML, parses relevant information such as timestamps and message content, and organizes the data by date. The processed data is then written to a JSON file, ready for further analysis.',
	result: {},
	conclusion: {},
	initialSteps:
		' The project commences with the establishment of essential prerequisites. The tokens and information necessary to initiate the process are gathered as per the guidelines provided by DiscordChatExporter.',
	dataCollection:
		'In this phase, raw chat data is extracted from various Discord channels, including channels dedicated to specific academic courses and general discussion channels. The extraction is performed using DiscordChatExporter, a tool designed to retrieve data efficiently.',
	dataParsing:
		'After the data has been collected, it undergoes parsing. A Python script reads each JSON file containing the chat data, interpreting the content and structuring it into a manageable format. This stage essentially turns the raw data into a structured dataset that can be further cleaned and analyzed.',
	dataCleaning:
		'This phase involves the removal of unnecessary or irrelevant data to streamline the dataset for analysis. The Python script filters out elements that don not contain a message or where the message is null. It is a crucial step, ensuring the data is formatted appropriately for analysis by the OpenAI API and to comply with the token limits. If the data size exceeds the limit, the script splits it into appropriately sized chunks, saved as separate JSON objects.',
	dataAnalysis:
		'The final step is the analysis of the cleaned and parsed data. The Python script connects to the OpenAI API and uses the GPT-4 model to perform sentiment analysis on the data. It aims to gauge the sentiments expressed in the chat data and generate meaningful insights into the overall mood and engagement within the Discord channels.',
};
