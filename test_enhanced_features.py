#!/usr/bin/env python3
"""
🧪 Test Enhanced Features
Test script for the new location changing and smart detection features
"""
import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()

def test_enhanced_features():
    print("🧪 TESTING ENHANCED FEATURES")
    print("="*50)
    
    try:
        from tinderbotz.session import Session
        from tinderbotz.helpers.geomatch_helper import GeomatchHelper
        
        print("✅ Imports successful")
        
        # Create session
        print("\n🚀 Creating test session...")
        session = Session(headless=False, store_session=False, incognito=True)
        print("✅ Session created successfully")
        
        # Test manual login
        print("\n🔑 Testing manual login...")
        success = session.login_manually(timeout_minutes=5)
        
        if not success:
            print("❌ Login failed or timed out")
            return
            
        print("✅ Login successful!")
        
        # Get enhanced helper
        print("\n🤖 Creating enhanced geomatch helper...")
        helper = GeomatchHelper(session.browser)
        print("✅ Helper created successfully")
        
        # Test menu
        while True:
            print("\n" + "="*50)
            print("🧪 FEATURE TEST MENU")
            print("="*50)
            print("1. 🔍 Test 'Out of Matches' Detection")
            print("2. 📍 Test Location Change")
            print("3. 🔧 Test Popup Dismissal")
            print("4. 👍 Test Smart Like Detection")
            print("5. 👎 Test Smart Dislike Detection")
            print("6. 🚀 Test Smart Swipe Session (3 cities)")
            print("7. 🚪 Exit Tests")
            print("="*50)
            
            choice = input("👉 Choose test: ").strip()
            
            if choice == '1':
                print("\n🔍 TESTING OUT OF MATCHES DETECTION")
                print("Checking if current location has matches...")
                
                if helper.check_out_of_matches():
                    print("✅ OUT OF MATCHES DETECTED!")
                    print("   This means the location change feature should trigger")
                else:
                    print("ℹ️ Still have matches available")
                    print("   Location change won't be needed yet")
                    
            elif choice == '2':
                print("\n📍 TESTING LOCATION CHANGE")
                
                test_cities = ["Berlin, Germany", "Paris, France", "London, UK"]
                
                print("Available test cities:")
                for i, city in enumerate(test_cities, 1):
                    print(f"   {i}. {city}")
                
                city_choice = input("Choose city number (1-3): ").strip()
                
                try:
                    city_index = int(city_choice) - 1
                    if 0 <= city_index < len(test_cities):
                        test_city = test_cities[city_index]
                        
                        print(f"\n🌍 Testing location change to: {test_city}")
                        print("This will:")
                        print("   1. Click on profile")
                        print("   2. Navigate to location settings")
                        print("   3. Search for the city")
                        print("   4. Select from dropdown")
                        print("   5. Confirm location marker")
                        print("   6. Return to swiping")
                        
                        proceed = input("\nProceed with location change test? (y/n): ").lower()
                        
                        if proceed == 'y':
                            if helper.change_location(test_city):
                                print("✅ LOCATION CHANGE TEST SUCCESSFUL!")
                                print(f"   Successfully changed to {test_city}")
                            else:
                                print("❌ LOCATION CHANGE TEST FAILED")
                                print("   Check if Tinder Passport is available")
                    else:
                        print("❌ Invalid city choice")
                except ValueError:
                    print("❌ Please enter a valid number")
                    
            elif choice == '3':
                print("\n🔧 TESTING POPUP DISMISSAL")
                print("Looking for upgrade popups to dismiss...")
                
                if helper.dismiss_upgrade_popup():
                    print("✅ POPUP FOUND AND DISMISSED!")
                    print("   Successfully handled upgrade popup")
                else:
                    print("ℹ️ NO POPUP FOUND")
                    print("   No upgrade popups currently visible")
                    
            elif choice == '4':
                print("\n👍 TESTING SMART LIKE DETECTION")
                print("This will test if like button is available and clickable")
                
                proceed = input("Proceed with like test? (y/n): ").lower()
                if proceed == 'y':
                    if helper.like():
                        print("✅ SMART LIKE TEST SUCCESSFUL!")
                        print("   Like button was found and clicked")
                    else:
                        print("⚠️ SMART LIKE TEST - NO BUTTON")
                        print("   Like button not available (may be out of profiles)")
                        
            elif choice == '5':
                print("\n👎 TESTING SMART DISLIKE DETECTION")
                print("This will test if dislike button is available and clickable")
                
                proceed = input("Proceed with dislike test? (y/n): ").lower()
                if proceed == 'y':
                    if helper.dislike():
                        print("✅ SMART DISLIKE TEST SUCCESSFUL!")
                        print("   Dislike button was found and clicked")
                    else:
                        print("⚠️ SMART DISLIKE TEST - NO BUTTON")
                        print("   Dislike button not available")
                        
            elif choice == '6':
                print("\n🚀 TESTING SMART SWIPE SESSION")
                print("This will test the full smart session with location changes")
                
                test_cities = ["Istanbul, Turkey", "Berlin, Germany", "Paris, France"]
                swipes_per_city = 5  # Small number for testing
                
                print(f"Test configuration:")
                print(f"   Cities: {test_cities}")
                print(f"   Swipes per city: {swipes_per_city}")
                print(f"   Features: Auto location change, smart detection, popup handling")
                
                proceed = input("\nProceed with smart session test? (y/n): ").lower()
                if proceed == 'y':
                    print("\n🚀 Starting smart session test...")
                    
                    stats = helper.smart_swipe_session(test_cities, swipes_per_city)
                    
                    print("\n📊 SMART SESSION TEST RESULTS:")
                    print("="*40)
                    for key, value in stats.items():
                        print(f"   {key.replace('_', ' ').title()}: {value}")
                    print("="*40)
                    
                    if stats['cities_visited'] > 0:
                        print("✅ SMART SESSION TEST SUCCESSFUL!")
                    else:
                        print("⚠️ SMART SESSION TEST - LIMITED SUCCESS")
                        
            elif choice == '7':
                print("\n👋 Exiting feature tests...")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1-7")
                
        print("\n✅ All tests completed!")
        print("🔒 Session will be cleaned up automatically")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n🧹 Cleaning up test session...")
        print("✅ Tests completed!")

if __name__ == "__main__":
    print("🧪 Enhanced Features Test Suite")
    print("This will test the new location changing and smart detection features")
    
    proceed = input("\nStart feature tests? (y/n): ").lower()
    if proceed == 'y':
        test_enhanced_features()
    else:
        print("👋 Tests cancelled")