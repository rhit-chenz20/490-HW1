declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}

for WIDTH in 43
do
    for V in 1
    do
        let "count+=1"
        echo "running $count"

        python run.py -width $WIDTH  -duration 100 -rule 126 -fn "result/${date}/" -state "0000000000000000000001000000000000000000000"

    done
done

echo "Finished simulation."