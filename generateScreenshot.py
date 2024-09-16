import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def take_screenshot(url, save_path):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
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
