const auth = require("./auth.js");

const routes = (app) => {
    auth(app);
}

module.exports = routes;