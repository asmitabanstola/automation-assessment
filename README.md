# Test Automation Assignment

## Objective

Automate UI tests on [Daraz Nepal](https://daraz.com.np) and API tests on [Restful Booker](https://restful-booker.herokuapp.com).

## Project Structure

```
api-testing/
  ├─ API test.postman_collection.json
  ├─ API Test.postman_environment.json
  └─ API test.postman_result.json
chromedriver/        ← Place ChromeDriver binary here
ui-automation/
  ├─ login_test.py
  ├─ add_to_cart_test.py
  ├─ delete_items_test.py
  └─ edit_address_test.py
  └─ Pages/          ← Page object modules
```

## UI Test (Selenium)

1. Ensure Python 3.8+ and ChromeDriver are installed.
2. Install Selenium:
   ```bash
   pip install selenium
   ```
3. Export user credentials:
   ```bash
   export USERNAME="your_email@example.com"
   export PASSWORD="your_password"
   ```
4. Run each test script:
   ```bash
   python3 ui-automation/login_test.py
   python3 ui-automation/add_to_cart_test.py
   python3 ui-automation/delete_items_test.py
   python3 ui-automation/edit_address_test.py
   ```

## API Test (Postman)

1. Import `api-testing/API test.postman_collection.json` into Postman.
2. Run the collection using the Postman Runner.

---

*Tests are configured for public demo sites; CI integration and coverage reports are not included.*

