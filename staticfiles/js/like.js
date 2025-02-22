

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".like-button").forEach(function (button) {
        button.addEventListener("click", function () {
            var post_id = this.dataset.postId;
            var likeIcon = document.getElementById("like-icon-" + post_id);
            var likeCount = document.getElementById("like-count-" + post_id);

            fetch("/like/" + post_id + "/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                if (data.liked) {
                    likeIcon.classList.remove("fa-thumbs-o-up");
                    likeIcon.classList.add("fa-thumbs-up", "text-primary");
                } else {
                    likeIcon.classList.remove("fa-thumbs-up", "text-primary");
                    likeIcon.classList.add("fa-thumbs-o-up");
                }
                likeCount.textContent = data.total_likes;
            })
            .catch(error => console.error("Error:", error));
        });
    });
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
