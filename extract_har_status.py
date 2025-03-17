import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def capture_and_parse_har():
    driver = setup_browser()
    driver.get("https://exactspace.co/")
    driver.implicitly_wait(10)

    logs = driver.get_log("performance")
    status_codes = []

    for entry in logs:
        message = json.loads(entry["message"])
        try:
            if message['message']['method'] == "Network.responseReceived":
                status_code = message['message']['params']['response']['status']
                status_codes.append(status_code)
        except KeyError:
            continue  # Skip entries without valid status codes

    driver.quit()

    # Process Status Codes
    total_requests = len(status_codes)
    status_summary = {
        "total": total_requests,
        "2XX": sum(200 <= code < 300 for code in status_codes),
        "4XX": sum(400 <= code < 500 for code in status_codes),
        "5XX": sum(500 <= code < 600 for code in status_codes)
    }

    # Print the output in the required format
    print(json.dumps(status_summary, indent=4))

    # Save JSON output
    json_file_path = "status_counts.json"
    with open(json_file_path, "w") as json_file:
        json.dump(status_summary, json_file, indent=4)
    print(f"Status counts saved at {json_file_path}")

if __name__ == "__main__":
    capture_and_parse_har()
