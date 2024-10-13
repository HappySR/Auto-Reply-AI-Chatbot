# Auto-Reply-AI-Chatbot
Project Name: Auto Reply AI Chatbot

Description

This Python script leverages PyAutoGUI and OpenAI's GPT-3.5-turbo model to analyze chat history, identify messages from a specific sender, and generate witty responses in a humorous way. It automates the process within a web browser (specifically Chrome in this implementation) by:

• Selecting the chat history text. <br>
• Copying it to the clipboard. <br>
• Sending the copied text to OpenAI for analysis and response generation. <br>
• Pasting the generated response back into the chat window.

Features

• Automates chat analysis and response generation. <br>
• Identifies messages from a designated sender. <br>
• Uses OpenAI's GPT-3.5-turbo model for response generation. <br>
• Requires minimal user intervention (coordinates adjustment might be needed).

Target Audience

This script is intended for anyone who:

• Enjoy automating repetitive tasks. <br>
• Want to experiment with AI-powered chat interaction. <br>
• Seek a fun and creative way to add humor to chats.

Prerequisites

• Python (version 3.x recommended) <br>
• PyAutoGUI library (pip install pyautogui) <br>
• OpenAI API key (create a free account at https://beta.openai.com/account/api-keys)

Installation

Install Python and PyAutoGUI:

  pip install pyautogui
  
Note : Use code with caution.

Obtain your OpenAI API key and store it securely (Important: Not recommended to share your API key publicly)

Usage

1. Find Chat Window Coordinates:

Run the provided 01_get_cursor.py script to identify the coordinates of relevant points in your web browser's chat window (click locations, text selection area).

Replace the placeholder coordinates in the main script (03_bot.py) with your actual values.

2. Run the Main Script:

Open a terminal or command prompt in the project directory.

Execute the script:

  python 03_bot.py

Note : Use code with caution.

Customization

• Modify the sender_name variable in is_last_message_from_sender to identify the desired sender. <br>
• Adjust the coordinates in the script according to your specific setup. <br>
• Consider adding error handling for potential issues like API access or UI element location changes.

Disclaimer

• This script interacts with a web interface, so behavior might be affected by UI updates or website changes. <br>
• Use this script responsibly and ethically. Do not violate terms of service of any platforms you use it with.

Additional Notes

• The script currently assumes interactions within the Chrome browser window. You might need to adjust if using a different browser. <br>
• Using OpenAI's API comes with usage limits and potentially costs. Refer to their documentation for details.
