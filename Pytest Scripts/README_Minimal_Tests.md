# Minimal Pytests
Alongside my more detailed test scripts (with waits, expected conditions, and assertions), I added a set of minimal Pytest files.

# Why I added minimal tests
- To show that I can strip a test down to its core logic (just entering credentials and checking results).
- Demonstrates that I understand how to write concise tests without relying on extra waits or conditions.
- Highlights that I can build both best practice tests and lightweight exploratory tests depending on the situation.

# Files
- `test_login_minimal.py`: Tests a valid login using only username and password fields.
- `test_invalid_login_minimal.py`: Tests an invalid login by entering bad credentials and asserting the error message.

# Issues I ran into
I accidentally typed a variable name incorrectly (erorr_element instead of error_element), which caused a NameError. This reminded me to double-check variable spelling since Python is case/letter sensitive.
Without .text, I was only selecting the element itself and not the actual error message string which I needed for my assertion.

# What I learned
- How to use .text to extract the visible text from an element, not just grab the element itself.
- That [data-test='error'] is a clean and reliable CSS selector for the login error message on SauceDemo.
