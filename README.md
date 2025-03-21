# SDET Internship Assessment - ExactSpace

## Overview

This project automates the process of capturing and analyzing network requests from the website [exactspace.co](https://exactspace.co). The script:

- Navigates to the website using Selenium
- Captures network logs and extracts HTTP status codes
- Saves the network logs in a `.har` file
- Parses the `.har` file to generate a summary of HTTP status codes
- Saves the status summary in `status_counts.json`

## Requirements

- Python 3.x
- Google Chrome browser
- Chrome WebDriver
- Required Python libraries:
  - `selenium`
  - `webdriver-manager`
  - `json`

## Installation

1. Clone this repository or download the files.
2. Install required dependencies:
   ```sh
   pip install selenium webdriver-manager
   ```
3. Ensure Chrome is installed and up to date.

## Usage

Run the script to capture and analyze network requests:

```sh
python script.py
```

## Output Files

1. `network_log.har` - Contains the raw network logs captured from the website.
2. `status_counts.json` - Contains a summary of HTTP status codes in the following format:
   ```json
   {
       "total": 61,
       "2XX": 61,
       "4XX": 0,
       "5XX": 0
   }
   ```


## Notes

- The script runs in **headless mode** for automation.
- The `.har` file and status count JSON are automatically generated.
- Modify `script.py` if needed for additional functionality.

## Author

Adithya Narayan

