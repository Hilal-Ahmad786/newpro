import smtplib
import os
from email.message import EmailMessage
import logging
from datetime import datetime

class EmailHelper:
    """
    SECURE Email helper - uses environment variables for credentials
    ⚠️ CRITICAL FIX: Removed hardcoded gmail credentials
    """
    
    @staticmethod
    def send_mail_match_found(to):
        """
        Send match notification using secure environment variables
        Requires: EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT
        """
        logger = logging.getLogger(__name__)
        
        # Get credentials from environment
        email_address = os.getenv('EMAIL_ADDRESS')
        email_password = os.getenv('EMAIL_PASSWORD') 
        smtp_server = os.getenv('EMAIL_SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('EMAIL_SMTP_PORT', '587'))
        
        if not all([email_address, email_password]):
            logger.warning("Email credentials not configured. Set EMAIL_ADDRESS and EMAIL_PASSWORD environment variables.")
            return False
            
        try:
            msg = EmailMessage()
            msg.set_content(f"🔥 Congratulations! You've got a new match on Tinder! Check your app for details.")
            msg['Subject'] = f'🎉 New Tinder Match - {datetime.now().strftime("%H:%M")}'
            msg['From'] = email_address
            msg['To'] = to
            
            # Use secure STARTTLS connection
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(email_address, email_password)
                server.send_message(msg)
            
            logger.info("Match notification sent successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to send email notification: {e}")
            return False
