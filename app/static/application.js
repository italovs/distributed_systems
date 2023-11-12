const socket = io()

window.onload = function() {
}

document.addEventListener('DOMContentLoaded', function() {
  const type = document.querySelector("#type").value
  socket.emit("subscribe", type)
}, false);

function change_status(){
  let type = document.querySelector("#type").value
  let status = document.querySelector("#status").value
  let temperature_element = document.querySelector("#temperature")
  let temperature = ""

  if(temperature_element){
    temperature = temperature_element.value
  }

  json = {
    "name": type,
    "status": status,
    "temperature": temperature,
  }

  socket.emit("change_status", json)
}

socket.on('data', (msg) => {
  const section = document.querySelector("#info");
  section.removeChild(section.firstElementChild)

  const span = document.createElement("span");
  const div = document.createElement("div");

  span_content = `Sensor: ${msg["sensor"]['name']} ${msg["sensor"]['value']}; |`
  span_content = span_content + ` Actuator: ${msg['actuator']['name']} state: ${msg['actuator']["value"]}; `

  if(msg['actuator']['name'] == "ar condicionado"){
    span_content = span_content + `temperature: ${msg['actuator']["temperature"]};`
  }
  span.innerHTML =  span_content

  div.append(span)
  section.append(div);
});
