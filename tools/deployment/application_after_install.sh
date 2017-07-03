# TODO execute `python setup.py install` command.

APPLICATION_NAME="travel_app"
PROJECT_NAME="travel_platform"

PROJECT_FILES=/usr/local/etc/$PROJECT_NAME

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
mkvirtualenv $PROJECT_NAME
workon $PROJECT_NAME

# Install packages.
pip install -r $PROJECT_FILES/requirements.txt

# Install custom packages.
#python $PROJECT_FILES/setup.py install

# Install nginx
sudo yum -y install nginx
sudo cp /usr/local/bin/pip /usr/sbin/
sudo pip install uwsgi

# Hack for extracting project path for last build.
# Read for details:
# http://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html
DEPLOYMENT_PATH=`cat /opt/codedeploy-agent/deployment-root/deployment-instructions/"$DEPLOYMENT_GROUP_ID"_last_successful_install`
PROJECT_ROOT_PATH="$DEPLOYMENT_PATH/deployment-archive"
PROJECT_PATH=$PROJECT_ROOT_PATH/$PROJECT_NAME
APPLICATION_PATH=$PROJECT_PATH/$APPLICATION_NAME
echo $PROJECT_PATH

# FIXME pivanchy: Replace variables with values via sed.
# FIXME pivanchy: Finish setup for uwsgi.

# Replace custom variables.
#sed -i'' -e "s|APPLICATION|my/other/path|g" /etc/nginx/nginx.conf
