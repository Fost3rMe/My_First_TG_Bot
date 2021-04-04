import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import datetime
from threading import Thread
import time

userlist = []


# repeatable_func = Repeated_func(send_notifications)
# repeatable_func.run()
def send_notifications(ctx: CallbackContext) -> None:
    """Send the alarm message."""
    job = ctx.job
    send_fact = Fact()
    send_text = send_fact.some_fact
    ctx.bot.send_message(job.context, text=f"Hello, my dear friend!\n"
                                           f"today is {datetime.datetime.now()}\n"
                                           f"Today some interesting fact about cats is:\n"
                                           f"{send_text}")


def enable(u: Update, ctx: CallbackContext) -> None:
    """Add a job to the queue."""
    chat_id = u.message.chat_id
    remove_job_if_exists(str(chat_id), ctx)
    ctx.job_queue.run_repeating(send_notifications, 5, context=chat_id, name=str(chat_id))


def disable(u: Update, ctx: CallbackContext) -> None:
    chat_id = u.message.chat_id
    remove_job_if_exists(str(chat_id), ctx)


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

class Fact:

    def __init__(self, url='https://cat-fact.herokuapp.com/facts/random'):
        self.url = url

    @property
    def some_fact(self):
        fact_request = requests.get(self.url)
        fact = fact_request.json()['text']
        return fact

# class Repeated_func:
#
#     def __init__(self, func):
#         self.func = func
#         self.isCancel = False
#
#     def _run(self):
#         while not self.isCancel:
#             self.func()
#
#     def run(self):
#         self.isCancel = False
#         thread = Thread(target=Repeated_func._run, args={self})
#         thread.start()
#
#     def stop(self):
#         self.isCancel = True
