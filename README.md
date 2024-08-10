# QA_Bootcamp_Final_Project
# Demo Blaze Web Application Test Project

Welcome to the **Demo Blaze Web Application Test Project**! This project showcases my commitment to delivering high-quality, automated testing solutions for web applications. Leveraging the power of Python, Selenium WebDriver, and a range of modern testing tools, I meticulously crafted a comprehensive suite of automated test cases to ensure the robustness and reliability of the Demo Blaze web application.

## Key Features

- **Automated Testing:** Utilized Python and Selenium WebDriver to automate a wide range of test cases, ensuring consistency and efficiency.
- **Test Execution:** Integrated Pytest for streamlined test execution, with options to run tests via terminal commands or manually in PyCharm.
- **Comprehensive Reporting:** Implemented Allure and HTML reporting for detailed insights into test results and execution metrics.


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
```

### Installation Steps

1. Clone this repository to your local machine. https://github.com/Ehab05/QA_Bootcamp_Final_Project.git
2. Navigate to the project directory.
3. Install the required packages using the command above.

## Usage

### Running Tests via Pytest

To run all tests using Pytest and generate reports:

```bash
pytest --alluredir=allure-results
```

For specific tests using pytest.mark:

```bash
pytest -m "marker_name" --alluredir=allure-results
```

To generate an HTML report:

```bash
pytest --html=report.html
```

## Running Tests Manually in PyCharm
1. Open the project in PyCharm.
2. Navigate to the desired test file.
3. Right-click on the test function and select "Run" to execute it individually.

## Project Structure
- **infra/:** Contains infrastructure-related files and settings.
- **logic/:** Houses the core logic, organized by UI and API components.
- **tests/:** Contains test cases, organized by API and UI, with utilities for support.
- **demo_blaze_config/:** Stores configuration of the project.
- **logs/:** Directory for log files generated during test execution.

## Technologies Used
- **Python:** Core programming language.
- **Selenium WebDriver:** Browser automation.
- **Pytest:** Test execution framework.
- **Allure:** Reporting tool for detailed insights.
- **Faker:** Data generation.
- **JIRA:** Issue tracking and management.
- **Requests:** For API interactions.

## Logging and Configuration

The project uses a JSON configuration file to manage settings and a Logger to track and record 
information and errors during execution. Logs are stored in the logs/ directory for easy access and review.

## Contributors
This project was developed and is maintained by Ehab Khalil

## Contact
For more details on contributing, known issues, or other inquiries, feel free to reach out or explore the project documentation.
🔗 Ehabkhalil5@gmail.com