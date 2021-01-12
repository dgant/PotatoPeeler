#!/bin/sh

PROC="${PROC:-0}"
PROCS="${PROCS:-1}"
SCBWDIR="${APPDATA}/scbw/"
MAPDIR="${APPDATA}/scbw/maps/sscai/"
BOT='PurpleWave'
OPPONENTS=(
'adias'           \
'Locutus'         \
'Proxy'           \
'tscmoor'         \
'KaonBot'         \
'GuiBot'          \
'ZurZurZur'       \
'legacy'          \
)
MAPS=(
'(4)Circuit Breaker.scx' \
'(2)Heartbreak Ridge.scx' \
'(3)Neo Moon Glaive.scx' \
'(3)Tau Cross.scx' \
'(4)Andromeda.scx' \
'(4)Fighting Spirit.scx' \
'(2)Benzene.scx' \
'(2)Destination.scx' \
'(4)Empire of the Sun.scm' \
'(4)Icarus.scx' \
'(4)Jade.scx' \
'(4)La Mancha1.1.scx' \
'(4)Python.scx' \
'(4)Roadrunner.scx'
)
cd "${SCBWDIR}"
function ecco() {
  echo "(PROC ${PROC}/${PROCS}): $1"
}
ecco "Playing against:"
for OPPONENT in "${OPPONENTS[@]}"
do
    ecco "$OPPONENT"
done
ecco ""
ecco "On maps:"
for MAP in "${MAPS[@]}"
do
    ecco "$MAP"
done
ecco ""
ecco "In process $PROC / $PROCS"
mkdir -p "${SCBWDIR}/games/"
sleep 1
while true
do
  for MAP in "${MAPS[@]}"
  do
      OPPONENT_INDEX=-1
      for OPPONENT in "${OPPONENTS[@]}"
      do
          OPPONENT_INDEX=$(expr $OPPONENT_INDEX + 1)
          OPPONENT_PROC=$(expr $OPPONENT_INDEX % $PROCS)
          if [ $OPPONENT_PROC -ne $PROC ]; then continue; fi
          MATCHUP="as $RACE on $MAP vs $OPPONENT"
          ecco "Playing $MATCHUP"
          scbw.play                                \
          --docker_image starcraft:game            \
          --bots "$BOT" "$OPPONENT"                \
          --read_overwrite                         \
          --timeout 2400                           \
          --game_speed 0                           \
          --map_dir "$MAPDIR"                      \
          --map "$MAP"                             \
          --headless                               \
          | tee --append "$SCBWDIR/potato-log.txt" \
          | grep "player_0.rep|Winner|ERROR|Traceback"
          ecco "Finished playing $MATCHUP"
          ecco ""
      done
  done
done
