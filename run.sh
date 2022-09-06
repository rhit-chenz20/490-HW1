declare date="Sep6"
declare c=0
declare max=30

mkdir result
mkdir result/${date}
mkdir result/${date}/CSV
mkdir result/${date}/plot

for SIZE in 100
do
    for V in {1..10}
    do
        let "count+=1"
        echo "running $count"

        python3 run.py -size $SIZE -length "" -mutateR "" -points "" -prange "" -fn "result/${date}/CSV/_$V" -e "" -sel "" -fit "" -max "" 
        # if ((count>$max))
        # then
        #     wait
        #     let "count=0"
        # fi
    done
done

echo "Finished simulation. Now plotting"


for MS in 10
do
    for FS in 10
    do
        for FM in 1
        do
            for COST in 0
            do
                for FIT in 0
                do

                    let "c+=1"
                    python3 plot.py -files result/${date}/CSV/""_*.csv -out result/${date}/plot/"" 
                    echo "finished plotting $c"
                    
                    if ((c>$max))
                        then
                            wait
                            let "c=0"
                        fi

                done
            done
        done
    done
done              
echo "finished plotting"

# bash runmanythre.sh