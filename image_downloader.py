import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Get the current directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the paths to the Chrome and ChromeDriver executables within the project directory
chromedriver_path = os.path.join(script_directory, "chromedriver.exe")
chromepath = os.path.join(script_directory, "chrome-win64", "chrome.exe")

# Initialize Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chromepath
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument(f"executable_path={chromedriver_path}")  # Set ChromeDriver executable path

# List of categories
categories = ["Car", "Bus", "Bicycle", "Motorcycle", "Train", "Airplane", "Ship", "Boat", "Rocket", "City",
    "Mountain", "Beach", "Forest", "Desert", "Skyline", "Building", "Bridge", "Sunset", "Sunrise", "Rainbow",
    "Moon", "Stars", "Clouds", "Lake", "River", "Waterfall", "Volcano", "Island", "Book", "Pen", "Notebook",
    "Computer", "Phone", "Glasses", "Clock", "Camera", "Microphone", "Headphones", "Music", "Art", "Painting",
    "Sculpture", "Photography", "Food", "Coffee", "Pizza", "Burger", "Ice Cream", "Fruit", "Vegetable",
    "Cake", "Cupcake", "Wine", "Beer", "Travel", "Suitcase", "Passport", "Globe", "Map", "Compass", "Adventure",
    "Nature", "Sunflower", "Rose", "Waterfalls", "Leaf", "Daisy", "Sunrise", "Sunset", "Mountains", "Beach"]  # Add more categories as needed

# Number of images to download per category
num_images = 200

# Specify download directory
download_directory = "image_download"

# Create the download directory if it doesn't exist (in case you decided to download again)
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Initialize Chrome WebDriver using options
driver = webdriver.Chrome(options=chrome_options)


# Loop through each category and download images
for category in categories:
    # Reset the img_index for each category
    img_index = 1
    
    # Create the category directory if it doesn't exist
    category_directory = os.path.join(download_directory, category)
    if not os.path.exists(category_directory):
        os.makedirs(category_directory)
    
    print(f"Downloading images for category: {category}")
    # Navigate to Google Images
    driver.get("https://www.google.com/imghp")
    
    # Find the search input element by name using By.NAME selector
    search_box = driver.find_element(By.NAME, "q")
    
    # Enter the category and perform the search
    search_box.send_keys(category)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for a few seconds to allow the page to load completely
    time.sleep(8)
    
    # Scroll to load more images until the desired number is reached
    while img_index <= num_images:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for images to load
        
        # Get image elements
        img_elements = driver.find_elements(By.CLASS_NAME, "rg_i")
        
        # Download images
        for img_element in img_elements:
            if img_index > num_images:
                break

            img_url = img_element.get_attribute("src")
            if img_url:
                img_extension = ".jpg"  # Change to ".png" if needed
                img_filename = os.path.join(download_directory, category, f"{category}_{img_index}{img_extension}")

                try:
                    img_response = requests.get(img_url)
                    if img_response.status_code == 200:
                        with open(img_filename, "wb") as img_file:
                            img_file.write(img_response.content)
                        print(f"Downloaded: {img_filename}")
                        img_index += 1  # Increment the image index
                    else:
                        print(f"Failed to download image: {img_url}")
                except Exception as e:
                    print(f"Error downloading image {img_url}: {str(e)}")

# Close the WebDriver
driver.quit()

print("Download complete.")
