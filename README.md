# 🥔 PotatoPeeler 🍟
### Measures your BWAPI bot against a gauntlet of opponents.
### Gets your potato in shape!

![Example screenshot of win-loss records against each opponent and on each map](https://github.com/dgant/PotatoPeeler/blob/main/exampleresults.png)

*Results from PotatoPeeler running hundreds of games, showing your bot's win-loss-incomplete records against each opponent and on each map*

## Purpose
When developing a bot to compete at StarCraft: Brood War using [BWAPI](https://github.com/bwapi/bwapi), you may want to measure your bot's performance against salient opponents. PotatoPeeler is a set of simple scripts to run lots of games via [SC-Docker](https://github.com/basil-ladder/sc-docker) and measure how your bot is doing.

PotatoPeeler can also analyze results from SC-Docker games you've run manually via `scbw.play`; there's no difference between games queued by PotatoPeeler and those

PotatoPeeler is deliberately simple. There are no plans for additional features.

## Using PotatoPeeler

### `potato-run`
Runs games of your bot against a gauntlet of your opponents.

The script specifies which bot to test (yours), which opponents to play against, and which maps to use. Modify the script directly to customize your run.

`potato-run` runs games indefinitely. Press Ctrl+C to halt the run.

Results from `potato-run` games go in the default scbw "games" directory. If you want to start start a fresh test run, delete or move the games in that directory.

Three considerations when using `potato-run`:
1. `potato-run` adds more 
1. `potato-run` kills all running Docker containers on start by running `dockerstop.sh`. If you're using Docker for other purposes, you should remove this step.
2. Ending potato-run doesn't always succeed at ending all the processes it spawns. If this happens, you'll need those processes.

### `potato-status`
Displays results of the most recent potato-run. Collects replays and logs of games your bot lost.

`potato-status` prints results directly to the console (see example above). It copies replays and logs of losses to a "losses" directory inside your SC-Docker directory.

![Example screenshot screenshot of Windows Explorer showing aggregated replays and log files](https://github.com/dgant/PotatoPeeler/blob/main/examplelosses.png)

The files are named with each game's timestamp, so if you sort the "losses" directory by name it'll also be sorted by game, in chronological order.

You can run potato-status while potato-run is still in progress.

## Setup
1. Install [SC-Docker](https://github.com/basil-ladder/sc-docker)
2. Install [Python 3](https://www.python.org/downloads/)

On Windows, you'll need access to Bash or an equivalent shell. Some good options for doing this:
1. (Recommended) Install [Git Bash](https://gitforwindows.org/). This is part of Git for Windows, so you likely already have this installed.
2. Install [https://www.cygwin.com/](https://www.cygwin.com/)
3. `git clone https://github.com/dgant/PotatoPeeler`