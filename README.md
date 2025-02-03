# BrowserStack Playwright Automation

This project demonstrates how to use Playwright for automating browser interactions on BrowserStack. It includes tests for logging into a demo site and performing an item purchase action, using the `playwright-python` library and BrowserStack as the cloud testing service.

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.6+
- [Playwright](https://playwright.dev/python/docs/intro) (via pip)
- [pytest](https://pytest.org/)
- A [BrowserStack account](https://www.browserstack.com/)
  - Set your `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` as environment variables or replace them in the script.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/browserstack-playwright-automation.git
    cd browserstack-playwright-automation
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    `requirements.txt` should contain:
    ```txt
    playwright
    pytest
    ```

3. Install Playwright dependencies:

    ```bash
    playwright install
    ```

4. Set your BrowserStack credentials:
   - Either set the following environment variables:
     ```bash
     export BROWSERSTACK_USERNAME=your_browserstack_username
     export BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key
     ```
   - Or replace the placeholders in the script with your actual BrowserStack credentials.

## Running the Tests

Once everything is set up, you can run the tests with pytest:

```bash
pytest test_script.py
