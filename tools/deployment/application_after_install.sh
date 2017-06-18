# TODO execute `python setup.py install` command.
# Update and upgrade package repositories.
sudo yum update
sudo yum upgrade

# Install Python and some basic packages.
sudo yum install python-pip
sudo easy_install --upgrade pip
sudo yum install python-devel
sudo yum groupinstall 'Development Tools'

# Install virtualenvwrapper
pip install virtualenvwrapper

if [[ ! -s "$HOME/.bash_profile" && -s "$HOME/.profile" ]] ; then
  profile_file="$HOME/.profile"
else
  profile_file="$HOME/.bash_profile"
fi

if ! grep -q 'virtualenvwrapper.sh' "${profile_file}" ; then
  echo "export WORKON_HOME=$HOME/.virtualenvs" >> "${profile_file}"
  echo "source /usr/local/bin/virtualenvwrapper.sh" >> "${profile_file}"
fi

source "${profile_file}"

echo "Current folder" + $PWD

# Prepare virtual environment.
mkvirtualenv travel_platform
workon travel_platform

# Install packages.
pip install -r /usr/local/etc/requirements.txt

# Install custom packages.
python setup.py install

