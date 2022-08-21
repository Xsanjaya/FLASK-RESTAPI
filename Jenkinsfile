pipeline {
  agent {
    label 'Linux1'
  }
  stages {
    stage('PREPARATION') {
      steps {
        sh '''
        echo "STARTING DEPLOYMENT ${JOB_NAME}"
        cd ..
        tar -czf ${JOB_NAME}.tar.gz ${JOB_NAME}
        mv ~/.jenkins/workspace/${JOB_NAME}.tar.gz ~/pypro/${JOB_NAME}.tar.gz
        cd ~/pypro
        tar -xf ${JOB_NAME}.tar.gz
        rm ${JOB_NAME}.tar.gz
        mv -i ${JOB_NAME}/*  FLASK-API/
        rm -rf ${JOB_NAME}
        '''
      }
    }
    stage('Runing APP') {
      steps {
        sh '''
        cd ~/pypro/
        MYENV/bin/activate
        cd ~/pypro/FLASK-API/
        flask db init
        flask db migrate
        flask db upgrade
        '''
      }
    }
  }  
}
