# 🎓 FAQ University Telegram Bot

This is a simple and customizable Telegram chatbot for answering university-related questions.  
Built with Python using the `python-telegram-bot` library and deployed 24/7 on Railway.

---

## 💡 Features

- Replies to student questions via Telegram
- Easily expandable with CSV-based FAQs (coming soon)
- Secure token handling using environment variables
- Lightweight and fast
- Open-source and easy to edit

---

## 🛠 Tech Stack

- **Language:** Python 3.9+
- **Bot Framework:** [python-telegram-bot](https://python-telegram-bot.org)
- **Hosting:** [Railway](https://railway.app)
- **Version Control:** Git + GitHub

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/faq-uni-chatbot.git
cd faq-uni-chatbot

2. Create a .env file in the root folder
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

3. Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For macOS/Linux

4. Install dependencies
pip install -r requirements.txt

5. Run the bot
python faq_bot.py


🌐 Deployment (Railway)
This project is hosted for free using Railway.

The Procfile tells Railway how to run the bot:

worker: python faq_bot.py

Environment variables (like your bot token) are securely stored in Railway settings.

GitHub pushes automatically trigger a redeploy.


🔧 Planned Features

 Load questions/answers from a .csv file

 Add Telegram buttons for quick replies

 Multilingual support (Arabic / French / English)

 Web dashboard (admin-facing)

🤝 Contributing
Forks, pull requests, and ideas are welcome.
Feel free to adapt this bot for your own school, startup, or support system.

📄 License
This project is licensed under the MIT License.
