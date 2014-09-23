var Bob = function() {
	this.hey = function(input) {
		isQuestion = function(input) {
			return input.charAt(input.length - 1) === '?';
		}
		isYelling = function(input) {
			return input.toUpperCase() === input && /[A-Z]/.test(input);
		}
		isSilent = function(input) {
			return input === '' || /^\s+$/.test(input);
		}
		if (isYelling(input)) {
			return 'Whoa, chill out!';
		}
		if (isQuestion(input)) {
			return 'Sure.';
		}
		if (isSilent(input)) {
			return 'Fine. Be that way!';
		}
		return "Whatever.";
	};
};
module.exports = Bob;
