const API_BASE = "https://3taivwqnrd.execute-api.ap-south-1.amazonaws.com/prod";

async function getLabels() {
  const fileInput = document.getElementById("imageInput");
  const output = document.getElementById("output");

  if (!fileInput.files.length) {
    alert("Select an image first");
    return;
  }

  const file = fileInput.files[0];
  console.log("Uploading:", file.name, file.type);
  output.innerHTML = "⬆️ Uploading image...";

  // 1️⃣ Get pre-signed URL
  const presignRes = await fetch(
    `${API_BASE}/upload-url?fileName=${encodeURIComponent(file.name)}&fileType=${encodeURIComponent(file.type)}`
  );

  const presignData = await presignRes.json();

  // 🚨 CRITICAL CHECK
  if (!presignData.imageName) {
    output.innerHTML = "❌ Failed to get image name";
    return;
  }

  const imageName = presignData.imageName;

  // 2️⃣ Upload image to S3
await fetch(presignData.uploadUrl, {
  method: "PUT",
  body: file
});




  output.innerHTML = "🧠 Processing image...";

  // 3️⃣ Poll for labels
  pollForLabels(imageName, 0);
}

async function pollForLabels(imageName, attempt) {
  const output = document.getElementById("output");

  if (!imageName) {
    output.innerHTML = "❌ Image name is undefined";
    return;
  }

  if (attempt > 10) {
    output.innerHTML = "❌ Processing took too long. Try again.";
    return;
  }

  const res = await fetch(
    `${API_BASE}/labels?imageName=${encodeURIComponent(imageName)}`
  );

  if (res.status === 200) {
    const data = await res.json();

    if (data.labels) {
      let html = "<h3>Detected Labels</h3><ul>";
      data.labels.forEach(l => {
        html += `<li>${l.Name} – ${l.Confidence}%</li>`;
      });
      html += "</ul>";
      output.innerHTML = html;
      return;
    }
  }

  setTimeout(() => {
    pollForLabels(imageName, attempt + 1);
  }, 2000);
}
