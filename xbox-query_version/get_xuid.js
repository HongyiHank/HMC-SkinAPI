const { exec } = require('child_process');

const gamertag = process.argv[2];

if (!gamertag) {
    console.error('Gamertag is required');
    process.exit(1);
}

exec(`xbox-query query ${gamertag}`, (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
    }
    if (stderr) {
        console.error(`Stderr: ${stderr}`);
        process.exit(1);
    }

    const lines = stdout.split('\n');
    for (const line of lines) {
        if (line.startsWith('XUID:')) {
            const xuid = line.split(' ').filter(Boolean).pop();
            console.log(xuid);
            break;
        }
    }
});