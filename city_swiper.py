#!/usr/bin/env python3
"""
🌍 City Hopper - Turkey-First Location Priorities
Changes city every N swipes with optimized delays
"""
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# CITIES PRIORITIZED: Turkey first, then neighbors, then Europe, then world
PRIORITY_CITIES = [
    # === TIER 1: TURKEY METROPOLITAN CITIES (HIGHEST PRIORITY) ===
    "Istanbul, Turkey",
    "Ankara, Turkey", 
    "Izmir, Turkey",
    "Bursa, Turkey",
    "Antalya, Turkey",
    "Adana, Turkey",
    "Konya, Turkey",
    "Gaziantep, Turkey",
    "Mersin, Turkey",
    "Kayseri, Turkey",
    "Eskisehir, Turkey",
    "Diyarbakir, Turkey",
    "Samsun, Turkey",
    "Denizli, Turkey",
    "Sanliurfa, Turkey",
    "Malatya, Turkey",
    "Trabzon, Turkey",
    "Erzurum, Turkey",
    "Kocaeli, Turkey",
    "Sakarya, Turkey",
    
    # === TIER 2: TURKEY TOURISM/COASTAL CITIES ===
    "Bodrum, Turkey",
    "Marmaris, Turkey",
    "Fethiye, Turkey",
    "Alanya, Turkey",
    "Kusadasi, Turkey",
    "Cesme, Turkey",
    "Ayvalik, Turkey",
    
    # === TIER 3: NEIGHBORING COUNTRIES (Near Turkey) ===
    "Athens, Greece",
    "Thessaloniki, Greece",
    "Sofia, Bulgaria",
    "Plovdiv, Bulgaria",
    "Bucharest, Romania",
    "Tbilisi, Georgia",
    "Batumi, Georgia",
    "Yerevan, Armenia",
    "Baku, Azerbaijan",
    "Nicosia, Cyprus",
    "Beirut, Lebanon",
    "Damascus, Syria",
    "Tehran, Iran",
    
    # === TIER 4: EUROPE (Popular cities) ===
    "London, UK",
    "Paris, France",
    "Berlin, Germany",
    "Amsterdam, Netherlands",
    "Barcelona, Spain",
    "Madrid, Spain",
    "Rome, Italy",
    "Milan, Italy",
    "Vienna, Austria",
    "Prague, Czech Republic",
    "Budapest, Hungary",
    "Warsaw, Poland",
    "Stockholm, Sweden",
    "Copenhagen, Denmark",
    "Oslo, Norway",
    "Helsinki, Finland",
    "Lisbon, Portugal",
    "Brussels, Belgium",
    "Zurich, Switzerland",
    "Dublin, Ireland",
    
    # === TIER 5: REST OF WORLD ===
    "Dubai, UAE",
    "New York, USA",
    "Los Angeles, USA",
    "Miami, USA",
    "Toronto, Canada",
    "Sydney, Australia",
    "Tokyo, Japan",
    "Bangkok, Thailand",
    "Singapore",
    "Mumbai, India",
]

def change_city(session, city_name):
    """
    Optimized city changing function
    """
    print(f"\n🌍 Changing to: {city_name}")
    browser = session.browser
    
    try:
        # Navigate to profile
        browser.get("https://tinder.com/app/profile")
        time.sleep(1)  # Reduced from 2-3 seconds
        
        # Click location settings
        location_btn = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Location')]"))
        )
        location_btn.click()
        time.sleep(0.5)  # Reduced delay
        
        # Search for city
        search_field = WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
        )
        search_field.clear()
        search_field.send_keys(city_name.split(',')[0])  # Just city name
        time.sleep(1)  # Wait for dropdown
        
        # Click first result
        search_field.send_keys(Keys.RETURN)
        time.sleep(1.5)  # Reduced from 3 seconds
        
        # Return to swiping
        browser.get("https://tinder.com/app/recs")
        time.sleep(1)  # Reduced delay
        
        print(f"✅ Location changed to {city_name}")
        return True
        
    except Exception as e:
        print(f"⚠️ Failed to change city: {e}")
        browser.get("https://tinder.com/app/recs")
        return False

def fast_swipe(browser, amount=10):
    """
    Optimized fast swiping with reduced delays
    """
    print(f"\n⚡ Fast swiping {amount} profiles...")
    action = ActionChains(browser)
    
    for i in range(amount):
        try:
            # Use keyboard shortcut (fastest method)
            action.send_keys(Keys.ARROW_RIGHT).perform()
            
            # OPTIMIZED DELAY: 0.5-2 seconds (reduced from 3-5)
            delay = random.uniform(0.5, 2.0)
            time.sleep(delay)
            
            # Progress update
            if (i + 1) % 10 == 0:
                print(f"   ✅ {i + 1}/{amount} swiped")
                
        except Exception as e:
            print(f"   ⚠️ Swipe {i+1} failed: {e}")
            time.sleep(1)
            
    print(f"✅ Completed {amount} swipes")

def city_hopper_session(session):
    """
    Main city hopper function with Turkey-first priorities
    """
    print("\n🌍 CITY HOPPER MODE")
    print("="*50)
    print("📍 Priority: Turkey → Neighbors → Europe → World")
    print("⚡ Optimized delays: 0.5-2 seconds per swipe")
    print("="*50)
    
    # Settings
    swipes_per_city = int(input("Swipes per city? (10-100): ") or "25")
    num_cities = int(input("How many cities? (1-50): ") or "10")
    
    print(f"\n🚀 Starting: {num_cities} cities × {swipes_per_city} swipes")
    print("Cities in priority order:")
    for i, city in enumerate(PRIORITY_CITIES[:num_cities], 1):
        tier = "🇹🇷 Turkey" if "Turkey" in city else "🌍 International"
        print(f"  {i}. {city} {tier}")
    
    input("\nPress Enter to start...")
    
    # Main loop
    total_swipes = 0
    successful_cities = 0
    
    for city_index in range(num_cities):
        city = PRIORITY_CITIES[city_index % len(PRIORITY_CITIES)]
        
        print(f"\n{'='*50}")
        print(f"📍 City {city_index + 1}/{num_cities}: {city}")
        
        # Change city
        if change_city(session, city):
            successful_cities += 1
            
            # Fast swipe in this city
            fast_swipe(session.browser, swipes_per_city)
            total_swipes += swipes_per_city
            
            # Brief pause between cities
            print(f"⏸️ Cooldown: 3 seconds...")
            time.sleep(3)
        else:
            print(f"⚠️ Skipping {city} due to error")
    
    # Summary
    print(f"\n{'='*50}")
    print("🎉 CITY HOPPER COMPLETED!")
    print(f"📊 Statistics:")
    print(f"   Cities visited: {successful_cities}/{num_cities}")
    print(f"   Total swipes: {total_swipes}")
    print(f"   Success rate: {(successful_cities/num_cities)*100:.1f}%")
    
    return total_swipes

# Standalone execution
if __name__ == "__main__":
    print("🌍 City Hopper Standalone Mode")
    print("Please run main.py instead!")
    print("This module is meant to be imported.")