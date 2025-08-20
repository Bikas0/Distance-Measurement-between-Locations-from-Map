# # # import time
# # # import pandas as pd
# # # from itertools import combinations
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.by import By
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # ---------------- Helper Function ---------------- #

# # # def scrape_distance_and_route(origin_address, dest_address, mode="driving"):
# # #     """Scrape distance and duration between two addresses using Google Maps."""
# # #     options = webdriver.ChromeOptions()
# # #     options.add_argument("--headless")  # run without opening browser
# # #     options.add_argument("--no-sandbox")
# # #     options.add_argument("--disable-dev-shm-usage")

# # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # #     try:
# # #         maps_url = (
# # #             f"https://www.google.com/maps/dir/?api=1"
# # #             f"&origin={origin_address.replace(' ', '+')}"
# # #             f"&destination={dest_address.replace(' ', '+')}"
# # #             f"&travelmode={mode}"
# # #         )
# # #         driver.get(maps_url)
# # #         time.sleep(8)  # wait for directions to load

# # #         # Distance
# # #         try:
# # #             distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
# # #             distance = distance_elem.text
# # #         except:
# # #             distance = "N/A"

# # #         # Duration
# # #         try:
# # #             duration_elem = driver.find_element(By.XPATH, '//div[contains(@class,"ivN21e")]')
# # #             duration = duration_elem.text
# # #         except:
# # #             duration = "N/A"

# # #         return maps_url, distance, duration

# # #     finally:
# # #         driver.quit()


# # # # ---------------- Main Execution ---------------- #

# # # if __name__ == "__main__":
# # #     # Load branch CSV
# # #     df = pd.read_csv("branch_clean_addresses.csv")  # make sure file exists
# # #     branches = df[['Branch Name', 'Clean Address']].to_dict(orient='records')

# # #     results = []
# # #     branch_names = [b['Branch Name'] for b in branches]
# # #     total_pairs = len(branches) * (len(branches) - 1) // 2
# # #     pair_count = 0

# # #     for origin, dest in combinations(branches, 2):
# # #         pair_count += 1
# # #         print(f"🚗 {pair_count}/{total_pairs}: {origin['Branch Name']} → {dest['Branch Name']}")

# # #         maps_url, distance, duration = scrape_distance_and_route(
# # #             origin['Clean Address'], dest['Clean Address']
# # #         )

# # #         results.append({
# # #             'Origin': origin['Branch Name'],
# # #             'Destination': dest['Branch Name'],
# # #             'Origin Address': origin['Clean Address'],
# # #             'Destination Address': dest['Clean Address'],
# # #             'Distance': distance,
# # #             'Duration': duration,
# # #             'Google Maps URL': maps_url
# # #         })

# # #     # Save results
# # #     results_df = pd.DataFrame(results)
# # #     results_df.to_csv("branch_distances.csv", index=False)
# # #     print("✅ All distances saved to branch_distances.csv")


# # # import time
# # # import pandas as pd
# # # from itertools import combinations
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.by import By
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # ---------------- Helper Function ---------------- #

# # # def scrape_distance_and_route(origin_address, dest_address, mode="driving"):
# # #     """Scrape distance and duration between two addresses using Google Maps."""
# # #     options = webdriver.ChromeOptions()
# # #     options.add_argument("--headless")  # run without opening browser
# # #     options.add_argument("--no-sandbox")
# # #     options.add_argument("--disable-dev-shm-usage")

# # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # #     try:
# # #         maps_url = (
# # #             f"https://www.google.com/maps/dir/?api=1"
# # #             f"&origin={origin_address.replace(' ', '+')}"
# # #             f"&destination={dest_address.replace(' ', '+')}"
# # #             f"&travelmode={mode}"
# # #         )
# # #         driver.get(maps_url)
# # #         time.sleep(8)  # wait for directions to load

# # #         # Distance
# # #         try:
# # #             distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
# # #             distance = distance_elem.text
# # #         except:
# # #             distance = "N/A"

# # #         # Duration
# # #         try:
# # #             duration_elem = driver.find_element(By.XPATH, '//div[contains(@class,"ivN21e")]')
# # #             duration = duration_elem.text
# # #         except:
# # #             duration = "N/A"

# # #         return maps_url, distance, duration

# # #     finally:
# # #         driver.quit()


# # # # ---------------- Main Execution ---------------- #

# # # if __name__ == "__main__":
# # #     # Load branch CSV
# # #     df = pd.read_csv("branch_clean_addresses.csv")  # make sure file exists
# # #     branches = df[['Branch Name', 'Clean Address']].to_dict(orient='records')

# # #     results = []
# # #     branch_names = [b['Branch Name'] for b in branches]
# # #     total_pairs = len(branches) * (len(branches) - 1) // 2
# # #     pair_count = 0

# # #     for origin, dest in combinations(branches, 2):
# # #         pair_count += 1
# # #         print(f"\n🚗 {pair_count}/{total_pairs}: {origin['Branch Name']} → {dest['Branch Name']}")

# # #         maps_url, distance, duration = scrape_distance_and_route(
# # #             origin['Clean Address'], dest['Clean Address']
# # #         )

# # #         # Print result immediately after fetching
# # #         print(f"   📍 Distance: {distance} | Duration: {duration}")

# # #         results.append({
# # #             'Origin': origin['Branch Name'],
# # #             'Destination': dest['Branch Name'],
# # #             'Origin Address': origin['Clean Address'],
# # #             'Destination Address': dest['Clean Address'],
# # #             'Distance': distance,
# # #             'Duration': duration,
# # #             'Google Maps URL': maps_url
# # #         })

# # #     # Save results
# # #     results_df = pd.DataFrame(results)
# # #     results_df.to_csv("branch_distances.csv", index=False)
# # #     print("\n✅ All distances saved to branch_distances.csv")



# # # import time
# # # import pandas as pd
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.by import By
# # # from webdriver_manager.chrome import ChromeDriverManager

# # # # ---------------- Helper Function ---------------- #

# # # def scrape_distance_and_latlng(origin_address, dest_address, mode="driving"):
# # #     """Scrape distance and coordinates between two addresses using Google Maps."""
# # #     options = webdriver.ChromeOptions()
# # #     options.add_argument("--headless")  # run without opening browser
# # #     options.add_argument("--no-sandbox")
# # #     options.add_argument("--disable-dev-shm-usage")

# # #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # #     try:
# # #         maps_url = (
# # #             f"https://www.google.com/maps/dir/?api=1"
# # #             f"&origin={origin_address.replace(' ', '+')}"
# # #             f"&destination={dest_address.replace(' ', '+')}"
# # #             f"&travelmode={mode}"
# # #         )
# # #         driver.get(maps_url)
# # #         time.sleep(8)  # wait for page to load

# # #         # Distance
# # #         try:
# # #             distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
# # #             distance = distance_elem.text
# # #         except:
# # #             distance = "N/A"

# # #         # Coordinates extraction from URL
# # #         try:
# # #             origin_link = driver.find_element(By.XPATH, '//a[contains(@aria-label,"Directions from")]').get_attribute('href')
# # #             dest_link = driver.find_element(By.XPATH, '//a[contains(@aria-label,"Directions to")]').get_attribute('href')

# # #             origin_latlng = origin_link.split("/@")[1].split(",")[:2] if "/@" in origin_link else ["N/A", "N/A"]
# # #             dest_latlng = dest_link.split("/@")[1].split(",")[:2] if "/@" in dest_link else ["N/A", "N/A"]
# # #         except:
# # #             origin_latlng = ["N/A", "N/A"]
# # #             dest_latlng = ["N/A", "N/A"]

# # #         return {
# # #             "maps_url": maps_url,
# # #             "distance": distance,
# # #             "origin_lat": origin_latlng[0],
# # #             "origin_lng": origin_latlng[1],
# # #             "dest_lat": dest_latlng[0],
# # #             "dest_lng": dest_latlng[1],
# # #         }

# # #     finally:
# # #         driver.quit()


# # # # ---------------- Main Execution ---------------- #

# # # if __name__ == "__main__":
# # #     # Read CSV
# # #     df = pd.read_csv("address_combinations.csv")  # CSV must have columns: Origin, Destination

# # #     results = []

# # #     for index, row in df.iterrows():
# # #         origin = row['Address1']
# # #         dest = row['Address2']
# # #         print(f"Processing: {origin} → {dest}")

# # #         result = scrape_distance_and_latlng(origin, dest)
# # #         results.append({
# # #             "Origin Address": origin,
# # #             "Destination Address": dest,
# # #             "Distance": result["distance"],
# # #             "Origin Latitude": result["origin_lat"],
# # #             "Origin Longitude": result["origin_lng"],
# # #             "Destination Latitude": result["dest_lat"],
# # #             "Destination Longitude": result["dest_lng"],
# # #             "Google Maps URL": result["maps_url"]
# # #         })

# # #     # Save to CSV
# # #     results_df = pd.DataFrame(results)
# # #     results_df.to_csv("branch_distances_latlng.csv", index=False)
# # #     print("\n✅ Distances and coordinates saved to branch_distances_latlng.csv")



# # import time
# # import pandas as pd
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager

# # # ---------------- Helper Function ---------------- #

# # def scrape_distance_and_latlng(origin_address, dest_address, mode="driving"):
# #     """Scrape distance and coordinates between two addresses using Google Maps."""
# #     options = webdriver.ChromeOptions()
# #     options.add_argument("--headless")  # run without opening browser
# #     options.add_argument("--no-sandbox")
# #     options.add_argument("--disable-dev-shm-usage")

# #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# #     try:
# #         maps_url = (
# #             f"https://www.google.com/maps/dir/?api=1"
# #             f"&origin={origin_address.replace(' ', '+')}"
# #             f"&destination={dest_address.replace(' ', '+')}"
# #             f"&travelmode={mode}"
# #         )
# #         driver.get(maps_url)
# #         time.sleep(8)  # wait for page to load

# #         # Distance
# #         try:
# #             distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
# #             distance = distance_elem.text
# #         except:
# #             distance = "N/A"

# #         # Coordinates extraction from URL
# #         try:
# #             origin_link = driver.find_element(By.XPATH, '//a[contains(@aria-label,"Directions from")]').get_attribute('href')
# #             dest_link = driver.find_element(By.XPATH, '//a[contains(@aria-label,"Directions to")]').get_attribute('href')

# #             origin_latlng = origin_link.split("/@")[1].split(",")[:2] if "/@" in origin_link else ["N/A", "N/A"]
# #             dest_latlng = dest_link.split("/@")[1].split(",")[:2] if "/@" in dest_link else ["N/A", "N/A"]
# #         except:
# #             origin_latlng = ["N/A", "N/A"]
# #             dest_latlng = ["N/A", "N/A"]

# #         return {
# #             "maps_url": maps_url,
# #             "distance": distance,
# #             "origin_lat": origin_latlng[0],
# #             "origin_lng": origin_latlng[1],
# #             "dest_lat": dest_latlng[0],
# #             "dest_lng": dest_latlng[1],
# #         }

# #     finally:
# #         driver.quit()


# # # ---------------- Main Execution ---------------- #

# # if __name__ == "__main__":
# #     # Read CSV
# #     df = pd.read_csv("address_combinations.csv")  # CSV must have columns: Address1, Address2

# #     results = []

# #     for index, row in df.iterrows():
# #         origin = row['Address1']
# #         dest = row['Address2']
# #         print(f"\nProcessing: {origin} → {dest}")

# #         result = scrape_distance_and_latlng(origin, dest)

# #         # Print distance immediately
# #         print(f"Distance: {result['distance']}")

# #         results.append({
# #             "Origin Address": origin,
# #             "Destination Address": dest,
# #             "Distance": result["distance"],
# #             "Origin Latitude": result["origin_lat"],
# #             "Origin Longitude": result["origin_lng"],
# #             "Destination Latitude": result["dest_lat"],
# #             "Destination Longitude": result["dest_lng"],
# #             "Google Maps URL": result["maps_url"]
# #         })

# #     # Save to CSV
# #     results_df = pd.DataFrame(results)
# #     results_df.to_csv("branch_distances_latlng.csv", index=False)
# #     print("\n✅ Distances and coordinates saved to branch_distances_latlng.csv")


# import time
# import pandas as pd
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from urllib.parse import urlparse, parse_qs

# # ---------------- Helper Function ---------------- #

# def extract_latlng_from_url(url):
#     """Extract latitude and longitude from Google Maps URL."""
#     try:
#         if "/@ " in url or "/@" in url:
#             parts = url.split("/@")[1].split(",")
#             lat, lng = parts[0], parts[1]
#             return lat, lng
#         else:
#             return "N/A", "N/A"
#     except:
#         return "N/A", "N/A"


# def scrape_distance_and_latlng(origin_address, dest_address, mode="driving"):
#     """Scrape distance and coordinates between two addresses using Google Maps."""
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # run without opening browser
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     try:
#         maps_url = (
#             f"https://www.google.com/maps/dir/?api=1"
#             f"&origin={origin_address.replace(' ', '+')}"
#             f"&destination={dest_address.replace(' ', '+')}"
#             f"&travelmode={mode}"
#         )
#         driver.get(maps_url)
#         time.sleep(8)  # wait for page to load

#         # Distance
#         try:
#             distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
#             distance = distance_elem.text
#         except:
#             distance = "N/A"

#         # Get current URL (with coordinates)
#         current_url = driver.current_url

#         origin_lat, origin_lng = extract_latlng_from_url(current_url)
#         dest_lat, dest_lng = origin_lat, origin_lng  # Google Maps usually shows route from origin to dest, may need refinement

#         return {
#             "maps_url": maps_url,
#             "distance": distance,
#             "origin_lat": origin_lat,
#             "origin_lng": origin_lng,
#             "dest_lat": dest_lat,
#             "dest_lng": dest_lng,
#         }

#     finally:
#         driver.quit()


# # ---------------- Main Execution ---------------- #

# if __name__ == "__main__":
#     df = pd.read_csv("address_combinations.csv")  # CSV must have columns: Address1, Address2
#     output_file = "branch_distances_latlngAug20.csv"

#     if not os.path.exists(output_file):
#         pd.DataFrame(columns=[
#             "Origin Address", "Destination Address", "Distance",
#             "Origin Latitude", "Origin Longitude",
#             "Destination Latitude", "Destination Longitude",
#             "Google Maps URL"
#         ]).to_csv(output_file, index=False)

#     for index, row in df.iterrows():
#         origin = str(row['Address1']).strip()
#         dest = str(row['Address2']).strip()

#         if not origin or not dest:
#             print(f"Skipping row {index}: Missing origin or destination")
#             continue

#         print(f"\nProcessing: {origin} → {dest}")
#         result = scrape_distance_and_latlng(origin, dest)
#         print(f"Distance: {result['distance']}")
#         print(f"Origin: ({result['origin_lat']}, {result['origin_lng']}) | "
#               f"Destination: ({result['dest_lat']}, {result['dest_lng']})")

#         # Append result to CSV immediately
#         pd.DataFrame([{
#             "Origin Address": origin,
#             "Destination Address": dest,
#             "Distance": result["distance"],
#             "Origin Latitude": result["origin_lat"],
#             "Origin Longitude": result["origin_lng"],
#             "Destination Latitude": result["dest_lat"],
#             "Destination Longitude": result["dest_lng"],
#             "Google Maps URL": result["maps_url"]
#         }]).to_csv(output_file, mode='a', header=False, index=False)

#     print(f"\n✅ Distances and coordinates saved to {output_file}")




import os
import re
import time
import pandas as pd
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
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        maps_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&origin={origin_latlon[0]},{origin_latlon[1]}"
            f"&destination={dest_latlon[0]},{dest_latlon[1]}"
            f"&travelmode={mode}"
        )
        driver.get(maps_url)
        time.sleep(10)

        try:
            distance_elem = driver.find_element(By.XPATH, '//div[contains(@class,"MespJc")]')
            distance = distance_elem.text
        except:
            distance = "N/A"

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
    input_csv = "address_combinations.csv"
    output_csv = "AUG2025.csv"

    # Create output CSV with header if not exists
    if not os.path.exists(output_csv):
        header = [
            "Origin Input", "Origin Exact", "Origin Lat", "Origin Lon",
            "Destination Input", "Destination Exact", "Destination Lat", "Destination Lon",
            "Travel Mode", "Distance", "Duration", "Google Maps URL"
        ]
        pd.DataFrame(columns=header).to_csv(output_csv, index=False)

    df = pd.read_csv(input_csv)

    for idx, row in df.iterrows():
        origin_input = row["Address1"]
        destination_input = row["Address2"]
        travel_mode = "driving"

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            origin_name, origin_latlon = get_location_info(origin_input, driver)
            dest_name, dest_latlon = get_location_info(destination_input, driver)
        finally:
            driver.quit()

        if not validate_latlon(origin_latlon):
            print(f"❌ Invalid origin coordinates: {origin_latlon}")
            continue
        if not validate_latlon(dest_latlon):
            print(f"❌ Invalid destination coordinates: {dest_latlon}")
            continue

        maps_url, distance, duration = scrape_distance_and_route(origin_latlon, dest_latlon, mode=travel_mode)

        print(f"[{idx+1}] {origin_name} ➝ {dest_name} | {distance} | {duration}")

        # Append result directly to CSV (row by row)
        result_row = pd.DataFrame([{
            "Origin Input": origin_input,
            "Origin Exact": origin_name,
            "Origin Lat": origin_latlon[0],
            "Origin Lon": origin_latlon[1],
            "Destination Input": destination_input,
            "Destination Exact": dest_name,
            "Destination Lat": dest_latlon[0],
            "Destination Lon": dest_latlon[1],
            "Travel Mode": travel_mode,
            "Distance": distance,
            "Duration": duration,
            "Google Maps URL": maps_url
        }])

        result_row.to_csv(output_csv, mode="a", header=False, index=False)

    print(f"\n✅ Results saved continuously to {output_csv}")
