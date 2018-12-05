$(function(){
	//取消冒泡，退出按钮点击事件
	$('#out_login').click(function(evt){
		evt.stopPropagation();
		window.location.href=tmooc_path;
	});
});

//去用户中心的界面
function toUserCenter(){
	window.location.href=TTS_URL+"user/userCenter";
}