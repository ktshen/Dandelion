<?php 
require_once'php/live_stream_db.php';
require_once'php/function.php';

?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
 <!-- 給行動裝置或平板顯示用，根據裝置寬度而定，初始放大比例 1 -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Live_Stream</title>
<!-- CSS -->
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<link rel="stylesheet" href="css/style.css">
</head>



<body>
<div class="top">
<div class="jumbotron">
		<div class="container">
			<div class="row">
				<div class="col-xs-12">
					<h1 class="text-center">Stream-Live</h1> 


					<ul class="nav nav-pills">
					  <li role="presentation"><a href="index.php">首頁</a></li>
					  <li role="presentation"><a href="teach.php">教學</a></li>
					  <li role="presentation"><a href="register.php">註冊</a></li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="main">
 	<div class="container">
 		<div class="row">
 		
 		
 			
 			
 			
 		
 		</div>
 	</div>
</div>

<div class="foot">
 <div class="container">
        <!-- 建立第一個 row 空間，裡面準備放格線系統 -->
        <div class="row">
          <!-- 在 xs 尺寸，佔12格，可參考 http://getbootstrap.com/css/#grid 說明-->
          <div class="col-xs-12">
            <p class="text-center">
              &copy; <?php echo date("Y")?>
              Stream-Live
            </p>
          </div>
        </div>
	</div>
</div>
</body>
</html>


