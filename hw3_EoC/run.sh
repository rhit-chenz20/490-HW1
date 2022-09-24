declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}

for WIDTH in 128
do
    for V in 1
    do
        for L in .65
        do
            for D in 1000
            do
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L 
                python run.py -width $WIDTH  -duration $D -rule 1 -fn "result/${date}/" -l $L
            done
        done
    done
done
echo "Finished simulation."