cd ~
git clone https://github.com/Microsoft/vcpkg.git
cd vcpkg
./bootstrap-vcpkg.sh -disableMetrics
# sudo update-alternatives --set vcpkg "/usr/bin/vcpkg/vcpkg"
sudo update-alternatives --install /usr/bin/vcpkg vcpkg $PWD/vcpkg 10
# sudo update-alternatives --remove-all vcpkg
