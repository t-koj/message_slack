import sys
import os
import asyncio
from slack_sdk import WebClient
from slack_sdk.web import SlackResponse
from simple_parsing import parse_known_args, field
from dataclasses import dataclass

@dataclass
class Arguments:
    message: str = field(positional=True)

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

def _print_usage():
    print("Usage: python main.py <message>")

async def _main(args: Arguments):
    message = args.message
    if not message:
        _print_usage()
        sys.exit(1)
    response = await post_message(message)
    if response["ok"]:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response['error']}")

if __name__ == "__main__":
    args = parse_known_args(Arguments)
    asyncio.run(_main(args))
