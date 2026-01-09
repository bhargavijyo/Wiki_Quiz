const { useState, useEffect } = React;

function App() {
  const [url, setUrl] = useState("");
  const [quiz, setQuiz] = useState(null);
  const [history, setHistory] = useState([]);

  const generateQuiz = async () => {
    const res = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url })
    });
    
  const data = await res.json();

  if (!res.ok) {
    console.error("Backend error:", data);
    alert("Error: " + (data.detail || "Unknown error"));
    return;
  }

  setQuiz(data);
  };

  useEffect(() => {
    fetch("http://localhost:8000/history")
      .then(res => res.json())
      .then(setHistory);
  }, []);

  return (
    <div>
      <h2>Generate Quiz</h2>
      <input onChange={e => setUrl(e.target.value)} />
      <button
  onClick={() => {
    if (!url.trim()) {
      alert("Please enter a Wikipedia URL");
      return;
    }
    generateQuiz();
  }}
>
  Generate
</button>


      {quiz && quiz.quiz.map(q => (
        <div className="card">
          <h4>{q.question}</h4>
          {q.options.map(o => <p>{o}</p>)}
          <p><b>{q.answer}</b></p>
        </div>
      ))}

      <h2>History</h2>
      {history.map(h => <p>{h.title}</p>)}
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
