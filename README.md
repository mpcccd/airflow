# Setup #

## Install Ubuntu on Windows ##

- On powershell (run as administrator): 
 execute
`
PS C:\Windows\System32> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
`

## Map Window's root 'C:\' to unix root '/' ##
`sudo nano /etc/wsl.conf`


```
[automount]
root = / 
options = "metadata"
```
`

## Install Programs on Ubuntu ##

```
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
```

## Install Airflow and external libs ##
```
export AIRFLOW_VERSION=2.2.2
export PYTHON_VERSION=3.8
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip3 install "apache-airflowpip==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

pip3 install apache-airflow-providers-oracle
pip3 install cryptography
pip3 install pyspark
```


## Install Oracle Client Libraries ##
Will help us remote connect
https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html#installing-cx-oracle-on-linux

```
pip3 install cx_Oracle --upgrade
```
- Download https://www.oracle.com/database/technologies/instant-client/downloads.html
- Save Zip at ${AIRFLOW_HOME} location
- Unzip at same location
- 




## Set Environment variables ##
In ~/.bashrc
```
export AIRFLOW_HOME=/c/Users/mpaysan/airflow
export LD_LIBRARY_PATH=${AIRFLOW_HOME}/Oracle/instantclient_21_3
```


# Fire up workflow #
```
airflow db init
airflow webserver -p 8080
airflow scheduler    #(use different shell, or run in background by running 'airflow scheduler &', & is background operator)

```

