import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_car_model_from_license(license_plate):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }

    # Set up the webdriver
    driver = webdriver.Chrome()
    
    # Load the website
    url = "https://findbyplate.com/"
    driver.get(url)
    time.sleep(1)

    # Add cookies to the browser to tell it to select state CA
    cookies = {
        "name" : "userstate",
        "value": "CA"
    }
    driver.add_cookie(cookies)

    # Refresh the page to use the added cookies
    driver.refresh()

    search_box = driver.find_element(By.NAME, "platenumber")
    
    # Enter the license plate into the input box
    search_box.send_keys(license_plate)
    
    # Submit the form (press Enter)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results to load (adjust time as needed)
    time.sleep(5)

    # Get the vehicle model
    try:
        element = driver.find_element(By.CLASS_NAME, "vehicle-modal")
        car_model = element.text
    except:
        car_model = "NA"

    driver.quit()
    return car_model

def populate_plate_list():
    plates = []
    for l1 in range(0,10):
      for l2 in range(0,10):
        for l3 in range(0,10):
           plates.append(f"8PNW{l1}{l2}{l3}")
    print(f"Checking {len(plates)} plates.")
    return plates

def main():
    plate_to_model = {}
    plates = populate_plate_list()

    for plate in plates:
        model = get_car_model_from_license(plate)
        print(f"{plate} --> {model}")
        plate_to_model[plate] = model

    print(plate_to_model)

if __name__ == "__main__":
    main()
