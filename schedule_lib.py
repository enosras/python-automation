#Some cron high level version
import schedule
import time

def jon():
    print("Automation")
    
    
schedule.every().day.at("15:19").do(jon)

while True:
    schedule.run_pending()
    time.sleep(1)