#!/usr/bin/env python3
"""
🤖 TinderBot - Optimized Version
Fast swiping with Turkey-first location preferences
"""
import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import Sexuality

def main():
    print("🤖 TINDERBOT - OPTIMIZED VERSION")
    print("="*50)
    print("✅ Turkey cities prioritized")
    print("⚡ Fast swiping (0.5-2 sec delays)")
    print("🔒 Secure credentials via .env")
    print("="*50)
    
    # Create session in INCOGNITO mode
    session = Session(headless=False, store_session=False, incognito=True)
    
    # Login options
    print("\n🔑 Choose login method:")
    print("1. Manual login (RECOMMENDED)")
    print("2. Google login")
    print("3. Facebook login")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == '1':
        print("\n🔑 Manual login mode...")
        success = session.login_manually(timeout_minutes=10)
    elif choice == '2':
        email = os.getenv('TINDER_EMAIL', input("Email: "))
        password = os.getenv('TINDER_PASSWORD', input("Password: "))
        session.login_using_google(email, password)
        success = True
    elif choice == '3':
        email = os.getenv('TINDER_EMAIL', input("Email: "))
        password = os.getenv('TINDER_PASSWORD', input("Password: "))
        session.login_using_facebook(email, password)
        success = True
    else:
        print("❌ Invalid choice")
        return
    
    if not success:
        print("❌ Login failed")
        return
    
    print("\n✅ Login successful!")
    
    # Main menu
    while True:
        print("\n📋 MAIN MENU:")
        print("1. 🚀 Fast swipe (current location)")
        print("2. 🌍 City hopper mode")
        print("3. ⚙️ Settings")
        print("4. 💬 Check matches")
        print("5. 🚪 Exit")
        
        action = input("\nChoice: ").strip()
        
        if action == '1':
            # Fast swipe mode
            amount = int(input("How many swipes? (1-500): ") or "50")
            print(f"\n⚡ Fast swiping {amount} profiles...")
            print("Delays: 0.5-2 seconds (optimized)")
            
            session.like(
                amount=amount,
                ratio="85%",  # 85% like, 15% dislike
                sleep=0.5,     # Base sleep reduced from 3 to 0.5
                randomize_sleep=True  # Will vary between 0.25-1.15 seconds
            )
            
        elif action == '2':
            # City hopper mode
            print("\n🌍 City Hopper Mode")
            print("This will change cities and swipe")
            
            # Import city hopper
            from city_swiper import city_hopper_session
            city_hopper_session(session)
            
        elif action == '3':
            # Settings
            print("\n⚙️ Settings")
            print("1. Set age range")
            print("2. Set distance")
            print("3. Set preferences")
            
            setting = input("Choice: ").strip()
            
            if setting == '1':
                min_age = int(input("Min age (18-100): ") or "18")
                max_age = int(input("Max age (18-100): ") or "55")
                session.set_age_range(min_age, max_age)
                print(f"✅ Age range set to {min_age}-{max_age}")
                
            elif setting == '2':
                distance = int(input("Max distance in km (1-160): ") or "50")
                session.set_distance_range(distance)
                print(f"✅ Distance set to {distance}km")
                
            elif setting == '3':
                print("Select preference:")
                print("1. Women")
                print("2. Men") 
                print("3. Everyone")
                pref = input("Choice: ").strip()
                
                if pref == '1':
                    session.set_sexuality(Sexuality.WOMEN)
                elif pref == '2':
                    session.set_sexuality(Sexuality.MEN)
                elif pref == '3':
                    session.set_sexuality(Sexuality.EVERYONE)
                print("✅ Preference updated")
                
        elif action == '4':
            # Check matches
            print("\n💬 Getting matches...")
            matches = session.get_new_matches(amount=10, quickload=True)
            print(f"✅ You have {len(matches)} new matches!")
            
            for i, match in enumerate(matches[:5], 1):
                print(f"  {i}. {match.get_name()}")
                
        elif action == '5':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")
    
    return session

if __name__ == "__main__":
    try:
        session = main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting safely...")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()