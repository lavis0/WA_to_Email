"""Main entry point for the country picker application."""

import sys
from server.messaging_module.src.messaging_module.app import run_app

if __name__ == "__main__":
    sys.exit(run_app())