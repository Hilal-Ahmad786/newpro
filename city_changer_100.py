#!/usr/bin/env python3
"""
🌍 City Changer - 10000 Swipes Version
Changes city every 10000 swipes with 50 high-quality cities
Optimized for speed with maximum 2-second delays
"""
import time
import sys

def main():
    print("🌍 CITY CHANGER - 10000 SWIPES VERSION")
    print("="*60)
    print("🚀 Fast swiping with city changes every 10000 swipes")
    print("🌎 Using 50 premium cities from Europe, America, UAE")
    print("⚡ Maximum 2-second delays between swipes")
    print("="*60)
    
    try:
        # Import required modules
        try:
            import undetected_chromedriver as uc
        except ImportError:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "undetected-chromedriver"])
            import undetected_chromedriver as uc
        
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        import time
        import random
        
        premium_cities = [
            # --- Europe - Western (from your list, kept) ---
            "London", "Paris", "Berlin", "Amsterdam", "Stockholm", "Copenhagen",
            "Barcelona", "Madrid", "Milan", "Rome", "Vienna", "Zurich",
            "Geneva", "Brussels", "Dublin", "Edinburgh", "Munich", "Hamburg",
            "Frankfurt", "Cologne", "Lyon", "Nice", "Marseille", "Florence",
            "Venice", "Naples", "Prague", "Budapest", "Warsaw", "Krakow",

            # --- Türkiye (most popular & travel hotspots) ---
            "Istanbul", "Ankara", "Izmir", "Bursa", "Antalya", "Adana",
            "Konya", "Gaziantep", "Mersin", "Kayseri", "Eskisehir",
            "Diyarbakir", "Samsun", "Trabzon", "Sanliurfa", "Kocaeli",
            "Sakarya", "Denizli", "Bodrum", "Fethiye", "Alanya",

            # --- Europe - Near Türkiye / Balkans / East Europe ---
            "Athens", "Thessaloniki", "Sofia", "Bucharest", "Cluj-Napoca", "Constanta",
            "Belgrade", "Sarajevo", "Skopje", "Tirana", "Podgorica", "Pristina",
            "Chisinau", "Zagreb", "Split", "Dubrovnik", "Ljubljana",
            "Bratislava", "Kosice", "Varna", "Plovdiv",
            # Caucasus & Cyprus (nearby)
            "Tbilisi", "Batumi", "Yerevan", "Baku", "Nicosia", "Limassol",

            # --- Europe - Wider coverage ---
            # UK & Ireland
            "Manchester", "Birmingham", "Liverpool", "Leeds", "Bristol", "Glasgow",
            "Cardiff", "Belfast", "Cork", "Galway",
            # France
            "Toulouse", "Bordeaux", "Nantes", "Lille", "Strasbourg", "Montpellier",
            # Germany
            "Stuttgart", "Dusseldorf", "Dortmund", "Leipzig", "Dresden",
            "Nuremberg", "Hannover", "Bremen",
            # Spain & Portugal
            "Valencia", "Seville", "Malaga", "Bilbao", "Palma de Mallorca",
            "Lisbon", "Porto",
            # Italy
            "Turin", "Bologna", "Palermo", "Catania", "Bari",
            # Benelux & Switzerland & Austria
            "Rotterdam", "The Hague", "Utrecht", "Eindhoven",
            "Antwerp", "Ghent",
            "Basel", "Lausanne", "Lugano",
            "Salzburg", "Graz", "Innsbruck",
            # Nordics & Baltics
            "Oslo", "Bergen", "Trondheim", "Helsinki", "Tampere", "Turku",
            "Gothenburg", "Malmo",
            "Tallinn", "Riga", "Vilnius", "Kaunas",
            # Central/Eastern
            "Wroclaw", "Gdansk", "Poznan", "Szczecin", "Lodz",
            "Brno", "Ostrava", "Debrecen", "Szeged",

            # --- North America (expanded coverage) ---
            # USA
            "New York", "Los Angeles", "Chicago", "Miami", "San Francisco",
            "Las Vegas", "Boston", "Seattle", "Austin", "Denver", "Atlanta",
            "Phoenix", "Dallas", "Houston", "San Diego", "San Jose",
            "Philadelphia", "Washington", "Charlotte", "Orlando", "Tampa",
            "Nashville", "Portland", "Sacramento", "San Antonio",
            "Detroit", "Minneapolis", "Raleigh", "Columbus", "Cleveland",
            "Pittsburgh", "Baltimore", "Indianapolis", "Kansas City",
            "New Orleans", "Salt Lake City",
            # Canada
            "Toronto", "Vancouver", "Montreal", "Calgary",
            "Ottawa", "Edmonton", "Winnipeg", "Quebec City", "Halifax", "Victoria", "Hamilton",
            # Mexico
            "Mexico City", "Guadalajara", "Monterrey", "Tijuana", "Puebla",
            "Merida", "Cancun", "Queretaro", "Leon",

            # --- Africa (major/popular urban hubs) ---
            "Cairo", "Alexandria",
            "Casablanca", "Marrakech", "Rabat", "Tangier",
            "Tunis", "Algiers", "Oran",
            "Lagos", "Abuja", "Accra", "Abidjan", "Dakar",
            "Nairobi", "Mombasa", "Addis Ababa", "Kampala", "Dar es Salaam", "Kigali", "Luanda",
            "Johannesburg", "Cape Town", "Durban", "Pretoria", "Maputo", "Harare",

            # --- South America (high-activity metros) ---
            "Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasilia", "Salvador",
            "Recife", "Fortaleza", "Curitiba", "Porto Alegre",
            "Buenos Aires", "Cordoba", "Rosario", "Mendoza",
            "Santiago", "Valparaiso",
            "Lima",
            "Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena",
            "Quito", "Guayaquil",
            "Montevideo",
            "Asuncion",
            "La Paz", "Santa Cruz",
            "Caracas",

            # --- East Asia (Japan & South Korea) ---
            "Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Fukuoka", "Sapporo", "Kobe", "Hiroshima", "Sendai",
            "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Suwon",

            # --- Southeast Asia (requested countries) ---
            # Vietnam
            "Ho Chi Minh City", "Hanoi", "Da Nang", "Haiphong", "Nha Trang",
            # Indonesia
            "Jakarta", "Surabaya", "Bandung", "Denpasar", "Yogyakarta", "Medan",
            # Malaysia
            "Kuala Lumpur", "George Town", "Johor Bahru", "Kota Kinabalu", "Kuching", "Shah Alam",
            # Thailand
            "Bangkok", "Chiang Mai", "Pattaya", "Phuket", "Hat Yai",

            # --- Middle East & Others (from your list + a few hubs) ---
            "Dubai", "Abu Dhabi", "Tel Aviv",
            "Doha", "Manama", "Kuwait City", "Muscat", "Amman", "Beirut",

            # --- Oceania (you already had AU; adding a couple for coverage) ---
            "Sydney", "Melbourne", "Brisbane", "Perth", "Auckland"
        ]

        # Create incognito browser
        options = uc.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--no-first-run")
        options.add_argument("--lang=en-US")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        print("🚀 Starting optimized incognito browser...")
        browser = uc.Chrome(options=options)
        
        print("🌍 Opening Tinder...")
        browser.get("https://tinder.com/")
        time.sleep(3)
        
        # Manual login
        print("\n🔑 Please login manually...")
        print("⏰ You have 10 minutes")
        
        start_time = time.time()
        while True:
            if time.time() - start_time > 600:  # 10 minutes
                print("⏰ Login timeout!")
                browser.quit()
                return
            
            if "tinder.com/app" in browser.current_url.lower():
                print("✅ Login detected!")
                break
            
            if int(time.time() - start_time) % 30 == 0:
                remaining = int(600 - (time.time() - start_time))
                print(f"⏳ Login timeout in {remaining//60}:{remaining%60:02d}")
            
            time.sleep(2)
        
        # Enhanced popup handling
        def handle_popups():
            """Fast popup handling optimized for speed"""
            popup_selectors = [
                # Permission popups
                "//*[@data-testid='allow']",
                "//*[@data-testid='decline']",
                # The specific "No Thanks" button
                "//button[.//div[contains(@class, 'lxn9zzn') and contains(text(), 'No Thanks')]]",
                "//div[contains(@class, 'lxn9zzn') and contains(text(), 'No Thanks')]/../../../..",
                # General "No Thanks" patterns
                "//button[.//div[contains(text(), 'No Thanks')]]",
                "//div[contains(text(), 'No Thanks')]",
                "//button[contains(text(), 'No Thanks')]",
                # Other common popups
                "//button[contains(text(), 'Not Interested')]",
                "//button[contains(text(), 'Maybe Later')]",
                "//button[contains(text(), 'Skip')]",
                "//button[contains(text(), 'Continue')]",
                # Generic dismiss
                "//button[@aria-label='Close']"
            ]
            
            handled_count = 0
            for selector in popup_selectors:
                try:
                    element = WebDriverWait(browser, 0.5).until(  # Very fast timeout
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    element.click()
                    handled_count += 1
                    time.sleep(0.3)  # Brief pause
                except:
                    continue
            
            return handled_count > 0
        
        handle_popups()
        
        # Optimized city changing function
        def change_city(city_name):
            print(f"\n🌍 Changing location to: {city_name}")
            
            try:
                # Step 1: Go to profile (fast)
                profile_selectors = [
                    "//a[@title='My Profile']",
                    "//a[@href='/app/profile']",
                    "//h2[contains(text(), 'You')]/.."
                ]
                
                for selector in profile_selectors:
                    try:
                        profile_btn = WebDriverWait(browser, 2).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                        profile_btn.click()
                        time.sleep(1)  # Faster
                        break
                    except:
                        continue
                
                # Step 2: Click Location
                location_selectors = [
                    "//span[contains(text(), 'Location')]",
                    "//span[contains(text(), 'Location')]/..",
                    "//span[contains(text(), 'Location')]/../../.."
                ]
                
                for selector in location_selectors:
                    try:
                        location_btn = WebDriverWait(browser, 2).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                        location_btn.click()
                        time.sleep(1)  # Faster
                        break
                    except:
                        continue
                
                # Step 3: Find search field
                search_selectors = [
                    "//input[@type='text']",
                    "//input[@placeholder]",
                    "//input"
                ]
                
                search_field = None
                for selector in search_selectors:
                    try:
                        search_field = WebDriverWait(browser, 2).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                        search_field.click()
                        time.sleep(0.5)  # Faster
                        break
                    except:
                        continue
                
                if search_field:
                    # Step 4: Enter city
                    search_field.clear()
                    search_field.send_keys(city_name)
                    time.sleep(1)  # Wait for dropdown
                    
                    # Step 5: Click dropdown
                    dropdown_selectors = [
                        f"//div[@role='button' and .//h3[contains(text(), '{city_name}')]]",
                        f"//div[contains(@class, 'passport__search__item') and .//h3[contains(text(), '{city_name}')]]",
                        f"//h3[contains(text(), '{city_name}')]/../.."
                    ]
                    
                    dropdown_clicked = False
                    for selector in dropdown_selectors:
                        try:
                            dropdown_item = WebDriverWait(browser, 2).until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                            dropdown_item.click()
                            time.sleep(1)  # Faster
                            dropdown_clicked = True
                            break
                        except:
                            continue
                    
                    if not dropdown_clicked:
                        search_field.send_keys(Keys.RETURN)
                        time.sleep(1)
                    
                    # Step 6: Click location marker
                    time.sleep(2)  # Wait for map
                    
                    marker_selectors = [
                        f"//div[contains(@class, 'passport__locationMarker') and .//h1[contains(text(), '{city_name}')]]",
                        f"//h1[contains(text(), '{city_name}')]/../../..",
                        "//div[contains(@class, 'passport__locationMarker')]"
                    ]
                    
                    for selector in marker_selectors:
                        try:
                            marker = WebDriverWait(browser, 3).until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                            browser.execute_script("arguments[0].scrollIntoView(true);", marker)
                            time.sleep(0.5)
                            marker.click()
                            time.sleep(1)  # Faster
                            break
                        except:
                            continue
                    
                    # Step 7: Return to swiping
                    browser.get("https://tinder.com/app/recs")
                    time.sleep(2)  # Faster
                    
                    print(f"   ✅ Location changed to {city_name}")
                    return True
                    
            except Exception as e:
                print(f"   ❌ City change failed: {e}")
                try:
                    browser.get("https://tinder.com/app/recs")
                    time.sleep(1)
                except:
                    pass
                return False
        
        # Fast swiping function with city changes
        def fast_swipe_with_cities(total_swipes=10000):
            print(f"\n⚡ Starting FAST swiping: {total_swipes} swipes")
            print("🌍 Changes city every 10000 swipes")
            print("⏱️ Maximum 2-second delays")
            
            city_index = 0
            swipe_count = 0
            successful_swipes = 0
            
            for i in range(total_swipes):
                # Change city every 10000 swipes
                if i % 10000 == 0:
                    current_city = premium_cities[city_index % len(premium_cities)]
                    print(f"\n🔄 Swipe {i+1}: Changing to {current_city}")
                    
                    if change_city(current_city):
                        city_index += 1
                    
                    handle_popups()  # Clean start
                
                # Perform fast swipe
                current_city_name = premium_cities[(city_index-1) % len(premium_cities)]
                print(f"👍 Swipe {i+1}/{total_swipes} in {current_city_name}")
                
                try:
                    # Quick popup check (0.5s max)
                    if handle_popups():
                        print("   🔧 Popup dismissed")
                    
                    # Fast swipe
                    ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
                    successful_swipes += 1
                    print(f"   ✅ Swiped! ({successful_swipes}/{total_swipes})")
                    
                    # Optimized delay (0.5-2 seconds)
                    delay = 0.5 + (random.random() * 1)  # 0.5-2.0 seconds
                    time.sleep(delay)
                    
                    # Quick popup check after swipe
                    handle_popups()
                    
                except Exception as e:
                    print(f"   ⚠️ Swipe failed: {e}")
                    handle_popups()
                    time.sleep(1)
                
                # Progress update every 25 swipes
                if (i + 1) % 25 == 0:
                    progress = ((i + 1) / total_swipes) * 10000
                    print(f"\n📊 Progress: {i+1}/{total_swipes} ({progress:.1f}%) - {successful_swipes} successful")
            
            print(f"\n🎉 FAST SWIPING COMPLETED!")
            print(f"   Total swipes: {successful_swipes}/{total_swipes}")
            print(f"   Cities used: {min(city_index, len(premium_cities))}")
            print(f"   Success rate: {(successful_swipes/total_swipes)*10000:.1f}%")
        
        # Start the automation
        print("\n🚀 Ready to start fast automation!")
        print("Settings:")
        print("- 10000 swipes per city")
        print("- 0.5-2.0 second delays")
        print("- Auto popup handling")
        print("- 50 premium cities")
        
        choice = input("\nStart 10000-swipe automation? (y/n): ").lower()
        
        if choice == 'y':
            fast_swipe_with_cities(1000)
        else:
            # Custom amount
            try:
                custom_amount = int(input("Enter custom swipe amount (1-500): "))
                if 1 <= custom_amount <= 500:
                    fast_swipe_with_cities(custom_amount)
                else:
                    print("❌ Invalid amount")
            except:
                print("❌ Invalid input")
        
        print("\n💡 Automation completed! Session still active for manual commands.")
        print("Available: 'swipe 50', 'city Paris', 'exit'")
        
        # Interactive mode
        try:
            while True:
                cmd = input("\n💬 Command: ").strip().lower()
                
                if cmd == 'exit':
                    break
                elif cmd.startswith('swipe'):
                    try:
                        amount = int(cmd.split()[1]) if len(cmd.split()) > 1 else 10
                        print(f"🚀 Starting {amount} fast swipes...")
                        
                        for i in range(amount):
                            handle_popups()
                            ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
                            print(f"   ✅ Swipe {i+1}/{amount}")
                            time.sleep(random.uniform(0.5, 1.5))
                            
                        print(f"🎉 Completed {amount} swipes!")
                        
                    except Exception as e:
                        print(f"❌ Error: {e}")
                        
                elif cmd.startswith('city'):
                    try:
                        city = cmd.split(' ', 1)[1] if len(cmd.split()) > 1 else "London"
                        change_city(city)
                    except:
                        change_city("London")
                        
                else:
                    print("Commands: 'swipe 25', 'city Berlin', 'exit'")
        
        except KeyboardInterrupt:
            pass
        
        print("\n🔒 Closing optimized session...")
        print("⚡ Fast automation completed!")
        
        browser.quit()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()