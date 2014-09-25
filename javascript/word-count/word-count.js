var words = function(input) {

    this.crillic    = "\u0400-\u04FF";
    this.diacritics = "ÁáĆćÉéÍíĹĺŃńÓóŔŕŚśÚúÝýŹźŐőŰűÀàÈèÌìÒòÙùÂâĈĉÊêĜĝĤĥÎîĴĵÔôŜŝÛûŴŵŶŷÄäËëÏïÖöÜüǖǘǚǜŸÿÃãẼẽĨĩÑñÕõŨũỸỹÇçĢģĶķĻļŅņŖŗŞşŢţǍǎČčĎďĚěǏǐĽľŇňǑǒŘřŠšŤťǓǔŽžĂăĔĕĞğĬĭŎŏŬŭĀāĒēĪīŌōŪūȲȳǢǣĊċĖėĠġİıŻżḌḍḤḥḶḷḸḹṂṃṆṇṚṛṜṝṢṣṬṭÅåŮůĄąĘęĮįǪǫŲųĐđĦħŁłĿŀ";

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
                array[i] = array[i].replace(
                    new RegExp('[^A-z|' + 
                        this.crillic + '|' + 
                        this.diacritics + ']', 'g'
                    ), '');
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