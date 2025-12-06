async function main() {
  let prueba = "hola como te encuentras";

  const response = await fetch('http://localhost:11434/api/chat',{
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      model: 'Jarvis:latest',
      messages: [{role: 'user', content: prueba}],
      stream: false
    })
  })
  const data = await response.json();

  console.log(data.message.content)

}

main();
