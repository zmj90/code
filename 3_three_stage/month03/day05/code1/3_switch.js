var m = prompt('输入：');
switch(m){
    case '1':
    case '3':
    case '5':
    case '7':
    case '8':
    case '10':
    case '12':
        alert('31天');
        break;
    case '2':
        alert("28天");
        break;
    case '4':
    case '6':
    case '9':
    case '11':
        alert('30天');
        break
    default:
        alert('请输入正确的月份');
        break;
}