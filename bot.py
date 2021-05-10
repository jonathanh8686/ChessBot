from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import solve
import random

CHESS_URL = "https://www.chess.com/"

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get(CHESS_URL)

IN_GAME = False

while True:
    try:
        IN_GAME = ("puzzles/rated" in driver.current_url and len(driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[1]/span")) >= 1)

        if(IN_GAME):
            move_state = driver.find_elements_by_xpath("/html/body/div[3]/div/div/div[1]/span")[0]

            side = "w" if "White" in move_state.text else "b"

            try:
                board = driver.find_elements_by_xpath("/html/body/div[2]/div/chess-board")[0]
            except Exception as e:
                print("Found exception while trying to retrieve board element!\n" + str(e))
                continue

            piece_elements = board.find_elements_by_class_name("piece")
            piece_string = [piece.get_attribute("class") for piece in piece_elements]
            print(solve.get_fen(solve.process_pieces(piece_string), side))


    except KeyboardInterrupt:
        break

