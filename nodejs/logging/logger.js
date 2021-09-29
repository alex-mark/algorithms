const EventEmitter = require("events").EventEmitter;
const uuid = require("uuid");

class Logger extends EventEmitter {
  log(msg) {
    // Call event
    this.emit("message", { id: uuid.v4(), msg });
  }
}

module.exports = Logger;
