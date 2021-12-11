result=$1




blacklist=`cat blacklist.txt`

wc -l $result

#resultdata=`cat $result`

#echo $resultdata
#remove blacklist from file in $1
for i in $blacklist

do



    echo "Removing $i from $1 file"
    vi -c ":%s/.*$i.*//g" -c ":wq" $result
   
    #resultdata= `echo $resultdata | sed "s/.*$i.*//g" | sed '/^$/d'`
done

vi -c ":%g/^$/d" -c ":wq" $result
#rm -f $result
#mv $result.tmp $result
#echo $resultdata #> $result

wc -l $result