
for op_region in 'Estrella' 'Completa' 'Rueda' 'Ochoa' 'Multihub' 'Grande66' 'Grande50'
do
  for op_algorithm in "random" "greedy" "busqueda_local" "busqueda_local_iter"
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

for op_region in 'Estrella' 'Completa' 'Rueda' 'Ochoa' 'Multihub' 'Grande66' 'Grande50'
do
  for degrees in 3 5 10 15
  do
    echo $op_region "grasp" $degrees
    for iter in $(seq 1 100)
    do
      python tp.py -region $op_region -algorithm "grasp" -degrees $degrees
    done
  done
done

# Optimizamos el tamaño del enjambre y la cantidad de lideres
for op_region in 'Estrella' 'Completa' 'Rueda' 'Ochoa' 'Multihub' 'Grande66' 'Grande50'
do
  for iter in $(seq 1 100)
  do
    echo $op_region "swarm" $degrees $iter
    python tp.py -region $op_region -algorithm "swarm" -degrees 15
  done
done
