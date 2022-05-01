const express = require("express");
const { spawn } = require("child_process");
const cors = require("cors");
const app = express();
const port = 5000;

app.use(cors())

app.get("/filters", (req, res) => {
    const Crawler = spawn("python", ["Crawler.py"]);

    Crawler.on("close", () => {
        console.log("Crawling finished.");
        const Filters = spawn("python", ["Filters.py"]);
        Filters.on("close", () =>{
            console.log("Filtering finished.");
        })
        res.send();
        });
})

app.listen(port, () => console.log(`Listening on port ${port}`));