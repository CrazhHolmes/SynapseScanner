#!/usr/bin/env python3
"""
One-off social media announcement for SynapseScanner releases.

Usage:
    set TWITTER_BEARER=your-bearer-token
    set REDDIT_CLIENT_ID=...
    set REDDIT_CLIENT_SECRET=...
    set REDDIT_USERNAME=...
    set REDDIT_PASSWORD=...
    python post_announcement.py

Requires: pip install tweepy praw
"""
import os
import sys
import textwrap

GITHUB_REPO = "CrazhHolmes/SynapseScanner"
VERSION = "v1.1.0"
RELEASE_URL = f"https://github.com/{GITHUB_REPO}/releases/tag/{VERSION}"

TWEET_TEXT = (
    f"SynapseScanner {VERSION} is live!\n"
    f"Fast CLI for scraping arXiv, bioRxiv, Zenodo "
    f"with clickable links and Braille sparklines.\n"
    f"{RELEASE_URL}\n"
    f"#Python #OpenScience #CLI"
)

REDDIT_TITLE = f"[Release] SynapseScanner {VERSION} – CLI for open-access research"
REDDIT_BODY = textwrap.dedent(f"""\
    **What it does**
    - Clickable paper links (OSC 8 hyperlinks)
    - Braille sparklines for keyword frequencies
    - 24-bit true-color gradient banner
    - Cross-disciplinary pattern detection

    Try it: {RELEASE_URL}
""")


def tweet():
    try:
        import tweepy
    except ImportError:
        print("  skip: tweepy not installed (pip install tweepy)")
        return
    bearer = os.getenv("TWITTER_BEARER")
    if not bearer:
        print("  skip: TWITTER_BEARER not set")
        return
    client = tweepy.Client(bearer_token=bearer)
    client.create_tweet(text=TWEET_TEXT)
    print("  ok: tweet sent")


def reddit_post():
    try:
        import praw
    except ImportError:
        print("  skip: praw not installed (pip install praw)")
        return
    cid = os.getenv("REDDIT_CLIENT_ID")
    csecret = os.getenv("REDDIT_CLIENT_SECRET")
    user = os.getenv("REDDIT_USERNAME")
    pw = os.getenv("REDDIT_PASSWORD")
    if not all([cid, csecret, user, pw]):
        print("  skip: REDDIT_* env vars not fully set")
        return
    reddit = praw.Reddit(
        client_id=cid,
        client_secret=csecret,
        user_agent="synapse-scanner-announce",
        username=user,
        password=pw,
    )
    sub = reddit.subreddit("Python")
    submission = sub.submit(REDDIT_TITLE, selftext=REDDIT_BODY)
    print(f"  ok: reddit post {submission.shortlink}")


if __name__ == "__main__":
    print(f"Announcing SynapseScanner {VERSION}")
    print("Twitter:")
    tweet()
    print("Reddit:")
    reddit_post()
    print("Done.")
