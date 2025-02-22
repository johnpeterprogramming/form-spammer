# To install dependencies
pip3 install -r requirements.txt

# Load environment variables
cp .env.example .env

# Run
python3 spam.py

# .env example
FORM_PAYLOAD="{\"entry.1108605661\":\"House Tau x Erica\"}"
FORM_URL="https://docs.google.com/forms/u/0/d/e/1FAIpQLScjIQIXjwTpIRpTa8natpJA9oNJzBHFM0mBs3l770AOZ79pow/formResponse"
