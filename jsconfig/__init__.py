__all__ = ["configuration"]

import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.read(Path.home() / '.jira-stats' / 'jira-stats.ini')

