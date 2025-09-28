# 🧪 Selenium Automation Framework: Pytest + Page Object Model

This repo is a Selenium-based test automation framework built in Python.
It follows the Page Object Model (POM) design pattern and integrates with Pytest for test execution and configuration across environments.

⸻

### 🚀 Tech Stack  
• Core: Python 3.8+

• Libraries & Tools:  
	- Selenium → browser automation
	- Pytest → test runner, fixtures & markers
	- Unittest → WebDriver setup base
	- urllib3 → handle SSL warnings
	
• Concepts Explored:  
	- Page Object Model (POM)
	- Cross-environment configuration
	- WebDriver setup & teardown
	- Pytest fixtures for flexible test orchestration

⸻

## 📂 Project Structure

A Selenium Page Object Model (POM) testing framework project.

```
src/
├── PageObject/
│   └── Pages/
│       └── HomePage.py          # Page object for home page
├── TestBase/
│   └── WebDriverSetup.py        # WebDriver setup and teardown
└── test/
    ├── config.py                # Configuration for different environments
    ├── conftest.py              # Pytest configuration and fixtures
    └── scripts/
        └── test_demo.py         # Test cases
```

## 🔑 Key Features
1.	Page Object Model (POM)
	•	Encapsulates web elements and interactions inside HomePage.py.
	•	Makes tests more readable, maintainable, and scalable.
2.	Reusable WebDriver Setup
	•	Centralized WebDriverSetup.py handles driver init, maximize window, and teardown.
3.	Environment-Aware Testing
	•	config.py and conftest.py provide dynamic configs (dev, qa, stg).
	•	Easily switch environments via CLI flag --env.
4.	Sample Test Workflow
	•	Demo test (test_demo.py) executes a sign-up flow on Test Automation Practice.

⸻

## ⚡ Getting Started

1. Clone Repo
```
git clone https://github.com/your-username/selenium-pytest-framework.git
cd selenium-pytest-framework
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Run Tests
Run with Pytest:
```
pytest -s -v --env=qa
```
Run with Unittest (directly from WebDriverSetup):
```
python -m unittest src/test/scripts/test_demo.py
```

## 🖥️ Example Test Case
```
def test_add_item_to_course_pack(self):
    driver = self.driver
    self.driver.get(HomePage.get_url_base())
    home_page = HomePage(driver)
    home_page.sign_up("John", "john@gmail.com", "9432344321", "Canada", "423 John Smith 04324, Ontario")
    home_page.click_sign_up()
```

### 💡 Why this project?
✔️ Clean separation of concerns with Page Object Model.
✔️ Pytest-driven, environment-configurable execution.
✔️ Scalable design for UI test automation.
✔️ A foundation to expand into CI/CD pipelines.

### 📜 License
This project is licensed under the MIT License.

✨ Thanks for checking it out!
Feel free to fork, contribute, or adapt this framework for your own automation needs. 🚀
