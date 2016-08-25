path=$(pwd) 
A=1
B=0
for i in $(seq 1 1 10)
do
C=$(($A + $B))
A=$B
B=$C
path="$path/$C"
mkdir $path
done
ls / -la>$path/root.txt
ls ~ -la>$path/home.txt
echo "Diego Fernando Chávarro Sánchez">$path/Mi_Nombre.txt
