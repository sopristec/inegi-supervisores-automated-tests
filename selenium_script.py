import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import concurrent.futures
from multiprocessing import Pool, Process
from concurrent.futures import ProcessPoolExecutor, as_completed
import logging
import redis
import json

logging.basicConfig(level=logging.INFO)


def upload_file(file_data):
    """
    Uploads file to Opera
    """
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")  # Uncomment if you want to run headless
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--v=1")  # Increase verbosity

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)  # Global implicit wait

    # no_files = sys.argv[2]
    file_name = file_data["file_name"]
    username = file_data["username"]
    file_path = os.path.join(os.getcwd(), file_name)

    try:
        # Navigate to the login page
        driver.get(
            "https://opera.inegi.org.mx/opera.auth/Account/Login?ReturnUrl=%2Fopera.auth%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dopera.web%26redirect_uri%3Dhttps%253A%252F%252Fopera.inegi.org.mx%252Fopera.web%252Fauth-callback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520access%26state%3D1952c1d396484ab99e9a8eadeb0416f9%26code_challenge%3Dgzk_opek4y_hVo4ALnC12DG0nti8-oeSxt9Eb3aemh4%26code_challenge_method%3DS256%26response_mode%3Dquery"
        )

        # Wait until the username input field is present and type the username
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="UserName"]'))
        ).send_keys(username)

        # Type the password
        driver.find_element(By.XPATH, '//*[@id="Password"]').send_keys("Univers@l")

        # Click the submit button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Navigate to the next URL
        WebDriverWait(driver, 20).until(
            EC.url_contains("https://opera.inegi.org.mx/opera.web/auth-callback")
        )

        driver.get("https://opera.inegi.org.mx/opera.web/")

        # Interact with elements on the page
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//mat-dialog-container[@id='mat-dialog-0']/app-get-evento-modal/div/div/div/div/div[2]/small",
                )
            )
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(.//*[normalize-space(text()) and normalize-space(.)='Prueba de volumen de la EIC2025'])[1]/following::div[11]",
                )
            )
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@id='cdk-accordion-child-0']/div/mat-list/div[2]/mat-list-item/div/button/span",
                )
            )
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(.//*[normalize-space(text()) and normalize-space(.)='Paquetes integrados'])[1]/following::div[3]",
                    # "//*[contains(text(), 'Integrar paquete ...')]",
                )
            )
        ).click()

        # Upload file
        driver.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)

        print("uploaded")
        # Wait for 10 seconds for file to upload
        # time.sleep(60)
        # print("uploaded")

        # Click on the button
        WebDriverWait(driver, 200).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//mat-dialog-container[@id='mat-dialog-1']/app-dialog/div/div[2]/div/button/span",
                )
            )
        ).click()
        print("finish")

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(.//*[normalize-space(text()) and normalize-space(.)='Prueba de volumen de la EIC2025'])[1]/following::mat-icon[1]",
                )
            )
        ).click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(.//*[normalize-space(text()) and normalize-space(.)='SIM'])[1]/following::span[4]",
                )
            )
        ).click()

        # Navigate back to login page
        driver.get(
            "https://opera.inegi.org.mx/opera.auth/Account/Login?ReturnUrl=%2Fopera.auth%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dopera.web%26redirect_uri%3Dhttps%253A%252F%252Fopera.inegi.org.mx%252Fopera.web%252Fauth-callback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520access%26state%3Dbcdc84f40da34e8ebad5734fbb6cda69%26code_challenge%3DtZakpLcxAk7aVfrTOAMxOCsoKaRUhvsQo8tDSfaHb08%26code_challenge_method%3DS256%26response_mode%3Dquery"
        )

    finally:
        # Close the browser
        driver.quit()
