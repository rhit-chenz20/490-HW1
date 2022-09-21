declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}

for WIDTH in 82
do
    for V in 1
    do
        let "count+=1"
        echo "running $count"

        python run.py -width $WIDTH  -duration 100 -rule 126 -fn "result/${date}/" -state "m"

    done
done

echo "Finished simulation."