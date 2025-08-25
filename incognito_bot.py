#!/usr/bin/env python3
"""
🕵️ TinderBot - INCOGNITO MODE
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
    
    print("🕵️ TINDERBOT - INCOGNITO MODE")
    print("="*50)
    print("✅ Maximum privacy - no history saved")
    print("✅ No cookies or cache stored")
    print("✅ Fresh session every time")
    print("="*50)
    
    # Create Chrome options with INCOGNITO mode
    options = uc.ChromeOptions()
    
    # FORCE INCOGNITO MODE
    options.add_argument("--incognito")
    options.add_argument("--no-first-run")
    options.add_argument("--no-service-autorun")
    options.add_argument("--password-store=basic")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=en-US")
    
    # Additional privacy settings
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-logging")
    
    # Disable automation detection
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    print("🚀 Starting incognito Chrome browser...")
    browser = uc.Chrome(options=options)
    
    # Additional stealth
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    print("✅ INCOGNITO BROWSER LAUNCHED!")
    print("🔒 No browsing data will be saved\n")
    
    return browser

def manual_login(browser, timeout_minutes=10):
    """Wait for manual login in incognito mode"""
    print("🔑 MANUAL LOGIN REQUIRED")
    print("="*50)
    print("1. The browser will open Tinder")
    print("2. Please login manually")
    print("3. Bot will detect when you're logged in")
    print(f"⏰ Timeout: {timeout_minutes} minutes")
    print("="*50)
    
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
    print("Speed: 0.5-2 seconds per swipe")
    
    action = ActionChains(browser)
    liked = 0
    
    for i in range(amount):
        try:
            # 85% chance to like
            if random.random() < 0.85:
                action.send_keys(Keys.ARROW_RIGHT).perform()
                liked += 1
                status = "👍 Liked"
            else:
                action.send_keys(Keys.ARROW_LEFT).perform()
                status = "👎 Passed"
            
            print(f"  {i+1}/{amount}: {status}")
            
            # Fast delay: 0.5-2 seconds
            delay = random.uniform(0.5, 2.0)
            time.sleep(delay)
            
            # Progress update every 10 swipes
            if (i + 1) % 10 == 0:
                print(f"  ✅ Progress: {i+1}/{amount} ({liked} liked)")
            
        except Exception as e:
            print(f"  ⚠️ Error on swipe {i+1}: {e}")
            time.sleep(1)
    
    print(f"\n🎉 Completed! Liked {liked}/{amount} profiles")

def handle_popups(browser):
    """Quick popup handler"""
    from selenium.webdriver.common.by import By
    
    popups = [
        "//button[contains(text(), 'No Thanks')]",
        "//button[contains(text(), 'Maybe Later')]",
        "//button[@aria-label='Close']",
        "//button[contains(text(), 'Not Interested')]"
    ]
    
    for xpath in popups:
        try:
            btn = browser.find_element(By.XPATH, xpath)
            btn.click()
            print("  🔧 Dismissed popup")
            return True
        except:
            continue
    return False

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
        
        # Main loop
        while True:
            print("\n📋 INCOGNITO BOT MENU:")
            print("1. ⚡ Fast swipe (50 profiles)")
            print("2. 🚀 Turbo swipe (100 profiles)")
            print("3. 🎯 Custom amount")
            print("4. 🚪 Exit")
            
            choice = input("\nChoice: ").strip()
            
            if choice == '1':
                handle_popups(browser)
                fast_swipe(browser, 50)
                
            elif choice == '2':
                handle_popups(browser)
                fast_swipe(browser, 100)
                
            elif choice == '3':
                amount = int(input("How many swipes? (1-500): ") or "25")
                handle_popups(browser)
                fast_swipe(browser, amount)
                
            elif choice == '4':
                print("\n👋 Exiting...")
                break
            else:
                print("❌ Invalid choice")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if browser:
            print("\n🔒 Closing incognito session...")
            print("✅ No data was saved")
            browser.quit()
            print("👋 Goodbye!")

if __name__ == "__main__":
    main()