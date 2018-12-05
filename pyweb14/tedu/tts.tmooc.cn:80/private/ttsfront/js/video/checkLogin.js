//检验是否处于登录状态
var timeId;
var flag=true;
function checksession(source){
	
	if(flag){
		timeId=setInterval(function(){
			checksessions(source);
		},120000);
	}
}
function popup(){
	
	layer.open({
		  title: '提示'
		  ,content: '您的账号在另一地点登录，您被迫下线',
			yes:function(){window.location.href = tmooc_path}
		});
}
//发送ajax 验证用户是否处于登录状态的请求
	function checksessions(source){
		  $.ajax({
			url:source+"tlogin/checkLogin",
			type:"POST",
			dataType:"json",
			success:function(data){
				if(data.code < 1 ){
					//登出状态
					flag=false;
					clearInterval(timeId);
					popup();
					setTimeout(function(){
						window.location.href = tmooc_path;
					},5000);
				} 
			}
		});                      
	}