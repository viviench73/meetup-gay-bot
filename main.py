from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

START_TEXT = """💐 Welcome to a secure and welcoming community designed exclusively for you to discover wonderful local friends, organize authentic face-to-face hangouts, and create unforgettable, joyful memories together. Whether you are looking to expand your social circle, share great conversations, or build meaningful connections in a trusted environment, you have finally arrived at the right place. Let's make every moment count!"""

HELP_TEXT = """Welcome to our community support guide! This bot is designed to help you easily navigate through our safe spaces, connect with local friends, and stay updated with our community guidelines. You can use /rules to review our community guidelines to ensure a safe environment, use /groups to explore all our official group links and join conversations, or use /contact to reach out directly to the administrator for any assistance, support, or questions. We are here to make your experience smooth and welcoming!"""

RULES_TEXT = """📌 Mutual Respect: Treat every member with respect. Harassment, hate speech, bullying, or toxic behavior will result in an immediate ban.

📌 Safety & Privacy: Do not share private information (phone numbers, addresses, or personal photos) of yourself or others without permission.

📌 No Spam: Avoid spamming messages, unauthorized promotional links, or unrelated advertisements in the community.

📌 Age Restriction: Members must be 18 years or older to join this community and participate in hangouts.

📌 Authentic Profiles: Use a clear profile picture and a recognizable name. Fake accounts or impersonation will be banned.

📌 Consent & Boundaries: Always respect others' personal boundaries. Unsolicited explicit content or harassment in private messages is strictly prohibited.

📌 Meetup Safety: When planning real-life hangouts, always meet in safe, public places and inform someone you trust."""

GROUPS_TEXT = """📌 A safe space to find local friends, plan real hangouts, and make memorable moments together.

💞 MeetUp Gay 🔗 https://t.me/+m0MwnTRahoZhZmZl

🏳️‍🌈 Tamil Gay Meeting 🔗 https://t.me/tamil_gay_meeting

⚡GenZ Tamil Chat 🔗 https://t.me/genz_tamil_chat

🌈 Tamil Queer chat 🔗https://t.me/tamil_queer_chat

❣️Chennai Hookups Crew 🔗 https://t.me/chennai_hookups_crew"""

CONTACT_TEXT = "@neoapexlord"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


async def rules_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(RULES_TEXT)


async def groups_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(GROUPS_TEXT)


async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(CONTACT_TEXT)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("rules", rules_command))
    app.add_handler(CommandHandler("groups", groups_command))
    app.add_handler(CommandHandler("contact", contact_command))

    app.run_polling()


if __name__ == "__main__":
    main()
