sudo apt update
wget -qO- https://apt.llvm.org/llvm-snapshot.gpg.key | sudo tee /etc/apt/trusted.gpg.d/apt.llvm.org.asc
# sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <PUBKEY>
sudo apt install clang-16 lldb-16 lld-16
python3 ~/.vim/plugged/YouCompleteMe/install.py --clang-complete
