const EventEmitter = require("events").EventEmitter;
const uuid = require("uuid");

class Logger extends EventEmitter {
  log(msg) {
    // Call event
    this.emit("message", { id: uuid.v4(), msg });
  }
}

const logger = new Logger();

logger.on("message", (data) => console.log("Called Listener", data));

logger.log("Hello");
logger.log("Hi");
logger.log("Salut");

// module.exports = Logger;
