var Hammer = function() {

	this.compute = function(sequenceOne, sequenceTwo) {

		s1 = sequenceOne; s2 = sequenceTwo;

		validateNotation = function(sequenceOne, sequenceTwo) {
			// http://bit.ly/YAB31c
			return !/[^ACTGRYKMSWBDHVN]/.test(sequenceOne + sequenceTwo);
		}

		countDistance = function(sequenceOne, sequenceTwo) {
			s1 = sequenceOne,
			s2 = sequenceTwo,
			shortestSequenceLength = (sequenceOne.length > sequenceTwo.length) ? 
				sequenceTwo.length : sequenceOne.length,
			mutations = 0;

			for (var i = shortestSequenceLength - 1; i >= 0; i--) {
				if ( s1[i] !== s2[i] ) {
					mutations++;
				}
			};

			return mutations;
		}

		validateNotation(s1, s2);
		return countDistance(s1, s2);
	}

}
module.exports = new Hammer;