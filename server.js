import express from "express";
import fetch from "node-fetch";

const app = express();
app.use(express.json());
app.use(express.static("public"));

app.post("/chat", async (req, res) => {
  try {
    const ollama = await fetch("http://127.0.0.1:11434/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(req.body),
    });

    const data = await ollama.json();
    res.json(data);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Error comunicating with ollama" });
  }
});

app.listen(3000, () => console.log("http://localhost:3000 ready!"));

