declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}


for WIDTH in 100
do
    for V in 1
    do
        python run.py -width $WIDTH -duration 3000 -rule 193 -fn "result/${date}/" -state "m" -dimen 2 --height 100
    done
done

echo "Finished simulation."