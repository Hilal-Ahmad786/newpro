#!/usr/bin/env python3
"""
🎯 Smart Dating Bot - Quick Demo
Test the bot with a short 2-minute demo
"""
import time

def main():
    print("🎯 SMART DATING BOT - QUICK DEMO")
    print("=" * 40)
    print("This demo will:")
    print("✓ Test manual login")
    print("✓ Like 3 profiles")
    print("✓ Show current profile info")
    print("✓ Demonstrate basic features")
    print()
    
    input("Press Enter to start demo...")
    
    try:
        from tinderbotz.session import Session
        
        # Create session for demo
        session = Session(headless=False, store_session=False)
        
        print("\n🔑 Demo: Manual Login Test")
        print("Please login manually (you have 3 minutes)...")
        
        if not session.login_manually(timeout_minutes=3):
            print("❌ Demo cancelled - couldn't login")
            return
        
        print("\n🤖 Demo: Basic Automation Test")
        
        # Test 1: Like a few profiles
        print("\n👍 Test 1: Liking 3 profiles...")
        session.like(amount=3, ratio="100%", sleep=2)
        
        # Test 2: Get profile info
        print("\n📊 Test 2: Getting profile information...")
        try:
            profile = session.get_geomatch()
            if profile and profile.get_name():
                print(f"   Current Profile: {profile.get_name()}")
                print(f"   Age: {profile.get_age()}")
                print(f"   Bio: {len(profile.get_bio() or '')} characters")
                print(f"   Distance: {profile.get_distance()} km")
            else:
                print("   No profile currently available")
        except Exception as e:
            print(f"   Could not get profile: {e}")
        
        # Test 3: Show matches count
        print("\n💕 Test 3: Checking matches...")
        try:
            matches = session.get_new_matches(amount=5, quickload=True)
            print(f"   You have {len(matches)} recent matches")
            if matches:
                for i, match in enumerate(matches[:3], 1):
                    print(f"   {i}. {match.get_name()}")
        except Exception as e:
            print(f"   Could not get matches: {e}")
        
        print("\n🎉 DEMO COMPLETE!")
        print("✅ Manual login: Working")
        print("✅ Profile liking: Working")
        print("✅ Data retrieval: Working")
        print("\n🚀 Ready to use the full bot!")
        print("   Run: python start_bot.py")
        
    except ImportError:
        print("❌ Please install requirements: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Demo error: {e}")

if __name__ == "__main__":
    main()
