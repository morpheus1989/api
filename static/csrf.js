
var csrf_ajax={
    //支持get/post请求
    'get':function (args) {
        args['method']='get';
        this.ajax(args);
        },
    'post':function (args) {
        args['method']='post';
        this.ajax(args);
        },
    'ajax':function (args) {
        this._ajaxSetup();
        $.ajax(args);
        },
    '_ajaxSetup':function () {
        //启动之前调用
        $.ajaxSetup({
            //发送请求之前执行该函数
            'beforeSend':function (xhr,settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain){
                    var token=$('meta[name=csrf-token]').attr('content');
                    xhr.setRequestHeader('X-CSRFToke',token);
                }
            }
        });
    }

};
