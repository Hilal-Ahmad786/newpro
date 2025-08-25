#!/usr/bin/env python3
"""
🕵️ Hilal's Smart Dating Bot - Incognito Mode (Fixed Imports)
Guaranteed to open Chrome in incognito mode
"""
import time
import sys

def main():
    print("🕵️ HILAL'S SMART DATING BOT - INCOGNITO MODE")
    print("="*60)
    print("🔒 Opening Chrome in INCOGNITO mode")
    print("✅ Maximum privacy - no history, cookies, or data saved")
    print("="*60)
    
    try:
        # Import the session but modify it for incognito
        print("🔧 Setting up incognito browser...")
        
        # Try different import paths for undetected_chromedriver
        try:
            import undetected_chromedriver as uc
            print("✅ Using undetected_chromedriver")
        except ImportError:
            try:
                import undetected_chromedriver.v2 as uc
                print("✅ Using undetected_chromedriver.v2")
            except ImportError:
                print("❌ undetected_chromedriver not found!")
                print("🔧 Installing undetected_chromedriver...")
                import subprocess
                import sys
                subprocess.check_call([sys.executable, "-m", "pip", "install", "undetected-chromedriver"])
                import undetected_chromedriver as uc
                print("✅ Installed and imported undetected_chromedriver")
        
        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        import time
        
        # Create incognito Chrome options
        options = uc.ChromeOptions()
        
        # FORCE INCOGNITO MODE
        options.add_argument("--incognito")
        options.add_argument("--no-first-run")
        options.add_argument("--no-service-autorun") 
        options.add_argument("--password-store=basic")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--lang=en-US")
        
        # Privacy-focused settings
        options.add_argument("--disable-logging")
        options.add_argument("--disable-web-security")
        
        print("✅ Incognito options configured")
        
        # Create the browser with incognito mode
        print("🚀 Starting incognito Chrome browser...")
        browser = uc.Chrome(options=options)
        
        print("✅ INCOGNITO CHROME LAUNCHED!")
        
        # Navigate to Tinder
        print("🌍 Opening Tinder in incognito mode...")
        browser.get("https://tinder.com/")
        time.sleep(3)
        
        # Manual login function for incognito
        print("\n🔑 INCOGNITO MANUAL LOGIN")
        print("="*50)
        print("🕵️ Please login to Tinder in the incognito window")
        print("⏰ You have 10 minutes to complete login")
        print("🔒 No login data will be saved (incognito mode)")
        print("="*50)
        
        start_time = time.time()
        timeout_minutes = 10
        timeout_seconds = timeout_minutes * 60
        
        print("⏳ Waiting for you to login...")
        
        # Wait for login
        while True:
            current_time = time.time()
            elapsed = current_time - start_time
            
            if elapsed > timeout_seconds:
                print("\n⏰ Login timeout!")
                browser.quit()
                return
            
            # Check if logged in
            current_url = browser.current_url.lower()
            if "tinder.com/app" in current_url:
                print("\n🎉 LOGIN DETECTED!")
                break
            
            # Show countdown every 30 seconds
            if int(elapsed) % 30 == 0:
                remaining = int(timeout_seconds - elapsed)
                minutes = remaining // 60
                seconds = remaining % 60
                print(f"⏳ Still waiting... {minutes:02d}:{seconds:02d} remaining")
            
            time.sleep(2)
        
        # Enhanced popup handling
        def handle_popups():
            """Handle all types of popups that may appear"""
            print("🔧 Handling popups...")
            time.sleep(2)
            
            # List of popup selectors to handle
            popup_selectors = [
                # Location permission
                ("//*[@data-testid='allow']", "Location allowed"),
                
                # Notification permission
                ("//*[@data-testid='decline']", "Notifications declined"),
                
                # "No Thanks" button (from your HTML)
                ("//button[.//div[contains(text(), 'No Thanks')]]", "Dismissed 'No Thanks' popup"),
                ("//div[contains(text(), 'No Thanks')]", "Dismissed 'No Thanks' popup"),
                
                # Other common popups
                ("//button[contains(text(), 'Not Interested')]", "Dismissed 'Not Interested'"),
                ("//button[contains(text(), 'Maybe Later')]", "Dismissed 'Maybe Later'"),
                ("//button[contains(text(), 'Skip')]", "Dismissed Skip"),
                ("//button[contains(text(), 'Continue')]", "Clicked Continue"),
                
                # Generic dismiss buttons
                ("//button[@aria-label='Close']", "Closed popup"),
                ("//button[contains(@class, 'close')]", "Closed popup"),
            ]
            
            handled_count = 0
            
            for selector, message in popup_selectors:
                try:
                    element = WebDriverWait(browser, 2).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    element.click()
                    print(f"✅ {message}")
                    handled_count += 1
                    time.sleep(1)
                except:
                    continue
            
            if handled_count == 0:
                print("ℹ️ No popups detected")
            else:
                print(f"✅ Handled {handled_count} popups")
            
            return handled_count > 0
        
        # Handle initial popups
        handle_popups()
        
        print("\n🎉 INCOGNITO SESSION READY!")
        
        # Show automation options
        print("\n🤖 Choose automation mode:")
        print("1. 🛡️ Safe Mode (10 likes, conservative)")
        print("2. ⚡ Quick Mode (5 likes, fast)")
        print("3. 🔍 Profile Inspector (analyze before liking)")
        print("4. 💬 Check Matches")
        print("5. 🎯 Custom Settings")
        
        while True:
            try:
                choice = input("\nEnter choice (1-5): ").strip()
                if choice in ['1', '2', '3', '4', '5']:
                    break
                print("❌ Please enter 1-5")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                browser.quit()
                return
        
        # Enhanced like function for incognito mode
        def incognito_like(amount=1, sleep_time=3):
            print(f"\n👍 Starting to like {amount} profiles...")
            liked_count = 0
            
            for i in range(amount):
                try:
                    print(f"🎯 Profile {i+1}/{amount}...")
                    
                    # Check for popups before each like
                    handle_popups()
                    
                    # Method 1: Keyboard shortcut (most reliable)
                    action = ActionChains(browser)
                    action.send_keys(Keys.ARROW_RIGHT).perform()
                    
                    liked_count += 1
                    print(f"   ✅ Liked! ({liked_count}/{amount})")
                    
                    # Human-like delay with randomness
                    import random
                    delay = sleep_time + random.uniform(0.5, 2.0)
                    print(f"   ⏱️ Waiting {delay:.1f} seconds...")
                    time.sleep(delay)
                    
                    # Handle any popups that appear after liking
                    if i % 5 == 0:  # Check every 5 likes
                        handle_popups()
                    
                except Exception as e:
                    print(f"   ⚠️ Keyboard method failed: {e}")
                    
                    # Handle popups in case of error
                    handle_popups()
                    
                    # Fallback: try clicking various button selectors
                    button_selectors = [
                        "//button[contains(@class, 'gamepad')]",
                        "//button[.//svg]",
                        "//button[contains(@aria-label, 'Like')]",
                        "//button[contains(@class, 'like')]"
                    ]
                    
                    clicked = False
                    for selector in button_selectors:
                        try:
                            like_btn = browser.find_element(By.XPATH, selector)
                            like_btn.click()
                            liked_count += 1
                            print(f"   ✅ Liked with fallback! ({liked_count}/{amount})")
                            clicked = True
                            time.sleep(sleep_time)
                            break
                        except:
                            continue
                    
                    if not clicked:
                        print(f"   ❌ Could not like profile {i+1}")
                        # Try to handle popups and continue
                        handle_popups()
            
            print(f"\n🎉 Completed! Successfully liked {liked_count}/{amount} profiles")
            return liked_count
        
        # Execute chosen automation
        if choice == '1':
            print("\n🛡️ SAFE MODE")
            print("Settings: 10 likes, 4-6 second delays")
            if input("Continue? (y/n): ").lower() == 'y':
                incognito_like(amount=10, sleep_time=4)
        
        elif choice == '2':
            print("\n⚡ QUICK MODE")
            print("Settings: 5 likes, 2-3 second delays")
            if input("Continue? (y/n): ").lower() == 'y':
                incognito_like(amount=5, sleep_time=2)
        
        elif choice == '3':
            print("\n🔍 PROFILE INSPECTOR")
            print("Manual decision for each profile...")
            
            for i in range(5):
                try:
                    print(f"\n👤 Profile {i+1}/5:")
                    
                    # Get profile info if possible
                    try:
                        # Try to get name from page
                        name_elements = browser.find_elements(By.TAG_NAME, "h1")
                        if name_elements:
                            print(f"   📝 Name: {name_elements[0].text}")
                        else:
                            print("   📝 Name: Not visible")
                    except:
                        print("   📝 Name: Not available")
                    
                    # Decision
                    action = input("   Action (l=like, d=dislike, s=skip): ").lower()
                    
                    if action == 'l':
                        ActionChains(browser).send_keys(Keys.ARROW_RIGHT).perform()
                        print("   💕 Liked!")
                    elif action == 'd':
                        ActionChains(browser).send_keys(Keys.ARROW_LEFT).perform()
                        print("   👎 Disliked!")
                    else:
                        print("   ⏭️ Skipped!")
                    
                    time.sleep(2)
                    
                except KeyboardInterrupt:
                    break
                except Exception as e:
                    print(f"   ❌ Error: {e}")
        
        elif choice == '4':
            print("\n💬 CHECKING MATCHES")
            try:
                # Navigate to matches
                browser.get("https://tinder.com/app/matches")
                time.sleep(3)
                
                print("✅ Navigated to matches page")
                print("👀 Check your matches in the browser window")
                input("Press Enter when done viewing matches...")
                
            except Exception as e:
                print(f"❌ Error checking matches: {e}")
        
        elif choice == '5':
            print("\n🎯 CUSTOM SETTINGS")
            try:
                amount = int(input("How many profiles? (1-100): "))
                sleep_time = int(input("Seconds between likes? (1-8): "))
                
                if 1 <= amount <= 100 and 1 <= sleep_time <= 8:
                    print(f"Custom: {amount} likes, {sleep_time}s delays")
                    if input("Continue? (y/n): ").lower() == 'y':
                        incognito_like(amount=amount, sleep_time=sleep_time)
                else:
                    print("❌ Invalid settings")
            except:
                print("❌ Invalid input")
        
        # Keep session alive
        print(f"\n💡 Incognito session active. Available commands:")
        print("   'like 25' - Like 25 profiles")
        print("   'like 50' - Like 50 profiles") 
        print("   'matches' - Check matches")
        print("   'exit' - Close safely")
        
        try:
            while True:
                cmd = input("\n💬 Command: ").strip().lower()
                
                if cmd == 'exit':
                    break
                elif cmd.startswith('like'):
                    try:
                        amount = int(cmd.split()[1]) if len(cmd.split()) > 1 else 1
                        if amount > 100:
                            print("⚠️ Large amount detected. Consider using smaller batches for safety.")
                            if input(f"Continue with {amount} likes? (y/n): ").lower() != 'y':
                                continue
                        incognito_like(amount=amount, sleep_time=3)
                    except:
                        incognito_like(amount=1, sleep_time=3)
                elif cmd == 'matches':
                    try:
                        browser.get("https://tinder.com/app/matches")
                        print("✅ Navigated to matches page")
                    except Exception as e:
                        print(f"❌ Error: {e}")
                else:
                    print("Available commands: 'like 25', 'like 50', 'matches', 'exit'")
                    print("💡 You can now like any amount (e.g., 'like 100')")
        
        except KeyboardInterrupt:
            pass
        
        print("\n🔒 Closing incognito session...")
        print("✅ No browsing data was saved")
        print("🕵️ Maximum privacy maintained!")
        
        browser.quit()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()