declare date="Sep9"
declare c=0
declare max=30

mkdir result
mkdir result/${date}
mkdir result/${date}/CSV
mkdir result/${date}/plot
mkdir result/${date}/CSV/exp_4

for SIZE in 10
do
    for N in 2 4 6
    do
    for V in {1..10}
    do
        let "count+=1"
        echo "running $count"

        python3 run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/exp_4/${V}_" -e 0 -sel 1 -fit 0 -max 1 -c 0 -n $N
        # -seed 7431
    done
    done
done

echo "Finished simulation. Now plotting"