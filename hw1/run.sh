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
    for N in 4 6
    do
    for V in 1
    do
        let "count+=1"
        echo "running $count"

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 1345
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 1345
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 1345


        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 457
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 457
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 457

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 56865
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 56865
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 56865

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 34565
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 34565
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 34565

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25554
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25554
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25554

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 765
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 765
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 765

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25645
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25645
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 25645

        python run.py -size $SIZE -length 15 -mutateR 0.001 -points 15 -prange 10 -fn "result/${date}/CSV/_.001_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 94843
        python run.py -size $SIZE -length 15 -mutateR 0.01 -points 15 -prange 10 -fn "result/${date}/CSV/_.01_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 94843
        python run.py -size $SIZE -length 15 -mutateR 0.1 -points 15 -prange 10 -fn "result/${date}/CSV/_.1_" -e 0 -sel 0 -fit 0 -max 5000 -c 1 -seed 94843
        # -seed 7431
        # if ((count>$max))
        # then
        #     wait
        #     let "count=0"
        # fi
    done
done

echo "Finished simulation. Now plotting"