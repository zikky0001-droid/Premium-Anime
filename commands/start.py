from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    user = update.effective_user
    
    # Welcome message
    welcome_text = f"""
🌟 *Welcome to My Bot, {user.first_name}!* 🌟

I'm your personal assistant bot. Here to help you with various tasks.

✨ *What I can do:*
• Provide information
• Help with commands
• And much more!

📌 *Get Started:*
Type /menu to see all available options

🔧 *Need Help?*
Use /help anytime

Let's get started! 🚀
    """
    
    # Send welcome message with photo
    try:
        with open('media/bot-image.jpg', 'rb') as photo:
            await update.message.reply_photo(
                photo, 
                caption=welcome_text,
                parse_mode='Markdown'
            )
    except FileNotFoundError:
        # Send text only if image doesn't exist
        await update.message.reply_text(
            welcome_text, 
            parse_mode='Markdown'
        )

def start_command():
    """Return the start command handler"""
    return CommandHandler("start", start_callback))