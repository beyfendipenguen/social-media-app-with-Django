const post2 = $("#posts2")
const spinnerBox = $("#spinner-box")

// TODO delete spinnerBox or add class "not-visible" to spinnerBox when all posts loaded
$.ajax({
    type: "GET",
    url: "/posts-json/",
    data: "data",
    dataType: "json",
    success: function (response) {
        post2.append($("<p>").text("created from jquery"))
        const data = JSON.parse(response.data)
        $.each(data, function (indexInArray, obj) { 
            post2.append($("<p>")
                .text(obj.fields.body)
            )
        });
    },
    error: function (error){
        console.log(error)
    }
});