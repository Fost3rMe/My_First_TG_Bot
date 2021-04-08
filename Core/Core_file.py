from telegram import Update   # TODO: поместить в файл requirements.txt
from telegram.ext import CallbackContext
import requests  # TODO: поместить в файл requirements.txt
import datetime


# TODO: Исправить определение функций! Аналогично файлу c Bot.py
# TODO: Уведомления же могут быть не только в виде фактов!
#  Можно сделать различный классы для разных уведомлений и
#  поместить их в отдельную папку как пакет python
def send_notifications(ctx: CallbackContext) -> None:
    """This function creating example of class
    which request information from repository.
    I used repository with some facts about cats for example"""
    job = ctx.job
    send_fact = Fact()
    send_text = send_fact.some_fact
    ctx.bot.send_message(job.context, text=f"Hello, my dear friend!\n"
                                           f"today is {datetime.datetime.now()}\n"
                                           f"Today some interesting fact about cats is:\n"
                                           f"{send_text}")


def enable(u: Update, ctx: CallbackContext) -> None:
    """Add a job to the queue. In this bot this function
    enabling notifications"""
    chat_id = u.message.chat_id
    remove_job_if_exists(str(chat_id), ctx)
    ctx.job_queue.run_repeating(send_notifications, 30, context=chat_id, name=str(chat_id))


def disable(u: Update, ctx: CallbackContext) -> None:
    """ Remove job from queue. In this bot this function
    disabling notifications"""
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


# TODO: Классы оформляют в отдельных модулях. Нужно перенести!
class Fact:
    """
    This class created for requesting information from repository,
    which https://cat-fact.herokuapp.com/facts/random by default
    """

    def __init__(self, url='https://cat-fact.herokuapp.com/facts/random'):
        self.url = url

    @property
    def some_fact(self):
        """
        Function making request and return JSON-format file with
        some information which was requested from repository
        :return: JSON-format file
        """
        fact_request = requests.get(self.url)
        fact = fact_request.json()['text']
        return fact
