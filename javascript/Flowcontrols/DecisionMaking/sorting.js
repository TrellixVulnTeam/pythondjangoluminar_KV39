var num1=19;
var num2=89;
var num3=45;
if((num1 > num2)&(num1 > num3)){
    console.log("num1 is large");
    if(num2>num3){
        console.log('num2 is the second largest');
        console.log(num1,num2,num3);
    }
    else{

        console.log('num3 is the second largest');
        console.log(num1,num3,num2);
    }
}
else if((num2 > num1)&(num2 > num3)){
    console.log("num2 is large");
    if(num3>num1){
        console.log('num3 is the second largest');
        console.log(num2,num3,num1);
    }
    else{
        console.log('num1 is the second largest');
        console.log(num2,num1,num3);
    }
}
else if((num3 > num1)&(num3 > num2)){
    console.log("num3 is large");
    if(num1>num2){
        console.log('num1 is the second largest');
        console.log(num3,num1,num2);
    }
    else{
        console.log('num2 is the second largest');
        console.log(num3,num2,num1);
    }
}
else if((num1 == num2)&(num1 == num3)){
    console.log("3 numbers are equal");
}