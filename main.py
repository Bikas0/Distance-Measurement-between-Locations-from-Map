import os
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# ---- Node: Get Exact Location Info ----
def get_location_info(name: str, driver: webdriver.Chrome):
    """Visit Google Maps and get exact name, latitude, longitude."""
    url = f"https://www.google.com/maps/search/{name.replace(' ', '+')}"
    driver.get(url)
    time.sleep(8)  # wait for page to load

    # Extract Lat/Lon from URL
    match = re.search(r"@(-?\d+\.\d+),(-?\d+\.\d+),", driver.current_url)
    latlon = (float(match.group(1)), float(match.group(2))) if match else None

    # Try to get exact location name from Google Maps title
    try:
        name_elem = driver.find_element(By.XPATH, '//h1[contains(@class,"DUwDvf")]')
        exact_name = name_elem.text.strip()
    except:
        exact_name = name

    return exact_name, latlon

# ---- Node: Validate Lat/Lon ----
def validate_latlon(latlon: tuple) -> bool:
    """Simple validation: check if latitude and longitude are reasonable."""
    if latlon is None:
        return False
    lat, lon = latlon
    return -90 <= lat <= 90 and -180 <= lon <= 180

# ---- Node: Scrape Distance, Duration & Route ----
def scrape_distance_and_route(origin_latlon, dest_latlon, mode="driving"):
    """
    origin_latlon: tuple (lat, lon)
    dest_latlon: tuple (lat, lon)
    mode: "driving", "walking", "bicycling", "transit"
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        # Build Google Maps directions URL with mode
        maps_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&origin={origin_latlon[0]},{origin_latlon[1]}"
            f"&destination={dest_latlon[0]},{dest_latlon[1]}"
            f"&travelmode={mode}"
        )
        driver.get(maps_url)
        time.sleep(10)  # wait for directions to load

        # Distance
        try:
            distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
            distance = distance_elem.text
        except:
            distance = "N/A"

        # Duration
        try:
            duration_elem = driver.find_element(By.XPATH, '//div[contains(@class,"ivN21e")]')
            duration = duration_elem.text
        except:
            duration = "N/A"

    
        return maps_url, distance, duration

    finally:
        driver.quit()

# ---- Main Execution ----
if __name__ == "__main__":
    origin_input = """Baneswar, Shibpur, Puthia, Rajshahi"""
    destination_input = """Kolahata, Kalikapur, Haroa, Bonpara, Boraigram, Natore"""

    # Choose travel mode: "driving", "walking", "bicycling", "transit"
    travel_mode = "driving"  

    # Initialize Selenium for initial extraction
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        origin_name, origin_latlon = get_location_info(origin_input, driver)
        dest_name, dest_latlon = get_location_info(destination_input, driver)
    finally:
        driver.quit()

    # Validate Lat/Lon
    if not validate_latlon(origin_latlon):
        raise ValueError(f"Invalid origin coordinates: {origin_latlon}")
    if not validate_latlon(dest_latlon):
        raise ValueError(f"Invalid destination coordinates: {dest_latlon}")

    # Scrape distance, duration, route
    maps_url, distance, duration = scrape_distance_and_route(origin_latlon, dest_latlon, mode=travel_mode)

    # ---- Print Results ----
    print("\n================ Final Result ================")
    print("✅ Origin exact name:", origin_name)
    print("✅ Destination exact name:", dest_name)
    print("✅ Origin Lat/Lon:", origin_latlon)
    print("✅ Destination Lat/Lon:", dest_latlon)
    print("✅ Google Maps URL:", maps_url)
    print("✅ Travel Mode:", travel_mode)
    print("✅ Distance:", distance)
    print("✅ Duration:", duration)
