async function main() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();

  let talked;

  recognition.continuous = false;
  recognition.lang = "es-ES"

  document.addEventListener("keydown", function(event) {
    if (event.key == "<") {
      recognition.start();
    }
  })

  recognition.onresult = async (event) => {
    talked = event.results[event.results.length - 1][0].transcript;

    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'Jarvis:latest',
        messages: [{ role: 'user', content: talked }],
        stream: false
      })
    })
    const data = await response.json();

    const textToVoice = new SpeechSynthesisUtterance();
    textToVoice.text = data.message.content;
    textToVoice.rate = 1.2;
    textToVoice.pitch = 0.8;
    textToVoice.lang = 'es-ES';
    speechSynthesis.speak(textToVoice);
    document.addEventListener("keydown", function(event) {
      if (event.key == "-") {
        speechSynthesis.cancel();
      }
    })
    console.log(data.message.content);

  }
}

main();
