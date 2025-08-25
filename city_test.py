#!/usr/bin/env python3
"""
🌍 City Changer Test - Changes city every 2 swipes
Test version for Hilal's Smart Dating Bot
"""
import time
import sys

def main():
    print("🌍 CITY CHANGER TEST")
    print("="*50)
    print("🧪 This will change city after every 2 swipes")
    print("🌎 Testing with popular European/American cities")
    print("="*50)
    
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
        
        # Test cities list (good cities for dating)
        test_cities = [
            "London, UK",
            "Paris, France", 
            "Berlin, Germany",
            "Amsterdam, Netherlands",
            "Stockholm, Sweden",
            "Barcelona, Spain",
            "Milan, Italy",
            "Vienna, Austria",
            "New York, USA",
            "Los Angeles, USA",
            "Miami, USA",
            "Toronto, Canada",
            "Dubai, UAE",
            "Sydney, Australia",
            "Tel Aviv, Israel"
        ]
        
        # Create incognito browser
        options = uc.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--no-first-run")
        options.add_argument("--lang=en-US")
        
        print("🚀 Starting incognito browser...")
        browser = uc.Chrome(options=options)
        
        print("🌍 Opening Tinder...")
        browser.get("https://tinder.com/")
        time.sleep(3)
        
        # Manual login
        print("\n🔑 Please login manually...")
        print("⏰ You have 5 minutes")
        
        start_time = time.time()
        while True:
            if time.time() - start_time > 300:  # 5 minutes
                print("⏰ Login timeout!")
                browser.quit()
                return
            
            if "tinder.com/app" in browser.current_url.lower():
                print("✅ Login detected!")
                break
            
            time.sleep(2)
        
        # Handle popups
        def handle_popups():
            """Enhanced popup handling including the specific 'No Thanks' button"""
            popup_selectors = [
                # Location permission
                "//*[@data-testid='allow']",
                # Notification permission  
                "//*[@data-testid='decline']",
                # The specific "No Thanks" button you provided
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
                # Generic dismiss buttons
                "//button[@aria-label='Close']",
                "//button[contains(@class, 'close')]"
            ]
            
            handled_count = 0
            for i, selector in enumerate(popup_selectors, 1):
                try:
                    element = WebDriverWait(browser, 1).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    
                    # Scroll into view if needed
                    browser.execute_script("arguments[0].scrollIntoView(true);", element)
                    time.sleep(0.5)
                    
                    element.click()
                    popup_text = "No Thanks" if "No Thanks" in selector else f"popup {i}"
                    print(f"   ✅ Dismissed {popup_text}")
                    handled_count += 1
                    time.sleep(1)
                    
                    # Don't break - might be multiple popups
                    
                except:
                    continue
            
            if handled_count == 0:
                print("   ℹ️ No popups detected")
            else:
                print(f"   🔧 Handled {handled_count} popups")
            
            return handled_count > 0
        
        handle_popups()
        
        # Function to change city
        def change_city(city_name):
            print(f"\n🌍 Changing location to: {city_name}")
            
            try:
                # Step 1: Click on profile picture to go to profile
                print("   📍 Step 1: Opening profile...")
                profile_selectors = [
                    "//a[@title='My Profile']",
                    "//a[@href='/app/profile']",
                    "//h2[contains(text(), 'You')]/..",
                ]
                
                for selector in profile_selectors:
                    try:
                        profile_btn = WebDriverWait(browser, 3).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                        profile_btn.click()
                        print("   ✅ Profile opened")
                        time.sleep(2)
                        break
                    except:
                        continue
                
                # Step 2: Click on Location/Settings
                print("   📍 Step 2: Opening location settings...")
                location_selectors = [
                    "//span[contains(text(), 'Location')]",
                    "//span[contains(text(), 'Location')]/..",
                    "//span[contains(text(), 'Location')]/../../..",
                ]
                
                for selector in location_selectors:
                    try:
                        location_btn = WebDriverWait(browser, 3).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                        location_btn.click()
                        print("   ✅ Location settings opened")
                        time.sleep(2)
                        break
                    except:
                        continue
                
                # Step 3: Find and click search/input field
                print("   📍 Step 3: Finding search field...")
                search_selectors = [
                    "//input[@type='text']",
                    "//input[@placeholder]",
                    "//input",
                    "//div[@contenteditable='true']",
                ]
                
                search_field = None
                for selector in search_selectors:
                    try:
                        search_field = WebDriverWait(browser, 3).until(
                            EC.element_to_be_clickable((By.XPATH, selector))
                        )
                        search_field.click()
                        print("   ✅ Search field found and clicked")
                        time.sleep(1)
                        break
                    except:
                        continue
                
                if search_field:
                    # Step 4: Clear and enter city name
                    print(f"   📍 Step 4: Entering {city_name}...")
                    search_field.clear()
                    time.sleep(0.5)
                    
                    # Extract just the city name (before comma)
                    city_only = city_name.split(',')[0].strip()
                    search_field.send_keys(city_only)
                    time.sleep(2)  # Wait for dropdown to appear
                    
                    # Step 5: Click on dropdown search result
                    print(f"   📍 Step 5: Looking for dropdown result with {city_only}...")
                    
                    # Look for the dropdown item that contains the city name
                    dropdown_selectors = [
                        f"//div[@role='button' and .//h3[contains(text(), '{city_only}')]]",
                        f"//div[contains(@class, 'passport__search__item') and .//h3[contains(text(), '{city_only}')]]",
                        f"//div[@tabindex='0' and .//h3[contains(text(), '{city_only}')]]",
                        f"//h3[contains(text(), '{city_only}')]/../..",
                        f"//h3[contains(text(), '{city_only}')]/../../..",
                    ]
                    
                    dropdown_clicked = False
                    for selector in dropdown_selectors:
                        try:
                            dropdown_item = WebDriverWait(browser, 3).until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                            dropdown_item.click()
                            print(f"   ✅ Clicked dropdown item for {city_only}")
                            time.sleep(2)
                            dropdown_clicked = True
                            break
                        except Exception as e:
                            print(f"   ⚠️ Dropdown selector failed: {selector[:50]}... - {e}")
                            continue
                    
                    if not dropdown_clicked:
                        print("   ❌ Could not find dropdown item, trying Enter key...")
                        search_field.send_keys(Keys.RETURN)
                        time.sleep(2)
                    
                    # Step 6: Look for location marker and click it
                    print(f"   📍 Step 6: Looking for location marker with {city_only}...")
                    
                    # Wait a bit for the map to load
                    time.sleep(3)
                    
                    marker_selectors = [
                        f"//div[contains(@class, 'passport__locationMarker') and .//h1[contains(text(), '{city_only}')]]",
                        f"//h1[contains(text(), '{city_only}')]/../../..",
                        "//div[contains(@class, 'passport__locationMarker')]",
                        "//div[@role='button' and contains(@class, 'passport__locationMarker')]",
                        "//button[@title='Add new location']",
                        f"//div[contains(@class, 'passport__locationMarker')]//h1[contains(text(), '{city_only}')]/../..",
                    ]
                    
                    marker_clicked = False
                    for selector in marker_selectors:
                        try:
                            marker = WebDriverWait(browser, 4).until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                            
                            # Scroll marker into view if needed
                            browser.execute_script("arguments[0].scrollIntoView(true);", marker)
                            time.sleep(1)
                            
                            marker.click()
                            print(f"   ✅ Location marker clicked for {city_only}")
                            time.sleep(2)
                            marker_clicked = True
                            break
                        except Exception as e:
                            print(f"   ⚠️ Marker selector failed: {selector[:50]}... - {e}")
                            continue
                    
                    if not marker_clicked:
                        print("   ⚠️ Could not find location marker, but continuing...")
                    
                    # Step 7: Go back to main swiping page
                    print("   📍 Step 7: Returning to main page...")
                    browser.get("https://tinder.com/app/recs")
                    time.sleep(3)
                    
                    print(f"   🎉 Completed location change process for {city_name}")
                    return True
                else:
                    print("   ❌ Could not find search field")
                    return False
                
            except Exception as e:
                print(f"   ❌ Error changing city: {e}")
                # Try to go back to main page anyway
                try:
                    browser.get("https://tinder.com/app/recs")
                    time.sleep(2)
                except:
                    pass
                return False
        
        # Function to like with city changing
        def like_with_city_change(total_swipes=6):  # 6 swipes = 3 cities (every 2 swipes)
            print(f"\n👍 Starting test: {total_swipes} swipes with city changes every 2 swipes")
            
            city_index = 0
            swipe_count = 0
            
            for i in range(total_swipes):
                # Change city every 2 swipes
                if i % 2 == 0:
                    current_city = test_cities[city_index % len(test_cities)]
                    print(f"\n🔄 Swipe {i+1}: Time to change city!")
                    
                    if change_city(current_city):
                        city_index += 1
                        print(f"✅ City changed successfully")
                    else:
                        print("⚠️ City change failed, continuing...")
                    
                    # Handle any popups after city change
                    handle_popups()
                
                # Perform the like/swipe
                print(f"\n👍 Swipe {i+1}/{total_swipes} in {test_cities[(city_index-1) % len(test_cities)]}")
                
                try:
                    # Handle popups before swiping (including "No Thanks")
                    print("   🔧 Checking for popups before swipe...")
                    handle_popups()
                    
                    # Swipe right (like)
                    action = ActionChains(browser)
                    action.send_keys(Keys.ARROW_RIGHT).perform()
                    print(f"   ✅ Swiped right!")
                    
                    swipe_count += 1
                    
                    # Brief pause then check for popups again
                    time.sleep(1)
                    print("   🔧 Checking for popups after swipe...")
                    handle_popups()
                    
                    # Wait between swipes
                    delay = 3 + (time.time() % 2)  # 3-5 seconds
                    print(f"   ⏱️ Waiting {delay:.1f} seconds...")
                    time.sleep(delay)
                    
                except Exception as e:
                    print(f"   ❌ Swipe failed: {e}")
                    # Try to handle popups even on error
                    handle_popups()
            
            print(f"\n🎉 Test completed!")
            print(f"   Total swipes: {swipe_count}")
            print(f"   Cities changed: {(swipe_count + 1) // 2}")
        
        # Start the test
        print("\n🧪 Starting city changer test...")
        print("This will:")
        print("- Swipe 1-2: Change to city 1, then swipe 2 times")
        print("- Swipe 3-4: Change to city 2, then swipe 2 times")  
        print("- Swipe 5-6: Change to city 3, then swipe 2 times")
        
        if input("\nReady to start test? (y/n): ").lower() == 'y':
            like_with_city_change(total_swipes=6)
        
        print("\n✅ Test completed!")
        print("💡 If this worked, we can implement the 1000-swipe version")
        
        input("\nPress Enter to close browser...")
        browser.quit()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()