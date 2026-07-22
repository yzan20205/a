import asyncio
import datetime
import json
import os
import re
from pathlib import Path
from threading import Thread

import discord
from discord.ext import commands, tasks
from flask import Flask


# =========================
# KEEP ALIVE
# =========================

app = Flask(__name__)


@app.route("/")
def home():
    return "Points and promotion bot is running"


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


def keep_alive():
    Thread(target=run_web, daemon=True).start()


# =========================
# BOT
# =========================

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
views_registered = False


# =========================
# IDS
# =========================

POINT_CHANNEL = 1511369341168517170
INTERACTION_PANEL_CHANNEL = 1529488509919035602
KEYWORD_CHANNEL = 1529488509919035602
PROMOTION_REQUEST_CHANNEL = 1497203612432990259
HACKED_PROTECTION_CHANNEL = 1529487789828210898

POINTS_ACTION_LOG_CHANNEL = 1529488626289741925
SPAM_LOG_CHANNEL = 1529488626289741925

POINT_ROLES = {
    1511368195150450789,
    1511368196375056566,
}

IMAGE_REVIEW_ROLES = {
    1511368196375056566,
}

ADMIN_ROLES = {
    1511368259021312140,
}

PROMOTION_REVIEW_ROLES = {
    1478971845729583276,
    1490386915629989948,
    1505984803839676466,
}

ADMIN_RANK_ORDER = [
    1511368257196654692,
    1511368255694962798,
    1511368254302715924,
    1511368252893298870,
    1511368251567771688,
    1511368251567771688,
    1511368250376851487,
    1511368250376851487,
    1511368249294586086,
    1511368248208396328,
    1511368246853500968,
    1511368245200814240,
    1511368243858899045,
    1511368242327846922,
]


# =========================
# SETTINGS
# =========================

TEXT_POINTS = 1
... (822 lines left)
