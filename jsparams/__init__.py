__all__ = ["issues", "command"]

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--command", help="The command we wish to perform")
parser.add_argument("--issue", help="The issue number we operate on", action="append")
parser.add_argument("--issues", help="The issue numbers we operate on", action="append")
parser.add_argument("--comment", help="If we can add a comment this is the text for it")


args = parser.parse_args()