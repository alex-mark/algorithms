const fs = require("fs");
const fsAsync = require("fs").promises;
const path = require("path");

// Create a folder
// fs.mkdir(path.join(__dirname, "/test"), {}, (err) => {
//   if (err) throw err;
//   console.log("folder created");
// });

// Create and write to file
// Sync version also exist
fs.writeFile(
  path.join(__dirname, "/test", "hello.txt"),
  "A new file content.",
  (err) => {
    if (err) throw err;
    console.log("File written to");

    // Create and write to file
    fs.appendFile(
      path.join(__dirname, "/test", "hello.txt"),
      " I love node.js",
      (err) => {
        if (err) throw err;
        console.log("File appended");
      }
    );
  }
);

// Async fs
(async () => {
  const err = await fsAsync.writeFile(
    path.join(__dirname, "/test", "hello2.txt"),
    "A new file content."
  );
  if (err) throw err;
  console.log("File written to");

  // Create and write to file
  await fs.promises.appendFile(
    path.join(__dirname, "/test", "hello.txt"),
    " I love node.js"
  );
  console.log("File appended");
})();

// Read file
fs.readFile(path.join(__dirname, "/test", "hello.txt"), "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Rename file
fs.rename(
  path.join(__dirname, "/test", "hello.txt"),
  path.join(__dirname, "/test", "not-hello.txt"),
  (err) => {
    if (err) throw err;
    console.log("File renamed");
  }
);
