Below is a draft Test Documentation that outlines our Test-Driven Development (TDD) approach for the Automated Pinterest Money Flow project. Please review and let me know if you'd like any modifications.

---

# Test Documentation for Automated Pinterest Money Flow

## 1. Overview

This document outlines the testing strategy and process for the Automated Pinterest Money Flow project. We will follow Test-Driven Development (TDD) to ensure that every module, microservice, and integration point is covered by tests before and during development.

---

## 2. Objectives

- **Ensure Quality:**  
  Validate that each functional module (scraping, posting, scheduling, data extraction, etc.) performs as expected.
  
- **Facilitate Refactoring:**  
  With robust tests in place, code changes and refactoring can be conducted with confidence.

- **Verify Integration:**  
  Confirm that independent microservices and backend-frontend interfaces integrate smoothly.

- **Automate Regression Testing:**  
  Provide a test suite that can be run automatically to catch regressions early.

---

## 3. Test Strategy

### 3.1 Test Types

- **Unit Tests:**  
  Cover individual modules (e.g., `AmazonResearcher`, `AmazonScraper`, `DataExtractor`, etc.).  
  *Tools:* Python’s built-in `unittest` framework (or alternatives like pytest).

- **Integration Tests:**  
  Verify the interactions between components (e.g., data flow from scraping to database, and from pin generation to posting).

- **End-to-End Tests (E2E):**  
  Simulate real user scenarios (e.g., triggering a full product research, generating pins, scheduling posts, and ensuring successful posting).  
  *Tools:* Tools such as Selenium for UI testing can be added later when the dashboard is implemented.

- **API Tests:**  
  Validate the backend RESTful API endpoints exposed for the React frontend.  
  *Tools:* Postman/Newman or pytest with HTTP libraries (e.g., requests).

### 3.2 Test Driven Development (TDD) Process

1. **Write a Failing Test:**  
   Before writing any new functionality, write a test that expresses the expected behavior of the module or feature.

2. **Implement Minimal Code:**  
   Write the minimal amount of code needed to pass the test.

3. **Refactor:**  
   Refactor the code while ensuring that all tests continue to pass.

4. **Repeat:**  
   Continue this cycle for every new feature or module.

---

## 4. Test Environment

- **Local Development:**  
  Tests will be executed locally within a Python virtual environment.
  
- **Continuous Integration:**  
  We plan to integrate tests with a CI tool (e.g., GitHub Actions) to automatically run tests on each commit and pull request.

- **Test Database:**  
  For database integration tests, a dedicated PostgreSQL test database will be used (which can be configured via environment variables).

- **Mocking & Stubbing:**  
  External calls (such as network requests to Amazon, Pinterest API calls, etc.) will be mocked to ensure tests are deterministic and do not rely on external services.

---

## 5. Test Coverage Areas

### 5.1 Scraping Service (AmazonResearcher & AmazonScraper)
- **Unit Tests:**  
  - Validate that the scraping logic correctly fetches the HTML content from the Amazon Best Sellers page.
  - Verify that the parser correctly extracts the expected product details.
- **Integration Tests:**  
  - Simulate a full scraping cycle, storing results in a test database or temporary CSV files.

### 5.2 Data Extraction & Storage (DataExtractor, DataStorage)
- **Unit Tests:**  
  - Ensure that product details (name, image URL, description, summary video, affiliate link) are parsed correctly.
  - Validate that placeholder fields (price, reviews, ratings) are initialized properly.
- **Integration Tests:**  
  - Verify that data is written to and read from PostgreSQL correctly.
  - Test data export functionality (e.g., exporting to CSV or JSON).

### 5.3 Pin Generation & Posting (PinterestPinGenerator, PinterestPoster)
- **Unit Tests:**  
  - Validate that the existing pin generation code produces the correct output given a set of inputs.
  - Test posting functions with mocked API calls to Pinterest.
- **Integration Tests:**  
  - Simulate the complete workflow from pin generation to posting, including error handling and retry mechanisms.

### 5.4 Scheduling (APScheduler Integration)
- **Unit Tests:**  
  - Ensure that jobs are scheduled at the correct times.
  - Validate that manual start/stop commands work as expected.
- **Integration Tests:**  
  - Test end-to-end job scheduling and execution cycles (e.g., trigger a scraping job, then a posting job).

### 5.5 Backend API for Dashboard
- **Unit Tests:**  
  - Validate individual API endpoints (authentication, data retrieval, job triggering).
- **Integration Tests:**  
  - Simulate interactions between the React frontend and backend APIs.
  - Ensure RBAC (role-based access control) mechanisms are enforced.

---

## 6. Test Cases Examples

### Example Test Case: AmazonResearcher

- **Test Name:** test_trending_product_research_returns_non_empty_list  
- **Description:** Verify that running the research process returns a non-empty list of trending products.  
- **Preconditions:** Amazon Best Sellers page is accessible (or the network call is mocked).  
- **Test Steps:**
  1. Instantiate the AmazonResearcher module with a test project folder.
  2. Trigger the `execute()` method.
  3. Assert that the returned list has a length greater than 0.
- **Expected Result:** A non-empty list containing dictionaries with product details.

### Example Test Case: Database Write/Read

- **Test Name:** test_write_and_read_csv  
- **Description:** Validate that data written to CSV is correctly read back.  
- **Preconditions:** A temporary test CSV file location.
- **Test Steps:**
  1. Use the BaseAgent’s `write_to_csv` method to write a sample data dictionary.
  2. Read the CSV file using the `open_csv` method.
  3. Assert that the read data matches the written data.
- **Expected Result:** The read data matches exactly with the sample data.

### Example Test Case: PinterestPoster Error Handling

- **Test Name:** test_posting_error_notifies_user  
- **Description:** Ensure that if posting fails, an appropriate error message is logged and returned.  
- **Preconditions:** The posting API call is mocked to simulate a failure.
- **Test Steps:**
  1. Instantiate the PinterestPoster module with test credentials.
  2. Simulate a posting attempt that raises an exception.
  3. Verify that the error is caught, logged, and that a clear error message is returned.
- **Expected Result:** The user sees an error message in plain English explaining the issue.

---

## 7. Tools and Frameworks

- **Python Unit Testing:**  
  - Use `unittest` or `pytest` for writing tests.
- **Mocking:**  
  - Use `unittest.mock` or `pytest-mock` to mock external services and network calls.
- **CI Integration:**  
  - GitHub Actions (or an equivalent CI/CD tool) for running tests on every commit.
- **Coverage Tools:**  
  - Tools like `coverage.py` to monitor test coverage and ensure critical areas are tested.

---

## 8. Running the Tests

- **Local Execution:**  
  From the command line, run:
  ```bash
  python -m unittest discover tests
  ```
  or if using pytest:
  ```bash
  pytest --maxfail=1 --disable-warnings -q
  ```

- **CI/CD Pipeline:**  
  Configure the CI tool (e.g., GitHub Actions) to run the above command as part of the build process.

---

## 9. Maintenance and Future Enhancements

- **Test Updates:**  
  As new features are added or changes occur, tests will be updated to cover new cases.
- **Regression Testing:**  
  Periodically run the full test suite to catch regressions during refactoring.
- **Documentation:**  
  Maintain a living document that includes instructions for writing new tests and updating existing ones as the system evolves.

