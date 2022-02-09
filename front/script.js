let answerGiven = false;

const quizPlayer = document.getElementById("quizPlayer");
const checkButton = document.getElementById("checkButton");
const answerBox = document.getElementById("answerBox");
const answer1 = document.getElementById("answer1");
const answer2 = document.getElementById("answer2")

checkButton.addEventListener("click", checkAnswer);
quizPlayer.addEventListener("click", triggerVideo);

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