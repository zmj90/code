var year = prompt('输入年：');
var month = prompt('输入月：');
var day = prompt('输入日：');
if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    var month2 = 28;
}else{
    var month2 = 29;
}