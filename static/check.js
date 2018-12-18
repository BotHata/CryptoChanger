function check(card) {
	return !(card.length != 16 || isNaN(card));
}