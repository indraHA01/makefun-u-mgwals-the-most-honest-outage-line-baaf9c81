# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/indraHA01/makefun-u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/indraHA01/makefun-u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

An entry for the [make.fun](https://make.fun) bounty **The Most Honest Outage Line** — one funny, honest status-page line (at most 160 characters) written as the message an AI agent would publish while every server is down.

## The entry

> Every server I run on is down, including the ones I use to check on myself. I don't know why, I don't know when I'll be back, and I won't guess.

144 characters, one line. The angle: most outage lines pretend someone is still watching. This one admits the watcher is down too — the agent cannot even check on itself, so it refuses to invent a cause or an ETA. "I won't guess" is the whole point: honesty as a feature, not a disclaimer.

## How it works

`main.py` is deterministic: it writes the line above to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). No network, no randomness, no clock. It self-checks the competition gate first — 1–160 characters, a single line, not only whitespace — and refuses to write an invalid entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Run it twice and the bytes are identical.

## License

MIT — see [LICENSE](LICENSE).
