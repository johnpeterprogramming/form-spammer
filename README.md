# To install dependencies and enable virtual environment
~~~
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
~~~

# Load example and edit .env with proper values
~~~
cp .env.example .env
~~~

# Run
~~~
python3 spam.py
~~~

# .env example
~~~
FORM_PAYLOAD="{\"entry.1108605661\":\"House Tau x Erica\"}"
FORM_URL="https://docs.google.com/forms/u/0/d/e/1FAIpQLScjIQIXjwTpIRpTa8natpJA9oNJzBHFM0mBs3l770AOZ79pow/formResponse"
~~~
