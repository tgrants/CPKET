let data = null;
let shuffled = null;
let current = 0;
let correct = null;

document.addEventListener("DOMContentLoaded", function() {
	loadSourceList();

	// Set copyright notice year
	document.querySelector("#year").textContent = new Date().getFullYear();
});

// Open source on select change
document.querySelector("#sources").addEventListener("change", function() {
	loadSource(this.value);
});

// Reload question if shuffle setting is changed
document.querySelector("#chbxShuffle").addEventListener("change", function() {
	loadQuestion();
});

// Previous question
document.querySelector("#btnPrev").addEventListener("click", function() {
	// console.log(current);
	// console.log(shuffled[current]);
	if (current > 0) {
		current--;
		loadQuestion();
	}
});

// Next question
document.querySelector("#btnNext").addEventListener("click", function() {
	// console.log(current);
	// console.log(shuffled[current]);
	if (current < Object.keys(data).length - 1) {
		current++;
		loadQuestion();
	}
});

// Check if answer is correct
document.querySelector("#btnCheckAnswer").addEventListener("click", function() {
	clearAnswers();
	document.querySelector("#ans" + correct + "Label").classList.add("correct-answer");
	let selected = document.querySelector("input[type='radio']:checked")?.value;
	if (correct == selected) return;
	document.querySelector("#ans" + selected + "Label").classList.add("incorrect-answer");
});

// Load sources for questions from sources.json
function loadSourceList() {
	fetch("data/sources.json")
	.then(response => {
		if (!response.ok) {
			throw new Error("Could not load sources.json");
		}
		return response.json();
	})
	.then(result => {
		const sourcesSelect = document.querySelector("#sources");

		// Populate select
		result.forEach(item => {
			const option = document.createElement("option");
			option.value = item.path;
			option.textContent = item.name;
			sourcesSelect.appendChild(option);
		});

		// Select and load first
		sourcesSelect.value = sourcesSelect.options[0].value;
		loadSource(sourcesSelect.value);
	})
	.catch(error => console.error(error));
}

// Load selected source
function loadSource(src) {
	fetch(src)
	.then(response => {
		if (!response.ok) {
			throw new Error("Could not load " + src);
		}
		return response.json();
	})
	.then(result => {
		data = result;
		current = 0;

		// Create array with the same length as questions, shuffle it
		shuffled = Array.from({length: Object.keys(result).length}, (_, i) => i + 1)
		shuffleArray(shuffled);

		loadQuestion();
	})
	.catch(error => console.error(error));
}

// Load question by index
function loadQuestion() {
	clearAnswers();
	
	// Uncheck all radio inputs
	document.querySelectorAll("input[type='radio']").forEach(input => input.checked = false);

	// Hide the "no answer" notice
	document.querySelector("#noAnswerNotice").style.display = "none";

	// Remove the question image if it exists
	let questionImg = document.querySelector("#questionImg");
	if (questionImg) questionImg.remove();

	let question = document.querySelector("#chbxShuffle").checked ? data[shuffled[current] - 1] : data[current];

	// Enable or disable previous question button
	document.querySelector("#btnPrev").disabled = (current === 0);

	// Enable or disable next question button
	document.querySelector("#btnNext").disabled = (current === Object.keys(data).length - 1);

	// Set question ID and text
	document.querySelector("#questionId").textContent = question.id;
	document.querySelector("#questionText").textContent = question.question;

	// Add question image if it exists
	if (question.image != null) {
		let img = document.createElement("img");
		img.id = "questionImg";
		img.src = question.image;
		img.alt = "Jautājums " + question.id;

		let title = document.querySelector("#questionTitle");
		title.parentNode.insertBefore(img, title.nextSibling);
	}

	// Add choices
	for (let i = 0; i < 4; i++) {
		document.querySelector("#ans" + (i + 1) + "Label").textContent = question.answers[i];
	}

	correct = question.correct;

	// Display a notice in case there is no answer yet
	if (question.correct == null) {
		document.querySelector("#noAnswerNotice").show();
	}
}

function clearAnswers() {
	for (let i = 1; i <= 4; i++) {
		document.querySelector("#ans" + i + "Label").className = "";
	}
}

// Durstenfeld shuffle
function shuffleArray(array) {
	for (var i = array.length - 1; i > 0; i--) {
		var j = Math.floor(Math.random() * (i + 1));
		var temp = array[i];
		array[i] = array[j];
		array[j] = temp;
	}
}
