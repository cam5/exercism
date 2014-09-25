var words = function(input) {

    // Common punctuation from latin block & latin supplement blocks
    // http://bit.ly/Yf54Uq & http://bit.ly/1Cpv1j5
    this.punctuation = /[\u0021-\u0040\u005b-\u0060\u007b-\u007e\u00a0-\u00bf]/g;
    // http://bit.ly/1suY6bC
    this.whiteSpaces    = /[\u0020\u000a-\u000d\u0085\u2028\u2029]/g;

    this.breakUpWords = function(input) {
        if (/[^[A-z]+$]/.test(input)) {
            return [];
        } else {
            return input.split(this.whiteSpaces);
        }
    }

    this.filterNonWords = function(array) {
        if (! array instanceof Array) {
            return false;
        } else {
            for (var i = array.length - 1; i >= 0; i--) {
                array[i] = array[i].replace(this.punctuation, '');
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
        wordArray = breakUpWords(input);
        wordArray = normalizeCase(filterNonWords(wordArray));
        return wordArray;
    }

    this.getWordCounts = function(array) {
        words = {};
        for (var i = array.length - 1; i >= 0; i--) {
            if (typeof(words[array[i]]) == 'number') { // guard against reserved words
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