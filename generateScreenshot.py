import argparse
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(url, save_path):
    chrome_profile_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--user-data-dir={chrome_profile_path}")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.set_window_size(1920, 1080)
        driver.get(url)
        driver.save_screenshot(save_path)
    finally:
        driver.quit()

# Parse arguments
parser = argparse.ArgumentParser(description='Generate a screenshot of a Web page defined by its URL.')
parser.add_argument('url', type=str, help='URL')
parser.add_argument('png_file', type=str, help='name of the PNG file (to be created) into which to write the screenshot')
args = parser.parse_args()

take_screenshot(args.url, args.png_file)
