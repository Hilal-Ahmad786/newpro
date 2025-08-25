#!/usr/bin/env python3
"""
🤖 Hilal's Smart Dating Bot - Enhanced Version
Now with automatic location changing and smart detection
"""
import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import Sexuality

def main():
    print("🤖 HILAL'S SMART DATING BOT - ENHANCED")
    print("="*60)
    print("🇹🇷 Auto Location Change - Turkey Priority")
    print("🤖 Smart Detection - No More Stuck Sessions")
    print("⚡ Ultra-Fast Swiping (0.5-2 sec delays)")
    print("🔒 Maximum Privacy (Incognito Mode)")
    print("="*60)
    
    # Turkey-first city list (prioritized order)
    TURKEY_CITIES = [
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
        "Bodrum, Turkey",
        "Marmaris, Turkey",
        "Fethiye, Turkey",
        "Alanya, Turkey"
    ]
    
    INTERNATIONAL_CITIES = [
        "London, UK",
        "Paris, France", 
        "Berlin, Germany",
        "Amsterdam, Netherlands",
        "Barcelona, Spain",
        "Madrid, Spain",
        "Rome, Italy",
        "Vienna, Austria",
        "Prague, Czech Republic",
        "Dubai, UAE",
        "New York, USA",
        "Los Angeles, USA",
        "Miami, USA",
        "Toronto, Canada"
    ]
    
    # Create session in INCOGNITO mode
    session = Session(headless=False, store_session=False, incognito=True)
    
    # Login options
    print("\n🔑 Choose your login method:")
    print("1. 🔴 Manual login (RECOMMENDED - Most Secure)")
    print("2. 🟠 Google login (Auto)")
    print("3. 🔵 Facebook login (Auto)")
    
    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            break
        print("❌ Please enter 1, 2, or 3")
    
    if choice == '1':
        print("\n🔑 Starting manual login...")
        success = session.login_manually(timeout_minutes=10)
    elif choice == '2':
        email = os.getenv('TINDER_EMAIL') or input("📧 Google Email: ")
        password = os.getenv('TINDER_PASSWORD') or input("🔐 Password: ")
        success = session.login_using_google(email, password)
    elif choice == '3':
        email = os.getenv('TINDER_EMAIL') or input("📧 Facebook Email: ")
        password = os.getenv('TINDER_PASSWORD') or input("🔐 Password: ")
        success = session.login_using_facebook(email, password)
    
    if not success:
        print("❌ Login failed - exiting")
        return
    
    print("\n✅ LOGIN SUCCESSFUL! 🎉")
    print("🤖 Enhanced Hilal's Dating Bot is ready!")
    
    # Get the enhanced helper
    from tinderbotz.helpers.geomatch_helper import GeomatchHelper
    geomatch_helper = GeomatchHelper(session.browser)
    
    # Main menu loop
    while True:
        print("\n" + "="*60)
        print("🤖 HILAL'S ENHANCED SMART DATING BOT")
        print("="*60)
        print("1. 🚀 Quick Swipe (Current Location)")
        print("2. 🇹🇷 Smart Turkey Mode (Auto Location Change)")
        print("3. 🌍 Smart International Mode (Auto Location Change)")
        print("4. 🎯 Custom Smart Session")
        print("5. 📍 Manual Location Change")
        print("6. ⚙️ Settings & Preferences") 
        print("7. 💬 Check New Matches")
        print("8. 🧪 Test Features")
        print("9. 🚪 Exit")
        print("="*60)
        
        action = input("👉 Your choice: ").strip()
        
        if action == '1':
            # Quick swipe mode (no location change)
            print("\n🚀 QUICK SWIPE MODE")
            amount = input("How many profiles to swipe? (default: 25): ").strip()
            amount = int(amount) if amount.isdigit() else 25
            
            print(f"\n⚡ Quick swiping {amount} profiles in current location...")
            
            swipes = 0
            likes = 0
            dislikes = 0
            
            while swipes < amount:
                # Check if out of matches
                if geomatch_helper.check_out_of_matches():
                    print(f"🚫 Ran out of matches after {swipes} swipes!")
                    print("💡 Try Smart Turkey Mode (option 2) to auto-change location")
                    break
                
                # Handle popups
                geomatch_helper.dismiss_upgrade_popup()
                
                # Like or dislike (85% like rate)
                should_like = random.random() < 0.85
                
                if should_like:
                    if geomatch_helper.like():
                        likes += 1
                        print(f"   👍 {swipes + 1}/{amount}: Liked")
                    else:
                        print(f"   ⚠️ Like button not available - stopping")
                        break
                else:
                    if geomatch_helper.dislike():
                        dislikes += 1  
                        print(f"   👎 {swipes + 1}/{amount}: Disliked")
                    else:
                        print(f"   ⚠️ Dislike button not available - stopping")
                        break
                
                swipes += 1
                
                # Smart delay
                import random
                delay = random.uniform(0.5, 2.0)
                time.sleep(delay)
                
                # Progress every 10 swipes
                if swipes % 10 == 0:
                    rate = (likes / swipes) * 100
                    print(f"   📊 Progress: {swipes}/{amount} | Likes: {likes} | Rate: {rate:.1f}%")
            
            print(f"\n✅ Quick swipe completed: {swipes} swipes, {likes} likes, {dislikes} dislikes")
            
        elif action == '2':
            # Smart Turkey mode with auto location changing
            print("\n🇹🇷 SMART TURKEY MODE")
            print("This mode automatically changes location when out of matches!")
            
            num_cities = input(f"Number of Turkish cities to visit (1-{len(TURKEY_CITIES)}): ").strip()
            num_cities = min(int(num_cities) if num_cities.isdigit() else 5, len(TURKEY_CITIES))
            
            swipes_per_city = input("Swipes per city (default: 25): ").strip()  
            swipes_per_city = int(swipes_per_city) if swipes_per_city.isdigit() else 25
            
            selected_cities = TURKEY_CITIES[:num_cities]
            
            print(f"\n🚀 Starting Smart Turkey Session:")
            print(f"   🌍 Cities: {selected_cities}")
            print(f"   👍 Swipes per city: {swipes_per_city}")
            
            confirm = input("\nStart Smart Turkey Session? (y/n): ").lower()
            if confirm == 'y':
                stats = geomatch_helper.smart_swipe_session(selected_cities, swipes_per_city)
                print(f"\n🇹🇷 TURKEY SESSION STATS:")
                for key, value in stats.items():
                    print(f"   {key.replace('_', ' ').title()}: {value}")
            
        elif action == '3':
            # Smart international mode
            print("\n🌍 SMART INTERNATIONAL MODE")
            print("Global cities with automatic location changing!")
            
            num_cities = input(f"Number of international cities (1-{len(INTERNATIONAL_CITIES)}): ").strip()
            num_cities = min(int(num_cities) if num_cities.isdigit() else 5, len(INTERNATIONAL_CITIES))
            
            swipes_per_city = input("Swipes per city (default: 20): ").strip()
            swipes_per_city = int(swipes_per_city) if swipes_per_city.isdigit() else 20
            
            selected_cities = INTERNATIONAL_CITIES[:num_cities]
            
            print(f"\n🚀 Starting Smart International Session:")
            print(f"   🌍 Cities: {selected_cities}")
            print(f"   👍 Swipes per city: {swipes_per_city}")
            
            confirm = input("\nStart International Session? (y/n): ").lower()
            if confirm == 'y':
                # Enable global mode first
                session.set_global(True)
                stats = geomatch_helper.smart_swipe_session(selected_cities, swipes_per_city)
                print(f"\n🌍 INTERNATIONAL SESSION STATS:")
                for key, value in stats.items():
                    print(f"   {key.replace('_', ' ').title()}: {value}")
            
        elif action == '4':
            # Custom smart session
            print("\n🎯 CUSTOM SMART SESSION")
            print("Create your own city list and settings!")
            
            # Choose region
            print("\nSelect region type:")
            print("1. Turkey cities only")
            print("2. International cities only")
            print("3. Mixed (Turkey + International)")
            
            region_choice = input("Region choice (1-3): ").strip()
            
            if region_choice == '1':
                available_cities = TURKEY_CITIES
                print(f"\n🇹🇷 Available Turkish cities: {len(available_cities)}")
            elif region_choice == '2':
                available_cities = INTERNATIONAL_CITIES
                print(f"\n🌍 Available international cities: {len(available_cities)}")
            else:
                available_cities = TURKEY_CITIES + INTERNATIONAL_CITIES
                print(f"\n🌍 Available mixed cities: {len(available_cities)}")
            
            # Show city options
            print("\nFirst 10 cities:")
            for i, city in enumerate(available_cities[:10], 1):
                print(f"   {i}. {city}")
            if len(available_cities) > 10:
                print(f"   ... and {len(available_cities) - 10} more")
            
            num_cities = input(f"\nNumber of cities to visit (1-{min(15, len(available_cities))}): ").strip()
            num_cities = min(int(num_cities) if num_cities.isdigit() else 5, len(available_cities))
            
            swipes_per_city = input("Swipes per city (10-50): ").strip()
            swipes_per_city = max(10, min(50, int(swipes_per_city) if swipes_per_city.isdigit() else 25))
            
            selected_cities = available_cities[:num_cities]
            
            print(f"\n🎯 Custom session configured:")
            print(f"   🌍 Cities: {num_cities} cities")
            print(f"   👍 Swipes per city: {swipes_per_city}")
            print(f"   📊 Total estimated swipes: {num_cities * swipes_per_city}")
            
            confirm = input("\nStart custom session? (y/n): ").lower()
            if confirm == 'y':
                if region_choice == '2':  # International only
                    session.set_global(True)
                stats = geomatch_helper.smart_swipe_session(selected_cities, swipes_per_city)
                print(f"\n🎯 CUSTOM SESSION STATS:")
                for key, value in stats.items():
                    print(f"   {key.replace('_', ' ').title()}: {value}")
            
        elif action == '5':
            # Manual location change
            print("\n📍 MANUAL LOCATION CHANGE")
            print("Change to a specific city manually")
            
            print("\nQuick options:")
            quick_cities = ["Istanbul, Turkey", "London, UK", "Paris, France", "Berlin, Germany", "New York, USA"]
            for i, city in enumerate(quick_cities, 1):
                print(f"   {i}. {city}")
            
            choice = input("\nEnter number (1-5) or type custom city name: ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= 5:
                city_name = quick_cities[int(choice) - 1]
            else:
                city_name = choice
            
            if city_name:
                print(f"\n🌍 Changing location to: {city_name}")
                if geomatch_helper.change_location(city_name):
                    print("✅ Location change successful!")
                else:
                    print("❌ Location change failed")
            
        elif action == '6':
            # Settings
            print("\n⚙️ SETTINGS & PREFERENCES")
            print("1. 🎂 Set Age Range")
            print("2. 📍 Set Distance Range") 
            print("3. 💘 Set Gender Preference")
            print("4. 🌍 Toggle Global Mode")
            print("5. ⬅️ Back to Main Menu")
            
            setting = input("Setting choice: ").strip()
            
            if setting == '1':
                try:
                    min_age = int(input("Minimum age (18-100): ") or "18")
                    max_age = int(input("Maximum age (18-100): ") or "35")
                    session.set_age_range(min_age, max_age)
                    print(f"✅ Age range set to {min_age}-{max_age}")
                except ValueError:
                    print("❌ Invalid age values")
                    
            elif setting == '2':
                try:
                    distance = int(input("Max distance in km (1-160): ") or "50")
                    session.set_distance_range(distance)
                    print(f"✅ Distance set to {distance}km")
                except ValueError:
                    print("❌ Invalid distance value")
                    
            elif setting == '3':
                print("Select your preference:")
                print("1. 👩 Women")
                print("2. 👨 Men") 
                print("3. 🏳️‍🌈 Everyone")
                pref = input("Preference: ").strip()
                
                if pref == '1':
                    session.set_sexuality(Sexuality.WOMEN)
                    print("✅ Set to: Women")
                elif pref == '2':
                    session.set_sexuality(Sexuality.MEN)
                    print("✅ Set to: Men")
                elif pref == '3':
                    session.set_sexuality(Sexuality.EVERYONE)
                    print("✅ Set to: Everyone")
                    
            elif setting == '4':
                global_mode = input("Enable global mode? (y/n): ").lower() == 'y'
                session.set_global(global_mode)
                print(f"✅ Global mode: {'Enabled' if global_mode else 'Disabled'}")
                
        elif action == '7':
            # Check matches
            print("\n💬 CHECKING YOUR MATCHES...")
            try:
                matches = session.get_new_matches(amount=10, quickload=True)
                
                if matches:
                    print(f"✅ You have {len(matches)} new matches! 🎉")
                    print("\n👥 Your New Matches:")
                    for i, match in enumerate(matches[:5], 1):
                        name = match.get_name() or "Unknown"
                        age = match.get_age() or "?"
                        distance = match.get_distance()
                        dist_str = f" ({distance}km away)" if distance else ""
                        print(f"  {i}. {name}, {age}{dist_str}")
                    
                    if len(matches) > 5:
                        print(f"  ... and {len(matches) - 5} more!")
                    
                    # Offer to send messages
                    send_msg = input("\n💌 Send messages to matches? (y/n): ").lower()
                    if send_msg == 'y':
                        message = input("💬 Enter your message: ")
                        if message.strip():
                            for match in matches[:3]:  # Only first 3
                                try:
                                    session.send_message(match.get_chat_id(), message)
                                    print(f"✅ Sent to {match.get_name()}")
                                    time.sleep(2)
                                except Exception as e:
                                    print(f"❌ Failed to message {match.get_name()}: {e}")
                else:
                    print("😔 No new matches found. Keep swiping!")
                    
            except Exception as e:
                print(f"❌ Error checking matches: {e}")
                
        elif action == '8':
            # Test features
            print("\n🧪 TEST FEATURES")
            print("1. 🔍 Test 'Out of Matches' Detection")
            print("2. 📍 Test Location Change")
            print("3. 🔧 Test Popup Dismissal")
            print("4. 👍 Test Smart Like Button")
            print("5. ⬅️ Back to Main Menu")
            
            test_choice = input("Test choice: ").strip()
            
            if test_choice == '1':
                print("🔍 Testing out of matches detection...")
                if geomatch_helper.check_out_of_matches():
                    print("✅ Out of matches detected!")
                else:
                    print("ℹ️ Still have matches available")
                    
            elif test_choice == '2':
                test_city = input("Enter city to test (e.g., 'Berlin, Germany'): ").strip()
                if test_city:
                    print(f"📍 Testing location change to {test_city}...")
                    if geomatch_helper.change_location(test_city):
                        print("✅ Location change test successful!")
                    else:
                        print("❌ Location change test failed")
                        
            elif test_choice == '3':
                print("🔧 Testing popup dismissal...")
                if geomatch_helper.dismiss_upgrade_popup():
                    print("✅ Popup found and dismissed!")
                else:
                    print("ℹ️ No popup found to dismiss")
                    
            elif test_choice == '4':
                print("👍 Testing smart like button...")
                if geomatch_helper.like():
                    print("✅ Like successful!")
                else:
                    print("⚠️ Like failed - no button available")
            
        elif action == '9':
            print("\n👋 Thanks for using Hilal's Enhanced Smart Dating Bot!")
            print("🔒 All session data will be securely cleared")
            print("🇹🇷 Happy dating with smart automation! 💙")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1-9")
    
    return session

if __name__ == "__main__":
    try:
        print("🚀 Initializing Hilal's Enhanced Smart Dating Bot...")
        session = main()
        print("\n✅ Session completed successfully!")
    except KeyboardInterrupt:
        print("\n\n⚠️ Bot stopped by user (Ctrl+C)")
        print("👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error occurred: {e}")
        print("💡 Try restarting the bot or check your internet connection")
        import traceback
        traceback.print_exc()
    finally:
        print("\n🔒 Cleaning up and securing session data...")
        print("✅ All done! Your privacy is protected.")