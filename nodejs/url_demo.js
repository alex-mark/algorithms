const url = require("url");

const myUrl = new URL(
  "http://alexmarkin.com:8000/hello.html?id=123&status=active"
);

// Serialized URL
console.log(myUrl.href);

// Host (root domain)
console.log(myUrl.host);

// Hostname (without port)
console.log(myUrl.hostname);

// Pathname
console.log(myUrl.pathname);

// Serialized query
console.log(myUrl.search);

// Params object
console.log(myUrl.searchParams);

// Add param
myUrl.searchParams.append("abc", "789");
console.log(myUrl.searchParams);

// Loop through Params
myUrl.searchParams.forEach((value, name) => console.log(`${name}: ${value}`));
