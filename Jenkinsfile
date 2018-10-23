@Library('jsharedlib@master') _
node {
	sh 'mkdir target/releaselink'
	sh 'echo "<html><body>testing html</body></html>" > target/releaselink/index.html'
	publishHTML target: [
	                        allowMissing:true,
	                        alwaysLinkToLastBuild: false,
	                        keepAll:true,
	                        reportDir: 'target/releaselink',
	                        reportFiles: 'index.html',
	                        reportName: 'ReleaseLink'
	                    ]
}

stdSbt {
	autoVersionRelease = false 
}
sh 'python3 --version'
