# YouTube Playlist Parser and Downloader

This Python project automates the parsing of YouTube playlists using the Selenium library. It retrieves all video links from a given playlist, organizes the links into a directory, and creates a text file containing the video URLs.

---

## Features  

- **Playlist Parsing**: Scrapes all video links from a specified YouTube playlist.
- **Directory Management**: Automatically creates a directory named after the playlist title and author to store data.
- **Duplicate Removal:** Filters duplicate video links and stores sorted links in a separate file.
- **Custom Browser Configuration:** Uses advanced Firefox options to minimize detection as a bot.

---

## Requirements  

- **Python 3.x**  
- **Firefox Browser**  
- **GeckoDriver**: Required to run the Selenium Firefox WebDriver.

## Setup and Execution  

### 1. Create and Activate a Virtual Environment  

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 2. Install the required libraries:  

```bash
pip install -r requirements.txt
```

### 3. Setup project configurations
Website where can you [Get User Agent](https://www.whatismybrowser.com/detect/what-is-my-user-agent/)

```bash
#!/bin/bash

# Define the path to the config directory and the .env file
CONFIG_DIR="config"
ENV_FILE="$CONFIG_DIR/.env"

# Create the config directory if it doesn't exist
if [ ! -d "$CONFIG_DIR" ]; then
    echo "Creating directory: $CONFIG_DIR"
    mkdir "$CONFIG_DIR"
else
    echo "Directory $CONFIG_DIR already exists."
fi

# Change to the config directory
cd "$CONFIG_DIR" || exit

# Check if the .env file already exists
if [ -f "$ENV_FILE" ]; then
    echo "$ENV_FILE already exists. Overwriting..."
else
    echo "$ENV_FILE does not exist. Creating a new one..."
fi

# Write the data into the .env file
echo "USER_AGENT='user agent'" > "$ENV_FILE"

echo ".env file created successfully with data:"
cat "$ENV_FILE"

 ```