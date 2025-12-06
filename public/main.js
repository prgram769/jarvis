async function main() {
  let prueba = "hola como te encuentras";

  const response = await fetch('/chat',{
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      model: 'Jarvis:latest',
      messages: [{role: 'user', content: prueba}],
      stream: false
    })
  })
  const data = await response.json();

  console.log(data.message?.content ?? data.response ?? data);

}

main();
// import ollama from 'ollama/browser'
//
// const response = await ollama.chat({
//   model: 'Jarvis:latest',
//   messages: [{ role: 'user', content: 'hola' }],
// })
// console.log(response.message.content)
