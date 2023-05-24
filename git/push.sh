echo -n "Enter path project: "
read path
# IF EMPTY ARG
if test -z $path
then
   echo "Error path"
   exit 1
fi
# IF DIR NO EXIST
if test -d $path
then
   cd $path
   echo -n "Enter name project: "
   read name
   7z a -p -mx=0 -mhe -t7z $name.7z ./
   cd ..
   git clone https://github.com/30334243/$name.git
   cd $name
   mv -n $path/$name.7z ./
   git add .
   git commit -m"ok"
   git branch -M main
   git push -u origin main
else
   echo "$path not exist"
fi
