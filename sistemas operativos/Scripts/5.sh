#!/bin/bash
OPTIONS=" 1 2 3 4 salir "
select op in $OPTIONS; do 
    if [ $op == "1" ]; then
        echo Ejecutando Script 1
        ./1.sh 
    elif [ "$op" == "2" ]; then
    echo Ejecutando Script 2
        ./2.sh
    elif [ "$op" == "3" ]; then
    echo Ejecutando Script 3
        ./3.sh
    elif [ "$op" == "4" ]; then
    echo Ejecutando Script 4
        ./4.sh
    elif [ "$op" == "salir" ]; then
        
        exit
    else
        echo opcion fuera de rango
    fi
done