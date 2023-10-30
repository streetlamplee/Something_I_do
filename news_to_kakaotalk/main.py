import sys
import time
import schedule
sys.path.append('./src/kakaopipeline')
from kakao_pipeline import Kakao



schedule.every().day.at('09:30').do(Kakao)

if __name__ == '__main__':
    Kakao()
    while True:
        schedule.run_pending()
        time.sleep(1)