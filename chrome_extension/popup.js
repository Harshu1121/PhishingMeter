document.getElementById('check').addEventListener('click', async () => {
  chrome.tabs.query({active: true, currentWindow: true}, async (tabs) => {
    const tabUrl = tabs[0].url;

    const features = extractFeaturesFromUrl(tabUrl);

    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features })
    });

    const data = await response.json();
    document.getElementById("result").textContent = `Result: ${data.result === 1 ? "Safe" : "Phishing"}`;
  });
});

// Simple mock feature extractor (18 features expected)
function extractFeaturesFromUrl(url) {
  const features = [];

  features.push(url.startsWith("https") ? 1 : -1);     // HTTPS
  features.push(url.includes("-") ? -1 : 1);           // Hyphen in URL
  features.push(url.length > 75 ? -1 : 1);             // Long URL

  // Fill remaining with dummy data to reach 18 features
  while (features.length < 18) {
    features.push(0);
  }

  return features;
}
