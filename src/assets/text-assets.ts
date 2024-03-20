export const textAssets = {
  introduction:
    'The project, titled "Webbutvecklare Distans Gänget - Sentiment Tracker," is focused on performing sentiment analysis on a Discord group used by students of the EC Fullstack .NET webbutvecklare program. The analysis will help gain insights into the overall sentiment, emotions, and perspectives within the group, which could be instrumental in decision-making or for deriving insights into the group dynamics.',
  socials: [
    { icon: "github", text: "Github", link: "https://github.com/perstarkse" },
    { icon: "web", text: "Personal webpage", link: "https://cv.perstark.xyz" },
    {
      icon: "linkedin",
      text: "LinkedIn",
      link: "https://linkedin.com/in/per-stark",
    },
  ],
  purpose:
    "The purpose of this project was to gain insights into the overall sentiment, emotions, and perspectives within the group, which could be helpful in decision-making. A personal note was to investigate and experiment with the usage of the OpenAI API for doing sentiment analysis and psychological analysis. The use of AI in this area has great potential to ease research in the psychology field.",
  limitations:
    "There are several great limitations to the validity of the analysis. 1, The interpretation done by gpt is not controlled in any way. It is taken at face value. One might argue that a qualitative analysis being done by humans also contain great potential for error. 2, The data used for analysis is from a chat group, there is some selection bias regarding who writes in the group or not, and what topics they express. ",
  method:
    "The tools used for this project include the DiscordChatExporter and a custom Python program called parser.py for data parsing and cleaning. DiscordChatExporter is an open-source tool, which was utilized to extract message history from various Discord channels. It supports the extraction of direct messages, group messages, server channels, and more. After exporting the message histories of the Discord channels, the parser.py program was employed to parse the data. This Python program reads the exported HTML, parses relevant information such as timestamps and message content, and organizes the data by date. The processed data is then written to a JSON file, ready for further analysis.",
  result: {},
  conclusion: {},
  dataCollection:
    'The data for this study was collected from a Discord chat group used by students of the EC Fullstack .NET webbutvecklare program. We used the DiscordChatExporter, an open-source tool, to extract message histories from various Discord channels, including specific channels dedicated to different courses (e.g., "html-css", "javascript-frontend", "c-sharp", "datalagring", "asp-net") and several general discussion channels (e.g., "allmänt-skolan", "orelaterat-till-plugget"). Voice channels were not included in the data extraction process.',
  dataParsingAndCleaning:
    "After exporting the message histories in HTML format, we developed a custom Python script to parse and clean the data. This program uses the BeautifulSoup library for HTML parsing and organizes the relevant information, such as timestamps and message content, by week number. The parsed data is stored in a dictionary where the keys represent the week numbers and the values are lists of message data for each corresponding week. During the parsing process, the script keeps track of the total number of messages and the number of messages with valid timestamps. Messages without a valid timestamp are skipped and not included in the analysis. After cleaning, 67,290 individual messages remained for analysis.",
  dataAnalysis: `I conducted the sentiment analysis of the collected and parsed Discord data using the same Python script. This script connects to the OpenAI API and employs the GPT-3.5-turbo model to perform the analysis on the input text data. For each week, the script concatenates the message content into a single text string. If the text exceeds a specified size limit (3,500 characters), it is split into smaller chunks to adhere to the API's token limit. Each chunk is then sent to the OpenAI API with a specific prompt, instructing the model to assign scores (0-100) for 'Demand', 'Control', 'Support', 'Sentiment', and 'Engagement' based on the Demand Control Support Model and sentiment analysis. The "temperature" parameter in the API request is set to 0 to minimize the degree of randomness in the model's responses, ensuring more consistent and deterministic output. The script expects the API response to be in JSON format, containing the scores for each category. If the response does not contain valid JSON, the script attempts to retry the analysis with a maximum number of retries. If no valid JSON is found after the retries, default scores of 50 are assigned to each category. The analysis results for each week are stored in a list, including the week number, number of messages, and the scores for each category.`,
  dataVisualization: `To present the analyzed data visually and make it accessible to users, we developed a web-based frontend using Vue3 and Chart.js. This combination of tools allows for the creation of dynamic and interactive charts that display the sentiment analysis data. The web application was deployed to sentiment.perstark.xyz.

  Vue3, a progressive JavaScript framework, was chosen for its versatility and the ability to create reusable custom components. The Vue Chartjs wrapper was used to integrate the Chart.js library within the Vue3 framework, enabling the use of reactive and customizable charts within the application.
  
  Chart.js, a powerful data visualization library, was employed to visualize various aspects of the sentiment analysis data, such as sentiment trends over time, distribution of different emotions, and discussion themes. The resulting frontend application provides an intuitive and user-friendly interface for exploring the insights derived from the sentiment analysis.
  `,
};
