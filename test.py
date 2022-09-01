html_doc = """
 <!Doctype html>
<html>

<head>
     <title>HTML Application</title>
	 <link href="css/site.css" rel="stylesheet">
</head>

<body>
    <div class="main-container">
        <div class="cloud-image">
            <img src="img/successCloudNew.svg" />
        </div>
        <div class="content">
            <div class="tweet-container">
            <a href="http://twitter.com/intent/tweet/?text=I%20just%20created%20a%20new%20HTML%20website%20on%20Azure%20using%20Azure%20DevOps%20Project&hashtags=AzureDevOpsProject%2CVSTS%20%40Azure%20%40VSTS">
                <img src="img/tweetThis.svg" />
            </a>            
        </div>
            <div class="content-body">
                <div class="success-text">Success!</div>
    </div>
    </div>
</div>
</body>
</html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.img[1].src)