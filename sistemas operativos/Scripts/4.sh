echo Como te llamas?
read name
echo Como te sientes?
read sentimiento
if [ -z "$sentimiento" ]; then
	echo "estas mal papu"	

else
	
	mkdir ~/Escritorio/$name
	cd /home/valentin/Escritorio/$name
	fecha=$(date)
	echo hoy $fecha me siento $sentimiento >> sentimiento.txt
	ub=$(pwd)
	echo El sentimiento del dia de hoy se ecuentra en $ub
fi



