//contact us form sublission
function contactUs() {
  //save data from the form fields in the JS object
  let data1 = {
    name: document.getElementById("Name").value,
    email: document.getElementById("Email").value,
    message: document.getElementById("Message").value
  }
  console.log(data1);
  document.getElementById("answer").innerHTML = (data1.name + ", thank you for submittin our form");

  //convert data to the JSON file
  myJSON = JSON.stringify(data1);
  console.log(myJSON);

  //sent data to server
  var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
  xmlhttp.open("POST", "http://127.0.0.1:8000/MangoAbout/");
  xmlhttp.setRequestHeader("Content-Type", "application/json");
  xmlhttp.send(myJSON);
  //save data to local storage
  localStorage.setItem("testJSON", myJSON);
}
//attempt to retrive data from the local storage - IT IS NOT WORKING
// text = localStorage.getItem("testJSON");
// obj = JSON.parse(text);
// console.log(obj);
// document.getElementById("demo").innerHTML = obj.name;

//testing GET method to retrive data from server

function getData() {
  var Http = new XMLHttpRequest();
  var url = 'http://127.0.0.1:8000/MangoAbout/';
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    var checkData = JSON.parse(Http.responseText);
    console.log(checkData);

    //List each item in the array - version 3 working
    checkData.forEach(showData);
    function showData(item, index) {
      const pe = document.createElement("p");
      pe.innerHTML = ("Id: " + index + "<br>Email: " + item.email + "<br>message: " + item.message + "<br>name: " + item.name);
      document.querySelector('#demo').append(pe);
    }
  }
  // keys for the array elements: item.body, item.id, item.title, item.userId
}
console.log("hello");