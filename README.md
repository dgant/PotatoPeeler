# PotatoPeeler
## Measure your BWAPI bot against a gauntlet of opponents

![Example screenshot of win-loss records against each opponent and on each map](https://github.com/dgant/PotatoPeeler/blob/master/exampleresults.png)

### Mission
When developing a bot to compete at StarCraft: Brood War using [BWAPI](https://github.com/bwapi/bwapi), you may want to measure your bot's performance against salient opponents. PotatoPeeler is a set of simple scripts to run lots of games via [SC-Docker](https://github.com/basil-ladder/sc-docker) and measure how your bot is doing.

PotatoPeeler is deliberately simple. There are no plans for additional features.

### Using PotatoPeeler

#### `potato-run`
Runs games of your bot against a gauntlet of your opponents.

The script specifies which bot to test (yours), which opponents to play against, and which maps to use. Modify the script directly to customize your run.

`potato-run` runs games indefinitely. Press Ctrl+C to halt the run.

Two things to be careful about:
1. `potato-run` kills all running Docker containers on start by running `dockerstop.sh`. If you're using Docker for other purposes, you should remove this step.
2. Ending potato-run doesn't always succeed at ending all the processes it spawns. If this happens, you'll need those processes.

#### `potato-status`
Displays results of the most recent potato-run. Collects replays and logs of games your bot lost.

Results are printed directly to console (see example above). Replays and logs of losses are copied to a "losses" directory inside your SC-Docker directory.

![Example screenshot screenshot of Windows Explorer showing aggregated replays and log files](https://github.com/dgant/PotatoPeeler/blob/master/examplelosses.png)

You can run potato-status while potato-run is still in progress.

### Setup
1. Install [SC-Docker](https://github.com/basil-ladder/sc-docker)
2. Install [Python 3](https://www.python.org/downloads/)

On Windows, you'll need access to Bash or an equivalent shell. Some good options for doing this:
1. (Recommended) Install [Git Bash](https://gitforwindows.org/). This is part of Git for Windows, so you likely already have this installed.
2. Install [https://www.cygwin.com/](https://www.cygwin.com/)