
for op_region in 'Estrella' 'Completa' 'Rueda' 'Ochoa' 'Multihub' 'Grande66' 'Grande50'
do
  for op_algorithm in "random" "busqueda_local" "busqueda_local_iter"
  do
    echo $op_region $op_algorithm
    for iter in $(seq 1 100)
    do
      python tp.py -region $op_region -algorithm $op_algorithm
    done
  done
done

for op_region in 'Estrella' 'Completa' 'Rueda' 'Ochoa'
do
  echo $op_region "backtraking"
  for iter in $(seq 1 100)
  do
    python tp.py -region $op_region -algorithm "backtraking"
  done
done
