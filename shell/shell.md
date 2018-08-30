#Some useful shell scripting hints

## Using a index var loop
```bash
i=0; while [ $i -lt 10 ]
do
    i=$(($i+1))
    echo $i
done
```