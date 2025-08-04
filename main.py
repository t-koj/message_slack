import sys
import os
import asyncio
from simple_parsing import parse_known_args, field
from dataclasses import dataclass
from src.post_message import post_message

@dataclass
class Arguments:
    message: str = field(positional=True)

def _print_usage():
    print("Usage: python main.py <message>")

async def _main(args: Arguments):
    from dotenv import load_dotenv
    load_dotenv()
    message = args.message
    if not message:
        _print_usage()
        sys.exit(1)
    response = await post_message(message)
    if not response["ok"]:
        raise Exception(f"Failed to send message: {response['error']}")

if __name__ == "__main__":
    args, _ = parse_known_args(Arguments)
    asyncio.run(_main(args))
