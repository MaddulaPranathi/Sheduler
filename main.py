import schedule
import time
from plyer import notification
from chatbot import parse_input
from db import init_db,add_reminder
init_db()
def remind(task):
    print(f"⏰ Reminder triggered: {task}")
    notification.notify(
        title="Reminder",
        message=task,
        timeout=10
    )
print("Chatbot Scheduler Ready...! Type your Reminder :")
while True:
    user_input=input("YOU: ")
    task,time_str=parse_input(user_input)
    if task and time_str:
        add_reminder(task,time_str)
        schedule.every().day.at(time_str).do(remind, task)
        print(f"BOT: Reminder saved for '{task} at {time_str}")
    else:
        print("BOT: Sorry,I didnot understand. Try: Remind me to <task> at HH:MM")
    schedule.run_pending()
    time.sleep(1)