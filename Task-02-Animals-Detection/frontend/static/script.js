document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.getElementById("drop-area");
  const fileInput = document.getElementById("fileElem");
  const uploadBtn = document.getElementById("uploadBtn");
  const popup = document.getElementById("popup");
  const popupText = document.getElementById("popup-text");
  const resultContainer = document.getElementById("result-container");

  let selectedFile = null;

  // Drag & Drop Handling
  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("highlight");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("highlight");
  });

  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("highlight");
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      selectedFile = files[0];
      dropArea.querySelector("p").textContent = selectedFile.name;
    }
  });

  fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
      selectedFile = fileInput.files[0];
      dropArea.querySelector("p").textContent = selectedFile.name;
    }
  });

  uploadBtn.addEventListener("click", async () => {
    if (!selectedFile) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    // Show loading text while processing
    popupText.textContent = "Processing...";
    popup.classList.remove("hidden");

    try {
      const response = await fetch("/detect", {
        method: "POST",
        body: formData,
      });

      const result = await response.json();

      if (result.error) {
        popupText.textContent = `Error: ${result.error}`;
        return;
      }

      const carnivoreCount = parseInt(result.carnivores_detected || 0);
      const outputUrl = `/get_output/${result.output_filename}`;

      resultContainer.innerHTML = `
        <p style="margin-bottom: 10px;">Detected Carnivores: ${carnivoreCount}</p>
        ${
          result.type === "image"
            ? `<img src="/get_output/${result.output_filename}" alt="Detected Result" style="max-width: 100%; border-radius: 8px;" />`
            : `<video controls style="max-width: 100%; border-radius: 8px;">
                <source src="/get_output/${result.output_filename}" type="video/webm">
                Your browser does not support the video tag.
              </video>`
        }
      `;

      if (carnivoreCount > 0) {
        popupText.textContent = `Detected ${carnivoreCount} carnivore${carnivoreCount > 1 ? "s" : ""}!`;
        popup.classList.remove("hidden");
      } else {
        popup.classList.add("hidden");
      }


    } catch (error) {
      popupText.textContent = "Error during upload. Please try again.";
      console.error("Upload failed:", error);
    }
  });

  document.querySelector("#popup button").addEventListener("click", () => {
    popup.classList.add("hidden");
  });
});
