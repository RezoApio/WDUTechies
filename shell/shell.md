#Some useful shell scripting hints

## Using a index var loop
```bash
i=0; while [ $i -lt 10 ]
do
    i=$(($i+1))
    echo $i
done
```

## CSV file splitter (with Header preserved)

```bash
#Generating csv test file
i=1; echo "ENTETE;TOTO" > wdu.csv; while [ $i -lt 100 ]
do
    i=$(($i+1))
    echo "ligne$i" >> wdu.csv
done

#Csv splitter (using len and file as parameters)
i=0; len=27; file=wdu.csv; grandmax=`wc -l $file | awk '{print $1}'`; nb=$((($grandmax / $len)+1)); while [ $i -lt $nb ]
do
    name=`basename $file .csv`
    min=$(($i * $len + 1))
    if [ $min -eq 1 ]; then min=2; fi
    i=$(($i+1))
    max=$(($i * $len ))
    if [ $max -gt $grandmax ]; then max=$grandmax; fi
    size=$(($max - $min + 1))
    head -1 $file > $name${i}.csv
    head -$max $file | tail -$size >> $name${i}.csv
done
```