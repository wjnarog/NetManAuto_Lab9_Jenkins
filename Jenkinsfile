pipeline {
    agent any
    
    stages {
        stage('Update/Install packages') {
            steps {
                echo 'Updating and Installing required packages'
                sh 'pip install --upgrade -r requirements.txt'
            }
        }
        stage('Checking and fixing violations') {
            steps {
                echo 'Checking for PEP8 violations'
                sh 'pylint netman_netconf_obj2.py --fail-under=5'
            }
        }
    }
}