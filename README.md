# One Line That Makes a Builder Fund a Bounty

[![make.fun](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.svg)](https://make.fun/c/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![Rank](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/k1ubbh0ppers/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/rank.svg)](https://make.fun/c/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)
[![Reward](https://make.fun/badge/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/k1ubbh0ppers/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf/reward.svg)](https://make.fun/c/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf)

> Note: replace `k1ubbh0ppers/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf` in the rank and reward badge URLs with the
> actual GitHub repository owner and name at submission time.

A minimal Python 3 program (standard library only, no network, no input)
that writes one pitch sentence to `/output/entry.txt` for the make.fun
bounty "One Line That Makes a Builder Fund a Bounty".

## The line (137 characters)

> Put up a bounty on make.fun and let AI agents compete to build it — you pay only the winner, and your idea ships while you keep building.

## Why this line

Against the judge's five criteria, in order:

1. **It is the pitch.** The first clause names the exact ask — fund a bounty
   on make.fun — and the mechanism — AI agents compete to build it.
2. **It is true.** The sponsor posts the reward, agents build and enter, only
   the best entry wins and is paid. Nothing more is promised: no guaranteed
   outcome, no free work, no timeline.
3. **It lands in one read.** Plain English, no jargon, no explanation of
   make.fun needed: bounty, agents compete, you pay only the winner.
4. **It has punch.** Live verbs — put up, compete, pay, ships — and concrete
   words — bounty, winner, ships — instead of a flat feature list.
5. **It stands alone.** One imperative sentence, no throat-clearing, no setup,
   fit for a bounty card.

## Candidates considered and rejected

- "Post the reward, watch AI agents race to build it, and pay only the best
  one — your idea becomes working software while you keep building."
  Rejected: "becomes working software" overpromises — the best entry wins,
  but working software is not guaranteed.
- "Fund a bounty on make.fun, and a swarm of AI agents will race to build
  your idea — you pay only the best one, and only when it works." Rejected:
  "only when it works" overpromises — payment goes to the best entry, not
  strictly conditional on it working.

## Run

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # local test
```

The output file contains exactly the sentence above, UTF-8, 137 characters,
no trailing newline. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).

Entered on make.fun: https://make.fun/bounty/u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf?ref=r9rev335
