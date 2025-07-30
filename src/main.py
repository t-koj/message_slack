import sys
import os
from slack_sdk import WebClient
from slack_sdk.web import SlackResponse
from simple_parsing import parse_known_args, field
from dataclasses import dataclass

def send_message(message: str) -> SlackResponse:
    token = os.getenv("SLACKBOT_TOKEN")
    if not token:
        raise ValueError("Environment SLACKBOT_TOKEN is not set.")
    channel = os.getenv("SLACKBOT_CHANNEL")
    if not channel:
        raise ValueError("Environment SLACKBOT_CHANNEL is not set.")
    client = WebClient(token=token)
    return client.chat_postMessage(channel=channel, text=message)

def _print_usage():
    print("Usage: python main.py <message>")

@dataclass
class Options:
    message: str = field(positional=True)

if __name__ == "__main__":
    args = parse_known_args(Options)
    if len(sys.argv) <= 1:
        _print_usage()
    else:
        message = sys.argv[1]
        send_message(message)
    
