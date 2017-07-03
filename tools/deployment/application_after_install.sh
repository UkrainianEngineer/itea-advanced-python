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
#python $TRAVEL_PLATFORM_FILES/setup.py install

# Install nginx
sudo yum -y install nginx
sudo cp /usr/local/bin/pip /usr/sbin/
sudo pip install uwsgi

echo "LIST OF ENVS"
PROJECT_PATH=`cat /opt/codedeploy-agent/deployment-root/deployment-instructions/"$DEPLOYMENT_GROUP_ID_last_successful_install"`
echo $PROJECT_PATH

# Replace custom variables.
#sed -i'' -e "s|APPLICATION|my/other/path|g" /etc/nginx/nginx.conf
