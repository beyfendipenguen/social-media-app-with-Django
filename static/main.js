const post2 = $("#posts2")
const loadAnimation = $("#spinner-box");

$.ajax({
    type: "GET",
    url: "/posts-json/",
    data: "data",
    dataType: "json",
    beforeSend: function () { loadAnimation.show(); },
    
    success: function (response) {
        post2.append($("<p>").text("created from jquery"))
        const data = JSON.parse(response.data)
        console.log(data);
        setTimeout(() => {
            $.each(data, function (indexInArray, obj) {
                post2.append($("<p>")
                    .text(obj.fields.body)
                )
            });
            loadAnimation.hide();
        }, 1500);

    },
    error: function (error) {
        console.log(error)
    }
});
