__all__ = ["issues", "command"]

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--command", help="The command we wish to perform")
parser.add_argument("--issue", help="The issue number we operate on", action="append")
parser.add_argument("--issues", help="The issue numbers we operate on", action="append")
parser.add_argument("--comment", help="If we can add a comment this is the text for it")
parser.add_argument("--fields", help="The fields to include in the operation - empty is all or relevant depending on command", action="append")


args = parser.parse_args()