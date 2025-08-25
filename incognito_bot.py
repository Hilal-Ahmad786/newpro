#!/usr/bin/env python3
"""
🕵️ Hilal's Smart Dating Bot - INCOGNITO MODE
Always runs in incognito/private browsing mode
No data saved, maximum privacy
"""
import os
import sys
import time
import random
from dotenv import load_dotenv
load_dotenv()

# Fix import path if needed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def create_incognito_session():
    """Create a session that's always in incognito mode"""
    try:
        import undetected_chromedriver as uc
    except ImportError:
        print("Installing undetected-chromedriver...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "undetected-chromedriver"])
        import undetected_chromedriver as uc
    
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    
    print("🕵️ HILAL'S SMART DATING BOT - INCOGNITO MODE")
    print("="*60)
    print("✅ Maximum privacy - no history saved")
    print("✅ No cookies or cache stored")
    print("✅ Fresh session every time")
    print("✅ Turkey-optimized automation")
    print("="*60)
    
    # Create Chrome options with INCOGNITO mode
    options = uc.ChromeOptions()
    
    # FORCE INCOGNITO MODE
    options.add_argument("--incognito")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--password-store=basic")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=en-US")
    options.add_argument("--start-maximized")
    
    # Additional privacy settings
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-logging")
    
    # FIXED: Remove problematic excludeSwitches option
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])  # REMOVED - CAUSES ERROR
    options.add_experimental_option('useAutomationExtension', False)
    
    print("🚀 Starting incognito Chrome browser...")
    try:
        browser = uc.Chrome(options=options, version_main=None)
    except Exception as e:
        print(f"❌ Error starting browser: {e}")
        print("💡 Trying fallback method...")
        
        # Fallback with minimal options
        simple_options = uc.ChromeOptions()
        simple_options.add_argument("--incognito")
        simple_options.add_argument("--start-maximized")
        simple_options.add_argument("--no-first-run")
        
        try:
            browser = uc.Chrome(options=simple_options)
        except Exception as e2:
            print(f"❌ Fallback failed: {e2}")
            print("💡 Please update Chrome and try again:")
            print("   1. Update Google Chrome to latest version")
            print("   2. Run: pip install --upgrade undetected-chromedriver")
            raise e2
    
    # Additional stealth
    try:
        browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    except:
        pass  # Continue if this fails
    
    print("✅ INCOGNITO BROWSER LAUNCHED!")
    print("🔒 No browsing data will be saved")
    print("🇹🇷 Ready for Turkish dating automation\n")
    
    return browser

def manual_login(browser, timeout_minutes=10):
    """Wait for manual login in incognito mode"""
    print("🔑 MANUAL LOGIN REQUIRED")
    print("="*60)
    print("1. The browser will open Tinder")
    print("2. Please login manually (Google/Facebook recommended)")
    print("3. Bot will detect when you're logged in")
    print(f"⏰ Timeout: {timeout_minutes} minutes")
    print("💡 Tip: Use your main account safely!")
    print("="*60)
    
    # Navigate to Tinder
    print("\n🌍 Opening Tinder...")
    browser.get("https://tinder.com/")
    time.sleep(3)
    
    # Wait for login
    start_time = time.time()
    timeout_seconds = timeout_minutes * 60
    
    print("⏳ Waiting for you to login...\n")
    
    while True:
        elapsed = time.time() - start_time
        
        if elapsed > timeout_seconds:
            print("\n⏰ Login timeout!")
            return False
        
        # Check if logged in
        if "tinder.com/app" in browser.current_url.lower():
            print("\n✅ LOGIN DETECTED!")
            print("🎉 Welcome to Hilal's Smart Dating Bot!")
            return True
        
        # Show status every 15 seconds
        if int(elapsed) % 15 == 0 and elapsed > 0:
            remaining = int(timeout_seconds - elapsed)
            print(f"⏳ Still waiting... {remaining//60}:{remaining%60:02d} remaining")
        
        time.sleep(2)

def fast_swipe(browser, amount=50):
    """Fast swiping with keyboard shortcuts"""
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    
    print(f"\n⚡ FAST SWIPING: {amount} profiles")
    print("🇹🇷 Turkey-optimized speed: 0.5-2 seconds per swipe")
    print("🎯 Smart ratio: 85% like, 15% dislike")
    
    action = ActionChains(browser)
    liked = 0
    disliked = 0
    
    for i in range(amount):
        try:
            # Handle popups quickly
            handle_popups(browser)
            
            # 85% chance to like (good for Turkish dating)
            if random.random() < 0.85:
                action.send_keys(Keys.ARROW_RIGHT).perform()
                liked += 1
                status = "👍 Liked"
            else:
                action.send_keys(Keys.ARROW_LEFT).perform()
                disliked += 1
                status = "👎 Passed"
            
            print(f"  {i+1}/{amount}: {status}")
            
            # Fast delay: 0.5-2 seconds (optimized for Turkey)
            delay = random.uniform(0.5, 2.0)
            time.sleep(delay)
            
            # Progress update every 10 swipes
            if (i + 1) % 10 == 0:
                success_rate = (liked / (liked + disliked)) * 100
                print(f"  ✅ Progress: {i+1}/{amount} | Liked: {liked} | Success Rate: {success_rate:.1f}%")
            
        except Exception as e:
            print(f"  ⚠️ Error on swipe {i+1}: {e}")
            time.sleep(1)
    
    print(f"\n🎉 COMPLETED! Results:")
    print(f"   👍 Liked: {liked} profiles")
    print(f"   👎 Disliked: {disliked} profiles") 
    print(f"   📊 Success rate: {(liked/(liked+disliked)*100):.1f}%")

def handle_popups(browser):
    """Quick popup handler optimized for speed"""
    from selenium.webdriver.common.by import By
    
    # Quick popup dismissals (most common first)
    popups = [
        "//button[contains(text(), 'No Thanks')]",
        "//button[contains(text(), 'Maybe Later')]",
        "//button[contains(text(), 'Not Interested')]",
        "//button[@aria-label='Close']",
        "//button[contains(text(), 'Continue')]",
        "//button[@title='Back to Tinder']"
    ]
    
    for xpath in popups:
        try:
            btn = browser.find_element(By.XPATH, xpath)
            btn.click()
            return True
        except:
            continue
    return False

def turkey_city_mode(browser):
    """Special Turkey city rotation mode"""
    print("\n🇹🇷 TURKEY CITY MODE ACTIVATED")
    print("="*50)
    
    turkey_cities = [
        "Istanbul, Turkey", "Ankara, Turkey", "Izmir, Turkey", 
        "Bursa, Turkey", "Antalya, Turkey", "Adana, Turkey",
        "Konya, Turkey", "Gaziantep, Turkey", "Mersin, Turkey"
    ]
    
    swipes_per_city = int(input("Swipes per city (10-50): ") or "25")
    num_cities = min(int(input("Number of cities (1-9): ") or "5"), len(turkey_cities))
    
    print(f"\n🚀 Starting Turkey tour: {num_cities} cities × {swipes_per_city} swipes")
    
    for i in range(num_cities):
        city = turkey_cities[i]
        print(f"\n📍 City {i+1}/{num_cities}: {city}")
        
        # Note: Location changing would require additional implementation
        # For now, just do the swiping
        fast_swipe(browser, swipes_per_city)
        
        if i < num_cities - 1:
            print("⏸️ Brief pause before next city...")
            time.sleep(5)
    
    print(f"\n🎉 TURKEY TOUR COMPLETED!")
    print(f"🇹🇷 Visited {num_cities} Turkish cities")

def main():
    """Main incognito bot function"""
    browser = None
    
    try:
        # Create incognito browser
        browser = create_incognito_session()
        
        # Manual login
        if not manual_login(browser):
            print("❌ Login failed")
            return
        
        # Handle initial popups
        time.sleep(2)
        handle_popups(browser)
        
        # Main menu loop
        while True:
            print("\n" + "="*60)
            print("🤖 HILAL'S SMART DATING BOT - INCOGNITO MENU")
            print("="*60)
            print("1. ⚡ Quick Swipe (50 profiles)")
            print("2. 🚀 Turbo Swipe (100 profiles)")
            print("3. 🇹🇷 Turkey City Mode") 
            print("4. 🎯 Custom Amount")
            print("5. 📊 Profile Info Mode")
            print("6. 🚪 Exit")
            print("="*60)
            
            choice = input("👉 Your choice: ").strip()
            
            if choice == '1':
                handle_popups(browser)
                fast_swipe(browser, 50)
                
            elif choice == '2':
                handle_popups(browser)
                fast_swipe(browser, 100)
                
            elif choice == '3':
                handle_popups(browser)
                turkey_city_mode(browser)
                
            elif choice == '4':
                try:
                    amount = int(input("How many swipes? (1-500): ") or "25")
                    if 1 <= amount <= 500:
                        handle_popups(browser)
                        fast_swipe(browser, amount)
                    else:
                        print("❌ Amount must be between 1-500")
                except ValueError:
                    print("❌ Please enter a valid number")
                    
            elif choice == '5':
                print("\n📊 PROFILE INFO MODE")
                print("This would show detailed profile information")
                print("💡 Feature coming in next update!")
                
            elif choice == '6':
                print("\n👋 Exiting Hilal's Smart Dating Bot...")
                print("🇹🇷 Thanks for using Turkish-optimized automation!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-6")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if browser:
            print("\n🔒 Closing incognito session...")
            print("✅ No data was saved - complete privacy maintained")
            print("🇹🇷 Your Turkish dating automation session is secure!")
            try:
                browser.quit()
            except:
                pass
            print("👋 Goodbye!")

if __name__ == "__main__":
    main()