sh dockerkill.sh
set potatolog="/c/users/%USERNAME%/AppData/Roaming/scbw/potato-log.txt"
rm %potatolog%
touch %potatolog%
START /B sh -c "PROCS=1 PROC=0 ./potato-run.sh | tee -a ${potatolog}"
tail -f %potatolog%