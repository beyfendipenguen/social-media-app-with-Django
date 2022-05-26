const toFollowModalBody = $("#to-follow-modal-body")
const toFollowBtn = $("#to-follow-btn")
const loadAnimation = $("#spinner-box")
var isAjaxLoaded = false
$("#to-follow-btn").click(function (e) { 
    if (!isAjaxLoaded) {
        $.ajax({
            type: "GET",
            url: "/profiles/my-profiles-json/",
            data: "data",
            dataType: "json",
            beforeSend: function () { loadAnimation.show(); },
            success: function (response) {
                const data = response.pf_data
                console.log(data)
                setTimeout(() => {
                    $.each(data, function (indexInArray, obj) {
                        /*  
                        <div class="row align-items-center mb-2">
                            <div class="col-2">
                                <img src="/media/avatars/avatar.png" alt="" height=50 width=50 class="rounded-circle border border-warning">
                            </div>
                            <div class="col-3 text-muted">muhammed</div>
                            <div class="col text-right">
                                <a href="" class="btn btn-success">follow</a>
                            </div>
                        </div>
                        */
                        toFollowModalBody.append($("<div>")
                            .attr("class", "row align-items-center mb-2")
                            .append($("<div>")
                                .attr("class","col-2")
                                .append($("<img>")
                                    .attr("src", obj.avatar)
                                    .attr("height", 50)
                                    .attr("width", 50)
                                    .attr("class", "rounded-circle border border-warning")
                                )
                            )
                            .append($("<div>")
                                .attr("class", "col-3 text-muted")
                                .text(obj.user)
                            )
                            .append($("<div>")
                                .attr("class", "col text-right")
                                .append($("<a>")
                                    .attr("class", "btn btn-success")
                                    .text("follow")
                                )
                            )
                        )
                    });
                    loadAnimation.hide();
                }, 1500);
                isAjaxLoaded = true;
            },
            error: function (error) {
                console.log(error)
            }
        });

    }
});