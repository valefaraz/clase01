#!/bin/bash
echo Ingrese la ruta del archivo
read i
if [ -f $i ];
then
echo "Sí, sí existe."
else
echo "No, no existe"
fi

wc -c $i
