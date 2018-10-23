@Library('jsharedlib@master') _
node {
    echo "mkdir"
	sh 'mkdir -p target/releaselink'
	echo "write file"
	sh 'echo "<html><body>testing html</body></html>" > target/releaselink/index.html'
	echo "publish Html "
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
