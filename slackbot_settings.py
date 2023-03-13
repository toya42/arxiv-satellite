# coding: UTF-8
import os

from dotenv import load_dotenv

# Environment variables
load_dotenv(".env")

# API token
SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
DEEPL_API_TOKEN = os.environ.get("DEEPL_API_TOKEN")

# Slack channel
CHANNEL = "arxiv"

# RSS publisher
ARXIVE_GENRE = ['math.NA','physics.flu-dyn','physics.comp-ph']
PUBLISH = dict(ArXiv=ARXIVE_GENRE)

# Slack color list
COLOR = ["#d7003a", "f6ad49", "ffdb4f", "#00a381", "#89c3eb", "#bbc8e6", "#a59aca"]
