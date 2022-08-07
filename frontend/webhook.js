// Эту поебень надо допилить немного, без работающей сборки тяжеловато, доберусь до компа, сделаю
const http = require("http");
const url = require("url");
const host = 'frontend';
const port = process.env.WEBHOOK_PORT || 80;
const { exec } = require("child_process");

const requestListener = function (req, res) {
    res.writeHead(200);
    const secretKey = process.env.WEBHOOK_SECRET;
    if (!secretKey) {
        res.end('Secret key not configured');
        return;
    }
    const secretKeyRequest = url.parse(req.url, true)?.query?.secret
    console.log(secretKey)
    console.log(secretKeyRequest)
    if (secretKeyRequest === secretKey) {
        // Здесь название команды
        exec("npm run build", (error, stdout, stderr) => {
            if (error) {
                res.end(`error: ${error.message}`)
                return;
            }

            else if (stderr) {
                res.end(`stderr: ${stderr}`)
                return;
            }
            res.end(`welldone`)
            return;
        });
    } else {
        res.end('Missing secret key')
        return;
    }
    res.end('End of File')
    return;
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});
