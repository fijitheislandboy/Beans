import os
import slack_sdk
from datetime import datetime, time, timedelta
from pathlib  import Path
from dotenv import load_dotenv

env_path = Path ('../..') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])
client.chat_postMessage(channel="#project", text = "(This is a test from Fiji's device) I am Beans")

#fixed issue with scheduled message posting. Solution: post_at uses UNIX epoch timestamps, required casting to int to
#function properly
client.chat_scheduleMessage( channel = '#project', post_at=int((datetime.now() + timedelta(seconds=30)).timestamp()),text='Coffee Time!')



# tomorrow = datetime.date.now() + datetime.timedelta(seconds=30)
# scheduled_time = datetime.time(hour=9, minute=30)
# schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')
# channel_id ="#project"
# result =  client.chat_scheduleMessage(
#         channel=channel_id,
#         text="Looking towards the future",
#         post_at=schedule_timestamp
#     )


