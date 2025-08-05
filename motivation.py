import random
import datetime

quotes = [
    "🚀 The future belongs to those who create it.",
    "🔥 Stay focused. Stay hungry. Build relentlessly.",
    "🧠 Think big. Start small. Move fast.",
    "🌱 Every day is a chance to grow.",
    "💡 Ideas are easy. Execution is everything.",
    "🎯 You don’t need motivation. You need discipline.",
    "⚡ Greatness is built daily. Not in one go.",
]

today = datetime.date.today()
quote = random.choice(quotes)

print(f"\n📅 {today.strftime('%A, %B %d, %Y')}")
print(f"\n🧠 Your Motivation for Today:\n{quote}\n")
