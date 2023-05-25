#!groovy
properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'built-in'
        }
    enviroment {
    BEGET_USER=credentials('BEGET_USER')
    }
    triggers {
        pollSCM('* * * * *')
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("Deploy on beget") {
            steps {
                bat '"C:\\Program Files (x86)\\PuTTY PORTABLE\\plink" %BEGET_USER% -i C:\\Users\\user\\.ssh\\private.ppk -hostkey 15:35:a7:47:3a:e5:2d:79:c0:9f:66:fe:e7:b5:2e:40 source ./deploy.sh'
            }
        }

    }
}