var fs=require('fs')
console.log("/file content type before read")
var a=fs.readFileSync("a.csv","utf8");
fs.appendFile("b.csv",a,function(err){

    if(err)
    console.log(err);
    else{
        console.log("/n file after append:",fs.readFileSync("b.csv","utf8"));
    }
});

