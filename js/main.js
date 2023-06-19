let data = null;
let shuffled = null;
let current = 0;
let correct = null;

$(document).ready(() => {
	loadSourceList();

	// Set copyright notice year
	$("#year").text(new Date().getFullYear());
});

// Open source on select change
$(document).on("change", "#sources", function() {
	loadSource(this.value);
});

// Reload question if shuffle setting is changed
$(document).on("change", "#chbxShuffle", function() {
	loadQuestion();
});

// Previous question
$(document).on("click", "#btnPrev", function(){
	if (current > 0) {
		current--;
		loadQuestion();
	} else {
		// TODO: disable button
	}
}); 

// Next question
$(document).on("click", "#btnNext", function(){
	if (current < Object.keys(data).length) {
		current++;
		loadQuestion();
	} else {
		// TODO: disable button
	}
}); 

// Check if answer is correct
$(document).on("click", "#btnCheckAnswer", function(){
	// TODO: Check if none selected
	clearAnswers();
	$("#ans" + correct + "Label").addClass("correct-answer");
	let selected = $("input[type='radio']:checked").val();
	if (correct == selected) return;
	$("#ans" + selected + "Label").addClass("incorrect-answer");
}); 

// Load sources for questions from sources.json
function loadSourceList() {
	$.ajax({
		url: "data/sources.json",
		success: (result) => {
			// Populate select
			$.each(result, function(i, item) {
				$("<option />", {
					value: item.path,
					text: item.name
				}).appendTo("#sources");
			});

			// Select and load first
			$("#sources").val($("#sources option:first").val());
			loadSource($("#sources").val());

			return true;
		},
		error: () => { console.error("Could not load sources.json"); return false; }
	});
}

// Load selected source
function loadSource(src) {
	$.ajax({
		url: src,
		success: (result) => {
			data = result;
			current = 0;

			// Create array with the same length as questions, shuffle it
			shuffled = Array.from({length: Object.keys(result).length}, (_, i) => i + 1)
			shuffleArray(shuffled);

			loadQuestion();

			return true;
		},
		error: () => { console.error("Could not load " + src); return false; }
	});
}

// Load question by index
function loadQuestion() {
	clearAnswers();
	$("input[type='radio']").prop('checked', false);
	$("#noAnswerNotice").hide();

	let question = $("#chbxShuffle").is(":checked") ? data[shuffled[current]] : data[current];

	$("#questionId").text(question.id);
	$("#questionText").text(question.question);
	for (let i = 0; i < 4; i++)
		$("#ans" + (i + 1) + "Label").text(question.answers[i]);
	correct = question.correct;

	// Display a notice in case there is no answer yet
	if (question.correct == null) $("#noAnswerNotice").show();
}

function clearAnswers(clearRadioButtons) {
	for (let i = 1; i <= 4; i++) {
		$("#ans" + i + "Label").removeClass()
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