cd $1
echo -n "Enter path install: "
read path
if test -n $path
then
   path=$PWD
fi
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
# sudo update-alternatives --set vcpkg "/usr/bin/vcpkg/vcpkg"
sudo update-alternatives --install /usr/bin/vcpkg vcpkg $PWD/vcpkg 10
# sudo update-alternatives --remove-all vcpkg
