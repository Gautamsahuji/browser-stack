
# BrowserStack Selenium Technical Assignment

## Overview
This project demonstrates **web scraping, API integration, text processing, and cross‑browser testing** using Python and Selenium.

The script automates scraping articles from the **El País Opinion section**, translates article titles into English, analyzes repeated words, and runs the same test across multiple browsers and devices using **BrowserStack parallel execution**.

---

## Features
- Web scraping using Selenium WebDriver
- Extracts the **first 5 articles** from El País Opinion section
- Prints **article title and content in Spanish**
- Downloads **cover images locally**
- Translates article titles into **English using Google Translate API**
- Performs **word frequency analysis**
- Executes tests across **multiple browsers and mobile devices**
- Runs tests in **parallel using Python threading**

---

## Technologies Used
- Python
- Selenium WebDriver
- BrowserStack Automate
- Google Translate API (googletrans)
- Requests library
- Regex and Counter for text analysis

---

## Test Execution Flow
1. Open El País Opinion page
2. Collect the first 5 article links
3. Extract:
   - Spanish article title
   - Article content
   - Cover image
4. Translate titles into English
5. Perform text analysis to identify repeated words
6. Execute the same test across multiple browsers using BrowserStack

---

## Cross Browser Testing
The script runs in parallel across:

- Chrome (Windows 10)
- Edge (Windows 11)
- Safari (macOS Monterey)
- iPhone 13
- Samsung Galaxy S22

This ensures **cross‑browser and cross‑device compatibility testing**.

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/browserstack-assignment.git

Install dependencies:

pip install selenium
pip install requests
pip install googletrans==4.0.0-rc1

---

## Run the Script

python main.py

---

## Output
The script will:
- Print article titles and content in Spanish
- Download cover images
- Display translated article titles
- Show repeated words appearing more than twice
- Execute tests across multiple browsers using BrowserStack

---

## Author
**Gautam Sahu**
