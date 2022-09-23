declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}


for WIDTH in 100
do
    for V in 1
    do
        
        let "count = 0"
        # while [ $count -lt 256 ]
        # do
            python run.py -width $WIDTH -heightFor2D $WIDTH -duration 10 -rule 154 -fn "result/${date}/" -state "00100" -dimen 2 -percentageAlive 10 -seed 1
            let "count+=1"
        # done
    done
done

echo "Finished simulation."