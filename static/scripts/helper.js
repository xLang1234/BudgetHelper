function doAJAXCall(partialLink, dataToSend, callback, callbackFailed) {

    var url = "http://localhost:5000/api/" + partialLink;

    var data = dataToSend;
    $.ajax({
        url: url,
        type: 'GET',
        data: data,
        success: function(arr) {
            console.log("Success")
            callback(arr);
            return "Success";
        },
        error: function(arr) {
            console.log("Failed")
            callback(arr);
            return "Failed";
        }
    });

}

function doAJAXCallPost(partialLink, dataToSend, callback, callbackFailed) {

    var url = "http://localhost:5000/api/" + partialLink;

    var data = dataToSend;
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: function(arr) {
            console.log("Success")
            callback(arr);
            return "Success";
        },
        error: function(arr) {
            console.log("Failed")
            callback(arr);
            return "Failed";
        }
    });

}
