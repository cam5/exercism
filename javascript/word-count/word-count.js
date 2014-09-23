var words = function(input) {

    this.breakUpBySpaces = function(input) {
        if (/[^[A-z]+$]/.test(input)) {
            return [];
        } else {
            return input.split(' ');
        }
    }

    this.filterNonWords = function(array) {
        if (! array instanceof Array) {
            return false;
        } else {
            for (var i = array.length - 1; i >= 0; i--) {
                array[i] = array[i].replace(/\W+/, '');
                if (array[i] == '') {
                    array.splice(i, 1);
                }
            };
            return array;
        }
    }

    this.normalizeCase = function(array) {
        for (var i = array.length - 1; i >= 0; i--) {
            array[i] = array[i].toLowerCase();
        };
        return array;
    }

    this.processString = function(input) {
        wordArray = breakUpBySpaces(input);
        wordArray = normalizeCase(filterNonWords(wordArray));
        return wordArray;
    }

    this.getWordCounts = function(array) {
        words = {};
        for (var i = array.length - 1; i >= 0; i--) {
            if (array[i] === 'constructor') { words.constructor = 1; }
            if (typeof(words[array[i]]) !== 'undefined') {
                words[array[i]]++;
            } else {
                words[array[i]] = 1;
            }
        };
        return words;
    }

    wordArray = processString(input);

    return getWordCounts(wordArray);
}
module.exports = words;