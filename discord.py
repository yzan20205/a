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

POINT_CHANNEL = 1497204458680090779
INTERACTION_PANEL_CHANNEL = 1497642199859593388
KEYWORD_CHANNEL = 1497911384191668254
PROMOTION_REQUEST_CHANNEL = 1497203612432990259
HACKED_PROTECTION_CHANNEL = 1514000444349878483

POINTS_ACTION_LOG_CHANNEL = 1516309944129818735
SPAM_LOG_CHANNEL = 1516295642824310824

POINT_ROLES = {
    1482194383515422752,
    1480443913557905499,
}

IMAGE_REVIEW_ROLES = {
    1477492633847857252,
}

ADMIN_ROLES = {
    1478970736717598840,
    1495873706923393205,
    1490386915629989948,
    1478971845729583276,
}

PROMOTION_REVIEW_ROLES = {
    1478971845729583276,
    1490386915629989948,
    1505984803839676466,
}

ADMIN_RANK_ORDER = [
    1485560413146841210,
    1485549583861022802,
    1480649204593332324,
    1485551861334540378,
    1518903745637908540,
    1518903845198237807,
    1488591572042780725,
    1518903808778960896,
    1518903917927338074,
    1480818082426392637,
    1480390711651336244,
    1480391201227280535,
]


# =========================
# SETTINGS
# =========================

TEXT_POINTS = 15
... (822 lines left)
