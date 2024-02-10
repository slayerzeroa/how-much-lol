import requests
from bs4 import BeautifulSoup
import requests
import time

from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By

import numpy as np

import lol_api as lol
import time


def get_game_count (driver):
    table = driver.find_elements(By.CLASS_NAME, "winratio-graph")
    count = 0
    for i in table:
        split_list = (i.text.split("\n"))
        for j in split_list:
            count+=int(j[:-1])
    return count

def total_game_count(driver):
    game_count = 0

    driver.find_element(By.XPATH, '//*[@id="content-container"]/div/div/div[1]/div[2]/div/button').click()

    season_list = driver.find_elements(By.CLASS_NAME, "season-list")

    for i in range(len(season_list[0].text.split("\n"))):
        driver.find_element(By.XPATH, f'//*[@id="content-container"]/div/div/div[1]/div[2]/div/div/button[{i+1}]').click()
        game_count += get_game_count(driver)
        driver.implicitly_wait(0.5)
        driver.find_element(By.XPATH, '//*[@id="content-container"]/div/div/div[1]/div[2]/div/button').click()
    return game_count