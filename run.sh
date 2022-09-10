declare date="Sep9"
declare c=0
declare max=30

mkdir result
mkdir result/${date}
mkdir result/${date}/CSV
mkdir result/${date}/plot

for SIZE in 100
do
    for V in 1
    do
        let "count+=1"
        echo "running $count"

        python3 run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/exp_2_" -e 0 -sel 0 -fit 0 -max 1000 -c 0 
        # -seed 7431
    done
done

echo "Finished simulation. Now plotting"