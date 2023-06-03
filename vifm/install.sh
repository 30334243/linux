sudo apt install gcc g++ make libncurses-dev
cd ~
git clone https://github.com/vifm/vifm.git
cd vifm
./configure
make
sudo make install
cp ./desert.vifm ~/.config/vifm/colors
cp ./vifmrc ~/.config/vifm
