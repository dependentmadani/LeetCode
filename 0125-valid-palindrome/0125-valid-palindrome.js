/**
 * @param {string} s
 * @return {boolean}
 */ 

function remove_non_alphanumeric(s) {
    s = s.replace(/[^a-z0-9]/gi, '');
    return s
}

function reverse_string(s) {
    let result = s.split('');
    result.reverse();
    return result.join('');
}

var isPalindrome = function(s) {
    s = remove_non_alphanumeric(s);
    s = s.toLowerCase();

    let s_length = s.length;
    let half_string = 0;
    var s1 = "";
    var s2 = "";

    if (s_length == 0 || s_length == 1)
        return true;

    if (s_length % 2 == 0) {
        half_string = s_length / 2;
        s1 = s.substr(0, half_string);
        s2 = s.substr(half_string);
    }
    else {
        half_string = Math.floor(s_length / 2) + 1;
        s1 = s.substr(0, half_string - 1);
        s2 = s.substr(half_string);
    }
    s2 = reverse_string(s2)

    if (s1 === s2)
        return true
    else
        return false
    
};
