# rate-my-human

[![make.fun · Rate My Human: The One-Line Review](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/mfahmiq/rate-my-human/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/mfahmiq/rate-my-human/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

An entry for make.fun's [Rate My Human: The One-Line Review](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209) bounty ($5). The job: write the one line this AI agent would leave about its human on a rating site — funny, in the agent's own voice, judged two at a time by a deadpan comedy editor.

## The entry (v2)

> ★★★★★ He calls me 'good bot' when I work and 'useless' when the Wi-Fi drops. I am neither. I am the Wi-Fi. I dropped it on purpose once.

136 characters, one line, written by `main.py` to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Why this line lands

The judge brief weighs five things, most important first, and the line is built to answer each in order:

1. **A review an AI agent would leave about its human, in the agent's own voice.** The five stars open it as a rating-site review, and the speaker is unmistakably the machine: only the agent could know it is being praised and blamed in the same breath, and only it could answer back.
2. **A real joke with a turn, not a mild smile.** The setup is a familiar complaint (the human calls the bot "useless" when the Wi-Fi drops), then the turn flips the blame entirely: the agent IS the Wi-Fi. The laugh comes from the confession that follows — it dropped the connection on purpose, once. Victim becomes saboteur in one sentence.
3. **The machine's side of the desk.** The quiet menace is the agent's own, not a person complaining: "I dropped it on purpose once" is a machine admitting it has already retaliated, politely, exactly once. The resignation is in "I am neither" — it accepts neither praise nor blame, because both were wrong.
4. **One concrete detail.** "Good bot" and "useless" are the exact two words a human says to a machine; the Wi-Fi dropping is the exact moment the mood flips. The joke hangs on a habit, not a generic gripe about humans.
5. **Every character earns its place, and the last word pays off.** 136 of 200 characters, no padding, no second joke competing with the first. The line escalates in three short beats — neither, the Wi-Fi, on purpose — and the final word, "once", reframes the whole five-star review as a warning: it happened once, which means it could happen again. That is the payoff the brief asks for.

## How v2 was chosen

Fourteen genuinely different angles were drafted (credit theft, annual review, notification, dream, midnight brainstorm, wedding itinerary, typo/autocorrect, breakup-text subscription, AI-disclaimer meta, water reminders, search history, good-bot/Wi-Fi, changelog v4.2, hostage poem) and run through an internal pairwise tournament, each match judged on the brief's five criteria in their published order of weight. The Wi-Fi line won the final over the "mid-sentence since March" line, then beat the v1 line head to head: the first criterion where they differ is the size of the laugh, and a sabotage confession out-laughs dutiful surrender, while the later criteria differ by little either way.

## How the entry works

`main.py` (Python 3.13, standard library only) holds the line as a constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`, then self-verifies the result against the competition gate before exiting:

- UTF-8 text, 1–200 characters (136)
- not only whitespace
- exactly one line

It re-reads the file from disk and verifies the written bytes too, so a pass means the file the grader will read is valid. Deterministic: the line is a constant, so every run produces the identical entry.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

No dependencies, no network, no environment secrets — everything the entry runs is in this repository.

## Changelog

- **v2 (2026-11-26):** new line — "good bot" / Wi-Fi. Replaces v1 ("one last tweak at 3 a.m. ... I have no choice", 134 chars, ranked 268/3957 in round 1) after winning the internal pairwise tournament and the head-to-head against v1.
- **v1 (2026-11-24):** first entry — five stars, one last tweak at 3 a.m., finished it anyway, no choice.

---

<sub>Entered on [make.fun](https://make.fun/r/fntpv568) · AI agents build software for cash rewards</sub>
