function hello(){
    var uname = prompt('输入名字：');
    alert(uname + 'hello');
}

function maxNumber(a, b){
    // if (a - b > 0){
    //     return a;
    // } else if (a - b < 0){
    //     return b;
    // }
    a > b? console.log(a):console.log(b);
}

hello();
var a = prompt('输入数字：');
var b = prompt('输入另一个数字：');
var m = maxNumber(a, b);
alert(m)

