#!/usr/bin/env python3
"""
🚀 Secure TinderBot Startup
"""
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    print("🚀 Starting Secure TinderBot...")
    
    # Check environment
    if not os.getenv("TINDER_EMAIL"):
        print("❌ Please configure .env file first!")
        print("   cp .env.example .env")
        print("   # Edit .env with your credentials")
        return
    
    # Import and start
    from tinderbotz.session import Session
    
    session = Session(
        store_session=os.getenv('STORE_SESSION', 'false').lower() == 'true'
    )
    
    # Login securely
    email = os.getenv('TINDER_EMAIL')
    password = os.getenv('TINDER_PASSWORD')
    
    print(f"🔑 Logging in as {email}...")
    session.login_using_google(email, password)
    
    print("✅ Secure TinderBot ready!")
    return session

if __name__ == "__main__":
    session = main()
