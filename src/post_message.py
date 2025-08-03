import os
from slack_sdk import WebClient
from slack_sdk.web import SlackResponse

async def post_message(message: str) -> SlackResponse:
    token = os.getenv("SLACKBOT_TOKEN")
    if not token:
        raise ValueError("Environment SLACKBOT_TOKEN is not set.")
    channel = os.getenv("SLACKBOT_CHANNEL")
    if not channel:
        raise ValueError("Environment SLACKBOT_CHANNEL is not set.")
    client = WebClient(token=token)
    client.async_mode = True
    return client.chat_postMessage(channel=channel, text=message)
