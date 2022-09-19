declare date="Sep9"
declare c=0
declare max=30

mkdir result
mkdir result/${date}
mkdir result/${date}/CSV
mkdir result/${date}/plot
mkdir result/${date}/CSV/exp_4

for SIZE in 100
do
    for V in 1
    do
        let "count+=1"
        echo "running $count"


        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25554


        # -seed 7431
        # if ((count>$max))
        # then
        #     wait
        #     let "count=0"
        # fi
    done
done