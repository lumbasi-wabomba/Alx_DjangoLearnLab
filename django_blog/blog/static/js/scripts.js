document.addEventListener("DOMContentLoaded", function () {
    const likeButton = document.getElementById("like-button");
    const likeCount = document.getElementById("like-count");

    likeButton.addEventListener("click", function () {
        let count = parseInt(likeCount.textContent);
        count++;
        likeCount.textContent = count;
    });
});
