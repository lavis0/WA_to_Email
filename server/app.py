"""Establish the event loop and shows the main window of the application."""

import argparse

def parse_args() -> str:
    """Parse command line arguments and run the application."""
    parser = argparse.ArgumentParser(
        description="Containerised server for the WA to email mock application."
    )
    parser.add_argument(
        'source_user_id', '-u', '--source_uid',
        metavar='SOURCE_USER_ID',
        required=True,
        help='Source user ID'
    )
    parser.add_argument(
        '-s', '--send',
        metavar=('TARGET', 'TYPE', 'MESSAGE'),
        nargs=3,
        help='Send a message: -s <target> <type> <message>'
    )
    parser.add_argument(
        '-r', '--receive',
        help='Print your received messages and mark them as read'
    )
    args = parser.parse_args()
    return args.select

# TODO: add match/case or if statements for logic flow
def run_app(args=parse_args()) -> int:
    """Run the functions from the server."""
