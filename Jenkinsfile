def buildClosure = {
    withPythonVenv('venv') {
        stage('Install')
        sh 'pip3 install --upgrade pip'
        sh 'pip3 install -r requirements.txt'
    }
}

def buildParameterMap = [:]
buildParameterMap['appName'] = 'python-nexus-github'
buildParameterMap['buildClosure'] = buildClosure
buildParameterMap['jenkinsNodeLabel'] = 'openshift-jenkins-agent-python'
buildParameterMap['buildStrategy'] =
// ster staat voor de branch
  [
    '*':[
      'checkout',
      //'build',
      'sonar',
      //'sonarQualityGate',
      //'dependencyCheck',
      'containerize',
      'deploy:ot-abr-dev',
      'deploy:ot-abr-tst',
      //'robot:ot-abr-tst',
      'deploy:ot-abr-acc',
      //'robot:ot-abr-acc',
      //'promote:ot-abr-prd',
    ]
  ]

buildAndDeployGeneric(buildParameterMap)

// vim: set ft=groovy:
