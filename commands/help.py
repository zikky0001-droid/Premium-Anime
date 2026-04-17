from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command"""
    
    help_text = """
❓ *HELP CENTER*
━━━━━━━━━━━━━━━

*Available Commands:*

/start - Initialize the bot
/menu - Show main menu
/help - Display this help message

━━━━━━━━━━━━━━━

*How to Use:*
1. Type /start to begin
2. Use /menu to see options
3. Click buttons to interact

━━━━━━━━━━━━━━━

📧 *Support:*
Contact: @YourSupportHandle
Email: support@example.com

*More features coming soon!* 🚀
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

def help_command():
    """Return the help command handler"""
    return CommandHandler("help", help_callback)