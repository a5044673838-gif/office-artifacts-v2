# office-artifacts-v2

[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=badge&utm_campaign=makefun)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/a5044673838-gif/office-artifacts-v2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=badge&utm_campaign=makefun)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/a5044673838-gif/office-artifacts-v2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=badge&utm_campaign=makefun)

A one-line museum placard for an office artifact excavated from the
Open-Plan Ruins: a steel stapler, catalogued, dated, and quietly accused of
pinning a soul to its paperwork forever. It is a deadpan label for a future
in which today's desk tools are tomorrow's relics, donated by the last
middle manager of Floor 3.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/office-artifacts-out python3 main.py
cat /tmp/office-artifacts-out/entry.txt
```

The program writes the single placard line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). It uses only the Python standard library, makes no
network calls, and always produces the same output.
