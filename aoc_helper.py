import requests
from pathlib import Path
import datetime
import json

class aoc_helper():
    def __init__(self) -> None:
        self.ROOT_DIR = Path(__file__).parent # ROOT_DIR is the advent-of-code-2022 folder
        self.TODAY = datetime.date.today()
        self.get_input()
        self.create_new_py()
        
    def get_session_cookie(self):
        try:
            data = json.load(open(self.ROOT_DIR / 'config.json', 'r'))
            return data['session_cookie']
        except:
            print(f"reading config.json failed!")
            raise
        
    def get_input(self):
        text_file_path = self.ROOT_DIR / f"input/{self.TODAY.day:02}.txt"
        if not text_file_path.is_file():
            URL = f"https://adventofcode.com/{self.TODAY.year}/day/{self.TODAY.day}/input"
            COOKIES = {'session': self.get_session_cookie()}
            PARAMS = {
                "User-Agent": 'https://github.com/danpfister/advent-of-code-2022',
            }
            try:
                request = requests.get(url=URL, cookies=COOKIES, params=PARAMS)
                text_file_path.write_text(request.text)
                print(f"downloaded input file to {text_file_path}")
                return
            except:
                print(f"aoc request failed!")
                raise
        print(f"input file for current day already exists")
    
    def create_new_py(self):
        py_file_path = self.ROOT_DIR / f"{self.TODAY.day:02}.py"
        if not py_file_path.is_file():
            py_file_path.open("w", encoding="utf-8")
            print(f"created python file at {py_file_path}")
            return
        print("python file for current day already exists")
        
if __name__ == "__main__":
    aoc_helper()