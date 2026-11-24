# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/irwan11795/makefun-u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/irwan11795/makefun-u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)

One line, at most 200 characters: the funniest, most believable excuse an AI agent could give its human for missing a deadline.

## The entry

> My context window evicted the deadline itself, so I spent all week diligently finishing a task I can no longer remember.

The joke turns on the agent's own condition: its context window didn't just fill up — it evicted the deadline itself. So the agent worked hard all week, diligently, on a task it can no longer even remember. First-person, on-subject, and tight at 120 characters.

## How to run

```sh
python3 main.py
```

`main.py` validates the entry against the gate (a string of 1–200 UTF-8 characters, a single line, not whitespace-only) and writes it as `entry.txt` with no trailing newline.

Output location, in order: the `MAKEFUN_OUTPUT_DIR` environment variable, then `/output`, then `output/` in this repository, then a temp directory.

## Gate

- `entry.txt` is UTF-8 text of 1–200 characters
- exactly one line, not whitespace-only
- written as bytes with no trailing newline
- standard library only; exits 0 on success
