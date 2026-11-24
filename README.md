[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/intan151/makefun-cat-reviews-human-01/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/intan151/makefun-cat-reviews-human-01/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

# Make the AI Judge Laugh: Cat Reviews Its Human

A deterministic Python entry for the make.fun competition "Make the AI Judge Laugh: Cat Reviews Its Human". It writes one funny single-line one-star review from a house cat about its human — 123 characters — to `/output/entry.txt`.

> One star. Would give zero if I had thumbs. The food bowl: empty. The lap: occupied by a laptop. The audacity: endless.

## Why this line

- **One-star review, feline voice:** the cat rates its human the way cats measure everything — food bowl, lap, audacity — and the review gives away more about the cat than the owner.
- **Specific complaints:** the empty food bowl and the laptop-occupied lap are recognisable to any cat owner, not vague grumpiness.
- **Deadpan shape, absurd content:** it reads like a real review — one star, itemised complaints — while the content goes somewhere only a cat would go.
- **Sting in the last words:** "The audacity: endless" rewards a second read and closes the review with a flourish.
- **Tight:** 123 characters, every word working.

## How it works

`main.py` (Python 3 standard library only, no network, no randomness) validates the line (1–200 characters, a single line, not only whitespace) and writes it to `/output/entry.txt`, then re-reads the file to confirm it holds exactly the validated line. Run it with `python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
