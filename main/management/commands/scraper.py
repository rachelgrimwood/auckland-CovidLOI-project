import time
from get_list import pop_item, get_list, my_url, MOH_url
import logging
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

logger = logging.getLogger(__name__)


def my_job():
    current_response = get_list(my_url, "</tr>", "</table>")
    new_response = get_list(MOH_url, "<tbody>", "</tbody>")      
    for i in new_response:
      if "Auckland" in i[1]:
        if i not in current_response: 
          i.insert(0, 1)
          i.append(int(time.time()))
          i = tuple(i)
          pop_item(i)


# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after job has run.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
  """
  This job deletes APScheduler job execution entries older than `max_age` from the database.
  It helps to prevent the database from filling up with old historical records that are no
  longer useful.
  
  :param max_age: The maximum length of time to retain historical job execution records.
                  Defaults to 7 days.
  """
  DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
  help = "Runs APScheduler."

  def handle(self, *args, **options):
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
            my_job,
            trigger=CronTrigger(minute="*/10"),
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
    logger.info("Added job 'my_job'.")    


    try:
            logger.info("Starting scheduler...")
            scheduler.start()
    except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")