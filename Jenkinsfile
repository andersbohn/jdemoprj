@Library('jsharedlib@master') _

node('master') {  
  stage('Build') {
	print "jenkinsfile"
  }
  stage('Test') {
	print "g1: " 
	def x = g1 { 
       print " jf inside "
       return "hullo"
	}
	print "g1! " 
	echo "g1 x ${x}"
  }
}
