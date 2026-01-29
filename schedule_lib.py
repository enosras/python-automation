#Some cron high level version
import time

import schedule


def jon():
    print("Automation")
    print("We Need New Names")
    
    
schedule.every().day.at("15:19").do(jon)

while True:
    schedule.run_pending()
    time.sleep(1)



