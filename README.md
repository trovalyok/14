This repository contains Python code for a Telegram bot named GIFinder: 
https://t.me/one_gif_per_request_bot

GIFinder allows users to easily search for and share GIFs directly within Telegram. Below are key points about the bot and its functionality:

Dependencies:
Utilizes the python-telegram-bot library for seamless integration with the Telegram Bot API.
Relies on the GIPHY API to fetch GIFs based on user input.

Setup:
Before running the bot, obtain API credentials:
Generate a Telegram bot API token.
Obtain an API key from GIPHY for accessing their API.
Replace placeholders in the code (TOKEN and MY_API_KEY) with your actual API credentials.

Functionality:
Start the bot by sending the /start command to initiate a GIF search session.
Simply type a term or phrase to search for related GIFs.
GIFinder randomly selects a GIF from the search results and sends it to the user.
If no matching GIFs are found, the bot notifies the user accordingly.

Deployment:
Deploy the bot on any platform capable of running Python scripts.
Ensure compliance with Telegram and GIPHY API usage policies and terms of service.
