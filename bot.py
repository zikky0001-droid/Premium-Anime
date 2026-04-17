import asyncio
import os
from telegram.ext import Application
from commands.start import start_command
from commands.menu import menu_command
from commands.help import help_command  # Add this line

# Get token from environment variable
TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

async def main():
    # Create application
    app = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    app.add_handler(start_command())
    app.add_handler(menu_command())
    app.add_handler(help_command())  # Add this line
    
    # Start bot
    print("🤖 Bot is starting...")
    print("✅ Bot is now running! Press Ctrl+C to stop.")
    
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n❌ Bot stopped.")