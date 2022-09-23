declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}

for WIDTH in 100
do
    for V in 1
    do
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334 
        python run.py -width $WIDTH  -duration 1000 -rule 1 -fn "result/${date}/" -l .334
    done
done

echo "Finished simulation."