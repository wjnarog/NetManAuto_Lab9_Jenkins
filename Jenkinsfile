pipeline {
    agent any

    environment {
        QUAL_GATE = 5
        SCRIPT_TO_TEST = 'netman_netconf_obj2.py'
        EMAIL = ''
    }
    
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
                sh 'pylint ${SCRIPT_TO_TEST} --fail-under=5'
            }
        }
        stage('Running application') {
            steps {
                echo 'Running ${SCRIPT_TO_TEST} script'
                sh 'python3 ${SCRIPT_TO_TEST} | tee output.txt'
            }
        }
        
    }
}