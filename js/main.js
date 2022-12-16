$(document).ready(() => {
	// Load sources for questions from sources.txt
	loadSourceList();

	// Set copyright notice year
	$("#year").text(new Date().getFullYear());
});

// Open source on select change
$(document).on("change", "#sources", function(){
    alert("Change Happened");
});

function loadSourceList() {
	$.ajax({
		url: "data/sources.json",
		success: (result) => {
			$.each(result, function(i, item) {
				$("<option />", {
					value: item.path,
					text: item.name
				}).appendTo("#sources");
			});
			return true;
		},
		error: () => { console.error("Could not load file " + file); return false; }
	});
}

function loadSource() {
}