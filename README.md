# Discord Pruning Bot

## Description
This Discord bot is designed to automatically prune inactive members from all the guilds (servers) it is part of and then leave those guilds. It's a Python script using the discord.py library.

## Functionality
- **Pruning Members:** The bot prunes members who have been inactive for a specified number of days (default is 1 day). 
- **Leaving Guilds:** After pruning members, the bot will leave the guild, regardless of the success or failure of the pruning operation.

## Requirements
- Python 3.6 or higher
- discord.py library

## Setup and Installation
1. **Install Python:** Ensure Python 3.6 or newer is installed on your system.
2. **Install discord.py:** Run `pip install discord.py` to install the necessary Discord library.
3. **Bot Token:** Obtain a bot token from the Discord Developer Portal and replace `"bot token here"` in the script with your bot's token.
4. **Run the Bot:** Execute the script using Python to start the bot.

## Usage
- **Start the Bot:** Run the script. The bot will automatically start pruning members and then leave the guilds.
- **Adjust Parameters:** You can modify the `days` variable to change the inactivity threshold for pruning.

## Warning
This bot performs actions that can significantly alter the member structure of a guild and then leaves the guild. Use with caution, and ensure you have the necessary permissions and understanding of the implications.