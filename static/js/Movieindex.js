fetchTrendingResults("all", "week")

        var mediaType = document.getElementById("media_type")
        mediaType.addEventListener("change", function(event) {
            fetchTrendingResults(mediaType.options[mediaType.selectedIndex].value, "day")
        })

        function fetchTrendingResults(media_type, time_window) {
            var trendingDiv = document.getElementById("trendings")
            trendingDiv.innerHTML = ""
            fetch(`/api/trendings?media_type=${media_type}&time_window=${time_window}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }}
                // todo:movieとTVのIDをもらってこれをURLにFethして映画とTVの情報をそれぞれでスターが高い順に表示する。
                )
            .then(res => res.json())
            .then(data => {
                for (let i=0; i<data.results.length; i++) {
                    var mainDiv = document.createElement("div");
                    mainDiv.setAttribute("class", "card");
                    mainDiv.setAttribute("style", "width: 20rem;");
                    var img = document.createElement("img");
                    img.setAttribute("src", "https://image.tmdb.org/t/p/w200" + data.results[i].poster_path);
                    img.setAttribute("class", "card-img-top");
                    img.setAttribute("alt", "...");
                    var body = document.createElement("div");
                    body.setAttribute("class", "card-body");
                    var title = document.createElement("h5");
                    title.setAttribute("class", "card-title");
                    if (data.results[i].name) {
                        title.innerHTML = data.results[i].name;
                    } else {
                        title.innerHTML = data.results[i].title;
                    }
                    //var text = document.createElement("p");
                    //text.setAttribute("class", "card-text");
                    //text.innerHTML = data.results[i].overview;
                    var link = document.createElement("a");
                    link.setAttribute("href", "/" + data.results[i].media_type + "/" + data.results[i].id + "/");
                    link.setAttribute("class", "btn btn-primary");
                    link.innerHTML = "View Details";
                    body.appendChild(title);
                    //body.appendChild(text);
                    body.appendChild(link);
                    mainDiv.appendChild(img);
                    mainDiv.appendChild(body);
                    document.getElementById("trendings").appendChild(mainDiv);
                }
            })
        }
