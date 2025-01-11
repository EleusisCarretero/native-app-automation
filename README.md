# native-app-automation
This repository contains a perosnal proyect to automate the native apps for Samsung Galaxy A33
# Native App Automation

This project aims to automate native applications on a Samsung Galaxy A33 device using **Python**, **Appium**, and **Pytest**.

## Applications Tested
- **Messages:** Sending and receiving SMS.
- **Camera:** Capturing photos and recording videos.
- **Calculator:** Performing basic and advanced operations.
- **Contacts:** Creating, editing, and deleting contacts.

---

## Project Structure
```
native-app-automation/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                 # CI/CD configuration with GitHub Actions
├── config/
│   └── config.yaml                # Appium capabilities and other configurations
├── pages/
│   ├── base_page.py               # Base class for Page Objects
│   └── ...                        # POM classes for each app
├── tests/
│   ├── calculator/
│   │   ├── test_basic_operations.py
│   │   └── ...
│   ├── camera/
│   ├── contacts/
│   ├── messages/
│   └── conftest.py                # Shared Pytest configuration
├── utils/
│   ├── driver.py                  # Appium driver management
│   ├── tools.py                   # Auxiliary functions
│   └── __init__.py
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
├── pytest.ini                     # Pytest configuration
└── ...
```

---

## Environment Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your_user/your_project.git
cd your_project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure `pytest.ini`
Ensure the `pytest.ini` file includes the following configuration so Pytest recognizes the paths:
```ini
[pytest]
pythonpath = .
```

### 6. Verify Appium Server
Ensure the Appium server is running:
```bash
appium
```
You can install Appium using `npm` if not already installed:
```bash
npm install -g appium
```

### 7. Verify Device Connection
Confirm that the device is properly connected:
```bash
adb devices
```

---

## Running Tests

### Run All Tests
```bash
pytest
```

### Run a Specific Test File
```bash
pytest tests/calculator/test_basic_operations.py
```

### Run a Specific Test
```bash
pytest tests/calculator/test_basic_operations.py::test_addition
```

### Generate an HTML Report
If `pytest-html` is installed, you can generate a report with:
```bash
pytest --html=report.html
```

---

## Troubleshooting

### Issue: "No module named 'utils'"
If Pytest does not recognize the project modules, follow these steps:
1. Ensure each relevant directory has an `__init__.py` file.
2. Run `pytest` from the project root:
   ```bash
   pytest tests/calculator/test_basic_operations.py
   ```
3. Ensure the `pytest.ini` file includes:
   ```ini
   [pytest]
   pythonpath = .
   ```
4. If needed, manually add the base directory to the `PYTHONPATH`:
   ```bash
   export PYTHONPATH=$(pwd)
   ```

---

## Dependencies
Dependencies are listed in the `requirements.txt` file and include:
```
pytest                  # Test execution
pytest-html             # HTML reports
pytest-xdist            # Parallel test execution (optional)
Appium-Python-Client    # Appium client
selenium                # Support for hybrid contexts
pyyaml                  # YAML configuration management
```

To install dependencies:
```bash
pip install -r requirements.txt
```

---

## Contributions
Any improvements or suggestions are welcome. Please create a "Pull Request" or open an "Issue" in the repository.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.

