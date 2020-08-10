const express = require('express'); //used for server making
const ejs = require('ejs');//used to apply javascript into html code
const lodash = require('lodash');//used for text variations
const bodyParser = require('body-parser');//used to recives data from forms
let {PythonShell} = require('python-shell')
const app=express()

let pridictedAnimes = [];
app.set('view engine','ejs');


let options = {
  // mode: 'text',
  // pythonPath: 'path/to/python',
  // pythonOptions: ['-u'], // get print results in real-time
  // scriptPath: 'path/to/my/scripts',
  args: ['value1']
};




app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/",(req,res)=>{
  pridictedAnimes=[]
  res.render("home");
});

function callPythonCode(name){
  var spawn = require("child_process").spawn;
  var process = spawn('python',["Anime.py",name] );

  process.stdout.on('data',data=>{
    // res.send(data.toString())
    console.log(data.toString());
  });


};

 function test(res){
  var myPythonScriptPath = 'test1.py';

  var pyshell = new PythonShell(myPythonScriptPath);

  PythonShell.run('AnimePredictor.py',options,function(err,results){
    if (err) throw err;
    pridictedAnimes=results;
    console.log(pridictedAnimes);
    setTimeout(() => {  res.render("results",{
      animeList: pridictedAnimes,
      length: pridictedAnimes.length
    }); }, 200);
  });

  // pyshell.on('message', function (message) {
  //     // received a message sent from the Python script (a simple "print" statement)
  //     console.log(message);
  // });
  // pyshell.end(function (err) {
  //     if (err){
  //         throw err;
  //     };
  //
  //     console.log('finished');
  // });

}

app.post("/",(req,res)=>{
  const name = req.body.Name;
  options.args=name;
  test(res);

})




app.listen(process.env.PORT ||3000,function(){
  console.log("server started at port 3000");
})
