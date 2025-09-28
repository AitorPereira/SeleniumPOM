# Selenium POM Project

A Selenium Page Object Model (POM) testing framework project.

## Project Structure

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

## Setup

1. **Install dependencies:**
   ```bash
   pip install selenium pytest
   ```

2. **Run tests:**
   ```bash
   # Run all tests
   pytest src/test/ -v
   
   # Run specific test file
   pytest src/test/scripts/test_demo.py -v
   
   # Run with environment parameter
   pytest src/test/ -v --env qa
   ```

## Features

- Page Object Model pattern implementation
- Environment-based configuration (dev, qa, stg)
- Pytest integration with custom fixtures
- WebDriver setup with proper teardown
- Cross-platform support

## Requirements

- Python 3.12+
- Selenium 4.35.0
- Chrome WebDriver (automatically managed by Selenium)
