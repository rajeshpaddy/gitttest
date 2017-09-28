var book = require("./grades.js").book;
var express = require("express");
var app = express();
 
book.addGrade(100);
book.addGrade(90);

app.get("/", function(req,res){
    res.send("hello world");
});

app.get("/grade",function(req,res){
    // console.log(req.query.grades);
    var grades = req.query.grades.split(",");
    book.reset();
    for (var i = 0 ;i<grades.length;i++)    {
        book.addGrade(parseInt(grades[i]));
    }
        // console.log(book._grades);
        var average= book.getAverage();
        var letter = book.getLetterGrade();
        res.send ("Your average is " + average + " and grade is " + letter);
});

app.listen(3000);
console.log("Server is listening in port 3000");

