var http = require('http');
var os = require('os');

http.createServer(function (req, res) {
	var result = {};

	result.os = {
		uptime : os.uptime(),
		platform : os.platform(),
		totalmem : os.totalmem(),
		freemem : os.freemem(),
		cpus : os.cpus()
	};

	res.setHeader('Content-Type', 'application/json');
    	res.write(JSON.stringify(result));
	res.end();
}).listen(3000);
