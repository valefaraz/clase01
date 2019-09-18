#!/bin/bash
cd /
echo Usted se encuentra en $(pwd)
echo Ingrese un directorio
read ub
cd $ub
echo tamaño: $(du -sh)
