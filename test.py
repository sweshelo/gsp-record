from gsprecorder import recorder
import datetime
import random

def main():

    jsonf = "key.json"
    spread_sheet_key = "1yMwPnF_PUVvI7VhRs2QtpwGjzwRtqyPkluemnp3FdpQ"

    recode = recorder(jsonf, spread_sheet_key)

    detect_face = bool(random.randint(0, 1))
    detect_eye  = bool(random.randint(0, 1))
    back_temp   = random.uniform(19, 29)
    face_temp   = random.uniform(25, 35)
    judge = True
    data = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), detect_face, detect_eye, back_temp, face_temp, face_temp - back_temp, judge]

    recode.add_row(data, recode.get_length())
    recode.update()

if __name__ == "__main__":
    main()

