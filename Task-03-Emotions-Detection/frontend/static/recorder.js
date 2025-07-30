let mediaRecorder;
let audioChunks = [];

document.getElementById('recordButton').addEventListener('click', async () => {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();

  audioChunks = [];

  mediaRecorder.addEventListener("dataavailable", event => {
    audioChunks.push(event.data);
  });

  mediaRecorder.addEventListener("stop", () => {
    const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
    const formData = new FormData();
    formData.append("file", audioBlob, "recorded.wav");

    fetch("/upload", {
      method: "POST",
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.gender.toLowerCase() === "male") {
        showPopup("Please upload female voice");
      } else {
        showPopup(`Emotion: ${data.emotion}`);
      }
    })
    .catch(error => {
      showPopup("Error during prediction");
      console.error(error);
    });
  });

  document.getElementById('recordButton').disabled = true;
  document.getElementById('stopButton').disabled = false;
});

document.getElementById('stopButton').addEventListener('click', () => {
  mediaRecorder.stop();
  document.getElementById('recordButton').disabled = false;
  document.getElementById('stopButton').disabled = true;
});

const dropArea = document.getElementById("drop-area");
const fileInput = document.getElementById("fileInput");

dropArea.addEventListener("dragover", e => {
  e.preventDefault();
  dropArea.classList.add("active");
});

dropArea.addEventListener("dragleave", () => {
  dropArea.classList.remove("active");
});

dropArea.addEventListener("drop", e => {
  e.preventDefault();
  dropArea.classList.remove("active");

  const file = e.dataTransfer.files[0];
  handleUpload(file);
});

fileInput.addEventListener("change", () => {
  const file = fileInput.files[0];
  handleUpload(file);
});

function handleUpload(file) {
  const formData = new FormData();
  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    if (data.gender.toLowerCase() === "male") {
      showPopup("Please upload female voice");
    } else {
      showPopup(`Emotion: ${data.emotion}`);
    }
  })
  .catch(error => {
    showPopup("Error during prediction");
    console.error(error);
  });
}

// Custom popup box (for all messages)
function showPopup(message) {
  const popup = document.createElement('div');
  popup.innerText = message;
  popup.style.position = 'fixed';
  popup.style.top = '20px';
  popup.style.left = '50%';
  popup.style.transform = 'translateX(-50%)';
  popup.style.background = '#333';
  popup.style.color = '#fff';
  popup.style.padding = '12px 24px';
  popup.style.borderRadius = '12px';
  popup.style.zIndex = '1000';
  popup.style.fontSize = '16px';
  popup.style.boxShadow = '0px 4px 12px rgba(0, 0, 0, 0.2)';
  document.body.appendChild(popup);

  setTimeout(() => {
    popup.remove();
  }, 3000);
}
