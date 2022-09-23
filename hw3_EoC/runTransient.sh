declare date="Sep19"
declare c=0
declare max=30

mkdir result
mkdir result/${date}

for WIDTH in 20
do
    for V in 1
    do
        
        let "count = 0"
        while [ $count -lt 256 ]
        do
            python run.py -width $WIDTH  -duration 1000 -rule $count -fn "result/${date}/"
            let "count+=1"
        done
    done
done

echo "Finished simulation."