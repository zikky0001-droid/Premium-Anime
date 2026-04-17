from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CommandHandler, ContextTypes

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /menu command"""
    
    # Create custom keyboard with buttons
    keyboard = [
        [KeyboardButton("📊 Bot Info"), KeyboardButton("ℹ️ About")],
        [KeyboardButton("📞 Contact"), KeyboardButton("⚙️ Settings")],
        [KeyboardButton("🔙 Back to Start")]
    ]
    
    # Create reply keyboard markup
    reply_markup = ReplyKeyboardMarkup(
        keyboard, 
        resize_keyboard=True,  # Make keyboard smaller
        one_time_keyboard=False  # Keep keyboard visible
    )
    
    menu_text = """
📋 *MAIN MENU*
━━━━━━━━━━━━━━━

*Available Options:*

📊 *Bot Info* - See bot statistics and info
ℹ️ *About* - Learn about this bot  
📞 *Contact* - Get support contact
⚙️ *Settings* - Configure your preferences

━━━━━━━━━━━━━━━
💡 *Tip:* Use the buttons below to navigate
    """
    
    # Send menu with keyboard (no image)
    await update.message.reply_text(
        menu_text, 
        reply_markup=reply_markup, 
        parse_mode='Markdown'
    )

def menu_command():
    """Return the menu command handler"""
    return CommandHandler("menu", menu_callback)