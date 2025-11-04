import pywhatkit as pwk
import datetime
import os

def send_message():
    # Get group ID from environment variable
    group_id = os.getenv('D3XBFdzjsvLB6Mg0mCeGbI')
    
    if not group_id:
        print("Error: No group ID found")
        return
    
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1  # Send 1 minute from now
    
    # Determine message based on day
    if now.weekday() == 0:  # Monday
        message = """🏏 *WEEKLY FIXTURES UPDATE* 🏏

This week's matches are scheduled! 
Check Cricheroes for full details and timings.

📱 View Schedule: https://cricheroes.com/tournament/1640120/dcca-league-t16-indoor-fall-2025/matches/upcoming-matches

*Umpire Rule Reminder:* If assigned umpire is 15+ mins late, captains must mutually appoint player-umpires.

Good luck everyone!"""
    
    elif now.weekday() == 4:  # Friday
        message = """⚠️ *GAME DAY REMINDER* ⚠️

Matches are TOMORROW! 

📍 Location: https://maps.app.goo.gl/dKhaHXQzCnW8bMBN6?g_st=ipc
⏰ Time: 11 AM

📱 Live Scoring: Cricheroes App

*Umpire Protocol:* 
- Assigned umpire: [UMPIRE_NAME]
- 15-min rule in effect
- Captains arrange alternates if needed

Play fair and have fun!"""
    else:
        print("No message scheduled for today")
        return
    
    try:
        print("🤖 Starting WhatsApp automation...")
        print("📱 This will open WhatsApp Web in a browser")
        print("🔑 You need to scan QR code (one-time only)")
        
        # Calculate time 2 minutes from now
        send_time = datetime.datetime.now() + datetime.timedelta(minutes=2)
        hour = send_time.hour
        minute = send_time.minute
        
        print(f"⏰ Scheduled to send at: {hour:02d}:{minute:02d}")
        
        # Send message with longer wait time for QR scanning
        pwk.sendwhatmsg_to_group(
            group_id=group_id,
            message=message,
            time_hour=hour,
            time_min=minute,
            wait_time=30,  # 30 seconds to scan QR code
            tab_close=False  # Keep browser open to see what's happening
        )
        
        print("✅ Message sent successfully!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("💡 This is normal for first run - we need QR code setup")

if __name__ == "__main__":
    send_message()
