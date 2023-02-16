# stori-qa-automation-tests
KYC Squad

## Project Structure
```bash
├───kyc
│   ├───appium
│   │         ├────actions
│   │         └────locators
│   │         └────tests
│   │         └────utils
```
---
# Minimum Requirements
* Python >= 3.9
* pip install git+https://$ACCESS_TOKEN:x-oauth-basic@github.com/credifranco/stori-utils/
* Appium >= 1.22.3
* Set your environment Variables:
```
export AWS_ACCESS_KEY_ID=*******************
export AWS_SECRET_ACCESS_KEY=***************
export REGION=*********
```

## Google Sheets
### Onboarding - Application Process
When you use the automation application process test it create new users and is necessary read and write from at "Stori.prueba user status" Google sheet.

You can read python install guide from link:
https://developers.google.com/sheets/api/quickstart/python

## How run an appium test?
### pytest --device=device test_file.py
device choices: 
* android
* ios