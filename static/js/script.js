async function searchquery() {
    const inputField = document.getElementById("userinput");
    const resultsContainer = document.getElementById("results");

    try {
        const response = await fetch('/api/query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: inputField.value })
        });

        const data = await response.json();
        const output = data.engine_output;
        resultsContainer.innerHTML = "";
        output.metadatas[0].forEach((item, index) => {
            const resultDiv = document.createElement("div");

            resultDiv.innerHTML = `<div class="item">
                <a class="url" href="${item.url}" target="_blank">${item.title}</a>
                <p class="info">${output.documents[0][index]} </p></div>
            `;
            resultsContainer.appendChild(resultDiv);
        });

    } catch (err) {a
        console.error("Search failed:", err);
        resultsContainer.innerText = "Error: Could not connect to the server.";
    }
}