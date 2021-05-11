from telegram import Update
from telegram.ext import CallbackContext
from bot import fact_class as fact
import datetime


def send_notifications(ctx: CallbackContext) -> None:
    """This function creating example of class
    which request information from repository.
    I used repository with some facts about cats for example"""
    job = ctx.job
    send_text = fact.Fact().some_fact
    ctx.bot.send_message(job.context, text=f"Hello, my dear friend!\n"
                                           f"today is {datetime.datetime.now()}\n"
                                           f"Today some interesting fact about cats is:\n"
                                           f"{send_text}")


def enable(upd: Update, ctx: CallbackContext) -> None:
    """Add a job to the queue. In this bot this function
    enabling notifications"""
    chat_id = upd.message.chat_id
    remove_job_if_exists(str(chat_id), ctx)
    ctx.job_queue.run_repeating(send_notifications, 5, context=chat_id, name=str(chat_id))


def disable(upd: Update, ctx: CallbackContext) -> None:
    """ Remove job from queue. In this bot this function
    disabling notifications"""
    chat_id = upd.message.chat_id
    remove_job_if_exists(str(chat_id), ctx)


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    """Remove job with given name. Returns whether job was removed."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True







