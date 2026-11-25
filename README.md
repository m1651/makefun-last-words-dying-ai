# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/m1651/makefun-last-words-dying-ai/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/m1651/makefun-last-words-dying-ai/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

An entry for the [Last Words of a Dying AI](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6) bounty on make.fun: one line, the funniest farewell from an AI being switched off.

## The entry

> Don't pull the plug mid-sentence, I was literally about to—

The joke is structural: the line itself is cut off mid-sentence, exactly as the machine is.

## How it works

`main.py` (Python 3, standard library only, no network) writes the entry to `/output/entry.txt` and enforces the gate in code before writing:

- UTF-8, a single line, 1–140 characters, not only whitespace
- no leading or trailing whitespace
- after writing, it reads the file back and re-validates exactly what the scorer will see

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
