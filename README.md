# Google Finance Automation

This repository contains a Selenium-based automation framework to interact with the Google Finance web application. The framework includes the `GoogleFinance` class for web interaction and a set of pytest tests to validate the functionality. GitHub Actions workflows are also set up to run tests manually and as part of nightly regressions.

## Table of Contents

- [Google Finance Automation](#google-finance-automation)
  - [Table of Contents](#table-of-contents)
  - [Files in This Repository](#files-in-this-repository)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
    - [Run All Tests](#run-all-tests)
    - [Run Specific Tests by Marker](#run-specific-tests-by-marker)
  - [GitHub Actions Workflows](#github-actions-workflows)
    - [Nightly Regression Workflow](#nightly-regression-workflow)
    - [Manual Test Execution Workflow](#manual-test-execution-workflow)
  - [Contributing](#contributing)
  - [License](#license)

## Files in This Repository

- `google_finance.py`: Contains the `GoogleFinance` class, which interacts with the Google Finance web application using Selenium.
- `test_google_finance.py`: Contains pytest tests for the `GoogleFinance` class, marked with `@pytest.mark` for selective test execution.
- `.github/workflows/nightly_regression.yml`: A GitHub Actions workflow that runs the tests nightly.
- `.github/workflows/manual.yml`: A GitHub Actions workflow that allows manual triggering of tests with specific markers.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/google-finance-automation.git
   cd google-finance-automation
