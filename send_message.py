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

📱 View Schedule: [YOUR_CRICHEROES_LINK_HERE]

*Umpire Rule Reminder:* If assigned umpire is 15+ mins late, captains must mutually appoint player-umpires.

Good luck everyone!"""
    
    elif now.weekday() == 4:  # Friday
        message = """⚠️ *GAME DAY REMINDER* ⚠️

Matches are TOMORROW! 

📍 Location: [YOUR_GROUND_ADDRESS]
⏰ Time: [YOUR_START_TIME]

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
        print(f"Attempting to send message to group: {group_id}")
        pwk.sendwhatmsg_to_group(
            group_id=group_id,
            message=message,
            time_hour=hour,
            time_min=minute,
            wait_time=20,
            tab_close=True
        )
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

if __name__ == "__main__":
    send_message()
