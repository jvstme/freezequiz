let answerGiven = false;

const quizPlayer = document.getElementById("quizPlayer");
const checkButton = document.getElementById("checkButton");
const answerBox = document.getElementById("answerBox");
const prevButton = document.getElementById("prevButton");
const nextButton = document.getElementById("nextButton");

checkButton.addEventListener("click", checkAnswer);
quizPlayer.addEventListener("click", triggerVideo);
document.addEventListener("keydown", handleKeydown);

function checkAnswer() {
    answerGiven = true;
    quizPlayer.play();
    quizPlayer.classList.add("clickable");
    checkButton.classList.add("hidden");
    answerBox.classList.remove("hidden");

    setTimeout(function() {
        answerBox.classList.remove("transparent");
    }, 5000);
}

function triggerVideo() {
    if (!answerGiven) {
        return;
    }

    if (quizPlayer.paused) {
        quizPlayer.play()
    } else {
        quizPlayer.pause();
    }
}

function handleKeydown(e) {
    const key = e.key;

    if (key === "ArrowLeft") {
        prevButton.click();
    } else if (key === "ArrowRight") {
        nextButton.click();
    } else if (key === " ") {
        if (answerGiven) {
            triggerVideo();
        } else {
            checkAnswer();
        }
    }
}
