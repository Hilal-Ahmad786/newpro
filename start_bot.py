#!/usr/bin/env python3
"""
Hilal's Smart Dating Bot
"""
import sys
import os

def main():
    print("🤖 HILAL'S SMART DATING BOT")
    print("Testing import...")
    
    try:
        from tinderbotz.session import Session
        print("✅ Import successful!")
        
        session = Session(headless=False)
        print("✅ Session created!")
        
        # Test manual login if method exists
        if hasattr(session, 'login_manually'):
            print("✅ Manual login available!")
            print("🔑 Starting manual login...")
            success = session.login_manually(timeout_minutes=10)
        else:
            print("⚠️ Manual login not available, using browser directly")
            session.browser.get("https://tinder.com/")
            input("Please login manually and press Enter...")
            success = True
            
        if success:
            print("🎉 Bot ready!")
            return session
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    main()
