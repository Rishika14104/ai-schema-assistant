const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/generate-schema", async (req, res) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/analyze", {
            description: req.body.description
        });

        res.json(response.data);

    } catch (error) {
        res.status(500).json({ error: "AI Service Error" });
    }
});

app.listen(5000, () => {
    console.log("Backend running on http://localhost:5000");
});