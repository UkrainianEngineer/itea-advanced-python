# TODO execute `python setup.py install` command.

TRAVEL_PLATFORM_FILES=/usr/local/etc/travel_platform

# Update and upgrade package repositories.
sudo yum update
sudo yum upgrade

# Install Python and some basic packages.
sudo yum install python-pip
sudo easy_install --upgrade pip
sudo yum install python-devel
sudo yum groupinstall 'Development Tools'

# Install virtualenvwrapper
sudo pip install virtualenvwrapper

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
pip install -r $TRAVEL_PLATFORM_FILES/requirements.txt

# Install custom packages.
python $TRAVEL_PLATFORM_FILES/setup.py install

