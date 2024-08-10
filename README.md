# QA_Bootcamp_Final_Project
# Demo Blaze Web Application Test Project

Welcome to the **Demo Blaze Web Application Test Project**! This project showcases my commitment to delivering high-quality, automated testing solutions for web applications. Leveraging the power of Python, Selenium WebDriver, and a range of modern testing tools, I meticulously crafted a comprehensive suite of automated test cases to ensure the robustness and reliability of the Demo Blaze web application.

## Key Features

- **Automated Testing:** Utilized Python and Selenium WebDriver to automate a wide range of test cases, ensuring consistency and efficiency.
- **Test Execution:** Integrated Pytest for streamlined test execution, with options to run tests via terminal commands or manually in PyCharm.
- **Comprehensive Reporting:** Implemented Allure and HTML reporting for detailed insights into test results and execution metrics.
- **Advanced Marking:** Employed `pytest.mark` for selective test runs, providing flexibility in test management.

## Installation

### System Requirements

- Python 3.8+
- Pip (Python package manager)
- Chrome WebDriver (compatible with your Chrome browser version)

### Required Libraries

Before running the tests, ensure you have the following packages installed:

```bash
pip install selenium faker jira requests allure-pytest pytest
pytest --alluredir=allure-results
allure serve allure-results