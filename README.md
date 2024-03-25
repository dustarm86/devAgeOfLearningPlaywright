# devAgeOfLearningPlaywright
using python, pytest, and playwright this tool automates a test scenario utilizing the page object model within the PyCharm IDE

# how to install and run correctly
1. pip install pytest playwright pytest-playwright (this is using PyCharm as an IDE and using venv)
2. pip install configparser (to read config.ini file that contains the URL and Email/UN)
3. you may then need to run this command to add the most updated browsers (default is chromium) for playwright to use: playwright install
4. within the home_page.py file, you'll need to include the entire path where this project is stored locally on your PC for ConfigParser to read the config.ini file correctly. (e.g. /Users/dieter/python/devAgeOfLearningAutomation/config.ini')
5. by default, Playwright runs in headless mode, but if you'd like to see the end to end test run in headed mode include the flag "--headed" while running the pytest command in the correct directory the test is located within the project (e.g. cd tests, then pytest test_home_page.py --headed)
