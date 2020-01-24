
//jquery
//XMLHTTPResponse原生ajax

//整个文档加载完毕会执行下面函数，$是Jquery的简写
$(function () {
    $('#submit').click(function (event) {
        //阻止默认的提交表单行为
        event.preventDefault();
        var email=$('input[name=email]').val();
        var pwd=$('input[name=pwd]').val();
        //var token=$('input[name=csrf_token]').val();
        // var token=$('meta[name=csrf_token]').attr('content');
        //没有封装时写法
        // $.ajaxSetup({
        //     "beforeSend":function (xhr,settings) {
        //         if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain){
        //             xhr.setRequestHeader('X-CSRFToke',token)
        //         }
        //     }
        //
        //     }
        // );

        // $.post({
        //     //url必须指定，但是相同域名下可以省略域名不写
        //     "url":"/login/",
        //     "data":{
        //         "email":email,
        //         "pwd":pwd,
        //         'csrf_token':token
        //         },
        //     //成功以后执行
        //     "success":function (data) {
        //         console.log(data);
        //     },
        //     "fail":function (error) {
        //         console.log(error);
        //     }
        //
        //     });
        csrf_ajax.post({
             "url":"/login/",
            "data":{
                "email":email,
                "pwd":pwd},
            //成功以后执行
            "success":function (data) {
                console.log(data);
            },
            "fail":function (error) {
                console.log(error);
            }
        });
    });
});
