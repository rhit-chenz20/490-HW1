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


# for MS in 10
# do
#     for FS in 10
#     do
#         for FM in 1
#         do
#             for COST in 0
#             do
#                 for FIT in 0
#                 do

#                     let "c+=1"
#                     python3 plot.py -files result/${date}/CSV/""_*.csv -out result/${date}/plot/"" 
#                     echo "finished plotting $c"
                    
#                     if ((c>$max))
#                         then
#                             wait
#                             let "c=0"
#                         fi

#                 done
#             done
#         done
#     done
# done              
# echo "finished plotting"

# # bash runmanythre.sh