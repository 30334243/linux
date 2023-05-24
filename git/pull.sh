echo -n "Enter path project: "
read path
if test -z $path
then
   echo "error path"
   exit 1
elif test ! -d $path
then
   mkdir -p $path
fi
cd $path
cd ..
echo -n "Enter name project git: "
read name_git
git clone https://github.com/30334243/$name_git.git
cd $name_git
echo -n "Enter password: "
read pass
7z x $name_git.7z -o$path/ -p$pass
# cp -r !(*.7z) $path
