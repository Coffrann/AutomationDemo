
# Example Testing Framework with Pytest

## Introduction

Welcome to my Open Testing Framework repository! This project showcases my skills and expertise in automated testing using Pytest. Designed for fellow developers and QAs, this framework demonstrates best practices, clean code, and efficient automation strategies.

## Features

- **Comprehensive Test Coverage**: Includes a variety of test cases covering different aspects of web applications.
- **Modular Architecture**: Designed with a focus on reusability and maintainability.
- **Easy Setup and Execution**: Simple installation process and intuitive commands to run tests.
- **Detailed Reporting**: Generates detailed test reports for easy analysis and debugging.
- **CI/CD Integration**: Ready for integration with Continuous Integration and Continuous Deployment pipelines.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js and npm (for Playwright installation)
- Git (to clone the repository)
- Allure CLI (to visualize reports)

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:{user}/AutomationDemo.git
   cd AutomationDemo
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   playwright install
   ```

### Running Tests

To execute the test suite, use the following command:

```bash
pytest
```

For a specific test file or directory, you can specify the path:

```bash
pytest tests/test_example.py -n 4 --headless
```
- -n: Number of threads
- headless: Run tests with headless browser

### Generating Reports

After running the tests, a report will be generated with Allure, to open it run in the terminal: 
   ```
   allure serve ./report
   ```

## Project Structure

```
open-testing-framework/
│
├── constants/             # Constants for assertions
│   ├── pages/             # Browser tests constants
│   └── api/               # Api tests constants
│
├── tests/                 # Test cases
│   ├── test_example.py    # Example test file
│   └── ...
│
├── api/                   # Api Object Models
│   ├── base_api.py        # Base Api class
│   └── ...
│
├── pages/                 # Page Object Models
│   ├── base_page.py       # Base Page class
│   └── ...
│
├── report/                # Output files for report
│   └── ...
│
├── utils/                 # Utility functions and helpers
│   └── ...
│
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── README.md              # This README file
└── ...
```

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your features or bug fixes, and submit a pull request. Ensure your code adheres to the existing style and includes relevant tests.

## Contact

Feel free to reach out if you have any questions or suggestions. You can contact me via [email](mailto:franco.kleinerman@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/franco-kleinerman-b64ba718b/).

---

Thank you for visiting my project! I hope this framework provides a clear demonstration of my skills in automated testing with Python and Playwright.
