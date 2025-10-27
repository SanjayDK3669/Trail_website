const API_BASE = "http://127.0.0.1:8000"; // set via nginx or host if needed

const form = document.getElementById("contactForm");
const statusEl = document.getElementById("status");
const submitBtn = document.getElementById("submitBtn");

function setStatus(msg, isError=false) {
  statusEl.textContent = msg;
  statusEl.style.color = isError ? "crimson" : "green";
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  submitBtn.disabled = true;
  setStatus("Sending...");

  const payload = {
    name: document.getElementById("name").value.trim(),
    email: document.getElementById("email").value.trim(),
    phone: document.getElementById("phone").value.trim(),
    message: document.getElementById("message").value.trim(),
  };

  try {
    const res = await fetch(`${API_BASE}/api/submit`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      const data = await res.json();
      setStatus("Thanks — we received your message!");
      form.reset();
    } else {
      const err = await res.json();
      setStatus(err.error || "An error occurred. Try again later.", true);
      console.error("Error:", err);
    }
  } catch (ex) {
    console.error(ex);
    setStatus("Network error. Please try again later.", true);
  } finally {
    submitBtn.disabled = false;
  }
});
