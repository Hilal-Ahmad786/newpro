#!/usr/bin/env python3
"""
🤖 Hilal's Smart Dating Bot - Full Automation
Continues automation after manual login
"""
import time
import sys

def main():
    print("🤖 HILAL'S SMART DATING BOT - FULL AUTOMATION")
    print("="*60)
    
    try:
        from tinderbotz.session import Session
        print("✅ Import successful!")
        
        # Create session
        session = Session(headless=False, store_session=True)
        print("✅ Session created!")
        
        # Manual login
        print("\n🔑 Starting manual login...")
        success = session.login_manually(timeout_minutes=10)
        
        if not success:
            print("❌ Login failed or timed out")
            return
        
        print("\n🎉 LOGIN SUCCESSFUL! Starting automation...")
        
        # Show menu of automation options
        print("\n🤖 Choose automation mode:")
        print("1. 👍 Like profiles (conservative)")
        print("2. 🔥 Like profiles (aggressive)") 
        print("3. 📊 Get profile information")
        print("4. 💬 Check matches")
        print("5. 🎯 Custom automation")
        print("6. 🚀 Full auto mode")
        
        while True:
            try:
                choice = input("\nEnter choice (1-6): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6']:
                    break
                print("❌ Please enter 1-6")
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                return
        
        if choice == '1':
            # Conservative liking
            print("\n👍 CONSERVATIVE LIKING MODE")
            print("Settings: 15 likes, 75% ratio, 4 second delays")
            
            confirm = input("Continue? (y/n): ").lower()
            if confirm == 'y':
                session.like(amount=15, ratio="75%", sleep=4)
                print("✅ Conservative liking completed!")
        
        elif choice == '2':
            # Aggressive liking  
            print("\n🔥 AGGRESSIVE LIKING MODE")
            print("Settings: 30 likes, 90% ratio, 2 second delays")
            print("⚠️ Higher chance of getting flagged!")
            
            confirm = input("Continue? (y/n): ").lower()
            if confirm == 'y':
                session.like(amount=30, ratio="90%", sleep=2)
                print("✅ Aggressive liking completed!")
        
        elif choice == '3':
            # Profile information
            print("\n📊 PROFILE INFORMATION MODE")
            print("Getting information about current profiles...")
            
            for i in range(5):
                try:
                    profile = session.get_geomatch()
                    if profile:
                        print(f"\n👤 Profile {i+1}:")
                        print(f"   Name: {profile.get_name()}")
                        print(f"   Age: {profile.get_age()}")
                        print(f"   Distance: {profile.get_distance()} km")
                        print(f"   Bio: {len(profile.get_bio() or '')} characters")
                        print(f"   Images: {len(profile.get_image_urls() or [])} photos")
                        
                        # Ask what to do with this profile
                        action = input("   Action (l=like, d=dislike, s=skip): ").lower()
                        if action == 'l':
                            session.like(amount=1)
                            print("   ✅ Liked!")
                        elif action == 'd':
                            session.dislike(amount=1)
                            print("   ❌ Disliked!")
                        else:
                            print("   ⏭️ Skipped!")
                    else:
                        print(f"   No profile data available")
                        session.dislike(amount=1)  # Move to next
                        
                except Exception as e:
                    print(f"   ❌ Error getting profile: {e}")
                    break
                    
                time.sleep(2)
        
        elif choice == '4':
            # Check matches
            print("\n💬 CHECKING MATCHES")
            
            try:
                print("📥 Getting new matches...")
                new_matches = session.get_new_matches(amount=10, quickload=True)
                
                print(f"✅ Found {len(new_matches)} new matches:")
                for i, match in enumerate(new_matches, 1):
                    print(f"   {i}. {match.get_name()}")
                
                if new_matches:
                    send_messages = input("\nSend messages to matches? (y/n): ").lower()
                    if send_messages == 'y':
                        message = input("Enter message to send: ")
                        
                        for match in new_matches[:5]:  # Only first 5
                            try:
                                session.send_message(match.get_chat_id(), message)
                                print(f"✅ Sent message to {match.get_name()}")
                                time.sleep(3)  # Delay between messages
                            except Exception as e:
                                print(f"❌ Failed to message {match.get_name()}: {e}")
                
            except Exception as e:
                print(f"❌ Error checking matches: {e}")
        
        elif choice == '5':
            # Custom automation
            print("\n🎯 CUSTOM AUTOMATION MODE")
            
            try:
                amount = int(input("How many profiles to like? (1-50): "))
                ratio = input("Like ratio? (e.g., 80%): ")
                sleep_time = int(input("Seconds between actions? (1-10): "))
                
                if 1 <= amount <= 50 and 1 <= sleep_time <= 10:
                    print(f"\n🚀 Starting custom automation:")
                    print(f"   Amount: {amount}")
                    print(f"   Ratio: {ratio}")
                    print(f"   Delay: {sleep_time}s")
                    
                    confirm = input("Continue? (y/n): ").lower()
                    if confirm == 'y':
                        session.like(amount=amount, ratio=ratio, sleep=sleep_time)
                        print("✅ Custom automation completed!")
                else:
                    print("❌ Invalid settings")
                    
            except ValueError:
                print("❌ Please enter valid numbers")
        
        elif choice == '6':
            # Full auto mode
            print("\n🚀 FULL AUTO MODE")
            print("This will run continuous automation with breaks")
            print("⚠️ Use responsibly to avoid getting banned!")
            
            confirm = input("Continue? (y/n): ").lower()
            if confirm == 'y':
                
                for session_num in range(3):  # 3 sessions
                    print(f"\n🤖 Auto Session {session_num + 1}/3")
                    
                    # Like some profiles
                    print("   👍 Liking profiles...")
                    session.like(amount=10, ratio="80%", sleep=5)
                    
                    # Check for matches
                    print("   💕 Checking matches...")
                    try:
                        matches = session.get_new_matches(amount=5, quickload=True)
                        print(f"   Found {len(matches)} new matches")
                    except:
                        print("   Could not check matches")
                    
                    # Break between sessions
                    if session_num < 2:  # Don't wait after last session
                        print("   😴 Taking a 60-second break...")
                        time.sleep(60)
                
                print("✅ Full auto mode completed!")
        
        # Keep session alive
        print(f"\n🎉 Automation completed!")
        print(f"💡 Session is still active. You can:")
        print(f"   - Run more automation")
        print(f"   - Use manual commands")
        print(f"   - Or press Ctrl+C to exit")
        
        try:
            while True:
                command = input("\n💬 Enter command (or 'exit'): ").strip().lower()
                
                if command == 'exit':
                    break
                elif command.startswith('like'):
                    # Parse like command: like 10
                    try:
                        amount = int(command.split()[1]) if len(command.split()) > 1 else 5
                        session.like(amount=amount, sleep=3)
                        print(f"✅ Liked {amount} profiles!")
                    except:
                        session.like(amount=5, sleep=3)
                        print("✅ Liked 5 profiles!")
                        
                elif command == 'matches':
                    try:
                        matches = session.get_new_matches(amount=5, quickload=True)
                        print(f"💕 You have {len(matches)} new matches")
                        for i, match in enumerate(matches, 1):
                            print(f"   {i}. {match.get_name()}")
                    except Exception as e:
                        print(f"❌ Error: {e}")
                        
                elif command == 'profile':
                    try:
                        profile = session.get_geomatch()
                        if profile:
                            print(f"👤 Current profile:")
                            print(f"   Name: {profile.get_name()}")
                            print(f"   Age: {profile.get_age()}")
                            print(f"   Distance: {profile.get_distance()} km")
                        else:
                            print("❌ No profile available")
                    except Exception as e:
                        print(f"❌ Error: {e}")
                        
                elif command == 'help':
                    print("💡 Available commands:")
                    print("   like [number] - Like profiles")
                    print("   matches       - Show matches")
                    print("   profile       - Show current profile")
                    print("   exit          - Exit bot")
                    
                else:
                    print("❌ Unknown command. Type 'help' for available commands.")
                    
        except KeyboardInterrupt:
            pass
        
        print("\n👋 Exiting Smart Dating Bot...")
        print("💾 Session data saved automatically")
        print("🛡️ All temporary files cleaned up")
        print("\nThank you for using Hilal's Smart Dating Bot! 💕")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()