const socket = io()

window.onload = function() {
}

document.addEventListener('DOMContentLoaded', function() {
  const type = document.querySelector("input").value
  socket.emit("subscribe", type)
}, false);

socket.on('data', (msg) => {
  const section = document.querySelector("#info");
  section.removeChild(section.firstChild)

  const span = document.createElement("span");
  span_content = `Sensor: ${msg['sensor']['name']} ${msg['sensor']['value']}; |`
  span_content = span_content + ` Actuator: ${msg['actuator']['name']} state: ${msg['actuator']["value"]}; `

  if(msg['actuator']['name'] == "ar condicionado"){
    span_content = span_content + `temperature: ${msg['actuator']["temperature"]};`
  }
  span.innerHTML =  span_content

  section.append(span);
});