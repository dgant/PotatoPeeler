sh dockerkill.sh
set potatolog="/c/users/%USERNAME%/AppData/Roaming/scbw/potato-log.txt"
rm %potatolog%
touch %potatolog%
FOR %%T IN (0, 1, 2) DO START /B sh -c "PROCS=3 PROC=%%T ./potato-run.sh | tee -a %potatolog%"
tail -f %potatolog