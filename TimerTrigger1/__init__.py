import datetime
import logging
import requests
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    res = requests.get("https://momagiclight.azurewebsites.net/hello")
    print(res.status_code)
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Test: Python timer trigger function ran at %s',
                 utc_timestamp)
