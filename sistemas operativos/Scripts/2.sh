#!/bin/bash

echo Ingrese el nombre del nuevo directorio
read name
echo Donde desea ubicar el nuevo directorio?
read ub
cd
cd $ub
mkdir $name
echo Se creo $name en $ub

